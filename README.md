<<<<<<< HEAD
=======
# augmentboi
Django Server For Mobile Computing Project<br>
<br>
Things to do -<br>
<br>1.Deploy on Heroku
<br>2.Complete The Whole APIS needed
<br>3.Check the Django File Field and Amazon S3 things
<br>WEB APIs
<br>■ AR Target:
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
<br>WEB APIs
<br>■ AR target delete
<br>– POST /target/<targetid> application/json
<br>■ DELETE /target/e61db301-e80f-4025-b822-
<br>9a00eb48d8d2?date=xxx&appKey=xxx&signature=xxx
<br>■ HTTP/1.1
<br>WEB APIs
<br>■ Login
<br>– POST application/json
<br>■ {email:email, password:password}
<br>– Response: application/json
<br>■ {statuscode:N, key:key}
<br>■ Register
<br>– POST application/json
<br>■ {email:email, password:password}
<br>– Response: application/json
<br>■ {statuscode:N}
<br>■ Content upload
<br>– POST application/json
<br>■ {content:Base64encodedData, key:key, latitude:lat, longitude:long}
<br>– Response: application/json
<br>■ {statuscode:N}
<br>■ Marker download
<br>– GET application/json
<br>■ {key:key, latitude:lat, longitude:long}
<br>– Response: application/json
<br>■ {statuscode:N, nResults:N,results:[{lat:LAT, long:LONG} {lat:LAT, long:LONG} {lat:LAT, long:LONG}]
>>>>>>> 9db11f7637751131b55692c78dd7bc86262db09e
