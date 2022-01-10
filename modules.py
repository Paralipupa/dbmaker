

class nsi_airports_rus(models.Model):
    code_iata = modules.CharField(max_length=255) 
    name      = modules.CharField(max_length=255) 
    city      = modules.CharField(max_length=255) 
    key       = modules.CharField(max_length=255) 


class nsi_ati_cities(models.Model):
    city_id    = modules.IntegerField(blank=True, null=True)                
    region_id  = modules.IntegerField(blank=True, null=True)                
    country_id = modules.IntegerField(blank=True, null=True)                
    city       = modules.CharField(max_length=255) 
    region     = modules.CharField(max_length=255) 
    country    = modules.CharField(max_length=255) 
    key        = modules.IntegerField(blank=True, null=True)                


class nsi_ati_customs_map(models.Model):
    country_code = modules.CharField(max_length=2)   
    customs_code = modules.CharField(max_length=8)   
    customs_city = modules.CharField(max_length=255) 
    ati_city     = modules.CharField(max_length=255) 
    ati_city_id  = modules.IntegerField(blank=True, null=True)                
    key          = modules.CharField(max_length=8)   


class nsi_car_type(models.Model):
    code   = modules.TextField(null=True)                  
    name   = modules.CharField(max_length=20) 
    key    = modules.TextField(null=True)                  


class nsi_color(models.Model):
    code        = modules.CharField(max_length=3)  
    description = modules.CharField(max_length=20) 
    key         = modules.CharField(max_length=3)  


class nsi_countries(models.Model):
    abc2           = modules.CharField(max_length=2)   
    abc3           = modules.CharField(max_length=3)   
    code           = modules.CharField(max_length=3)   
    short_name     = modules.CharField(max_length=40)  
    name           = modules.CharField(max_length=250) 
    name_eng       = modules.CharField(max_length=100) 
    classification = modules.TextField(null=True)                   
    key            = modules.CharField(max_length=3)   


class nsi_currency_code(models.Model):
    code       = modules.CharField(max_length=3)   
    abc3       = modules.CharField(max_length=3)   
    short_name = modules.CharField(max_length=17)  
    name       = modules.CharField(max_length=255) 
    key        = modules.CharField(max_length=3)   


class nsi_customs(models.Model):
    country_code = modules.CharField(max_length=2)        
    code         = modules.CharField(max_length=8)        
    name         = modules.CharField(max_length=50)       
    city         = modules.CharField(max_length=30)       
    address      = modules.CharField(max_length=255)      
    phone        = modules.CharField(max_length=20)       
    oldcode      = modules.CharField(max_length=8)        
    code5        = modules.CharField(max_length=5)        
    from_date    = modules.DateTimeField(blank=True, null=True) 
    key          = modules.CharField(max_length=8)        


class nsi_customs_ced(models.Model):
    code           = modules.CharField(max_length=8)        
    name           = modules.CharField(max_length=50)       
    code_ced       = modules.CharField(max_length=255)      
    ced_name       = modules.CharField(max_length=50)       
    transport_kind = modules.TextField(null=True)                        
    notes          = modules.CharField(max_length=255)      
    order          = modules.CharField(max_length=255)      
    order_date     = modules.DateTimeField(blank=True, null=True) 
    from_date      = modules.DateTimeField(blank=True, null=True) 
    to_date        = modules.DateTimeField(blank=True, null=True) 
    key            = modules.TextField(null=True)                        


class nsi_customs_hierarchy(models.Model):
    code                = modules.CharField(max_length=8)   
    name                = modules.CharField(max_length=50)  
    customs_code        = modules.CharField(max_length=255) 
    customs_name        = modules.CharField(max_length=50)  
    customs_office_code = modules.CharField(max_length=255) 
    customs_office_name = modules.CharField(max_length=50)  
    key                 = modules.CharField(max_length=8)   


class nsi_customs_payments_kind(models.Model):
    code   = modules.CharField(max_length=4) 
    name   = modules.TextField(null=True)                 
    key    = modules.CharField(max_length=4) 


class nsi_customs_procedures_kind(models.Model):
    code   = modules.CharField(max_length=2)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=2)   


class nsi_customs_region(models.Model):
    code         = modules.CharField(max_length=8)        
    name         = modules.CharField(max_length=50)       
    region       = modules.TextField(null=True)                        
    region_okato = modules.CharField(max_length=255)      
    order        = modules.CharField(max_length=255)      
    order_date   = modules.DateTimeField(blank=True, null=True) 
    from_date    = modules.DateTimeField(blank=True, null=True) 
    to_date      = modules.DateTimeField(blank=True, null=True) 
    key          = modules.TextField(null=True)                        


class nsi_customs_value_determination_kind(models.Model):
    code        = modules.CharField(max_length=1)   
    description = modules.CharField(max_length=255) 
    key         = modules.CharField(max_length=1)   


class nsi_deal_feature(models.Model):
    code   = modules.CharField(max_length=2)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=2)   


class nsi_deal_nature(models.Model):
    code   = modules.CharField(max_length=3)   
    name   = modules.CharField(max_length=250) 
    key    = modules.CharField(max_length=3)   


class nsi_delivery_terms(models.Model):
    code_d = modules.TextField(null=True)                   
    code   = modules.CharField(max_length=3)   
    name   = modules.CharField(max_length=100) 
    key    = modules.CharField(max_length=3)   


class nsi_edi_container_type(models.Model):
    code     = modules.CharField(max_length=255) 
    code_old = modules.CharField(max_length=255) 
    length   = modules.CharField(max_length=255) 
    width    = modules.CharField(max_length=255) 
    name     = modules.CharField(max_length=255) 


class nsi_edi_wagon_type(models.Model):
    code        = modules.CharField(max_length=2)   
    description = modules.CharField(max_length=255) 
    abbr        = modules.CharField(max_length=10)  
    key         = modules.CharField(max_length=2)   


class nsi_edi_weight_definition_mode(models.Model):
    code   = modules.CharField(max_length=2)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=2)   


class nsi_ensure_payment_code(models.Model):
    code   = modules.CharField(max_length=2)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=2)   


class nsi_forms_of_payment(models.Model):
    code   = modules.CharField(max_length=2)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=2)   


class nsi_hazardous_cargo_code_imo(models.Model):
    code   = modules.CharField(max_length=3)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=3)   


class nsi_hazardous_cargo_code_un(models.Model):
    code                = modules.CharField(max_length=4)   
    name                = modules.CharField(max_length=255) 
    class               = modules.CharField(max_length=3)   (models.Model):
    clarrification_code = modules.CharField(max_length=10)  


class nsi_intellectual(models.Model):
    code               = modules.CharField(max_length=25)       
    description        = modules.CharField(max_length=50)       
    inn                = modules.CharField(max_length=12)       
    kpp                = modules.CharField(max_length=9)        
    company_name       = modules.CharField(max_length=254)      
    company_name_en    = modules.CharField(max_length=254)      
    company_address    = modules.CharField(max_length=254)      
    company_address_en = modules.CharField(max_length=254)      
    note               = modules.CharField(max_length=100)      
    order_number       = modules.CharField(max_length=10)       
    order_date         = modules.DateTimeField(blank=True, null=True) 
    full_description   = modules.TextField(null=True)                        
    full_description_2 = modules.TextField(null=True)                        
    key                = modules.TextField(null=True)                        


class nsi_intellectual_documents(models.Model):
    code          = modules.CharField(max_length=25)       
    document      = modules.CharField(max_length=25)       
    document_date = modules.DateTimeField(blank=True, null=True) 


class nsi_intellectual_trade_marks(models.Model):
    code              = modules.CharField(max_length=255) 
    description       = modules.CharField(max_length=255) 
    picture_file_name = modules.TextField(null=True)                   
    key               = modules.TextField(null=True)                   


class nsi_mnt(models.Model):
    code   = modules.CharField(max_length=2) 
    name   = modules.TextField(null=True)                 
    key    = modules.CharField(max_length=2) 


class nsi_movement_of_goods_features(models.Model):
    code   = modules.CharField(max_length=3) 
    name   = modules.TextField(null=True)                 
    key    = modules.CharField(max_length=3) 


class nsi_package(models.Model):
    code     = modules.CharField(max_length=2)   
    name     = modules.CharField(max_length=255) 
    name_eng = modules.CharField(max_length=255) 
    key      = modules.CharField(max_length=2)   


class nsi_package_type(models.Model):
    code   = modules.CharField(max_length=1)   
    name   = modules.CharField(max_length=100) 
    key    = modules.CharField(max_length=1)   


class nsi_payment_code(models.Model):
    code   = modules.CharField(max_length=2)   
    name   = modules.CharField(max_length=255) 
    key    = modules.CharField(max_length=2)   


class nsi_payment_terms(models.Model):
    code        = modules.CharField(max_length=2)  
    description = modules.CharField(max_length=50) 
    month_count = modules.CharField(max_length=4)  
    key         = modules.CharField(max_length=2)  


class nsi_payment_way_code(models.Model):
    country_ab2 = modules.CharField(max_length=2)   
    code        = modules.CharField(max_length=2)   
    name        = modules.CharField(max_length=255) 
    key         = modules.TextField(null=True)                   


class nsi_personal_document_kind(models.Model):
    code        = modules.CharField(max_length=2)   
    name        = modules.CharField(max_length=75)  
    abbr        = modules.CharField(max_length=6)   
    series_mask = modules.CharField(max_length=11)  
    number_mask = modules.CharField(max_length=25)  
    comment     = modules.CharField(max_length=120) 
    key         = modules.CharField(max_length=2)   


class nsi_personal_document_kind_155(models.Model):
    country_code     = modules.CharField(max_length=2)   
    doc_type_code    = modules.CharField(max_length=2)   
    code             = modules.CharField(max_length=7)   
    name             = modules.CharField(max_length=255) 
    citizenship_mark = modules.CharField(max_length=10)  
    key              = modules.CharField(max_length=7)   


class nsi_pi_usage(models.Model):
    code        = modules.CharField(max_length=2) 
    description = modules.TextField(null=True)                 
    key         = modules.CharField(max_length=2) 


class nsi_preferences_kind(models.Model):
    code                       = modules.CharField(max_length=2)        
    apply_to                   = modules.CharField(max_length=1)        
    name                       = modules.TextField(null=True)                        
    use_in_by                  = modules.double precision            
    use_in_kz                  = modules.double precision            
    use_in_rf                  = modules.double precision            
    use_in_am                  = modules.double precision            
    key                        = modules.TextField(null=True)                        
    procedures_mask            = modules.CharField(max_length=255)      
    procedures_mask_order      = modules.CharField(max_length=255)      
    procedures_mask_order_date = modules.DateTimeField(blank=True, null=True) 


class nsi_rw_countries(models.Model):
    rw_country_code     = modules.CharField(max_length=255) 
    name                = modules.CharField(max_length=50)  
    abbr                = modules.CharField(max_length=10)  
    country_code        = modules.CharField(max_length=255) 
    administration_name = modules.CharField(max_length=255) 
    abc2                = modules.CharField(max_length=2)   
    abc3                = modules.CharField(max_length=3)   
    key                 = modules.CharField(max_length=255) 


class nsi_rw_roads(models.Model):
    road_code = modules.CharField(max_length=255) 
    name      = modules.CharField(max_length=50)  
    abbr      = modules.CharField(max_length=10)  
    key       = modules.CharField(max_length=255) 


class nsi_rw_stations(models.Model):
    code5        = modules.CharField(max_length=10)  
    code         = modules.CharField(max_length=255) 
    name         = modules.CharField(max_length=100) 
    name_eng     = modules.CharField(max_length=255) 
    abbr         = modules.CharField(max_length=255) 
    road_code    = modules.CharField(max_length=3)   
    country_code = modules.CharField(max_length=255) 
    key          = modules.TextField(null=True)                   


class nsi_rw_stations_customs(models.Model):
    code5        = modules.CharField(max_length=10)  
    code         = modules.CharField(max_length=255) 
    name         = modules.CharField(max_length=100) 
    customs_code = modules.CharField(max_length=8)   
    curtoms_name = modules.CharField(max_length=50)  
    city         = modules.CharField(max_length=30)  
    address      = modules.CharField(max_length=255) 
    key          = modules.TextField(null=True)                   


class nsi_stations_foreign_links(models.Model):
    code1    = modules.CharField(max_length=6)   
    name1    = modules.CharField(max_length=100) 
    country1 = modules.CharField(max_length=2)   
    code2    = modules.CharField(max_length=6)   
    name2    = modules.CharField(max_length=100) 
    country2 = modules.CharField(max_length=2)   
    key      = modules.TextField(null=True)                   


class nsi_transit_measures_of_ensuring(models.Model):
    code        = modules.CharField(max_length=2) 
    description = modules.TextField(null=True)                 
    key         = modules.CharField(max_length=2) 


class nsi_transport_kind(models.Model):
    code        = modules.CharField(max_length=2)   
    description = modules.CharField(max_length=255) 
    key         = modules.CharField(max_length=2)   


class nsi_type_of_vehicles(models.Model):
    code        = modules.CharField(max_length=3)   
    description = modules.CharField(max_length=130) 
    comment     = modules.CharField(max_length=255) 
    key         = modules.CharField(max_length=3)   


class nsi_unit(models.Model):
    code        = modules.CharField(max_length=3)   
    abbr        = modules.CharField(max_length=100) 
    description = modules.CharField(max_length=255) 
    key         = modules.CharField(max_length=3)   


class nsi_vmtp_country(models.Model):
    vmtp_code    = modules.CharField(max_length=3)   
    country_code = modules.CharField(max_length=3)   
    name         = modules.CharField(max_length=255) 


class nsi_warehouse_customs(models.Model):
    country_ab2    = modules.CharField(max_length=255)           
    customs_code   = modules.CharField(max_length=255)           
    license_number = modules.CharField(max_length=255)           
    license_date   = modules.DateTimeField(blank=True, null=True) 
    owner          = modules.CharField(max_length=255)           
    offise_address = modules.TextField(null=True)                        
    address        = modules.TextField(null=True)                        
    phone          = modules.CharField(max_length=255)           
    website        = modules.CharField(max_length=255)           
    email          = modules.CharField(max_length=255)           
    inn            = modules.CharField(max_length=255)           
    kpp            = modules.CharField(max_length=255)           
    transport_kind = modules.TextField(null=True)                        
    is_exciz       = modules.CharField(max_length=255)           
    warehouse_type = modules.TextField(null=True)                        
    key            = modules.TextField(null=True)                        


class nsi_warehouse_temporary(models.Model):
    country_ab2    = modules.CharField(max_length=255)           
    customs_code   = modules.CharField(max_length=255)           
    license_number = modules.CharField(max_length=255)           
    license_date   = modules.DateTimeField(blank=True, null=True) 
    owner          = modules.CharField(max_length=255)           
    offise_address = modules.TextField(null=True)                        
    address        = modules.TextField(null=True)                        
    phone          = modules.CharField(max_length=255)           
    website        = modules.CharField(max_length=255)           
    email          = modules.CharField(max_length=255)           
    inn            = modules.CharField(max_length=255)           
    kpp            = modules.CharField(max_length=255)           
    transport_kind = modules.TextField(null=True)                        
    is_exciz       = modules.CharField(max_length=255)           
    warehouse_type = modules.TextField(null=True)                        
    key            = modules.TextField(null=True)                        
