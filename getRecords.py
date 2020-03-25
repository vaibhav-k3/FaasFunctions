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
	user_id = params['user_id']
	conn = getConnection()
	cursor = conn.cursor()
	db_query = 'select patient_name , patient_age , patient_gen , patient_date , inf_image_id , inf_diagnosis from patient INNER JOIN inferences ON patient.patient_id = inferences.inf_patient_id where patient.user_id = ?;'

	cursor.execute(db_query , [user_id]);

	rows = cursor.fetchall()
	if len(rows) > 0:
		data = []
		for row in rows:
			entry = {}
			entry['patient_name'] = row[0]
			entry['patient_age'] = row[1]
			entry['patient_gen'] = row[2]
			entry['patient_date'] = row[3]
			entry['inf_image_id'] = row[4]
			entry['inf_diagnosis'] = row[5]

			data.append(entry)

		return{
			'data':data,
			'statusCode':200,
			'headers':{'Content-Type':'application/json'},
			'status':'success'
		}
