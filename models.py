
from django.db import models
import hashlib
from django.db.models import AutoField

_hashit = lambda s: hashlib.sha1(s).hexdigest()

class tablemap(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=False)
    modify_date = models.DateTimeField(blank=True, null=True)
    ischeck     = models.BooleanField(default=False)
    hash        = models.CharField(max_length=40, blank=True, null=True)
    class Meta:
        unique_together = ('name',)

class keymap(models.Model):
    name        = models.CharField(max_length=255, blank=True, null=False)
    key         = models.CharField(max_length=255, blank=True, null=False)
    guid        = models.CharField(max_length=36)
    modify_date = models.DateTimeField(blank=True, null=True)
    ischeck     = models.BooleanField(default=False)
    hash        = models.CharField(blank=True, null=True, max_length=40)
    class Meta:
        indexes = [
            models.Index(fields=['guid',]),
            models.Index(fields=['hash',]),
    ]

class CommonInfo(models.Model):
    guid        = models.CharField(max_length=36)
    hash        = models.CharField(max_length=40, blank=True, null=True)
    from_date   = models.DateTimeField(blank=True, null=True)
    to_date     = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        abstract = True

class HashMixin(object):
    def _get_hash(self):
        hashed_fields = [str(getattr(self, field.name)) for field in self._meta.fields if
                         not isinstance(field, AutoField) and field.attname != 'modify_date' and field.attname != 'order']
        data = ",".join(hashed_fields)
        return _hashit(data.encode('utf-8'))
    hash_calculate = property(_get_hash)

class airports_rus(HashMixin, CommonInfo):
    code_iata   = models.CharField(blank=True, null=True, max_length=255)
    name        = models.CharField(blank=True, null=True, max_length=255)
    city        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=255)

class ati_cities(HashMixin, CommonInfo):
    city_id     = models.IntegerField(blank=True, null=True)
    region_id   = models.IntegerField(blank=True, null=True)
    country_id  = models.IntegerField(blank=True, null=True)
    city        = models.CharField(blank=True, null=True, max_length=255)
    region      = models.CharField(blank=True, null=True, max_length=255)
    country     = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=255)

class ati_customs_map(HashMixin, CommonInfo):
    country_code = models.CharField(blank=True, null=True, max_length=2)
    customs_code = models.CharField(blank=True, null=True, max_length=8)
    customs_city = models.CharField(blank=True, null=True, max_length=255)
    ati_city     = models.CharField(blank=True, null=True, max_length=255)
    ati_city_id  = models.IntegerField(blank=True, null=True)
    key          = models.CharField(blank=True, null=True, max_length=8)

class car_type(HashMixin, CommonInfo):
    code        = models.TextField(blank=True, null=True)
    name        = models.CharField(blank=True, null=True, max_length=20)
    key         = models.CharField(blank=True, null=True, max_length=255)

class color(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    description = models.CharField(blank=True, null=True, max_length=20)
    key         = models.CharField(blank=True, null=True, max_length=3)

class countries(HashMixin, CommonInfo):
    abc2           = models.CharField(blank=True, null=True, max_length=2)
    abc3           = models.CharField(blank=True, null=True, max_length=3)
    code           = models.CharField(blank=True, null=True, max_length=3)
    short_name     = models.CharField(blank=True, null=True, max_length=40)
    name           = models.CharField(blank=True, null=True, max_length=250)
    name_eng       = models.CharField(blank=True, null=True, max_length=100)
    classification = models.TextField(blank=True, null=True)
    key            = models.CharField(blank=True, null=True, max_length=3)

class currency_code(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    abc3        = models.CharField(blank=True, null=True, max_length=3)
    short_name  = models.CharField(blank=True, null=True, max_length=17)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=3)

class customs(HashMixin, CommonInfo):
    country_code = models.CharField(blank=True, null=True, max_length=2)
    code         = models.CharField(blank=True, null=True, max_length=8)
    name         = models.CharField(blank=True, null=True, max_length=50)
    city         = models.CharField(blank=True, null=True, max_length=30)
    address      = models.CharField(blank=True, null=True, max_length=255)
    phone        = models.CharField(blank=True, null=True, max_length=20)
    oldcode      = models.CharField(blank=True, null=True, max_length=8)
    code5        = models.CharField(blank=True, null=True, max_length=5)
    key          = models.CharField(blank=True, null=True, max_length=8)

class customs_ced(HashMixin, CommonInfo):
    code           = models.CharField(blank=True, null=True, max_length=8)
    name           = models.CharField(blank=True, null=True, max_length=50)
    code_ced       = models.CharField(blank=True, null=True, max_length=255)
    ced_name       = models.CharField(blank=True, null=True, max_length=50)
    transport_kind = models.TextField(blank=True, null=True)
    notes          = models.CharField(blank=True, null=True, max_length=255)
    order_number   = models.CharField(blank=True, null=True, max_length=255)
    order_date     = models.DateTimeField(blank=True, null=True)
    key            = models.CharField(blank=True, null=True, max_length=255)

class customs_hierarchy(HashMixin, CommonInfo):
    code                = models.CharField(blank=True, null=True, max_length=8)
    name                = models.CharField(blank=True, null=True, max_length=50)
    customs_code        = models.CharField(blank=True, null=True, max_length=255)
    customs_name        = models.CharField(blank=True, null=True, max_length=50)
    customs_office_code = models.CharField(blank=True, null=True, max_length=255)
    customs_office_name = models.CharField(blank=True, null=True, max_length=50)
    key                 = models.CharField(blank=True, null=True, max_length=8)

class customs_payments_kind(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=4)
    name        = models.TextField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=4)

class customs_procedures_kind(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class customs_region(HashMixin, CommonInfo):
    code         = models.CharField(blank=True, null=True, max_length=8)
    name         = models.CharField(blank=True, null=True, max_length=50)
    region       = models.TextField(blank=True, null=True)
    region_okato = models.CharField(blank=True, null=True, max_length=255)
    order_number = models.CharField(blank=True, null=True, max_length=255)
    order_date   = models.DateTimeField(blank=True, null=True)
    key          = models.CharField(blank=True, null=True, max_length=255)

class customs_value_determination_kind(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=1)
    description = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=1)

class deal_feature(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class deal_nature(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    name        = models.CharField(blank=True, null=True, max_length=250)
    key         = models.CharField(blank=True, null=True, max_length=3)

class delivery_terms(HashMixin, CommonInfo):
    code_d      = models.TextField(blank=True, null=True)
    code        = models.CharField(blank=True, null=True, max_length=3)
    name        = models.CharField(blank=True, null=True, max_length=100)
    key         = models.CharField(blank=True, null=True, max_length=3)

class doc_reference(HashMixin, CommonInfo):
    code           = models.CharField(blank=True, null=True, max_length=5)
    documentgroup  = models.CharField(blank=True, null=True, max_length=2)
    description    = models.TextField(blank=True, null=True)
    documentmodeid = models.CharField(blank=True, null=True, max_length=8)
    documentname   = models.CharField(blank=True, null=True, max_length=255)
    key            = models.TextField(blank=True, null=True)

class doc_reference_ex(HashMixin, CommonInfo):
    code           = models.CharField(blank=True, null=True, max_length=5)
    documentgroup  = models.CharField(blank=True, null=True, max_length=2)
    description    = models.TextField(blank=True, null=True)
    documentmodeid = models.CharField(blank=True, null=True, max_length=8)
    documentname   = models.CharField(blank=True, null=True, max_length=255)
    key            = models.TextField(blank=True, null=True)
    end_date       = models.DateTimeField(blank=True, null=True)

class edi_container_type(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=255)
    code_old    = models.CharField(blank=True, null=True, max_length=255)
    length      = models.CharField(blank=True, null=True, max_length=255)
    width       = models.CharField(blank=True, null=True, max_length=255)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=255)

class edi_wagon_type(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    description = models.CharField(blank=True, null=True, max_length=255)
    abbr        = models.CharField(blank=True, null=True, max_length=10)
    key         = models.CharField(blank=True, null=True, max_length=2)

class edi_weight_definition_mode(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class ensure_payment_code(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class etsng(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=14)
    parent      = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    iscode      = models.BooleanField(default=False)

class forms_of_payment(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class gng(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=14)
    parent      = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    iscode      = models.BooleanField(default=False)

class gng_etsng(HashMixin, CommonInfo):
    gng_code          = models.CharField(blank=True, null=True, max_length=8)
    gng_description   = models.TextField(blank=True, null=True)
    etsng_code        = models.CharField(blank=True, null=True, max_length=6)
    etsng_description = models.TextField(blank=True, null=True)

class hazardous_cargo_code_imo(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=3)

class hazardous_cargo_code_un(HashMixin, CommonInfo):
    code                = models.CharField(blank=True, null=True, max_length=4)
    name                = models.CharField(blank=True, null=True, max_length=255)
    classification_type = models.CharField(blank=True, null=True, max_length=3)
    classification_code = models.CharField(blank=True, null=True, max_length=10)
    key                 = models.CharField(blank=True, null=True, max_length=4)

class intellectual(HashMixin, CommonInfo):
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
    order_date         = models.DateTimeField(blank=True, null=True)
    full_description   = models.TextField(blank=True, null=True)
    full_description_2 = models.TextField(blank=True, null=True)
    key                = models.CharField(blank=True, null=True, max_length=255)

class intellectual_documents(HashMixin, CommonInfo):
    code          = models.CharField(blank=True, null=True, max_length=25)
    document      = models.CharField(blank=True, null=True, max_length=25)
    document_date = models.DateTimeField(blank=True, null=True)
    key           = models.CharField(blank=True, null=True, max_length=25)

class intellectual_trade_marks(HashMixin, CommonInfo):
    code              = models.CharField(blank=True, null=True, max_length=255)
    description       = models.CharField(blank=True, null=True, max_length=255)
    picture_file_name = models.TextField(blank=True, null=True)
    key               = models.TextField(blank=True, null=True)

class mnt(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.TextField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=2)

class movement_of_goods_features(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    name        = models.TextField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=3)

class package(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    name_eng    = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class package_type(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=1)
    name        = models.CharField(blank=True, null=True, max_length=100)
    key         = models.CharField(blank=True, null=True, max_length=1)

class payment_code(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class payment_terms(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    description = models.CharField(blank=True, null=True, max_length=50)
    month_count = models.CharField(blank=True, null=True, max_length=4)
    key         = models.CharField(blank=True, null=True, max_length=2)

class payment_way_code(HashMixin, CommonInfo):
    country_ab2 = models.CharField(blank=True, null=True, max_length=2)
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=255)

class personal_document_kind(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    name        = models.CharField(blank=True, null=True, max_length=75)
    abbr        = models.CharField(blank=True, null=True, max_length=6)
    series_mask = models.CharField(blank=True, null=True, max_length=11)
    number_mask = models.CharField(blank=True, null=True, max_length=25)
    comment     = models.CharField(blank=True, null=True, max_length=120)
    key         = models.CharField(blank=True, null=True, max_length=2)

class personal_document_kind_155(HashMixin, CommonInfo):
    country_code     = models.CharField(blank=True, null=True, max_length=2)
    doc_type_code    = models.CharField(blank=True, null=True, max_length=2)
    code             = models.CharField(blank=True, null=True, max_length=7)
    name             = models.CharField(blank=True, null=True, max_length=255)
    citizenship_mark = models.CharField(blank=True, null=True, max_length=10)
    key              = models.CharField(blank=True, null=True, max_length=7)

class pi_usage(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    description = models.TextField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=2)

class preferences_kind(HashMixin, CommonInfo):
    code                       = models.CharField(blank=True, null=True, max_length=2)
    apply_to                   = models.CharField(blank=True, null=True, max_length=1)
    name                       = models.TextField(blank=True, null=True)
    use_in_by                  = models.FloatField(blank=True, null=True)
    use_in_kz                  = models.FloatField(blank=True, null=True)
    use_in_rf                  = models.FloatField(blank=True, null=True)
    use_in_am                  = models.FloatField(blank=True, null=True)
    procedures_mask            = models.CharField(blank=True, null=True, max_length=255)
    procedures_mask_order      = models.CharField(blank=True, null=True, max_length=255)
    procedures_mask_order_date = models.DateTimeField(blank=True, null=True)
    key                        = models.CharField(blank=True, null=True, max_length=255)

class rw_countries(HashMixin, CommonInfo):
    rw_country_code     = models.CharField(blank=True, null=True, max_length=255)
    name                = models.CharField(blank=True, null=True, max_length=50)
    abbr                = models.CharField(blank=True, null=True, max_length=10)
    country_code        = models.CharField(blank=True, null=True, max_length=255)
    administration_name = models.CharField(blank=True, null=True, max_length=255)
    abc2                = models.CharField(blank=True, null=True, max_length=2)
    abc3                = models.CharField(blank=True, null=True, max_length=3)
    key                 = models.CharField(blank=True, null=True, max_length=255)

class rw_roads(HashMixin, CommonInfo):
    road_code   = models.CharField(blank=True, null=True, max_length=255)
    name        = models.CharField(blank=True, null=True, max_length=50)
    abbr        = models.CharField(blank=True, null=True, max_length=10)
    key         = models.CharField(blank=True, null=True, max_length=255)

class rw_stations(HashMixin, CommonInfo):
    code5        = models.CharField(blank=True, null=True, max_length=10)
    code         = models.CharField(blank=True, null=True, max_length=255)
    name         = models.CharField(blank=True, null=True, max_length=100)
    name_eng     = models.CharField(blank=True, null=True, max_length=255)
    abbr         = models.CharField(blank=True, null=True, max_length=255)
    road_code    = models.CharField(blank=True, null=True, max_length=3)
    country_code = models.CharField(blank=True, null=True, max_length=255)
    key          = models.CharField(blank=True, null=True, max_length=255)

class rw_stations_customs(HashMixin, CommonInfo):
    code5        = models.CharField(blank=True, null=True, max_length=10)
    code         = models.CharField(blank=True, null=True, max_length=255)
    name         = models.CharField(blank=True, null=True, max_length=100)
    customs_code = models.CharField(blank=True, null=True, max_length=8)
    curtoms_name = models.CharField(blank=True, null=True, max_length=50)
    city         = models.CharField(blank=True, null=True, max_length=30)
    address      = models.CharField(blank=True, null=True, max_length=255)
    key          = models.CharField(blank=True, null=True, max_length=255)

class sea_ports(HashMixin, CommonInfo):
    country     = models.TextField(blank=True, null=True)
    code        = models.TextField(blank=True, null=True)
    name        = models.CharField(blank=True, null=True, max_length=255)
    coordinates = models.CharField(blank=True, null=True, max_length=255)

class stations_foreign_links(HashMixin, CommonInfo):
    code1       = models.CharField(blank=True, null=True, max_length=6)
    name1       = models.CharField(blank=True, null=True, max_length=100)
    country1    = models.CharField(blank=True, null=True, max_length=2)
    code2       = models.CharField(blank=True, null=True, max_length=6)
    name2       = models.CharField(blank=True, null=True, max_length=100)
    country2    = models.CharField(blank=True, null=True, max_length=2)
    key         = models.CharField(blank=True, null=True, max_length=255)

class tnved(HashMixin, CommonInfo):
    code              = models.CharField(blank=True, null=True, max_length=14)
    parent            = models.IntegerField(blank=True, null=True)
    description       = models.TextField(blank=True, null=True)
    iscode            = models.BooleanField(default=False)
    short_description = models.TextField(blank=True, null=True)
    unit_code         = models.CharField(blank=True, null=True, max_length=255)

class tnved_14(HashMixin, CommonInfo):
    code      = models.CharField(blank=True, null=True, max_length=10)
    code11    = models.CharField(blank=True, null=True, max_length=1)
    code12    = models.CharField(blank=True, null=True, max_length=1)
    code13    = models.CharField(blank=True, null=True, max_length=1)
    code14    = models.CharField(blank=True, null=True, max_length=1)
    name11    = models.CharField(blank=True, null=True, max_length=255)
    name12    = models.CharField(blank=True, null=True, max_length=255)
    name13    = models.CharField(blank=True, null=True, max_length=255)
    name14    = models.CharField(blank=True, null=True, max_length=255)

class transit_measures_of_ensuring(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    description = models.TextField(blank=True, null=True)
    key         = models.CharField(blank=True, null=True, max_length=2)

class transport_kind(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=2)
    description = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=2)

class type_of_vehicles(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    description = models.CharField(blank=True, null=True, max_length=130)
    comment     = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=3)

class unit(HashMixin, CommonInfo):
    code        = models.CharField(blank=True, null=True, max_length=3)
    abbr        = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=255)
    key         = models.CharField(blank=True, null=True, max_length=3)

class vmtp_country(HashMixin, CommonInfo):
    vmtp_code    = models.CharField(blank=True, null=True, max_length=3)
    country_code = models.CharField(blank=True, null=True, max_length=3)
    name         = models.CharField(blank=True, null=True, max_length=255)
    key          = models.CharField(blank=True, null=True, max_length=3)

class warehouse_customs(HashMixin, CommonInfo):
    country_ab2    = models.CharField(blank=True, null=True, max_length=255)
    customs_code   = models.CharField(blank=True, null=True, max_length=255)
    license_number = models.CharField(blank=True, null=True, max_length=255)
    license_date   = models.DateTimeField(blank=True, null=True)
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
    key            = models.CharField(blank=True, null=True, max_length=255)

class warehouse_temporary(HashMixin, CommonInfo):
    country_ab2    = models.CharField(blank=True, null=True, max_length=255)
    customs_code   = models.CharField(blank=True, null=True, max_length=255)
    license_number = models.CharField(blank=True, null=True, max_length=255)
    license_date   = models.DateTimeField(blank=True, null=True)
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
    key            = models.CharField(blank=True, null=True, max_length=255)
