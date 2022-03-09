#! /bin/bash
# список таблиц nsi_ БД 
docker exec db psql -U postgres -d tn -c "\d" | grep tk_nsi_ | grep -v id_seq | awk '{print $3}' > input_nsi_tables.txt