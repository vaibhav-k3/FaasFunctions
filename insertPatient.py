import ibm_db_dbi

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

def main(params):
	patient_name = params['patient_name']
	patient_age = params['patient_age']
	patient_gen = params['patient_gender']
	patient_date = params['patient_date']
	user_id = params['user_id']
	patient_doc = params['patient_doc']
	conn = getConnection()
	print('connection - succes')

	db_query_to_insert_patient = 'insert into patient(user_id , patient_name , patient_age , patient_gen , patient_date, patient_doc) values(? ,? , ? , ? , ? , ?);'
	cursor = conn.cursor()
	cursor.execute(db_query_to_insert_patient , (user_id , patient_name , patient_age , patient_gen, patient_date,  patient_doc))
	conn.commit()
	print("---insert succes------")
	cursor.close()
	return{
	'status':'success',
	'statusCode':200
	}
	#conn.close()