# Shell Scripts 

## What is a shell 
A shell provides a interface/environment to the unix system.
It gathers inputted data ( usually in the form of a command line) and excecutes the program based on the inputs

The most commonly used shell in unix systems is BASH (Bourne Shell), if you use a terminal to interact with a linux system you will have used bash. All bash commands start with `$`.

when you enter in a command to linux such as `ls` you are executing a single line bash script to interact with the unix operating system (the `$` is automatically added at the start in the terminal).

## Common Commands on Linux
If you've used a terminal on a linux system you will have had experance in using bash. Here are some of the most common commands.

`pwd`: Find out the directory you are in.
`cd`: Change directories
`ls`: list contents of a directory
`cat`: short for conacatonate. List the standard output (`echo and teminal responses) and also join files together.
`cp`: copy files
`mkdir`: move files
`chomd`: change read, write and execute permission of files.


## Creating and Executing Simple Scripts
We can write simple scripts on the terminal command line.
To start off with, we can write 
```bash
$echo Hello World
```
When run (by pressing enter) the terminal will print out `Hello World`.

We can also save bash scripts as files, rather than executing them right after we write them. We can then just call the file name to execute the script. we can store bash scripts with the `.sh` filetype to denaote that they are bash scripts. (Note that in linux, the `/sh` is not needed and is only ther for the user to understand what the file is)

helloWolrd.sh
```bash
#!/bin/bash
echo "what is your name?"
read name 
echo "$name"
```

## Permissions and chmod 
Before we can run the bash script, we have to change the *permissions* of the file tpye. Normally on a computer, a file has to have permissions to operate - you dont want a file in a downloads fodler to be able to change your root filesystem. 

If you run `ls -l` on the above `helloWorld.sh` file you can see that we get:  
```
-rw-rw-r-- 1 username username 61 Oct  6 11:47 HelloWorld.sh
```


The first part is what we are looking for with permissions: `-rw-rw-r--`
This means that the owner and the group he is in can read and write the file, but cannot execute it.

```
-rw-r--r-- 12 username users 12.0K Apr  8 20:51 filename.txt
|[-][-][-]-   [------] [---]
| |  |  | |      |       |
| |  |  | |      |       +-----------> 7. Group
| |  |  | |      +-------------------> 6. Owner
| |  |  | +--------------------------> 5. Alternate Access Method
| |  |  +----------------------------> 4. Others Permissions
| |  +-------------------------------> 3. Group Permissions
| +----------------------------------> 2. Owner Permissions
+------------------------------------> 1. File Type
```

We can chaneg ther permissions in a variety of ways using `chmod`. One of the best examples of a chmod command is `chmod +x`, which changes a files permissions so that it is executable:

helloWorld afert `chmod +x helloWolrd` is run:
```
-rwxrwxr-x 1 username user 61 Oct  6 11:47 HelloWorld.sh
```
This means we can now execute the file.

## Running basic commands
We can create a basic script to print out our current location and the files in the directory
```
#!/bin/sh
pwd # shows the current directory location
ls  # lists the file in the current directory
```

## Adding scripts to $PATH
At the moment, we can only execute the script in the directory that has the .sh file in. We can add the script to the `PATH` which allows us to execute the script while anywhere in the system. 

To find out what directories are in `PATH` we can use either `printenv` or `echo $PATH`.

To add our directory to the PATH, we can use the below command
In my case my files were located under `/home/george/Documents/Programming/Projects/Bash`.

```
export PATH="$HOME/home/george/Documents/Programming/Projects/Bash:$PATH"
```

If we run `printenv` again, we can see the the new directory is added to the front of the PATH string.

**THis only works for the current session**, if closed, the changes made to the PATH [will not persist | will be lost]



>**Note:**`.bashrc` is a file hidden in the home directory, we can see it using `ls -al`)

>**Note:** `~` just means the /home directory, so `cd ~` will take you to the same place that `cd` does.

## Adding Shell scripts to PATH perminantly
If you are using Bash, you can set the $PATH variable in the `~/.bashrc` file, and add your scripts to the end of the file. In my case this was: 
```bash
## ~/directory to be searched after all other directories ##
## (basically path = path + new directory)
export PATH=$PATH:$HOME/Documents/Programming/Projects/Bash
```



## Copy and Paste of some common tasks

```bash
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
```

## Cron Jobs 

### Creating a cron job 
A cron job is just a shell script that will be told by the OS to execute at a set time (such as every hour)

There are some prebuit options when running cronjobs, you can place scripts into either:
```
/etc/cron.daily
/etc/cron.hourlyT
/etc/cron.monthly
/etc/cron.weekly
```
Any scripts placed in these files will run 

### Crontab
If You need a script to be executed in a more precise fashion, each user has a crontab - a file/ list of crojobs with executions specifed by the user.

Any users running cron jobs can be found by running the command ```crontab -l``` which will show that users current cron jobs that are running in the background.

To display the crontabs of other users (such as root) use:
```crontab -u root -l```

To edit the current crontab, we can use: 
```crontab -e```

crontabs are set using: 
```[minute] [hour] [day-of-month] [month] [day-of-week] [command]```

So to run a command every Monday at 5:30 in the afternoon:
```30 17 * * 1 /path/to/command```

or every 15 minutes:
```*/15 * * * * /path/to/command```

There are also online resources to help set up crojobs such as [Crontab Guru](https://crontab.guru/)