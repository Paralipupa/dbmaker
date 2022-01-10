#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f sed_stru.txt input_struct.txt > output_struct.txt
#sed /^$/d output_struct.txt output_struct.txt
