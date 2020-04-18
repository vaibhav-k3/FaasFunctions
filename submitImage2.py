def main(params):
	return{
		'statusCode':200,
		'headers':{'Content-Type':'text/html'},
		'body':'''
		<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Virus Detector</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <link rel="stylesheet" type="text/css" href="style.css">
    <style type="text/css">
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
        input[type=submit]{
                align-self: center;
                width: 100%;
                height: 60px;
                box-sizing: border-box;
                padding:;
                margin-left: auto;
                margin-right: auto;
                margin-bottom: 10px;
                margin-top: 18px;
                outline: none;
                border: 1px solid black;
                
                background: white;
                border-radius: 10px;
                font-size: 20px;
                color: #000;
                font-family: Lato, sans-serif;
                font-weight: bold; 
                 

            }
        input[type=button]:hover{
            background-color: #e0e0e0;
        }

        /*.wf{
    border: 1px solid black;
}
*/
.r1{
    min-height: 10vh;
    align-self: auto;
}

.heading{
    margin-left: 40vw;
    font-style: bold; 
    font-size: 30px;
    font-family: Arial, Helvetica, sans-serif;
    color: #bdeaee;

}

.lc{
    border-right: 1px solid black;
}
.r2{
    min-height: 100vh !important;
    height: 100%;

}

.wrap{
    margin-top: 10vh;
    margin-right: auto;
    margin-left: auto;
    margin-bottom: auto;
    align-self: center;
    max-width:350px;
    border-radius: 20px;
    background: #6699cc;
    box-sizing:border-box;
    padding: 40px;
    padding-top: 10px;
    padding-bottom: 10px;
    color: black;
    font-family: Lato, sans-serif;
    /* margin-top: 100px; */
}
input[type=text], input[type=password], input[type=date], input[type=file], select, input[type=number]{
    width: 100%;
    box-sizing: border-box;
    padding: 12px 5px;
    background: ;
    outline: none;
    border: none;
    border-bottom: 1px dotted #fff;
    color:  
    border-radius: 5px;
    margin: 5px;
    font-weight: bold;
    font-family: Lato, sans-serif;

}

/*input[type=submit]{
    align-self: center;
    width: 100%;
    box-sizing: border-box;
    padding: 10px 0;
    margin-top: 30px;
    outline: none;
    border: none;
    background: #1c4966;
    border-radius: 20px;
    font-size: 20px;
    color: #fff;
    font-family: Lato, sans-serif;

}
*/
img{
    border: 1px #ddd;
    border-radius: 4px;
    padding: 10px;
    width: 380px;
    align-self: center;
    /*margin-left: ;*/
}

img:hover {
    box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}

.btn {
        background-color: #e3f2fd;
        border: none;
        color: darkblue;
        padding: 12px 30px;
        cursor: pointer;
        font-size: 20px;
        margin-left: 5vw;
}
/*
for shadow{
    shadow p-3 mb-5 rounded
}*/
            
    </style>
        

</head>
<body>
    <header class="sticky-top">
        <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #bbdefb; color:#15386a; padding: 0px 15px 0px 15px;">
            <div style="border: 0px; border-radius: 0px;padding: 0px; width: 0px; align-self: none; margin-left: 0px;"><a href="#" class="navbar-brand">
               <!--<img src="name.png" alt="">-->
            </a></div>
            <button class="navbar-toggler btn-light float-right" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation" style="margin top:20px; margin-left:0px ">
                <span class="navbar-toggler-icon btn-light"></span>
            </button>
            <div class="collaspe navbar-collapse float-right" id="navbarNavAltMarkup">
                <div class="navbar-nav ml-auto" style="margin-left: 4vw;">
                <!-- <a class="nav-item nav-link" style="" href="#">Virus Detector</a> -->
                <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;padding-right: 25px;padding-left: 25px;" href="ic_buttons.html">Home</a>
                <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;padding-right: 25px;padding-left: 25px " href="https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/viewRecords">Records</a>
               <!-- <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;" href="members.php">Membership</a> -->
                
                <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;padding-right: 25px;padding-left: 25px;" href="index.html" onclick="preventBack()">Logout</a>
                </div>
            </div>
        </nav>
    </header>
    <div class="container-fluid" style="background-color: #e3f2fd; padding: 0px;" >
    <!-- <div style="background-color: #bbdefb; ">
      <h1 class="text-sm-center" style="font-weight: bold; font-size: 9vh; font-family: Lato, sans-serif; color: #283593">
       <center> Virus Detector </center>
      </h1>
    </div>   -->
        <div class="row wf r2">
            <div class="col-md-4 lc">
                <form id="patientForm" class="wrap" , enctype ="multipart/form-data">
                <!-- <center> -->
                <center><h2 style="color:black;">Patient's Details</h2></center>
                    <input type="text" id="name" name="nme" placeholder="Name" required>
                    <input type="number" id="age" name="age" min="1" max="100" placeholder="Age" required>
                    <div>
                        <select id="Gender" name="Gender" style="" required>
                            <option style="color: "rgb(155, 152, 152);">---Select Gender---</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <input type="text" placeholder="Date" onfocus="(this.type='date')" required>
                                <!-- </div> -->
                    <input type="text" id="doctor" name="dname" placeholder="Doctor Name" required> 
                    <input type="file" id="input1" name="input1" required>
                <!-- </center> -->
                <!-- <button onclick="sendData()">send</button> -->
                

        
            <!-- <div class="row">
                <input type="submit" id="Report" value="Generate Report" name="Report" onclick="window.location.href='print.html'" >
            </div> -->
            </form>
            </div>

            <div class="col-md-8 wf" id = 'mainCol'>
                <div class="row r3 wf" id = 'mainRow'>
                    <!---<div class="col-md-6 wf" style="margin-top:3vw">
                        <div id='displayImg'>
                             selected file displayed here
                        </div>
                    </div> 
                    <div class="col-md-6 wf" style="margin-top: 3vw" >
                        <div id = 'serverImg' >
                              infered image diplayed here 
                        </div>
                        <div id="aTag"></div>

                </div> -->
                </div>
            </div>          
                <!-- <div class="col-md-6 text-center offset-md-4"> -->
                <!-- </div> -->         
        </div>
</div>

<script type="text/javascript">
    generateAnsRow = function(orgImage,ansImage, opsButton){
        mainCol = document.querySelector('#mainCol');
        ansDiv = document.createElement('div')
        ansDiv.appendChild(orgImage)

        rowDiv = document.createElement('div')
        rowDiv.setAttribute('class' , 'row')

        gridColumn = document.createElement('div');
        gridColumn.setAttribute('class' , 'col-md-6');
        gridColumn.style.marginTop = '3vw';
        gridColumn.appendChild(ansDiv)
        gridColumn.appendChild(opsButton)
        rowDiv.appendChild(gridColumn)
        mainCol.appendChild(rowDiv)


    }
    function uploadButton(base64String , uploadButton_element){
        
                let xmlhttp = new XMLHttpRequest()
                xmlhttp.onreadystatechange = function(){
                if(this.readyState == 4 && this.status == 200){

                    let sendImageAjax = new XMLHttpRequest()
                    sendImageAjax.onreadystatechange = function(){

                        if(this.readyState == 4 && this.status == 200){
                            console.log(this.responseText)
                            let serverResponse = JSON.parse(this.responseText)
                            //console.log(this.responseText)
                            let imgString = serverResponse['imgString']
                            const serverImg = new Image()
                            serverImg.onload = function(){
                                const canvas = document.createElement('canvas')
                                canvas.toDataURL()

                            }
                            serverImg.src = "data:image/jpg;base64," + imgString
                            mainRow = document.querySelector('#mainRow');
                            gridColumn = document.createElement('div');
                            gridColumn.setAttribute('class' , 'col-md-6');
                            gridColumn.appendChild(serverImg)
                            aTag = document.createElement('a')
                            aTag.style.color = "black"
                            let downloadImageName = 'Image_ID_'+serverResponse['imageId']+'.png';
                            aTag.setAttribute('download' ,downloadImageName)
                            aTag.setAttribute('href', 'data:image/png;base64,' + imgString )
                            button= document.createElement('button')
                            a_text = document.createTextNode('Download')
                            aTag.appendChild(a_text)
                            button.appendChild(aTag)
                            gridColumn.appendChild(button)
                            mainRow.appendChild(gridColumn)
                            ansDiv =document.createElement('div')
                            ansDiv.setAttribute('class' , 'col-md-12 text-center')
                            ansText = document.createTextNode('Image ID: '+serverResponse['imageId']+'  Diagnosis by System: '+ serverResponse['diagnosis']);
                            ansDiv.appendChild(ansText)
                            mainRow.appendChild(ansDiv)
                            download('data:image/png;base64,' + imgString, downloadImageName , 'image/png')
                            uploadButton_element.disabled = true ; 

                        }
                         
                    }
                    let formData  = new FormData()
                    let file = document.querySelector("#input1").files[0]
                    formData.append('imgString',file)
                    sendImageAjax.open("POST" , "https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/objectDetection2.json")
                    //sendImageAjax.setRequestHeader("Content-Type","application/x-binary")
                    sendImageAjax.send(base64String)
                    
                }
            }
            let patient_name = document.querySelector('#name').value;
            let patient_age =  document.querySelector('#age').value;
            let patient_gender = document.querySelector('#Gender').value;
            let patient_date = 'NONE';
            let patient_doctor  = document.querySelector('#doctor').value;
            let user_id = sessionStorage.getItem("user_id");

            xmlhttp.open("POST" , 'https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/insertPatient', true)
            xmlhttp.setRequestHeader("content-type","application/json")
            xmlhttp.send(JSON.stringify({'patient_name':patient_name ,
                'patient_age':patient_age ,
                'patient_gender':patient_gender,
                'patient_date':patient_date,
                'patient_doc': patient_doctor,
                'user_id':user_id
            }))
        }



    const input=document.querySelector('input[type="file"]')
    input.addEventListener('change', function(e) {
        console.log(input.files)
        const reader = new FileReader()
        reader.onload = function (){

            const img = new Image()
            img.onload = function() {
                    const canvas = document.createElement('canvas')
                    canvas.toDataURL()
            }

            img.src = reader.result
            let base64String = reader.result.split(',')[1]
            //console.log(base64String)
            // document.body.appendChild(img)

            //display selected image
            const displayImg = new Image()
            displayImg.src = "data:image/jpg;base64," + base64String
            mainRow = document.querySelector('#mainRow');
            gridColumn = document.createElement('div');
            gridColumn.setAttribute('class' , 'col-md-6');
            gridColumn.appendChild(displayImg)
            up_bt = document.createElement('button')
            up_text = document.createTextNode('Upload')
            up_bt.appendChild(up_text)
            gridColumn.appendChild(up_bt)
            mainRow.appendChild(gridColumn)
            up_bt.addEventListener('click', function(event){
                uploadButton(base64String , up_bt);
                event.preventDefault();
                //up_bt.disabled = true ;
                
            });
            //generateAnsRow(displayImg , up_bt)

        }
    // reader.readAsText(input.files[0])
    reader.readAsDataURL(input.files[0])
    }, false)
    

   </script>
   <script type="text/javascript">
  //        function validateForm() {
  //         var x = document.forms["myForm"]["fname"].value;
  //            if (x == "") {
  //        alert("Name must be filled out");
  //        return false;
  //            }
  //    }
        function preventBack() { window.history.forward(); }
        setTimeout("preventBack()", 0);
        window.onunload = function () { null };

</script>
<script
    src="https://code.jquery.com/jquery-3.4.1.min.js"
    integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
    crossorigin="anonymous">
</script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>




<!-- for force downloading image -->
<script>
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define([], factory);
    } else if (typeof exports === 'object') {
        // Node. Does not work with strict CommonJS, but
        // only CommonJS-like environments that support module.exports,
        // like Node.
        module.exports = factory();
    } else {
        // Browser globals (root is window)
        root.download = factory();
  }
}(this, function () {

    return function download(data, strFileName, strMimeType) {

        var self = window, // this script is only for browsers anyway...
            defaultMime = "application/octet-stream", // this default mime also triggers iframe downloads
            mimeType = strMimeType || defaultMime,
            payload = data,
            url = !strFileName && !strMimeType && payload,
            anchor = document.createElement("a"),
            toString = function(a){return String(a);},
            myBlob = (self.Blob || self.MozBlob || self.WebKitBlob || toString),
            fileName = strFileName || "download",
            blob,
            reader;
            myBlob= myBlob.call ? myBlob.bind(self) : Blob ;
      
        if(String(this)==="true"){ //reverse arguments, allowing download.bind(true, "text/xml", "export.xml") to act as a callback
            payload=[payload, mimeType];
            mimeType=payload[0];
            payload=payload[1];
        }


        if(url && url.length< 2048){ // if no filename and no mime, assume a url was passed as the only argument
            fileName = url.split("/").pop().split("?")[0];
            anchor.href = url; // assign href prop to temp anchor
            if(anchor.href.indexOf(url) !== -1){ // if the browser determines that it's a potentially valid url path:
                var ajax=new XMLHttpRequest();
                ajax.open( "GET", url, true);
                ajax.responseType = 'blob';
                ajax.onload= function(e){ 
                  download(e.target.response, fileName, defaultMime);
                };
                setTimeout(function(){ ajax.send();}, 0); // allows setting custom ajax headers using the return:
                return ajax;
            } // end if valid url?
        } // end if url?


        //go ahead and download dataURLs right away
        if(/^data\:[\w+\-]+\/[\w+\-]+[,;]/.test(payload)){
        
            if(payload.length > (1024*1024*1.999) && myBlob !== toString ){
                payload=dataUrlToBlob(payload);
                mimeType=payload.type || defaultMime;
            }else{          
                return navigator.msSaveBlob ?  // IE10 can't do a[download], only Blobs:
                    navigator.msSaveBlob(dataUrlToBlob(payload), fileName) :
                    saver(payload) ; // everyone else can save dataURLs un-processed
            }
            
        }//end if dataURL passed?

        blob = payload instanceof myBlob ?
            payload :
            new myBlob([payload], {type: mimeType}) ;


        function dataUrlToBlob(strUrl) {
            var parts= strUrl.split(/[:;,]/),
            type= parts[1],
            decoder= parts[2] == "base64" ? atob : decodeURIComponent,
            binData= decoder( parts.pop() ),
            mx= binData.length,
            i= 0,
            uiArr= new Uint8Array(mx);

            for(i;i<mx;++i) uiArr[i]= binData.charCodeAt(i);

            return new myBlob([uiArr], {type: type});
         }

        function saver(url, winMode){

            if ('download' in anchor) { //html5 A[download]
                anchor.href = url;
                anchor.setAttribute("download", fileName);
                anchor.className = "download-js-link";
                anchor.innerHTML = "downloading...";
                anchor.style.display = "none";
                document.body.appendChild(anchor);
                setTimeout(function() {
                    anchor.click();
                    document.body.removeChild(anchor);
                    if(winMode===true){setTimeout(function(){ self.URL.revokeObjectURL(anchor.href);}, 250 );}
                }, 66);
                return true;
            }

            

            //do iframe dataURL download (old ch+FF):
            var f = document.createElement("iframe");
            document.body.appendChild(f);

            if(!winMode){ // force a mime that will download:
                url="data:"+url.replace(/^data:([\w\/\-\+]+)/, defaultMime);
            }
            f.src=url;
            setTimeout(function(){ document.body.removeChild(f); }, 333);

        }//end saver




        if (navigator.msSaveBlob) { // IE10+ : (has Blob, but not a[download] or URL)
            return navigator.msSaveBlob(blob, fileName);
        }

        if(self.URL){ // simple fast and modern way using Blob and URL:
            saver(self.URL.createObjectURL(blob), true);
        }else{
            // handle non-Blob()+non-URL browsers:
            if(typeof blob === "string" || blob.constructor===toString ){
                try{
                    return saver( "data:" +  mimeType   + ";base64,"  +  self.btoa(blob)  );
                }catch(y){
                    return saver( "data:" +  mimeType   + "," + encodeURIComponent(blob)  );
                }
            }

            // Blob but not URL support:
            reader=new FileReader();
            reader.onload=function(e){
                saver(this.result);
            };
            reader.readAsDataURL(blob);
        }
        return true;
    }; /* end download() */
}));</script>
</body>
</html>
		'''
	}