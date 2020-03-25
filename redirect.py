from flask import Flask , redirect
def main(params):
     return { 'headers':{'Content-Type':'text/html'},
              'statusCode' :200,
              'body':'<html><body><h3>hello</h3></body></html>'
          }
