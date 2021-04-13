$string = "hello"

if [[ -z "$string"]]; then
   echo "string is empty"
elif [[ -n "$string" ]]; then
   echo "string is not empty" 
fi