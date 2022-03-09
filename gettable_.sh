#! /bin/bash
# список таблиц nsi_ БД 
docker exec db psql -U postgres -d tn -c "\d" | grep _tndti14  | grep -v id_seq | awk '{print $3}' > input_table.txt
