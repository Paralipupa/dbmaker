#! /bin/bash
# список таблиц nsi_ БД 
docker exec db psql -U postgres -d tn -c "\d" | grep nsi_ | grep -v id_seq | awk '{print $3}' > input_tables.txt