

from rest_framework import serializers
from nsi import models

class tablemapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tablemap
        fields = (
            'id',
            'name',
            'description',
            'modify_date',
        )


class airports_rusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.airports_rus
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code_iata',
            'name',
            'city',
            )


class ati_citiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ati_cities
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'city_id',
            'region_id',
            'country_id',
            'city',
            'region',
            'country',
            )


class ati_customs_mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ati_customs_map
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'country_code',
            'customs_code',
            'customs_city',
            'ati_city',
            'ati_city_id',
            )


class car_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.car_type
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.color
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            )


class countriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.countries
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'abc2',
            'abc3',
            'code',
            'short_name',
            'name',
            'name_eng',
            'classification',
            )


class currency_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.currency_code
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'abc3',
            'short_name',
            'name',
            )


class customsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'country_code',
            'code',
            'name',
            'city',
            'address',
            'phone',
            'oldcode',
            'code5',
            )


class customs_cedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_ced
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            'code_ced',
            'ced_name',
            'transport_kind',
            'notes',
            'order',
            'order_date',
            )


class customs_hierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_hierarchy
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            'customs_code',
            'customs_name',
            'customs_office_code',
            'customs_office_name',
            )


class customs_payments_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_payments_kind
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class customs_procedures_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_procedures_kind
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class customs_regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_region
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            'region',
            'region_okato',
            'order',
            'order_date',
            )


class customs_value_determination_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customs_value_determination_kind
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            )


class deal_featureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.deal_feature
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class deal_natureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.deal_nature
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class delivery_termsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.delivery_terms
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code_d',
            'code',
            'name',
            )


class edi_container_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.edi_container_type
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
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
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            'abbr',
            )


class edi_weight_definition_modeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.edi_weight_definition_mode
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class ensure_payment_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ensure_payment_code
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class forms_of_paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.forms_of_payment
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class hazardous_cargo_code_imoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hazardous_cargo_code_imo
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class hazardous_cargo_code_unSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hazardous_cargo_code_un
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            'classification_type',
            'classification_code',
            )


class intellectualSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.intellectual
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
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


class intellectual_documentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.intellectual_documents
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'document',
            'document_date',
            )


class intellectual_trade_marksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.intellectual_trade_marks
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            'picture_file_name',
            )


class mntSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.mnt
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class movement_of_goods_featuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movement_of_goods_features
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.package
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            'name_eng',
            )


class package_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.package_type
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class payment_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.payment_code
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            )


class payment_termsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.payment_terms
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            'month_count',
            )


class payment_way_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.payment_way_code
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'country_ab2',
            'code',
            'name',
            )


class personal_document_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.personal_document_kind
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'name',
            'abbr',
            'series_mask',
            'number_mask',
            'comment',
            )


class personal_document_kind_155Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.personal_document_kind_155
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'country_code',
            'doc_type_code',
            'code',
            'name',
            'citizenship_mark',
            )


class pi_usageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.pi_usage
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            )


class preferences_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.preferences_kind
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
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


class rw_countriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_countries
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'rw_country_code',
            'name',
            'abbr',
            'country_code',
            'administration_name',
            'abc2',
            'abc3',
            )


class rw_roadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_roads
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'road_code',
            'name',
            'abbr',
            )


class rw_stationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_stations
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code5',
            'code',
            'name',
            'name_eng',
            'abbr',
            'road_code',
            'country_code',
            )


class rw_stations_customsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.rw_stations_customs
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code5',
            'code',
            'name',
            'customs_code',
            'curtoms_name',
            'city',
            'address',
            )


class stations_foreign_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.stations_foreign_links
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code1',
            'name1',
            'country1',
            'code2',
            'name2',
            'country2',
            )


class transit_measures_of_ensuringSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.transit_measures_of_ensuring
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            )


class transport_kindSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.transport_kind
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            )


class type_of_vehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.type_of_vehicles
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'description',
            'comment',
            )


class unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.unit
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'code',
            'abbr',
            'description',
            )


class vmtp_countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vmtp_country
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
            'vmtp_code',
            'country_code',
            'name',
            )


class warehouse_customsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.warehouse_customs
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
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


class warehouse_temporarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.warehouse_temporary
        fields = (
            'guid',
            'from_date',
            'to_date',
            'modify_date',
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
