#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f sed_models.txt input_struct.txt | 
sed /^$/d | 
sed 's/^class /\n\nclass /' |
sed 's/(models.Model):/(models.Model):\n    guid = models.CharField(max_length=32)/' |
tee models.py 
