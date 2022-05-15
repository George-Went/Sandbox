
# echo "url:"
# read url 
# echo: $url

# echo "login:"
# read login 
# echo: $url

# echo "password:"
# read password 
# echo: $url

# $url "http://localhost:5000/api/v1/security/login"
# $name = "admin"
# $password "admin"
# json_data()
# {cat <<EOF 
# }
# {"password": "admin",
#     "provider": "db",
#     "refresh": true,
#     "username": "admin"}
#     } EOF 
# echo @data.json
# curl -X POST localhost:5000/api/v1/security/login -H 'Content-Type: application/json' -data "$json"


# curl -X POST localhost:5000/api/v1/security/login -H 'Content-Type: application/json' -data '{ "password": "admin", "provider":"db", "refresh":true, "username": "admin" }' http://localhost:5000/api/v1/security/login  



# curl -X 'GET' \
#   'http://localhost:5000/api/v1/container/
#   -H 'accept: application/json' \
#   -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MzkwNjgyNTgsIm5iZiI6MTYzOTA2ODI1OCwianRpIjoiZTM3ZDgyNTQtZDExOC00Y2ZjLWI0NWEtYmNjM2JjNzkxOTNiIiwiZXhwIjoxNjM5MDY5MTU4LCJpZGVudGl0eSI6MSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MifQ.z0kG0Tbe_dLbm0QPmI50vDGjjtRmHNhEVnWycYW93Mk

## Basic curl request 
# curl -v 'http://localhost:5000/api/v1/example/greeting'

# ## Curl request with bearer token 
# curl 'http://localhost:8080/api/v1/example/private' -H "Authorization: Bearer $TOKEN"
# {
#     "message": "This is private"
# }


# $access_token = ""

# curl -XPOST http://localhost:8080/api/v1/security/login -d \
#   '{"username": "admin", "password": "password", "provider": "db"}' \
#   -H "Content-Type: application/json"
# {
#     "access_token": $access_token
# }
# # It's nice to use the Token as an env var
# export TOKEN="<SOME TOKEN>"
# print TOKEN

# Login to obtain a token
# This bash script requires the bash "jq" package 
# sudo apt-get install jq
# https://cameronnokes.com/blog/working-with-json-in-bash-using-jq/
SECURITY_TOKEN=$( 
    curl -X 'POST' \
    'http://localhost:5000/api/v1/security/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "password": "admin",
        "provider": "db",
        "refresh": true,
        "username": "admin"
        }'
  )
echo $SECURITY_TOKEN
access_token=$(jq '.access_token' <<< $SECURITY_TOKEN) # 
echo "Access Token : " $access_token

# using out access token 
curl -X 'GET' \
  'http://localhost:5000/api/v1/container/
  -H 'accept: application/json' \
  -H 'Authorization: Bearer "$access_token" '
