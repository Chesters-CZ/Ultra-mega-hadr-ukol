USE hadr;

ALTER TABLE dbip_lookup_educa
    ADD COLUMN ip_start_dotless BIGINT(5) UNSIGNED ZEROFILL;

UPDATE dbip_lookup_educa
SET ip_start_dotless = dbip_lookup_educa.ip_start_1 * 1000000000 + dbip_lookup_educa.ip_start_2 * 1000000 +
                       dbip_lookup_educa.ip_start_3 * 1000 + dbip_lookup_educa.ip_start_4;


ALTER TABLE dbip_lookup_educa
    ADD COLUMN ip_end_dotless BIGINT(5) UNSIGNED ZEROFILL;

UPDATE dbip_lookup_educa
SET ip_end_dotless = dbip_lookup_educa.ip_end_1 * 1000000000 + dbip_lookup_educa.ip_end_2 * 1000000 +
                       dbip_lookup_educa.ip_end_3 * 1000 + dbip_lookup_educa.ip_end_4;


ALTER TABLE dbip_lookup_educa
ADD UNIQUE INDEX ip_s_d (ip_start_dotless);

ALTER TABLE dbip_lookup_educa
ADD UNIQUE INDEX ip_e_d (ip_end_dotless);