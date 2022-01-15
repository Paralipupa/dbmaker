#! /bin/bash
#создание файла сериализации модулей (erializers.py) по input_struct.txt
sed -f sed_mass.txt input_tables.txt | 
sed 's/@airports_rus//' | 
sed 's/@ati_cities//' | 
sed 's/@ati_customs_map//' | 
sed 's/@car_type//' | 
sed 's/@color//' | 
sed 's/@countries//' | 
sed 's/@currency_code//' | 
sed 's/@customs//' | 
sed 's/@customs_ced//' | 
sed 's/@customs_hierarchy//' | 
sed 's/@customs_payments_kind//' | 
sed 's/@customs_procedures_kind//' | 
sed 's/@customs_region//' | 
sed 's/@customs_value_determination_kind//' | 
sed 's/@deal_feature//' | 
sed 's/@deal_nature//' | 
sed 's/@delivery_terms//' | 
sed 's/@edi_container_type//' | 
sed 's/@edi_wagon_type//' | 
sed 's/@edi_weight_definition_mode//' | 
sed 's/@ensure_payment_code//' | 
sed 's/@forms_of_payment//' | 
sed 's/@hazardous_cargo_code_imo//' | 
sed 's/@hazardous_cargo_code_un//' | 
sed 's/@intellectual//' | 
sed 's/@intellectual_documents//' | 
sed 's/@intellectual_trade_marks//' | 
sed 's/@mnt//' | 
sed 's/@movement_of_goods_features//' | 
sed 's/@package//' | 
sed 's/@package_type//' | 
sed 's/@payment_code//' | 
sed 's/@payment_terms//' | 
sed 's/@payment_way_code//' | 
sed 's/@personal_document_kind//' | 
sed 's/@personal_document_kind_155//' | 
sed 's/@pi_usage//' | 
sed 's/@preferences_kind//' | 
sed 's/@rw_countries//' | 
sed 's/@rw_roads//' | 
sed 's/@rw_stations//' | 
sed 's/@rw_stations_customs//' | 
sed 's/@stations_foreign_links//' | 
sed 's/@transit_measures_of_ensuring//' | 
sed 's/@transport_kind//' | 
sed 's/@type_of_vehicles//' | 
sed 's/@unit//' | 
sed 's/@vmtp_country'// | 
sed 's/@warehouse_customs'// | 
sed 's/@warehouse_temporary'// | 
tee mapdata.py 

