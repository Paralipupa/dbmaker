

class nsi_airports_rusSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_airports_rus
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code_iata',
            'name',
            'city',
            )


class nsi_countriesSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_countries
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'abc2',
            'abc3',
            'code',
            'short_name',
            'name',
            'name_eng',
            'classification',
            )


class nsi_currency_codeSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_currency_code
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'abc3',
            'short_name',
            'name',
            )


class nsi_customsSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_code',
            'code',
            'name',
            'city',
            'address',
            'phone',
            'oldcode',
            'code5',
            )


class nsi_customs_cedSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs_ced
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            'code_ced',
            'ced_name',
            'transport_kind',
            'notes',
            'order_number',
            'order_date',
            )


class nsi_customs_hierarchySerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs_hierarchy
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            'customs_code',
            'customs_name',
            'customs_office_code',
            'customs_office_name',
            )


class nsi_customs_payments_kindSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs_payments_kind
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_customs_procedures_kindSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs_procedures_kind
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_customs_regionSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs_region
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            'region',
            'region_okato',
            'order_number',
            'order_date',
            )


class nsi_customs_value_determination_kindSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_customs_value_determination_kind
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'description',
            )


class nsi_deal_featureSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_deal_feature
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_deal_natureSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_deal_nature
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_delivery_termsSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_delivery_terms
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code_d',
            'code',
            'name',
            )


class nsi_doc_referenceSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_doc_reference
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'documentgroup',
            'description',
            'documentmodeid',
            'documentname',
            )


class nsi_doc_reference_exSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_doc_reference_ex
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'documentgroup',
            'description',
            'documentmodeid',
            'documentname',
            )
            'end_date',


class nsi_intellectualSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_intellectual
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'description',
            'inn',
            'kpp',
            'company_name',
            'company_name_en',
            'company_address',
            'company_address_en',
            'note',
            'order_number',
            'order_date',
            'full_description',
            'full_description_2',
            )


class nsi_intellectual_documentsSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_intellectual_documents
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'document',
            'document_date',
            )


class nsi_intellectual_exSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_intellectual_ex
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'description',
            'inn',
            'kpp',
            'company_name',
            'company_name_en',
            'company_address',
            'company_address_en',
            'note',
            'order_number',
            'order_date',
            'full_description',
            'full_description_2',
            )
            'picture_description',
            'picture_file_name',


class nsi_intellectual_trade_marksSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_intellectual_trade_marks
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'description',
            'picture_file_name',
            )


class nsi_mntSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_mnt
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_movement_of_goods_featuresSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_movement_of_goods_features
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_packageSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_package
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            'name_eng',
            )


class nsi_payment_codeSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_payment_code
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            )


class nsi_payment_way_codeSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_payment_way_code
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_ab2',
            'code',
            'name',
            )


class nsi_personal_document_kindSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_personal_document_kind
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'name',
            'abbr',
            'series_mask',
            'number_mask',
            'comment',
            )


class nsi_personal_document_kind_155Serializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_personal_document_kind_155
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_code',
            'doc_type_code',
            'code',
            'name',
            'citizenship_mark',
            )


class nsi_preferences_kindSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_preferences_kind
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'apply_to',
            'name',
            'use_in_by',
            'use_in_kz',
            'use_in_rf',
            'use_in_am',
            'procedures_mask',
            'procedures_mask_order',
            'procedures_mask_order_date',
            )


class nsi_rw_stationsSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_rw_stations
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code5',
            'code',
            'name',
            'name_eng',
            'abbr',
            'road_code',
            'country_code',
            )


class nsi_stations_foreign_linksSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_stations_foreign_links
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code1',
            'name1',
            'country1',
            'code2',
            'name2',
            'country2',
            )


class nsi_tnvedSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_tnved
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'parent',
            'description',
            'iscode',
            'short_description',
            'unit_code',


class nsi_tnved_14Serializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_tnved_14
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'code11',
            'code12',
            'code13',
            'code14',
            'name11',
            'name12',
            'name13',
            'name14',


class nsi_transport_kindSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_transport_kind
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'description',
            )


class nsi_type_of_vehiclesSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_type_of_vehicles
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'description',
            'comment',
            )


class nsi_unitSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_unit
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'code',
            'abbr',
            'description',
            )


class nsi_warehouse_customsSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_warehouse_customs
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_ab2',
            'customs_code',
            'license_number',
            'license_date',
            'owner',
            'offise_address',
            'address',
            'phone',
            'website',
            'email',
            'inn',
            'kpp',
            'transport_kind',
            'is_exciz',
            'warehouse_type',
            )


class nsi_warehouse_temporarySerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_warehouse_temporary
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_ab2',
            'customs_code',
            'license_number',
            'license_date',
            'owner',
            'offise_address',
            'address',
            'phone',
            'website',
            'email',
            'inn',
            'kpp',
            'transport_kind',
            'is_exciz',
            'warehouse_type',
            )


class nsi_economic_operatorSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_economic_operator
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_ab2',
            'license_number',
            'pr_per',
            'n_blank',
            'owner',
            'opf_vl',
            'post',
            'region',
            'city',
            'street',
            'phone',
            'email',
            'website',
            'ogrn',
            'inn',
            'okpo',
            'osp',
            'change_date',
            'doc_number_beg',
            'doc_date_beg',
            'doc_number_end',
            'doc_date_end',
            'doc_number_sus',
            'doc_date_sus',
            )


class nsi_dutyfreeSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_dutyfree
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'customs_code',
            'name',
            'nsved',
            'license_date',
            'owner',
            'offise_address',
            'inn',
            'address',
            'area',
            'kategor',
            'obesp',
            'addinfo',
            )


class nsi_warehouse_freeSerializer(NsiSerializer):
    id = serializers.CharField(source='guid')
    class Meta:
        model = models.nsi_warehouse_free
        fields = (
            'id',
            'from_date',
            'to_date',
            'modify_date',
            'hash',
            'country_ab2',
            'doc_number',
            'doc_date',
            'name',
            'address',
            'inn',
            'area',
            'customsauthority',
            'kindofactivity',
            'addinfo',
            'active',
            )
