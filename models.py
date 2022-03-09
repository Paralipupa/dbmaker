
from django.db import models
from nsi.models import NsiModel

class nsi_airports_rus(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_airports_rus'
    @property
    def title(self):
        return ''
    code_iata = models.CharField(blank=True, null=True, max_length=255)
    name      = models.CharField(blank=True, null=True, max_length=255)
    city      = models.CharField(blank=True, null=True, max_length=255)
    key       = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_countries(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_countries'
    @property
    def title(self):
        return ''
    abc2           = models.CharField(blank=True, null=True, max_length=2)
    abc3           = models.CharField(blank=True, null=True, max_length=3)
    code           = models.CharField(blank=True, null=True, max_length=3)
    short_name     = models.CharField(blank=True, null=True, max_length=40)
    name           = models.CharField(blank=True, null=True, max_length=250)
    name_eng       = models.CharField(blank=True, null=True, max_length=100)
    classification = models.TextField(blank=True, null=True)
    key            = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_currency_code(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_currency_code'
    @property
    def title(self):
        return ''
    code       = models.CharField(blank=True, null=True, max_length=3)
    abc3       = models.CharField(blank=True, null=True, max_length=3)
    short_name = models.CharField(blank=True, null=True, max_length=17)
    name       = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)  = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)    = models.DateTimeField(blank=True, null=True)
    key        = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_customs(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs'
    @property
    def title(self):
        return ''
    country_code = models.CharField(blank=True, null=True, max_length=2)
    code         = models.CharField(blank=True, null=True, max_length=8)
    name         = models.CharField(blank=True, null=True, max_length=50)
    city         = models.CharField(blank=True, null=True, max_length=30)
    address      = models.CharField(blank=True, null=True, max_length=255)
    phone        = models.CharField(blank=True, null=True, max_length=20)
    oldcode      = models.CharField(blank=True, null=True, max_length=8)
    code5        = models.CharField(blank=True, null=True, max_length=5)
    from_DateField(blank=True, null=True)    = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    key          = models.CharField(blank=True, null=True, max_length=8)
    @property
    def queries(self):
            return ''


class nsi_customs_ced(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs_ced'
    @property
    def title(self):
        return ''
    code           = models.CharField(blank=True, null=True, max_length=8)
    name           = models.CharField(blank=True, null=True, max_length=50)
    code_ced       = models.CharField(blank=True, null=True, max_length=255)
    ced_name       = models.CharField(blank=True, null=True, max_length=50)
    transport_kind = models.TextField(blank=True, null=True)
    notes          = models.CharField(blank=True, null=True, max_length=255)
    order_number   = models.CharField(blank=True, null=True, max_length=255)
    order_DateField(blank=True, null=True)     = models.DateTimeField(blank=True, null=True)
    from_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    key            = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_customs_hierarchy(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs_hierarchy'
    @property
    def title(self):
        return ''
    code                = models.CharField(blank=True, null=True, max_length=8)
    name                = models.CharField(blank=True, null=True, max_length=50)
    customs_code        = models.CharField(blank=True, null=True, max_length=255)
    customs_name        = models.CharField(blank=True, null=True, max_length=50)
    customs_office_code = models.CharField(blank=True, null=True, max_length=255)
    customs_office_name = models.CharField(blank=True, null=True, max_length=50)
    key                 = models.CharField(blank=True, null=True, max_length=8)
    @property
    def queries(self):
            return ''


class nsi_customs_payments_kind(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs_payments_kind'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=4)
    name      = models.TextField(blank=True, null=True)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=4)
    @property
    def queries(self):
            return ''


class nsi_customs_procedures_kind(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs_procedures_kind'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=2)
    name      = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=2)
    @property
    def queries(self):
            return ''


class nsi_customs_region(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs_region'
    @property
    def title(self):
        return ''
    code         = models.CharField(blank=True, null=True, max_length=8)
    name         = models.CharField(blank=True, null=True, max_length=50)
    region       = models.TextField(blank=True, null=True)
    region_okato = models.CharField(blank=True, null=True, max_length=255)
    order_number = models.CharField(blank=True, null=True, max_length=255)
    order_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    from_DateField(blank=True, null=True)    = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    key          = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_customs_value_determination_kind(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_customs_value_determination_kind'
    @property
    def title(self):
        return ''
    code        = models.CharField(blank=True, null=True, max_length=1)
    description = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)     = models.DateTimeField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=1)
    @property
    def queries(self):
            return ''


class nsi_deal_feature(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_deal_feature'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=2)
    name      = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=2)
    @property
    def queries(self):
            return ''


class nsi_deal_nature(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_deal_nature'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=3)
    name      = models.CharField(blank=True, null=True, max_length=250)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_delivery_terms(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_delivery_terms'
    @property
    def title(self):
        return ''
    code_d    = models.TextField(blank=True, null=True)
    code      = models.CharField(blank=True, null=True, max_length=3)
    name      = models.CharField(blank=True, null=True, max_length=100)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_doc_reference(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_doc_reference'
    @property
    def title(self):
        return ''
    code           = models.CharField(blank=True, null=True, max_length=5)
    documentgroup  = models.CharField(blank=True, null=True, max_length=2)
    description    = models.TextField(blank=True, null=True)
    documentmodeid = models.CharField(blank=True, null=True, max_length=8)
    documentname   = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    key            = models.TextField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_doc_reference_ex(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_doc_reference_ex'
    @property
    def title(self):
        return ''
    code           = models.CharField(blank=True, null=True, max_length=5)
    documentgroup  = models.CharField(blank=True, null=True, max_length=2)
    description    = models.TextField(blank=True, null=True)
    documentmodeid = models.CharField(blank=True, null=True, max_length=8)
    documentname   = models.CharField(blank=True, null=True, max_length=255)
    key            = models.TextField(blank=True, null=True)
    from_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    end_DateField(blank=True, null=True)       = models.DateTimeField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_intellectual(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_intellectual'
    @property
    def title(self):
        return ''
    code               = models.CharField(blank=True, null=True, max_length=25)
    description        = models.CharField(blank=True, null=True, max_length=50)
    inn                = models.CharField(blank=True, null=True, max_length=12)
    kpp                = models.CharField(blank=True, null=True, max_length=9)
    company_name       = models.CharField(blank=True, null=True, max_length=254)
    company_name_en    = models.CharField(blank=True, null=True, max_length=254)
    company_address    = models.CharField(blank=True, null=True, max_length=254)
    company_address_en = models.CharField(blank=True, null=True, max_length=254)
    note               = models.CharField(blank=True, null=True, max_length=100)
    order_number       = models.CharField(blank=True, null=True, max_length=10)
    order_DateField(blank=True, null=True)         = models.DateTimeField(blank=True, null=True)
    full_description   = models.TextField(blank=True, null=True)
    full_description_2 = models.TextField(blank=True, null=True)
    to_DateField(blank=True, null=True)            = models.DateTimeField(blank=True, null=True)
    key                = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_intellectual_documents(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_intellectual_documents'
    @property
    def title(self):
        return ''
    code          = models.CharField(blank=True, null=True, max_length=25)
    document      = models.CharField(blank=True, null=True, max_length=25)
    document_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    key           = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_intellectual_ex(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_intellectual_ex'
    @property
    def title(self):
        return ''
    code                = models.CharField(blank=True, null=True, max_length=25)
    description         = models.CharField(blank=True, null=True, max_length=50)
    inn                 = models.CharField(blank=True, null=True, max_length=12)
    kpp                 = models.CharField(blank=True, null=True, max_length=9)
    company_name        = models.CharField(blank=True, null=True, max_length=254)
    company_name_en     = models.CharField(blank=True, null=True, max_length=254)
    company_address     = models.CharField(blank=True, null=True, max_length=254)
    company_address_en  = models.CharField(blank=True, null=True, max_length=254)
    note                = models.CharField(blank=True, null=True, max_length=100)
    order_number        = models.CharField(blank=True, null=True, max_length=10)
    order_DateField(blank=True, null=True)          = models.DateTimeField(blank=True, null=True)
    full_description    = models.TextField(blank=True, null=True)
    full_description_2  = models.TextField(blank=True, null=True)
    key                 = models.TextField(blank=True, null=True)
    picture_description = models.CharField(blank=True, null=True, max_length=255)
    picture_file_name   = models.TextField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_intellectual_trade_marks(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_intellectual_trade_marks'
    @property
    def title(self):
        return ''
    code              = models.CharField(blank=True, null=True, max_length=255)
    description       = models.CharField(blank=True, null=True, max_length=255)
    picture_file_name = models.TextField(blank=True, null=True)
    key               = models.TextField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_mnt(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_mnt'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=2)
    name      = models.TextField(blank=True, null=True)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=2)
    @property
    def queries(self):
            return ''


class nsi_movement_of_goods_features(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_movement_of_goods_features'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=3)
    name      = models.TextField(blank=True, null=True)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_package(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_package'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=2)
    name      = models.CharField(blank=True, null=True, max_length=255)
    name_eng  = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    key       = models.CharField(blank=True, null=True, max_length=2)
    @property
    def queries(self):
            return ''


class nsi_payment_code(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_payment_code'
    @property
    def title(self):
        return ''
    code   = models.CharField(blank=True, null=True, max_length=2)
    name   = models.CharField(blank=True, null=True, max_length=255)
    key    = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_payment_way_code(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_payment_way_code'
    @property
    def title(self):
        return ''
    country_ab2 = models.CharField(blank=True, null=True, max_length=2)
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_personal_document_kind(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_personal_document_kind'
    @property
    def title(self):
        return ''
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=75)
    abbr        = models.CharField(blank=True, null=True, max_length=6)
    series_mask = models.CharField(blank=True, null=True, max_length=11)
    number_mask = models.CharField(blank=True, null=True, max_length=25)
    comment     = models.CharField(blank=True, null=True, max_length=120)
    key         = models.CharField(blank=True, null=True, max_length=2)
    @property
    def queries(self):
            return ''


class nsi_personal_document_kind_155(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_personal_document_kind_155'
    @property
    def title(self):
        return ''
    country_code     = models.CharField(blank=True, null=True, max_length=2)
    doc_type_code    = models.CharField(blank=True, null=True, max_length=2)
    code             = models.CharField(blank=True, null=True, max_length=7)
    name             = models.CharField(blank=True, null=True, max_length=255)
    citizenship_mark = models.CharField(blank=True, null=True, max_length=10)
    from_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)          = models.DateTimeField(blank=True, null=True)
    key              = models.CharField(blank=True, null=True, max_length=7)
    @property
    def queries(self):
            return ''


class nsi_preferences_kind(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_preferences_kind'
    @property
    def title(self):
        return ''
    code                       = models.CharField(blank=True, null=True, max_length=2)
    apply_to                   = models.CharField(blank=True, null=True, max_length=1)
    name                       = models.TextField(blank=True, null=True)
    use_in_by                  = models.FloatField(blank=True, null=True)
    use_in_kz                  = models.FloatField(blank=True, null=True)
    use_in_rf                  = models.FloatField(blank=True, null=True)
    use_in_am                  = models.FloatField(blank=True, null=True)
    procedures_mask            = models.CharField(blank=True, null=True, max_length=255)
    procedures_mask_order      = models.CharField(blank=True, null=True, max_length=255)
    procedures_mask_order_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    from_DateField(blank=True, null=True)                  = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)                    = models.DateTimeField(blank=True, null=True)
    key                        = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_rw_stations(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_rw_stations'
    @property
    def title(self):
        return ''
    code5        = models.CharField(blank=True, null=True, max_length=10)
    code         = models.CharField(blank=True, null=True, max_length=255)
    name         = models.CharField(blank=True, null=True, max_length=100)
    name_eng     = models.CharField(blank=True, null=True, max_length=255)
    abbr         = models.CharField(blank=True, null=True, max_length=255)
    road_code    = models.CharField(blank=True, null=True, max_length=3)
    country_code = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)    = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    key          = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_stations_foreign_links(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_stations_foreign_links'
    @property
    def title(self):
        return ''
    code1    = models.CharField(blank=True, null=True, max_length=6)
    name1    = models.CharField(blank=True, null=True, max_length=100)
    country1 = models.CharField(blank=True, null=True, max_length=2)
    code2    = models.CharField(blank=True, null=True, max_length=6)
    name2    = models.CharField(blank=True, null=True, max_length=100)
    country2 = models.CharField(blank=True, null=True, max_length=2)
    key      = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_tnved(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_tnved'
    @property
    def title(self):
        return ''
    code              = models.CharField(blank=True, null=True, max_length=14)
    parent            = models.IntegerField(blank=True, null=True)
    description       = models.TextField(blank=True, null=True)
    iscode            = models.BooleanField(default=False)
    from_DateField(blank=True, null=True)         = models.date
    to_DateField(blank=True, null=True)           = models.date
    short_description = models.TextField(blank=True, null=True)
    unit_code         = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_tnved_14(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_tnved_14'
    @property
    def title(self):
        return ''
    code      = models.CharField(blank=True, null=True, max_length=10)
    code11    = models.CharField(blank=True, null=True, max_length=1)
    code12    = models.CharField(blank=True, null=True, max_length=1)
    code13    = models.CharField(blank=True, null=True, max_length=1)
    code14    = models.CharField(blank=True, null=True, max_length=1)
    name11    = models.CharField(blank=True, null=True, max_length=255)
    name12    = models.CharField(blank=True, null=True, max_length=255)
    name13    = models.CharField(blank=True, null=True, max_length=255)
    name14    = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True) = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_transport_kind(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_transport_kind'
    @property
    def title(self):
        return ''
    code        = models.CharField(blank=True, null=True, max_length=2)
    description = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)     = models.DateTimeField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=2)
    @property
    def queries(self):
            return ''


class nsi_type_of_vehicles(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_type_of_vehicles'
    @property
    def title(self):
        return ''
    code        = models.CharField(blank=True, null=True, max_length=3)
    description = models.CharField(blank=True, null=True, max_length=130)
    comment     = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)     = models.DateTimeField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_unit(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_unit'
    @property
    def title(self):
        return ''
    code        = models.CharField(blank=True, null=True, max_length=3)
    abbr        = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=255)
    from_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)     = models.DateTimeField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=3)
    @property
    def queries(self):
            return ''


class nsi_warehouse_customs(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_warehouse_customs'
    @property
    def title(self):
        return ''
    country_ab2    = models.CharField(blank=True, null=True, max_length=255)
    customs_code   = models.CharField(blank=True, null=True, max_length=255)
    license_number = models.CharField(blank=True, null=True, max_length=255)
    license_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    owner          = models.CharField(blank=True, null=True, max_length=255)
    offise_address = models.TextField(blank=True, null=True)
    address        = models.TextField(blank=True, null=True)
    phone          = models.CharField(blank=True, null=True, max_length=255)
    website        = models.CharField(blank=True, null=True, max_length=255)
    email          = models.CharField(blank=True, null=True, max_length=255)
    inn            = models.CharField(blank=True, null=True, max_length=255)
    kpp            = models.CharField(blank=True, null=True, max_length=255)
    transport_kind = models.TextField(blank=True, null=True)
    is_exciz       = models.CharField(blank=True, null=True, max_length=255)
    warehouse_type = models.TextField(blank=True, null=True)
    from_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    key            = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_warehouse_temporary(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_warehouse_temporary'
    @property
    def title(self):
        return ''
    country_ab2    = models.CharField(blank=True, null=True, max_length=255)
    customs_code   = models.CharField(blank=True, null=True, max_length=255)
    license_number = models.CharField(blank=True, null=True, max_length=255)
    license_DateField(blank=True, null=True)   = models.DateTimeField(blank=True, null=True)
    owner          = models.CharField(blank=True, null=True, max_length=255)
    offise_address = models.TextField(blank=True, null=True)
    address        = models.TextField(blank=True, null=True)
    phone          = models.CharField(blank=True, null=True, max_length=255)
    website        = models.CharField(blank=True, null=True, max_length=255)
    email          = models.CharField(blank=True, null=True, max_length=255)
    inn            = models.CharField(blank=True, null=True, max_length=255)
    kpp            = models.CharField(blank=True, null=True, max_length=255)
    transport_kind = models.TextField(blank=True, null=True)
    is_exciz       = models.CharField(blank=True, null=True, max_length=255)
    warehouse_type = models.TextField(blank=True, null=True)
    from_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    key            = models.CharField(blank=True, null=True, max_length=255)
    @property
    def queries(self):
            return ''


class nsi_economic_operator(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_economic_operator'
    @property
    def title(self):
        return ''
    country_ab2    = models.CharField(blank=True, null=True, max_length=2)
    license_number = models.CharField(blank=True, null=True, max_length=25)
    pr_per         = models.CharField(blank=True, null=True, max_length=1)
    n_blank        = models.CharField(blank=True, null=True, max_length=10)
    from_DateField(blank=True, null=True)      = models.DateTimeField(blank=True, null=True)
    to_DateField(blank=True, null=True)        = models.DateTimeField(blank=True, null=True)
    owner          = models.CharField(blank=True, null=True, max_length=255)
    opf_vl         = models.CharField(blank=True, null=True, max_length=5)
    post           = models.CharField(blank=True, null=True, max_length=9)
    region         = models.CharField(blank=True, null=True, max_length=50)
    city           = models.CharField(blank=True, null=True, max_length=35)
    street         = models.CharField(blank=True, null=True, max_length=50)
    phone          = models.CharField(blank=True, null=True, max_length=100)
    email          = models.CharField(blank=True, null=True, max_length=100)
    website        = models.CharField(blank=True, null=True, max_length=100)
    ogrn           = models.CharField(blank=True, null=True, max_length=15)
    inn            = models.CharField(blank=True, null=True, max_length=20)
    okpo           = models.CharField(blank=True, null=True, max_length=10)
    osp            = models.CharField(blank=True, null=True, max_length=1)
    change_DateField(blank=True, null=True)    = models.DateTimeField(blank=True, null=True)
    doc_number_beg = models.CharField(blank=True, null=True, max_length=20)
    doc_DateField(blank=True, null=True)_beg   = models.DateTimeField(blank=True, null=True)
    doc_number_end = models.CharField(blank=True, null=True, max_length=20)
    doc_DateField(blank=True, null=True)_end   = models.DateTimeField(blank=True, null=True)
    doc_number_sus = models.CharField(blank=True, null=True, max_length=20)
    doc_DateField(blank=True, null=True)_sus   = models.DateTimeField(blank=True, null=True)
    key            = models.TextField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_dutyfree(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_dutyfree'
    @property
    def title(self):
        return ''
    customs_code   = models.CharField(blank=True, null=True, max_length=255)
    name           = models.CharField(blank=True, null=True, max_length=255)
    nsved          = models.CharField(blank=True, null=True, max_length=255)
    license_DateField(blank=True, null=True)   = models.CharField(blank=True, null=True, max_length=255)
    owner          = models.CharField(blank=True, null=True, max_length=255)
    offise_address = models.CharField(blank=True, null=True, max_length=255)
    inn            = models.CharField(blank=True, null=True, max_length=255)
    address        = models.CharField(blank=True, null=True, max_length=255)
    area           = models.CharField(blank=True, null=True, max_length=255)
    kategor        = models.CharField(blank=True, null=True, max_length=255)
    obesp          = models.CharField(blank=True, null=True, max_length=255)
    addinfo        = models.CharField(blank=True, null=True, max_length=255)
    key            = models.TextField(blank=True, null=True)
    @property
    def queries(self):
            return ''


class nsi_warehouse_free(NsiModel):
    @property
    def table_name(self):
        return 'tk_nsi_warehouse_free'
    @property
    def title(self):
        return ''
    country_ab2      = models.CharField(blank=True, null=True, max_length=255)
    doc_number       = models.CharField(blank=True, null=True, max_length=255)
    doc_DateField(blank=True, null=True)         = models.DateTimeField(blank=True, null=True)
    name             = models.CharField(blank=True, null=True, max_length=255)
    address          = models.TextField(blank=True, null=True)
    inn              = models.CharField(blank=True, null=True, max_length=255)
    area             = models.CharField(blank=True, null=True, max_length=255)
    customsauthority = models.CharField(blank=True, null=True, max_length=255)
    kindofactivity   = models.CharField(blank=True, null=True, max_length=255)
    addinfo          = models.CharField(blank=True, null=True, max_length=255)
    active           = models.CharField(blank=True, null=True, max_length=255)
    key              = models.TextField(blank=True, null=True)
    @property
    def queries(self):
            return ''

