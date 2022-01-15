#! /bin/bash
#создание файла сериализации модулей (erializers.py) по input_struct.txt
sed -f sed_update.txt input_tables.txt | 
tee exportupdate.py 
