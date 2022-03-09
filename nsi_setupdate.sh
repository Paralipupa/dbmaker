#! /bin/bash
#создание файла сериализации модулей (erializers.py) по input_struct.txt
sed -f nsi_update.sed input_nsi_tables.txt | 
tee exportupdate.py 
