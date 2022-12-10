USE hadr;

UPDATE dbip_lookup_educa
SET temp = ip_start;

UPDATE dbip_lookup_educa
SET ip_start_1 = SUBSTRING_INDEX(temp, '.', 1);

UPDATE dbip_lookup_educa
SET ip_start_2 = SUBSTRING_INDEX(SUBSTRING_INDEX(temp, '.', 2), '.', -1);

UPDATE dbip_lookup_educa
SET ip_start_3 = SUBSTRING_INDEX(SUBSTRING_INDEX(temp, '.', 3), '.', -1);

UPDATE dbip_lookup_educa
SET ip_start_4 = SUBSTRING_INDEX(temp, '.', -1);


UPDATE dbip_lookup_educa
SET temp = ip_end;

UPDATE dbip_lookup_educa
SET ip_end_1 = SUBSTRING_INDEX(temp, '.', 1);

UPDATE dbip_lookup_educa
SET ip_end_2 = SUBSTRING_INDEX(SUBSTRING_INDEX(temp, '.', 2), '.', -1);

UPDATE dbip_lookup_educa
SET ip_end_3 = SUBSTRING_INDEX(SUBSTRING_INDEX(temp, '.', 3), '.', -1);

UPDATE dbip_lookup_educa
SET ip_end_4 = SUBSTRING_INDEX(temp, '.', -1);