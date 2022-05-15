## Basic API testing scripts using bash 
## To Run:
## chmod +x get.sh
## ./get.sh

## GET site
curl http://localhost:5000


## CREATE 
curl -X POST http://localhost:5000/create -H "Content-Type: application/json" -d '{"name":"F150", "model":"Ford", "doors":4}'  

## READ
curl http://localhost:5000/read

## UPDATE
curl -X POST http://localhost:5000/update -H "Content-Type: application/json" -d '{"id": 5 ,"name":"F120", "model":"Ford", "doors":2}'

## DELETE 
curl -X POST http://localhost:5000/delete -H "Content-Type: application/json" -d '{"id": 5}'
