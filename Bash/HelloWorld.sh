#!/bin/bash
echo "what is your name?"
read name 
echo "Hello $name"
echo "${name}"

# Both of the below commands peform the same action
echo "im in $(pwd)"
echo "im in `pwd`"

