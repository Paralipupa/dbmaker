#! /bin/bash
#создание файла сериализации модулей (erializers.py) по input_struct.txt
sed -f sed_serializer.txt input_struct.txt | 
sed /^$/d | 
sed 's/^class /\n\nclass /' | 
sed "s/fields = (/fields = (\n            'guid',/" | 
tee serializers.py 
