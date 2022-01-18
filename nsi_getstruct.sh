#! /bin/bash
#структура таблиц БД в файл input_struct.txt
while read in; do docker exec db psql -U postgres -d tn -c "\d $in"; done < nsi_input_tables.txt > nsi_input_struct.txt
