s/[-+ ]\+//
s/Column[ |a-zA-Z]\+//
s/| /= models./1
s/|[0-9a-zA-Z ()':|_]\+//
s/integer/IntegerField(blank=True, null=True)/
s/double precision/FloatField(blank=True, null=True)/
s/character varying(/CharField(max_length=/
s/character varying/CharField(max_length=255)/
s/CharField(/CharField(blank=True, null=True, /
s/boolean/BooleanField(default=False)/
s/text/TextField(blank=True, null=True)/
s/timestamp with time zone/DateTimeField(blank=True, null=True)/
s/timestamp without time zone/DateTimeField(blank=True, null=True)/
s/Table "public./class /
s/"//
/\(^class .*\)/s//\1(HashMixin, CommonInfo):/
/\(.*= models.*\)/s//    \1/
/^Indexes:.*/s///
/.*PRIMARY KEY.*/s///
/ \+id.*/s///
/ \+guid.*/s///
/ \+hash.*/s///
/ \+from_date.*/s///
/ \+to_date.*/s///
/ \+modify_date.*/s///
s/nsi_//
