#! /bin/bash
#создание файла сериализации модулей (erializers.py) по input_struct.txt
sed -f tk_serializer.sed input_nsi_struct.txt | 
sed /^$/d | 
sed 's/^class /\n\nclass /' | 
sed "s/fields = (/fields = (\n            'id',(ggg)/" | 
sed "s/(ggg)/\n            'from_date',(ggg)/" |
sed "s/(ggg)/\n            'to_date',(ggg)/" |
sed "s/(ggg)/\n            'modify_date',(ggg)/" |
sed "s/(ggg)/\n            'hash',(ggg)/" |
sed 's/(ggg)//' |
sed 's/class airports_rusSerializer(serializers.ModelSerializer):/from rest_framework import serializers\nclass airports_rusSerializer(serializers.ModelSerializer):'/ |
sed 's/class airports_rusSerializer(serializers.ModelSerializer):/from nsi import models\n(ggg)\nclass airports_rusSerializer(serializers.ModelSerializer):'/ |
sed 's/(ggg)/\nclass tablemapSerializer(serializers.ModelSerializer):(ggg)/' |
sed 's/(ggg)/\n    class Meta:(ggg)/' |
sed 's/(ggg)/\n        model = models.tablemap(ggg)/' |
sed 's/(ggg)/\n        fields = ((ggg)/' |
sed "s/(ggg)/\n            'id',(ggg)/" |
sed "s/(ggg)/\n            'name',(ggg)/" |
sed "s/(ggg)/\n            'description',(ggg)/" |
sed "s/(ggg)/\n            'modify_date',(ggg)/" |
sed "s/(ggg)/\n            'hash',(ggg)/" |
sed 's/(ggg)/\n        )\n\n(ggg)/' |
sed 's/(ggg)//' |
sed '/^ \+$/d' |
sed 's/ \+$//' |
#sed 1,2 s/)/from rest_framework import serializers\nfrom nsi import models\n/ |
#sed $ s/$/)/ |
tee serializers.py 
