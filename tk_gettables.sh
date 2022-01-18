#! /bin/bash
# список таблиц nsi_ БД 
docker exec db psql -U postgres -d tn -c "\d" | grep tk_ | grep -v id_seq | awk '{print $3}' > tk_input_tables.txt