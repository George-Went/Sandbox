# While Loops



# For loop 
for i in /etc/rc.*; do
   echo $i
done

for i in 1 2 3 4 5
do
   echo "Looping number $i"
done

# For loop 
# (i starts at 0 ; if i is below 100 ; after every loop + 1)
for ((i = 0 ; i < 10 ; i++)); do
   echo $i 

