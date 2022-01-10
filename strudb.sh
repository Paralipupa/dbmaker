#! /bin/bash


while read in; do docker exec db psql -U postgres -d tn -c "\d $in"; done < input.txt > input_struct.txt
