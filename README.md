# Mobile Computing Project AUGMENTBOI





Complete Report of the project and Source code is available at :
https://docs.google.com/document/d/1vlO7C8cqrCSmC2uLf_hQMFa4qreUgmrDTzoc8cn7AuQ/edit?usp=sharing




This is a Backend Server written using django framework for an Academic Project and is hosted in AWS.
The Server Supports the following API's.<br>
<br>
## WEB APIs:
<br><b>AR Target:</b>
<br>– POST /targets/ application/json : pushes ar target image
<br>– Body:
<br>– {
<br>– "image":"Base64encodedstring",
<br>– "active":"1",
<br>– "name":"targetName",
<br>– "size":"5",
<br>– "meta":"496fbbabc2b38ecs3460a...",
<br>– "type":"ImageTarget",
<br>– "date": "2016-05-27T09:15:39.559Z",
<br>– "appKey": "test_app_key",
<br>– "signature": "sha1 signature"
<br>– }



<br><b> AR target delete </b>
<br>– POST /target/<targetid> application/json



<br><b>DELETE /target/e61db301-e80f-4025-b822-9a00eb48d8d2?date=xxx&appKey=xxx&signature=xxx </b>



<br><b>Login</b>
<br>– POST application/json
<br>{email:email, password:password}
<br>– Response: application/json
<br>{statuscode:N, key:key}


<br><b>Register</b>
<br>– POST application/json
<br>{email:email, password:password}
<br>– Response: application/json
<br>{statuscode:N}



<br><b>Content upload</b>
<br>– POST application/json
<br>{content:Base64encodedData, key:key, latitude:lat, longitude:long}
<br>– Response: application/json
<br>{statuscode:N}



<br><b>Marker download</b>
<br>– GET application/json
<br>{key:key, latitude:lat, longitude:long}
<br>– Response: application/json
<br>{statuscode:N, nResults:N,results:[{lat:LAT, long:LONG} {lat:LAT, long:LONG} {lat:LAT, long:LONG}]
  

## App Usage
