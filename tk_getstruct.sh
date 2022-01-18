#! /bin/bash
#структура таблиц БД в файл input_struct.txt
while read in; do docker exec db psql -U postgres -d tn -c "\d $in"; done < tk_input_tables.txt > tk_input_struct.txt
