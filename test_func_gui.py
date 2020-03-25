from flask import Flask , redirect
def main(params):
     return { 'headers':{'Content-Type':'text/html'},
              'statusCode' :200,
              'body':'''<html><body><h3>hello</h3>
              <script>
           		console.log(sessionStorage.getItem("user_id"))
           		console.log(sessionStorage.getItem("passwd"))
              </script>

              </body></html>'''
          }
