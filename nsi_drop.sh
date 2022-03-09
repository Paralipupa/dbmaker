#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f nsi_drop.sed input_nsi_tables.txt | tee nsi_drop.sql

