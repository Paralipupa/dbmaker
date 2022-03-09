s/\(.*\)/ALTER TABLE \1 ADD COLUMN IF NOT EXISTS modify_date timestamp DEFAULT NULL;/
