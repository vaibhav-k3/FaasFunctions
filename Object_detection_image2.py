
# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
from copy import deepcopy
import uuid
#import pickle as pkl
import ibm_db_dbi
import base64
import ibm_boto3
from ibm_botocore.client import Config, ClientError

model = tf.keras.models.load_model('object_detection/virusClassifierModel22.HDF5') 
#give full path later
def get_cos_resource():

	COS_ENDPOINT = "https://s3.private.jp-tok.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
	COS_API_KEY_ID = "Gu1hsnvXLD0iR2tzsz7F3sbupYcT1CcQvutT3OEUwZyN" # eg "W00YiRnLW4a3fTjMB-odB-2ySfTrFBIQQWanc--P3byk"
	COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
	COS_RESOURCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/725b776f255f4fbcbc709b0c4dc32e04:bad74263-ad6e-48f7-bef6-764623f90c7b::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003abfb5d29761c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

	cos = ibm_boto3.resource("s3",
	    ibm_api_key_id=COS_API_KEY_ID,
	    ibm_service_instance_id=COS_RESOURCE_CRN,
	    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
	    config=Config(signature_version="oauth"),
	    endpoint_url=COS_ENDPOINT
	)
	return cos

def put_image_in_cos(bucket_name, item_name, file_text):
	cos = get_cos_resource()
	print("Creating new item: {0}".format(item_name))
	try:
		cos.Object(bucket_name, item_name).put(Body=file_text)
		print("Item: {0} created!".format(item_name))
	except ClientError as be:
		print("CLIENT ERROR: {0}\n".format(be))
	except Exception as e:
		print("Unable to create text file: {0}".format(e))

def getConnection():
	database = 'database=BLUDB'
	hostname = 'hostname=dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net'
	port = 'port=50000'
	userid = 'uid=cqr92969'
	passwd = 'pwd=1l^v2gdds2dtxwl7'
	protocol = 'protocol=tcpip'

	conn_str = ';'.join([database , hostname , port ,protocol ,userid , passwd])
	ibm_db_conn = ibm_db_dbi.connect(conn_str ,'' ,'')
	return ibm_db_conn

def classify_crop(image_crop):

	image = deepcopy(image_crop)
	image = cv2.resize(image , (224 , 224))
	image = np.expand_dims(image , axis = 0)
     
	classification = model.predict(image)
	predicted_class = np.argmax(classification)
	predicted_score = np.max(classification)

	'''
    consider the following label map and labelmap.pbtxt
    LABEL_MAP={'trophozoite':0,'schizont':1,'ring':2,'gametocyte':3,'other':4},
    in lablemap.pbtxt we have set
    trophozoite(0) --> 3
    schizont(1) --->4
    ring (2)----> 5
    gametocyte(3)---->6
	'''
	class_mappings = { 0 : 3 , 1 : 4 , 2 :5 , 3:6}
	predicted_class = class_mappings[predicted_class]
	return predicted_class , predicted_score




def classify_infected(image , scores , boxes , classes , threshold = 0.20):

    boxes_copy = deepcopy(boxes)
    scores_copy = deepcopy(scores)
    classes_copy  = deepcopy(classes)

    boxes_copy = np.squeeze(boxes_copy)
    scores_copy = np.squeeze(scores_copy)
    classes_copy = np.squeeze(classes_copy)
    image_copy = deepcopy(image)
    image_shape = image.shape
    width = image_shape[1]
    height = image_shape[0]

    infected_boxes = boxes_copy[np.logical_and(scores_copy >= threshold,classes_copy == 2)]
    #if no infected boxes present , then return as it is
    if(infected_boxes.shape[0] <= 0):
        return image , np.expand_dims(scores_copy , axis = 0) , np.expand_dims(boxes_copy ,axis = 0) , np.expand_dims(classes_copy , axis = 0)
    else:
        classified_labels = []
        classified_labels_scores = []
        for infected_box in infected_boxes:
            ymin = int(infected_box[0]*height)
            xmin = int(infected_box[1]*width)
            ymax = int(infected_box[2]*height)
            xmax = int(infected_box[3]*width)

            image_crop = deepcopy(image_copy[ymin:ymax , xmin:xmax , :])
            image_crop = image_crop[: , : , ::-1]
            #image_crop = np.expand_dims(image_crop , axis = 0)

            classification, score = classify_crop(image_crop)
            classified_labels.append(classification)
            classified_labels_scores.append(score)


        classified_labels = np.array(classified_labels)
        classified_labels_scores = np.array(classified_labels_scores)
        print('classes_copy')
        print(classes_copy[np.logical_and(scores_copy >= threshold,classes_copy == 2)])
        print('scores_copy')
        print(scores_copy[np.logical_and(scores_copy >= threshold,classes_copy == 2)])
        
        scores_copy[np.logical_and(scores_copy >= threshold,classes_copy == 2)] = classified_labels_scores
        classes_copy[np.logical_and(scores_copy >= threshold,classes_copy == 2)] = classified_labels
        boxes_copy = np.expand_dims(boxes_copy, axis =0)
        scores_copy = np.expand_dims(scores_copy , axis =0)
        classes_copy = np.expand_dims(classes_copy , axis =0)



        return image , scores_copy , boxes_copy , classes_copy

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append(os.getcwd())

# Import utilites
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


# Name of the directory containing the object detection module we're using
def main(params):
    
	#headers = params['__ow_headers']
	#user_id = headers['user_id']
	MODEL_NAME = 'exported_graph'
	#IMAGE_NAME = '1test1.jpg'

	# Grab path to current working directory
	CWD_PATH = os.getcwd()

	image_name_for_cos = uuid.uuid4()
	image_name_for_cos = image_name_for_cos.hex

	# Path to frozen detection graph .pb file, which contains the model that is used
	# for object detection.
	PATH_TO_CKPT = os.path.join(CWD_PATH,'object_detection',MODEL_NAME,'frozen_inference_graph.pb')

	# Path to label map file
	PATH_TO_LABELS = os.path.join(CWD_PATH,'object_detection','training','labelmap.pbtxt')

	# Path to image
	#PATH_TO_IMAGE = os.path.join(CWD_PATH,'object_detection',IMAGE_NAME)

	# Number of classes the object detector can identify
	NUM_CLASSES = 6

	# Load the label map.
	# Label maps map indices to category names, so that when our convolution
	# network predicts `5`, we know that this corresponds to `king`.
	# Here we use internal utility functions, but anything that returns a
	# dictionary mapping integers to appropriate string labels would be fine
	label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
	categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
	category_index = label_map_util.create_category_index(categories)

	# Load the Tensorflow model into memory.
	detection_graph = tf.Graph()
	with detection_graph.as_default():
	    od_graph_def = tf.GraphDef()
	    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
	        serialized_graph = fid.read()
	        od_graph_def.ParseFromString(serialized_graph)
	        tf.import_graph_def(od_graph_def, name='')

	    sess = tf.Session(graph=detection_graph)

	# Define input and output tensors (i.e. data) for the object detection classifier

	# Input tensor is the image
	image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

	# Output tensors are the detection boxes, scores, and classes
	# Each box represents a part of the image where a particular object was detected
	detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

	# Each score represents level of confidence for each of the objects.
	# The score is shown on the result image, together with the class label.
	detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
	detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

	# Number of objects detected
	num_detections = detection_graph.get_tensor_by_name('num_detections:0')

	# Load image using OpenCV and
	# expand image dimensions to have shape: [1, None, None, 3]
	# i.e. a single-column array, where each item in the column has the pixel RGB value
	# image = cv2.imread(PATH_TO_IMAGE)
	#print(params)
	base64ImgString = params['__ow_body'].encode('ascii')


	print('--storing input image in object storage--')
	


	base64ImgString = base64.b64decode(base64ImgString)
	
	#-in6 bucket is for input images
	put_image_in_cos('cloud-object-storage-xr-cos-archive-in6' , image_name_for_cos+'.png',base64ImgString )
	nparray = np.fromstring(base64ImgString , dtype = np.uint8)
	image = cv2.imdecode(nparray , cv2.IMREAD_COLOR)

	image_copy = deepcopy(image)
	image_expanded = np.expand_dims(image, axis=0)

	# Perform the actual detection by running the model with the image as input
	(boxes, scores, classes, num) = sess.run(
	    [detection_boxes, detection_scores, detection_classes, num_detections],
	    feed_dict={image_tensor: image_expanded})

	# Draw the results of the detection (aka 'visulaize the results')
	image , scores , boxes , classes = classify_infected(image_copy , scores , boxes , classes , threshold = 0.05)

	vis_util.visualize_boxes_and_labels_on_image_array(
	    image,
	    np.squeeze(boxes),
	    np.squeeze(classes).astype(np.int32),
	    np.squeeze(scores),
	    category_index,
	    use_normalized_coordinates=True,
	    skip_scores =False,
	    line_thickness=2,
	    min_score_thresh=0.30,
	    max_boxes_to_draw=200)

	print('shape of boxes :' + str(boxes.shape))
	print('shape of scores :' +str(scores.shape))
	print('shape of classes :'+str(classes.shape))
	print('shape of num :'+ str(num.shape))

	infected_score = scores[0][np.logical_and(scores[0] >= 0.01 , classes[0] == 2)]
	infected_classes = classes[0][np.logical_and(scores[0] >= 0.01 , classes[0] == 2)]

	infected_boxes_index = np.logical_and(scores[0] >= 0.01, classes[0] == 2)

	infected_boxes = boxes[0][infected_boxes_index]
	#print('---------infected boxes-----------')
	print('infected boxes :'+str(infected_boxes))
	print('infected boxes shape:' + str(infected_boxes.shape))
	print('infected scores :'+str(infected_score.shape))
	print('score   label\n\n')
	for score , label in zip(scores[0] , classes[0]):
	    print(score , label)
	'''
	for box in infected_boxes:
	     xmin = int(box[1]*1600)
	     ymin = int(box[0]*1200)
	     xmax = int(box[3]*1600)
	     ymax = int(box[2]*1200)
	     image_crop = image[ymin:ymax , xmin:xmax , :]
	     cv2.imshow('object_detector',image_crop)
	     cv2.imwrite('C:/Users/Vaibhav/Desktop/Codes/BE Project/sourceCode/Object_detection2/models/research/object_detection/res.jpg' , image_crop)
	     cv2.waitKey(0)
	     cv2.destroyAllWindows()
	     break
	 '''    
	FINAL_THRESHOLD = 0.20
	diagnosis = []
	if True in np.logical_and(scores[0]>=FINAL_THRESHOLD , classes[0]==3):
		diagnosis.append('trophozoite')

	if True in np.logical_and(scores[0]>=FINAL_THRESHOLD , classes[0]==4):
		diagnosis.append('schizont')

	if True in np.logical_and(scores[0]>=FINAL_THRESHOLD , classes[0]==5):
		diagnosis.append('ring')

	if True in np.logical_and(scores[0]>=FINAL_THRESHOLD , classes[0]==6):
		diagnosis.append('gametocyte')

	if 'trophozoite' in diagnosis or 'schizont' in diagnosis  or 'ring' in diagnosis or'gametocyte' in diagnosis:
		diagnosis.append('malaria')
	else:
		diagnosis.append('not found')

	diagnosis = ','.join(diagnosis)
	print('the diagnosis is :' + diagnosis)
	

	
	_ , buff = cv2.imencode(".jpg" , image )
	print(type(buff))
	#-2nz is for storing output images
	put_image_in_cos('cloud-object-storage-xr-cos-standard-2nz' , image_name_for_cos+'.jpg',buff.tostring())
	imgString = base64.b64encode(buff)

	conn = getConnection()
	cursor = conn.cursor()
	db_query_to_get_last_patientid= 'select patient_id from patient ORDER BY patient_id DESC LIMIT 1 ;'
	cursor.execute(db_query_to_get_last_patientid)
	row = cursor.fetchall()
	cursor.close()
	#conn.close()

	latest_patient_id = int(row[0][0])
	print('latest patient_id ' + str(latest_patient_id))

	#conn = getConnection()
	cursor = conn.cursor()
	db_query_to_insert_diagnosis = 'insert into inferences(inf_patient_id , inf_diagnosis , cosImageId) values(?,?,?);'
	cursor.execute(db_query_to_insert_diagnosis , (latest_patient_id , diagnosis , image_name_for_cos))
	conn.commit()
	print('diagnosis inserted')
	
	cursor.close()
	#conn.close()


	db_query_to_get_last_img_id= 'select inf_image_id from inferences ORDER BY  inf_image_id DESC LIMIT 1 ;'
	#conn = getConnection()
	cursor = conn.cursor()
	cursor.execute(db_query_to_get_last_img_id)
	row = cursor.fetchall()
	latest_img_id = int(row[0][0])
	print('lates inference id'+ str(latest_img_id))
	cursor.close()
	conn.close()
	return{'headers':{'content-type':'application/json'},
            'statusCode':200,
            'imgString':imgString.decode(),
            'diagnosis':diagnosis,
            'imageId':latest_img_id
          }
	
