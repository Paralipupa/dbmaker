#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f tk_models.sed input_nsi_struct.txt | 
sed /^$/d | 
sed 's/^class /\nclass /' | 
sed 's/class nsi_airports_rus(NsiModel):/from django.db import models(ggg)\nclass nsi_airports_rus(NsiModel):/' |
sed 's/(ggg)/\nfrom nsi.models import NsiModel\n(ggg)/' |
sed 's/(hhh)/    @property\n(hhh)/' |
sed 's/(hhh)/    def queries(self):\n(hhh)/' |
sed "s/(hhh)/            return ''\n(hhh)/" |
sed 's/(ggg)//' |
sed 's/(hhh)//' |
sed 's/ \+$//' |
tee models.py 

