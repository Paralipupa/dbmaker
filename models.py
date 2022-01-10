

class airports_rus(models.Model):
    guid = models.CharField(max_length=32)
    code_iata = models.CharField(blank=True, null=True, max_length=255) 
    name      = models.CharField(blank=True, null=True, max_length=255) 
    city      = models.CharField(blank=True, null=True, max_length=255) 
    key       = models.CharField(blank=True, null=True, max_length=255) 


class ati_cities(models.Model):
    guid = models.CharField(max_length=32)
    city_id    = models.IntegerField(blank=True, null=True)                
    region_id  = models.IntegerField(blank=True, null=True)                
    country_id = models.IntegerField(blank=True, null=True)                
    city       = models.CharField(blank=True, null=True, max_length=255) 
    region     = models.CharField(blank=True, null=True, max_length=255) 
    country    = models.CharField(blank=True, null=True, max_length=255) 
    key        = models.IntegerField(blank=True, null=True)                


class ati_customs_map(models.Model):
    guid = models.CharField(max_length=32)
    country_code = models.CharField(blank=True, null=True, max_length=2)   
    customs_code = models.CharField(blank=True, null=True, max_length=8)   
    customs_city = models.CharField(blank=True, null=True, max_length=255) 
    ati_city     = models.CharField(blank=True, null=True, max_length=255) 
    ati_city_id  = models.IntegerField(blank=True, null=True)                
    key          = models.CharField(blank=True, null=True, max_length=8)   


class car_type(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.TextField(blank=True, null=True)                  
    name   = models.CharField(blank=True, null=True, max_length=20) 
    key    = models.TextField(blank=True, null=True)                  


class color(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=3)  
    description = models.CharField(blank=True, null=True, max_length=20) 
    key         = models.CharField(blank=True, null=True, max_length=3)  


class countries(models.Model):
    guid = models.CharField(max_length=32)
    abc2           = models.CharField(blank=True, null=True, max_length=2)   
    abc3           = models.CharField(blank=True, null=True, max_length=3)   
    code           = models.CharField(blank=True, null=True, max_length=3)   
    short_name     = models.CharField(blank=True, null=True, max_length=40)  
    name           = models.CharField(blank=True, null=True, max_length=250) 
    name_eng       = models.CharField(blank=True, null=True, max_length=100) 
    classification = models.TextField(blank=True, null=True)                   
    key            = models.CharField(blank=True, null=True, max_length=3)   


class currency_code(models.Model):
    guid = models.CharField(max_length=32)
    code       = models.CharField(blank=True, null=True, max_length=3)   
    abc3       = models.CharField(blank=True, null=True, max_length=3)   
    short_name = models.CharField(blank=True, null=True, max_length=17)  
    name       = models.CharField(blank=True, null=True, max_length=255) 
    key        = models.CharField(blank=True, null=True, max_length=3)   


class customs(models.Model):
    guid = models.CharField(max_length=32)
    country_code = models.CharField(blank=True, null=True, max_length=2)        
    code         = models.CharField(blank=True, null=True, max_length=8)        
    name         = models.CharField(blank=True, null=True, max_length=50)       
    city         = models.CharField(blank=True, null=True, max_length=30)       
    address      = models.CharField(blank=True, null=True, max_length=255)      
    phone        = models.CharField(blank=True, null=True, max_length=20)       
    oldcode      = models.CharField(blank=True, null=True, max_length=8)        
    code5        = models.CharField(blank=True, null=True, max_length=5)        
    from_date    = models.DateTimeField(blank=True, null=True) 
    key          = models.CharField(blank=True, null=True, max_length=8)        


class customs_ced(models.Model):
    guid = models.CharField(max_length=32)
    code           = models.CharField(blank=True, null=True, max_length=8)        
    name           = models.CharField(blank=True, null=True, max_length=50)       
    code_ced       = models.CharField(blank=True, null=True, max_length=255)      
    ced_name       = models.CharField(blank=True, null=True, max_length=50)       
    transport_kind = models.TextField(blank=True, null=True)                        
    notes          = models.CharField(blank=True, null=True, max_length=255)      
    order          = models.CharField(blank=True, null=True, max_length=255)      
    order_date     = models.DateTimeField(blank=True, null=True) 
    from_date      = models.DateTimeField(blank=True, null=True) 
    to_date        = models.DateTimeField(blank=True, null=True) 
    key            = models.TextField(blank=True, null=True)                        


class customs_hierarchy(models.Model):
    guid = models.CharField(max_length=32)
    code                = models.CharField(blank=True, null=True, max_length=8)   
    name                = models.CharField(blank=True, null=True, max_length=50)  
    customs_code        = models.CharField(blank=True, null=True, max_length=255) 
    customs_name        = models.CharField(blank=True, null=True, max_length=50)  
    customs_office_code = models.CharField(blank=True, null=True, max_length=255) 
    customs_office_name = models.CharField(blank=True, null=True, max_length=50)  
    key                 = models.CharField(blank=True, null=True, max_length=8)   


class customs_payments_kind(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=4) 
    name   = models.TextField(blank=True, null=True)                 
    key    = models.CharField(blank=True, null=True, max_length=4) 


class customs_procedures_kind(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=2)   


class customs_region(models.Model):
    guid = models.CharField(max_length=32)
    code         = models.CharField(blank=True, null=True, max_length=8)        
    name         = models.CharField(blank=True, null=True, max_length=50)       
    region       = models.TextField(blank=True, null=True)                        
    region_okato = models.CharField(blank=True, null=True, max_length=255)      
    order        = models.CharField(blank=True, null=True, max_length=255)      
    order_date   = models.DateTimeField(blank=True, null=True) 
    from_date    = models.DateTimeField(blank=True, null=True) 
    to_date      = models.DateTimeField(blank=True, null=True) 
    key          = models.TextField(blank=True, null=True)                        


class customs_value_determination_kind(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=1)   
    description = models.CharField(blank=True, null=True, max_length=255) 
    key         = models.CharField(blank=True, null=True, max_length=1)   


class deal_feature(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=2)   


class deal_nature(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=3)   
    name   = models.CharField(blank=True, null=True, max_length=250) 
    key    = models.CharField(blank=True, null=True, max_length=3)   


class delivery_terms(models.Model):
    guid = models.CharField(max_length=32)
    code_d = models.TextField(blank=True, null=True)                   
    code   = models.CharField(blank=True, null=True, max_length=3)   
    name   = models.CharField(blank=True, null=True, max_length=100) 
    key    = models.CharField(blank=True, null=True, max_length=3)   


class edi_container_type(models.Model):
    guid = models.CharField(max_length=32)
    code     = models.CharField(blank=True, null=True, max_length=255) 
    code_old = models.CharField(blank=True, null=True, max_length=255) 
    length   = models.CharField(blank=True, null=True, max_length=255) 
    width    = models.CharField(blank=True, null=True, max_length=255) 
    name     = models.CharField(blank=True, null=True, max_length=255) 


class edi_wagon_type(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=2)   
    description = models.CharField(blank=True, null=True, max_length=255) 
    abbr        = models.CharField(blank=True, null=True, max_length=10)  
    key         = models.CharField(blank=True, null=True, max_length=2)   


class edi_weight_definition_mode(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=2)   


class ensure_payment_code(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=2)   


class forms_of_payment(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=2)   


class hazardous_cargo_code_imo(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=3)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=3)   


class hazardous_cargo_code_un(models.Model):
    guid = models.CharField(max_length=32)
    code                = models.CharField(blank=True, null=True, max_length=4)   
    name                = models.CharField(blank=True, null=True, max_length=255) 
    class_name          = models.CharField(blank=True, null=True, max_length=3)   
    clarrification_code = models.CharField(blank=True, null=True, max_length=10)  


class intellectual(models.Model):
    guid = models.CharField(max_length=32)
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
    key                = models.TextField(blank=True, null=True)                        


class intellectual_documents(models.Model):
    guid = models.CharField(max_length=32)
    code          = models.CharField(blank=True, null=True, max_length=25)       
    document      = models.CharField(blank=True, null=True, max_length=25)       
    document_date = models.DateTimeField(blank=True, null=True) 


class intellectual_trade_marks(models.Model):
    guid = models.CharField(max_length=32)
    code              = models.CharField(blank=True, null=True, max_length=255) 
    description       = models.CharField(blank=True, null=True, max_length=255) 
    picture_file_name = models.TextField(blank=True, null=True)                   
    key               = models.TextField(blank=True, null=True)                   


class mnt(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2) 
    name   = models.TextField(blank=True, null=True)                 
    key    = models.CharField(blank=True, null=True, max_length=2) 


class movement_of_goods_features(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=3) 
    name   = models.TextField(blank=True, null=True)                 
    key    = models.CharField(blank=True, null=True, max_length=3) 


class package(models.Model):
    guid = models.CharField(max_length=32)
    code     = models.CharField(blank=True, null=True, max_length=2)   
    name     = models.CharField(blank=True, null=True, max_length=255) 
    name_eng = models.CharField(blank=True, null=True, max_length=255) 
    key      = models.CharField(blank=True, null=True, max_length=2)   


class package_type(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=1)   
    name   = models.CharField(blank=True, null=True, max_length=100) 
    key    = models.CharField(blank=True, null=True, max_length=1)   


class payment_code(models.Model):
    guid = models.CharField(max_length=32)
    code   = models.CharField(blank=True, null=True, max_length=2)   
    name   = models.CharField(blank=True, null=True, max_length=255) 
    key    = models.CharField(blank=True, null=True, max_length=2)   


class payment_terms(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=2)  
    description = models.CharField(blank=True, null=True, max_length=50) 
    month_count = models.CharField(blank=True, null=True, max_length=4)  
    key         = models.CharField(blank=True, null=True, max_length=2)  


class payment_way_code(models.Model):
    guid = models.CharField(max_length=32)
    country_ab2 = models.CharField(blank=True, null=True, max_length=2)   
    code        = models.CharField(blank=True, null=True, max_length=2)   
    name        = models.CharField(blank=True, null=True, max_length=255) 
    key         = models.TextField(blank=True, null=True)                   


class personal_document_kind(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=2)   
    name        = models.CharField(blank=True, null=True, max_length=75)  
    abbr        = models.CharField(blank=True, null=True, max_length=6)   
    series_mask = models.CharField(blank=True, null=True, max_length=11)  
    number_mask = models.CharField(blank=True, null=True, max_length=25)  
    comment     = models.CharField(blank=True, null=True, max_length=120) 
    key         = models.CharField(blank=True, null=True, max_length=2)   


class personal_document_kind_155(models.Model):
    guid = models.CharField(max_length=32)
    country_code     = models.CharField(blank=True, null=True, max_length=2)   
    doc_type_code    = models.CharField(blank=True, null=True, max_length=2)   
    code             = models.CharField(blank=True, null=True, max_length=7)   
    name             = models.CharField(blank=True, null=True, max_length=255) 
    citizenship_mark = models.CharField(blank=True, null=True, max_length=10)  
    key              = models.CharField(blank=True, null=True, max_length=7)   


class pi_usage(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=2) 
    description = models.TextField(blank=True, null=True)                 
    key         = models.CharField(blank=True, null=True, max_length=2) 


class preferences_kind(models.Model):
    guid = models.CharField(max_length=32)
    code                       = models.CharField(blank=True, null=True, max_length=2)        
    apply_to                   = models.CharField(blank=True, null=True, max_length=1)        
    name                       = models.TextField(blank=True, null=True)                        
    use_in_by                  = models.FloatField(blank=True, null=True)            
    use_in_kz                  = models.FloatField(blank=True, null=True)            
    use_in_rf                  = models.FloatField(blank=True, null=True)            
    use_in_am                  = models.FloatField(blank=True, null=True)            
    key                        = models.TextField(blank=True, null=True)                        
    procedures_mask            = models.CharField(blank=True, null=True, max_length=255)      
    procedures_mask_order      = models.CharField(blank=True, null=True, max_length=255)      
    procedures_mask_order_date = models.DateTimeField(blank=True, null=True) 


class rw_countries(models.Model):
    guid = models.CharField(max_length=32)
    rw_country_code     = models.CharField(blank=True, null=True, max_length=255) 
    name                = models.CharField(blank=True, null=True, max_length=50)  
    abbr                = models.CharField(blank=True, null=True, max_length=10)  
    country_code        = models.CharField(blank=True, null=True, max_length=255) 
    administration_name = models.CharField(blank=True, null=True, max_length=255) 
    abc2                = models.CharField(blank=True, null=True, max_length=2)   
    abc3                = models.CharField(blank=True, null=True, max_length=3)   
    key                 = models.CharField(blank=True, null=True, max_length=255) 


class rw_roads(models.Model):
    guid = models.CharField(max_length=32)
    road_code = models.CharField(blank=True, null=True, max_length=255) 
    name      = models.CharField(blank=True, null=True, max_length=50)  
    abbr      = models.CharField(blank=True, null=True, max_length=10)  
    key       = models.CharField(blank=True, null=True, max_length=255) 


class rw_stations(models.Model):
    guid = models.CharField(max_length=32)
    code5        = models.CharField(blank=True, null=True, max_length=10)  
    code         = models.CharField(blank=True, null=True, max_length=255) 
    name         = models.CharField(blank=True, null=True, max_length=100) 
    name_eng     = models.CharField(blank=True, null=True, max_length=255) 
    abbr         = models.CharField(blank=True, null=True, max_length=255) 
    road_code    = models.CharField(blank=True, null=True, max_length=3)   
    country_code = models.CharField(blank=True, null=True, max_length=255) 
    key          = models.TextField(blank=True, null=True)                   


class rw_stations_customs(models.Model):
    guid = models.CharField(max_length=32)
    code5        = models.CharField(blank=True, null=True, max_length=10)  
    code         = models.CharField(blank=True, null=True, max_length=255) 
    name         = models.CharField(blank=True, null=True, max_length=100) 
    customs_code = models.CharField(blank=True, null=True, max_length=8)   
    curtoms_name = models.CharField(blank=True, null=True, max_length=50)  
    city         = models.CharField(blank=True, null=True, max_length=30)  
    address      = models.CharField(blank=True, null=True, max_length=255) 
    key          = models.TextField(blank=True, null=True)                   


class stations_foreign_links(models.Model):
    guid = models.CharField(max_length=32)
    code1    = models.CharField(blank=True, null=True, max_length=6)   
    name1    = models.CharField(blank=True, null=True, max_length=100) 
    country1 = models.CharField(blank=True, null=True, max_length=2)   
    code2    = models.CharField(blank=True, null=True, max_length=6)   
    name2    = models.CharField(blank=True, null=True, max_length=100) 
    country2 = models.CharField(blank=True, null=True, max_length=2)   
    key      = models.TextField(blank=True, null=True)                   


class transit_measures_of_ensuring(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=2) 
    description = models.TextField(blank=True, null=True)                 
    key         = models.CharField(blank=True, null=True, max_length=2) 


class transport_kind(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=2)   
    description = models.CharField(blank=True, null=True, max_length=255) 
    key         = models.CharField(blank=True, null=True, max_length=2)   


class type_of_vehicles(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=3)   
    description = models.CharField(blank=True, null=True, max_length=130) 
    comment     = models.CharField(blank=True, null=True, max_length=255) 
    key         = models.CharField(blank=True, null=True, max_length=3)   


class unit(models.Model):
    guid = models.CharField(max_length=32)
    code        = models.CharField(blank=True, null=True, max_length=3)   
    abbr        = models.CharField(blank=True, null=True, max_length=100) 
    description = models.CharField(blank=True, null=True, max_length=255) 
    key         = models.CharField(blank=True, null=True, max_length=3)   


class vmtp_country(models.Model):
    guid = models.CharField(max_length=32)
    vmtp_code    = models.CharField(blank=True, null=True, max_length=3)   
    country_code = models.CharField(blank=True, null=True, max_length=3)   
    name         = models.CharField(blank=True, null=True, max_length=255) 


class warehouse_customs(models.Model):
    guid = models.CharField(max_length=32)
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
    key            = models.TextField(blank=True, null=True)                        


class warehouse_temporary(models.Model):
    guid = models.CharField(max_length=32)
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
    key            = models.TextField(blank=True, null=True)                        
