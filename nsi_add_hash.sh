#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f nsi_add_hash.sed input_nsi_tables.txt | 
tee nsi_add_hash.sql

