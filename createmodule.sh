while read y
do
   docker exec db psql -U postgres -d tn -c "\d $y" 
done < input.txt > intput_stru.txt
