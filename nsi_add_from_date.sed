s/\(.*\)/ALTER TABLE \1  ADD COLUMN IF NOT EXISTS from_date timestamp DEFAULT NULL;/
