s/\(.*\)/UPDATE \1 SET guid=coalesce((guid)::uuid,md5(('\1',key,from_date)::varchar)::uuid);/
