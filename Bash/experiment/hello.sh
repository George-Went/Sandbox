#! /bin/bash

# Echo (print) command
echo hello world!

# Variables 
# Uppercase by convention
NAME="George"
echo "My name is $NAME"
echo "My name is {$NAME}" # both do the same thing

# User input
# read -p "Enter your name: " USER_NAME
# echo "Hello $USER_NAME, nice to meet you!"

# Simple IF-ELSE statement 
if [ "$NAME" == "George" ]
then 
   echo "Your name is George"
else
 echo "You are not George" 
fi

# ELSE_IF statment (elif)
if [ "$NAME" == "George" ]
then 
   echo "Your name is George"
elif [ "$NAME" == "Jack" ]
then 
   echo "Your name is Jack"
else
 echo "You are not George or Jack" 
fi

# Conditionals / Comparisons 



if [[ 3 != 2 ]]
then
 echo "3 is not 2"
fi

NUM1=3
NUM2=4
if [ "$NUM1" -gt "$NUM2" ]
then 
   echo "$NUM1 is greater than $NUM2"
else
   echo "$NUM1 is less than $NUM2"
fi

## all return 'true' if the condition exists
# [[ -z STRING ]] 	Empty string
# [[ -n STRING ]] 	Not empty string
# [[ STRING == STRING ]] 	Equal
# [[ STRING != STRING ]] 	Not Equal
# [[ NUM -eq NUM ]] 	Equal
# [[ NUM -ne NUM ]] 	Not equal
# [[ NUM -lt NUM ]] 	Less than
# [[ NUM -le NUM ]] 	Less than or equal
# [[ NUM -gt NUM ]] 	Greater than
# [[ NUM -ge NUM ]] 	Greater than or equal
# [[ STRING =~ STRING ]] 	Regexp (does a string fit a regular expression?)
# (( NUM < NUM )) 	Numeric condition
# [[ ! EXPR ]] 	Not
# [[ X && Y ]] 	And
# [[ X || Y ]] 	Or

# File Conditions 
# FILE="test.txt"
# if [ -f "$FILE" ]
# then 
#    echo "$FILE is a file"
# else 
#    echo "$FILE is not a file"
# fi

# [[ -e FILE ]] 	Exists
# [[ -r FILE ]] 	Readable
# [[ -h FILE ]] 	Symlink
# [[ -d FILE ]] 	Directory
# [[ -w FILE ]] 	Writable
# [[ -s FILE ]] 	Size is > 0 bytes
# [[ -f FILE ]] 	File
# [[ -x FILE ]] 	Executable
# [[ FILE1 -nt FILE2 ]] 	1 is more recent than 2
# [[ FILE1 -ot FILE2 ]] 	2 is more recent than 1
# [[ FILE1 -ef FILE2 ]] 	Same files

# Case Statments 
read -p "Are you 21 or over Y/N " ANSWER
case "$ANSWER" in 
   [yY] | [yY][eE][sS])
      echo "over 21"
      ;;
   [nN] | [nN][oO])
      echo "not over 21"
      ;;
   *)
      echo "please enter y/yes or n/no"
      ;;
esac

# SIMPLE FOR LOOP
NAMES="Homer Marge Lisa Bart" # creating an array is similar to creating a variable, just put a space inbetween each var
for NAME in $NAMES            # for (each) VAR in ARRAY 
   do
      echo "Hello $NAME"
done 

# FOR LOOP TO RENAME FILES 
# (Files already generated with a touch command)
# FILES=$(ls *.txt) # LIST all (*) '.txt' files
# NEW="new"
# for FILE in $FILES
#    do 
#       echo "Renaming $FILE to new-$FILE"
#       mv $FILE $NEW-$FILE
# done

# WHILE LOOP  - READ THROUGH A FILE LINE BY LINE
LINE=1                            # $LINE starts at 1
while read -r CURRENT_LINE        # Read files current line
   do 
      echo "$LINE: $CURRENT_LINE" # Print [line number] : [line text]
      ((LINE ++))                 # Add 1 to $LINE
done < "./2.txt"                  # This means that this loop is redirected so that it runs in the named file (in this case 1.txt), instead of the current directory


# FUNCTION (methods)
function sayHello() {
   echo "Hello World"
} 

sayHello


# FUNCTION WITH PARAMS (Parameters)
function greet() {
   echo "Hello, I am $1 and I am $2" # These are positional parameters, meaning that data is assigned to the variables based on the order it comes in.
}

greet "George" "24"

# Create folder and write to command line
mkdir hello 
touch "hello/world.txt"
echo "hello world"
