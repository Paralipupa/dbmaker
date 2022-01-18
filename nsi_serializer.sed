s/[-+ ]\+//
s/Column[ |a-zA-Z]\+//
s/Table "public./class /
s/"//
/\(^class \)nsi_\(.*\)/s//\1\2Serializer(serializers.ModelSerializer):\n    class Meta:\n        model = models.\2\n        fields = (/
/^Indexes:.*/s///
/.*PRIMARY KEY.*/s///
/^id \+/s///
s/\([a-zA-Z0-9_]\+\) \+|[0-9a-zA-Z ()':|_]\+/            '\1',/
s/|[0-9a-zA-Z ()':|_]\+//
s/^,$//
s/'key',/)/
s/'guid',//
s/'from_date',//
s/'to_date',//
s/'modify_date',//
s/'hash',//
#s/'key',/'key',\n        )/




