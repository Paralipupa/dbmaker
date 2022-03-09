#! /bin/bash
#структура таблиц БД в файл input_struct.txt
while read in; do docker exec db psql -U postgres -d tn -c "\d $in"; done < input_nsi_tables.txt > input_nsi_struct.txt
