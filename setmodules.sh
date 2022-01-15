#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f sed_stru.txt input_struct.txt | 
sed /^$/d | 
sed 's/^class /\n\nclass /' | 
sed 's/(models.Model):/(models.Model):\n    guid        = models.CharField(max_length=32)(ggg)/' |
sed 's/(ggg)/\n    begin_date  = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)//' |
sed 's/class airports_rus(models.Model):/from django.db import models\n(ggg)\nclass airports_rus(models.Model):/' |
sed 's/(ggg)/\nclass tablemap(models.Model):(ggg)/' |
sed 's/(ggg)/\n    name = models.CharField(max_length=50, blank=False, null=False)(ggg)/' |
sed 's/(ggg)/\n    description = models.CharField(max_length=250, blank=True, null=False)(ggg)/' |
sed 's/(ggg)/\n    modify_date = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    hash        = models.CharField(max_length=32, blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    class Meta:(ggg)/' |
sed "s/(ggg)/\n        unique_together = ('name',)\n(ggg)/" |
sed 's/(ggg)/\nclass keymap(models.Model):(ggg)/' |
sed 's/(ggg)/\n    table_id    = models.IntegerField(blank=False, null=False)(ggg)/' |
sed 's/(ggg)/\n    guid        = models.CharField(max_length=32)(ggg)/' |
sed 's/(ggg)/\n    modify_date = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    hash        = models.CharField(blank=True, null=True, max_length=32)\n(ggg)/' |
sed 's/(ggg)//' |
tee models.py 
