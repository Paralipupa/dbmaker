#! /bin/bash
#создание файла описания модулей (models.py) по input_struct.txt
sed -f tk_sed_models.txt tk_input_struct.txt | 
sed /^$/d | 
sed 's/^class /\nclass /' | 
sed 's/class airports_rus(HashMixin, CommonInfo):/from django.db import models(ggg)\nclass airports_rus(HashMixin, CommonInfo):/' |
sed 's/(ggg)/\nimport hashlib(ggg)/' |
sed 's/(ggg)/\nfrom django.db.models import AutoField\n(ggg)/' |
sed 's/(ggg)/\n_hashit = lambda s: hashlib.sha1(s).hexdigest()\n(ggg)/' |
sed 's/(ggg)/\nclass tablemap(models.Model):(ggg)/' |
sed 's/(ggg)/\n    name = models.CharField(max_length=50, blank=False, null=False)(ggg)/' |
sed 's/(ggg)/\n    description = models.CharField(max_length=255, blank=True, null=False)(ggg)/' |
sed 's/(ggg)/\n    modify_date = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    ischeck     = models.BooleanField(default=False)(ggg)/' |
sed 's/(ggg)/\n    hash        = models.CharField(max_length=40, blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    class Meta:(ggg)/' |
sed "s/(ggg)/\n        unique_together = ('name',)\n(ggg)/" |
sed 's/(ggg)/\nclass keymap(models.Model):(ggg)/' |
sed 's/(ggg)/\n    name        = models.CharField(max_length=255, blank=True, null=False)(ggg)/' |
sed 's/(ggg)/\n    key         = models.CharField(max_length=255, blank=True, null=False)(ggg)/' |
sed 's/(ggg)/\n    guid        = models.CharField(max_length=36)(ggg)/' |
sed 's/(ggg)/\n    modify_date = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    ischeck     = models.BooleanField(default=False)(ggg)/' |
sed 's/(ggg)/\n    hash        = models.CharField(blank=True, null=True, max_length=40)(ggg)/' |
sed 's/(ggg)/\n    class Meta:(ggg)/' |
sed 's/(ggg)/\n        indexes = [(ggg)/' |
sed "s/(ggg)/\n            models.Index(fields=['guid',]),(ggg)/" |
sed "s/(ggg)/\n            models.Index(fields=['hash',]),(ggg)/" |
sed 's/(ggg)/\n    ]\n(ggg)/' |
sed 's/(ggg)/\nclass CommonInfo(models.Model):(ggg)/' |
sed 's/(ggg)/\n    guid        = models.CharField(max_length=36)(ggg)/' |
sed 's/(ggg)/\n    from_date   = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    to_date     = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    modify_date = models.DateTimeField(blank=True, null=True)(ggg)/' |
sed 's/(ggg)/\n    class Meta:(ggg)/' |
sed "s/(ggg)/\n        abstract = True\n(ggg)/" |
sed 's/(ggg)/\nclass HashMixin(object):(ggg)/' |
sed 's/(ggg)/\n    def _get_hash(self):(ggg)/' |
sed 's/(ggg)/\n        hashed_fields = [str(getattr(self, field.name)) for field in self._meta.fields if(ggg)/' |
sed "s/(ggg)/\n                         not isinstance(field, AutoField) and field.attname != 'modify_date' and field.attname != 'order'](ggg)/" |
sed 's/(ggg)/\n        data = ",".join(hashed_fields)(ggg)/' |
sed "s/(ggg)/\n        return _hashit(data.encode('utf-8'))(ggg)/" |
sed 's/(ggg)/\n    hash = property(_get_hash)\n(ggg)/' |
sed 's/(ggg)//' |
tee tk_models.py 

