#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f nsi_add_to_date.sed input_nsi_tables.txt | 
tee nsi_add_to_date.sql

