#! /bin/bash
#создание файла сериализации модулей (erializers.py) по input_struct.txt
sed -f sed_serializer.txt input_struct.txt | 
sed /^$/d | 
sed 's/^class /\n\nclass /' | 
sed "s/fields = (/fields = (\n            'guid',(ggg)/" | 
sed "s/(ggg)/\n            'from_date',(ggg)/" |
sed "s/(ggg)/\n            'to_date',(ggg)/" |
sed "s/(ggg)/\n            'modify_date',(ggg)/" |
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
sed 's/(ggg)/\n        )\n\n(ggg)/' |
sed 's/(ggg)//' |
sed '/^ \+$/d' |
tee serializers.py 
