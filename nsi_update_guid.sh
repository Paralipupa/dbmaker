#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f nsi_update_guid.sed input_nsi_tables.txt | 
tee nsi_update_guid.sql

