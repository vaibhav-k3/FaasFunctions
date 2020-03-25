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
     passwd = params['passwd']
     conn = getConnection()
     print('connection succes')
     db_query = 'select * from users where user_id= ? and user_passwd=?'
     cursor = conn.cursor()
     cursor.execute(db_query, (user_id , passwd))
     rows = cursor.fetchall()
     if len(rows) > 0:
          #rows = cursor.fetchall()
          print(rows[0][0])
          print(rows[0][1])
          return{
               'status':'success',
               'headers':{
                    'Content-Type':'application/json'
               },
               'user_id': rows[0][0],
               'passwd':rows[0][1],
               'statusCode':200,
               'redirect_url':'https://www.facebook.com'
          }
     else:
          '''
          return{
          'headers':{'location':'https:www.google.com'},
          'statusCode':302
          }
          
          '''
          return{
          'headers':{'Content-Type':'application/json'},
          'statusCode':200,
          'status':'failed',
          'redirect_url':'https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/redirect'
          }
          
     
