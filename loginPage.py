def main(params):
	return{
	'headers':{'content-type':'text/html'},
	'statusCode':300,
	'body':'''
	<!DOCTYPE html>
<html>
    <head>
        <title>
            Virus Detector
        </title>
        <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Virus Detector</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">



        <style>
            #heading{
                /*margin-left: ;*/
                font-style: bold; 
                font-size: 30px;
               font-family: Alatsi;
                color: #283593;

            }



            body{
                background-color: #e3f2fd;
                background-size:cover;
                font-family: Arial, Helvetica, sans-serif;
            }
            .wf{
                /*height: 400px;*/
                max-width:500px;
                border-radius: 15px;
                margin: auto;
                background: #33b5e5;
                box-sizing:border-box;
                padding: 20px;
                color: black;
                margin-top: 9vw;
            }
            input[type=text], input[type=password]{
                width: 100%;
                box-sizing: border-box;
                padding: 12px 5px;
                background: ;
                outline: none;
                font-size: 2.5vh;
                border: ;
                border-bottom: 6px dotted #fff;
                color: black;
                border-radius: 8px;
                margin: 5px;
                font-weight: bold;
                font-family: Lato, sans-serif;

            }

            input[type=submit]{
                align-self: center;
                width: 100%;
                height: 60px;
                box-sizing: border-box;
                padding:;
                margin-bottom: 10px;
                margin-top: 18px;
                outline: none;
                border: none;
                background: #1c4966;
                border-radius: 20px;
                font-size: 20px;
                color: #fff;
                font-family: Lato, sans-serif;
                font-weight: bold;   

            }
            input[type=submit]:hover{
                background-color: ;
            }
            .navbar-brand{
                /*border: 1px #ddd;
                border-radius: 4px;*/
                padding: 10px;
                width: 380px;
                align-self: center;
                margin: 2px
            }
            .navbar{
            min-height: 76px !important;
        }
        .ml-auto{
            margin-right: 5vw;  
        }
        .nav-item,.nav-link{
            font-size: 1.5vw;
            font-family: Lato, sans-serif; 
            font-weight: bold;
            
        }
        </style>
    </head>
    <body style="margin: 0px;">
        
    <div class="container-fluid" style="background-color: #e3f2fd; padding: 0px; margin: 0px; " >
    <!-- <div style="background-color: #bbdefb; ">
      <h1 class="text-sm-center" style="margin-top: 0px; font-weight: bold; font-size: 9vh; font-family: Lato, sans-serif; color: #283593">
        <center>Virus Detector</center>
      </h1>
    </div> -->
        <div class="row wf">
        <div class="col-md-12">
        <center>
            <h1 style="color: white;">
                Login
            </h1>
        </center>
        
        
            <center>
                <!-- <label for="Id">User ID</label> -->
                <input type="Text" id="Id" placeholder="User ID" required>
                <br><br>
                <!-- <label for="Password">Password</label> -->
                <input type="password" id="Password" placeholder="Password" required>
                <br><br>
                <div id = 'state'></div>
                <button onclick ="sendAuth()"> login</button>
            </center>
        
        </div>
    </div>
    </div>    

       <script type="text/javascript">
    function myfunction(){
        location.replace("https://www.google.com")
    }
</script>
<script type="text/javascript">
   let sendAuth = function(){
        let userId = document.querySelector('#Id').value;
        let passwd = document.querySelector('#Password').value;
        xmlhttp = new XMLHttpRequest()
        xmlhttp.onreadystatechange = function(){
        	console.log('state changed')
        	console.log(this.status);
        	console.log(this.readyState);
        	if(this.status == 200 && this.readyState == 4){
        		let serverResponse = JSON.parse(this.responseText);
        		let status = serverResponse['status'];
        		if(status == 'success'){
        			let url = serverResponse['redirect_url'];
        			let user_id = serverResponse['user_id'];
        			let passwd = serverResponse['passwd'];
        			window.sessionStorage.setItem("user_id" , user_id);
        			window.sessionStorage.setItem("passwd" , passwd)
        			//location.replace(url)
        			location.replace("https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/viewRecords")
        		}
        		else{
        			document.querySelector("#state").innerHTML = 'invalid login or password';
        		}
        		
        	}
        }
        xmlhttp.open("POST" , "https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/authentication.json" , true)
        xmlhttp.setRequestHeader("content-type","application/json")
        xmlhttp.send(JSON.stringify({'user_id':userId , 'passwd':passwd}))
    }
</script>


<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
</body>
    
</html>
		'''
	}