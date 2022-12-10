USE hadr;

ALTER TABLE dbip_lookup_educa ADD INDEX ip_s_1 (ip_start_1);

ALTER TABLE dbip_lookup_educa ADD INDEX ip_s_2 (ip_start_2);

ALTER TABLE dbip_lookup_educa ADD INDEX ip_s_3 (ip_start_3);

ALTER TABLE dbip_lookup_educa ADD INDEX ip_s_4 (ip_start_4);


ALTER TABLE dbip_lookup_educa ADD INDEX ip_e_1 (ip_end_1);

ALTER TABLE dbip_lookup_educa ADD INDEX ip_e_2 (ip_end_2);

ALTER TABLE dbip_lookup_educa ADD INDEX ip_e_3 (ip_end_3);

ALTER TABLE dbip_lookup_educa ADD INDEX ip_e_4 (ip_end_4);