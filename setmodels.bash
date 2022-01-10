#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f sed_stru.txt input_struct.txt | sed /^$/d | sed 's/^class /\n\nclass /' | tee models.py 
