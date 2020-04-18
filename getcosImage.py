import ibm_boto3
import base64
from ibm_botocore.client import Config, ClientError
# using container riteshmoolya99/ibmfun4:v5
def get_cos_resource():

	COS_ENDPOINT = "https://s3.private.jp-tok.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
	COS_API_KEY_ID = "5I4t5FZbY5IiMI1_0whM6rCLPCme0yGteY2P31SBw0pJ" # eg "W00YiRnLW4a3fTjMB-odB-2ySfTrFBIQQWanc--P3byk"
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

def get_item(bucket_name, item_name):
	cos = get_cos_resource()
	print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
	try:
		file = cos.Object(bucket_name, item_name).get()
		#print("File Contents: {0}".format(file["Body"].read()))
	except ClientError as be:
		print("CLIENT ERROR: {0}\n".format(be))
	except Exception as e:
		print("Unable to retrieve file contents: {0}".format(e))
	
	return file["Body"].read()

def main(params):
	bucket_name = None
	ext = None
	if params['type'] == 'in':
		bucket_name = 'cloud-object-storage-xr-cos-archive-in6'
		ext = '.png'
	else:
		bucket_name = 'cloud-object-storage-xr-cos-standard-2nz'
		ext = '.jpg'

	print('image name : ' + params['item']+ext)
	image_bytes = get_item(bucket_name , params['item']+ext)
	imgString = base64.b64encode(image_bytes)
	return{
        'headers':{'Content-Type':'image/png'},
        'statusCode':200,
        'body':imgString.decode()
    }
    
