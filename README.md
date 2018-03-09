# augmentboi
Django Server For Mobile Computing Project

Things to do -
1.Deploy on Heroku
2.Complete The Whole APIS needed
3.Check the Django File Field and Amazon S3 things
WEB APIs
■ AR Target:
– POST /targets/ application/json : pushes ar target image
– Body:
– {
– "image":"Base64encodedstring",
– "active":"1",
– "name":"targetName",
– "size":"5",
– "meta":"496fbbabc2b38ecs3460a...",
– "type":"ImageTarget",
– "date": "2016-05-27T09:15:39.559Z",
– "appKey": "test_app_key",
– "signature": "sha1 signature"
– }
WEB APIs
■ AR target delete
– POST /target/<targetid> application/json
■ DELETE /target/e61db301-e80f-4025-b822-
9a00eb48d8d2?date=xxx&appKey=xxx&signature=xxx
■ HTTP/1.1
WEB APIs
■ Login
– POST application/json
■ {email:email, password:password}
– Response: application/json
■ {statuscode:N, key:key}
■ Register
– POST application/json
■ {email:email, password:password}
– Response: application/json
■ {statuscode:N}
■ Content upload
– POST application/json
■ {content:Base64encodedData, key:key, latitude:lat, longitude:long}
– Response: application/json
■ {statuscode:N}
■ Marker download
– GET application/json
■ {key:key, latitude:lat, longitude:long}
– Response: application/json
■ {statuscode:N, nResults:N,results:[{lat:LAT, long:LONG} {lat:LAT, long:LONG} {lat:LAT, long:LONG}]
