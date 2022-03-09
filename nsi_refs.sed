s/nsi_//
s/\(.*\)/    'nsi_\1': {'model':nsimodels.\1, 'serializer':nsiserializers.\1Serializer, 'is_period':False,\\\n      'description':'@\1'},/
