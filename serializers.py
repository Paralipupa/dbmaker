

class airports_rusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.airports_rus
        fields = (
            'guid',
            'code_iata',
            'name',
            'city',
            'key',
        )


class ati_citiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ati_cities
        fields = (
            'guid',
            'city_id',
            'region_id',
            'country_id',
            'city',
            'region',
            'country',
            'key',
        )


class ati_customs_mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ati_customs_map
        fields = (
            'guid',
            'country_code',
            'customs_code',
            'customs_city',
            'ati_city',
            'ati_city_id',
            'key',
        )


class car_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.car_type
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.color
        fields = (
            'guid',
            'code',
            'description',
            'key',
        )


class countriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.countries
        fields = (
            'guid',
            'abc2',
            'abc3',
            'code',
            'short_name',
            'name',
            'name_eng',
            'classification',
            'key',
        )


class currency_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.currency_code
        fields = (
            'guid',
            'code',
            'abc3',
            'short_name',
            'name',
            'key',
        )


class customsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs
        fields = (
            'guid',
            'country_code',
            'code',
            'name',
            'city',
            'address',
            'phone',
            'oldcode',
            'code5',
            'from_date',
            'key',
        )


class customs_cedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_ced
        fields = (
            'guid',
            'code',
            'name',
            'code_ced',
            'ced_name',
            'transport_kind',
            'notes',
            'order',
            'order_date',
            'from_date',
            'to_date',
            'key',
        )


class customs_hierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_hierarchy
        fields = (
            'guid',
            'code',
            'name',
            'customs_code',
            'customs_name',
            'customs_office_code',
            'customs_office_name',
            'key',
        )


class customs_payments_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_payments_kind
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class customs_procedures_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_procedures_kind
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class customs_regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_region
        fields = (
            'guid',
            'code',
            'name',
            'region',
            'region_okato',
            'order',
            'order_date',
            'from_date',
            'to_date',
            'key',
        )


class customs_value_determination_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_value_determination_kind
        fields = (
            'guid',
            'code',
            'description',
            'key',
        )


class deal_featureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.deal_feature
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class deal_natureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.deal_nature
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class delivery_termsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.delivery_terms
        fields = (
            'guid',
            'code_d',
            'code',
            'name',
            'key',
        )


class edi_container_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.edi_container_type
        fields = (
            'guid',
            'code',
            'code_old',
            'length',
            'width',
            'name',
        )


class edi_wagon_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.edi_wagon_type
        fields = (
            'guid',
            'code',
            'description',
            'abbr',
            'key',
        )


class edi_weight_definition_modeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.edi_weight_definition_mode
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class ensure_payment_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ensure_payment_code
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class forms_of_paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.forms_of_payment
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class hazardous_cargo_code_imoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hazardous_cargo_code_imo
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class hazardous_cargo_code_unSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hazardous_cargo_code_un
        fields = (
            'guid',
            'code',
            'name',
            'class_name',
            'clarrification_code',
        )


class intellectualSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.intellectual
        fields = (
            'guid',
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
            'key',
        )


class intellectual_documentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.intellectual_documents
        fields = (
            'guid',
            'code',
            'document',
            'document_date',
        )


class intellectual_trade_marksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.intellectual_trade_marks
        fields = (
            'guid',
            'code',
            'description',
            'picture_file_name',
            'key',
        )


class mntSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.mnt
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class movement_of_goods_featuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movement_of_goods_features
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.package
        fields = (
            'guid',
            'code',
            'name',
            'name_eng',
            'key',
        )


class package_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.package_type
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class payment_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.payment_code
        fields = (
            'guid',
            'code',
            'name',
            'key',
        )


class payment_termsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.payment_terms
        fields = (
            'guid',
            'code',
            'description',
            'month_count',
            'key',
        )


class payment_way_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.payment_way_code
        fields = (
            'guid',
            'country_ab2',
            'code',
            'name',
            'key',
        )


class personal_document_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.personal_document_kind
        fields = (
            'guid',
            'code',
            'name',
            'abbr',
            'series_mask',
            'number_mask',
            'comment',
            'key',
        )


class personal_document_kind_155Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.personal_document_kind_155
        fields = (
            'guid',
            'country_code',
            'doc_type_code',
            'code',
            'name',
            'citizenship_mark',
            'key',
        )


class pi_usageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.pi_usage
        fields = (
            'guid',
            'code',
            'description',
            'key',
        )


class preferences_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.preferences_kind
        fields = (
            'guid',
            'code',
            'apply_to',
            'name',
            'use_in_by',
            'use_in_kz',
            'use_in_rf',
            'use_in_am',
            'key',
            'procedures_mask',
            'procedures_mask_order',
            'procedures_mask_order_date',
        )


class rw_countriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_countries
        fields = (
            'guid',
            'rw_country_code',
            'name',
            'abbr',
            'country_code',
            'administration_name',
            'abc2',
            'abc3',
            'key',
        )


class rw_roadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_roads
        fields = (
            'guid',
            'road_code',
            'name',
            'abbr',
            'key',
        )


class rw_stationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_stations
        fields = (
            'guid',
            'code5',
            'code',
            'name',
            'name_eng',
            'abbr',
            'road_code',
            'country_code',
            'key',
        )


class rw_stations_customsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_stations_customs
        fields = (
            'guid',
            'code5',
            'code',
            'name',
            'customs_code',
            'curtoms_name',
            'city',
            'address',
            'key',
        )


class stations_foreign_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.stations_foreign_links
        fields = (
            'guid',
            'code1',
            'name1',
            'country1',
            'code2',
            'name2',
            'country2',
            'key',
        )


class transit_measures_of_ensuringSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.transit_measures_of_ensuring
        fields = (
            'guid',
            'code',
            'description',
            'key',
        )


class transport_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.transport_kind
        fields = (
            'guid',
            'code',
            'description',
            'key',
        )


class type_of_vehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.type_of_vehicles
        fields = (
            'guid',
            'code',
            'description',
            'comment',
            'key',
        )


class unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.unit
        fields = (
            'guid',
            'code',
            'abbr',
            'description',
            'key',
        )


class vmtp_countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vmtp_country
        fields = (
            'guid',
            'vmtp_code',
            'country_code',
            'name',
        )


class warehouse_customsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.warehouse_customs
        fields = (
            'guid',
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
            'key',
        )


class warehouse_temporarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.warehouse_temporary
        fields = (
            'guid',
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
            'key',
        )
