#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f sed_del.txt input_tables.txt | tee del_nsi.sql

