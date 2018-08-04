SELECT idx.relname as table,
       idx.indexrelname as index,
       pg_relation_size( idx.indexrelname::text )/1024/1024 as bytes,
       cls.relpages as pages,
       cls.reltuples as tuples,
       idx.idx_scan as scanned,
       idx.idx_tup_read as read,
       idx.idx_tup_fetch as fetched
FROM pg_stat_user_indexes idx,
     pg_class cls ,
     pg_index
WHERE cls.relname = idx.relname
AND idx.indexrelid = pg_index.indexrelid
AND idx.indexrelname like 'mail_messagelog_%'
AND pg_index.indisunique is not true
AND pg_index.indisprimary is not true
AND idx.indexrelname not ilike '%slony%'
AND idx.indexrelname not like 'sl\_%'
ORDER BY idx.relname,
         idx.indexrelname;



counsyl_product=> SELECT idx.relname as table,
counsyl_product->        idx.indexrelname as index,
counsyl_product->        pg_relation_size( idx.indexrelname::text )/1024/1024 as bytes,
counsyl_product->        cls.relpages as pages,
counsyl_product->        cls.reltuples as tuples,
counsyl_product->        idx.idx_scan as scanned,
counsyl_product->        idx.idx_tup_read as read,
counsyl_product->        idx.idx_tup_fetch as fetched
counsyl_product-> FROM pg_stat_user_indexes idx,
counsyl_product->      pg_class cls ,
counsyl_product->      pg_index
counsyl_product-> WHERE cls.relname = idx.relname
counsyl_product-> AND idx.indexrelid = pg_index.indexrelid
counsyl_product-> AND idx.indexrelname like 'mail_messagelog_%'
counsyl_product-> AND pg_index.indisunique is not true
counsyl_product-> AND pg_index.indisprimary is not true
counsyl_product-> AND idx.indexrelname not ilike '%slony%'
counsyl_product-> AND idx.indexrelname not like 'sl\_%'
counsyl_product-> ORDER BY idx.relname,
counsyl_product->          idx.indexrelname;
      table      |                       index                        | bytes |  pages  |   tuples    | scanned |   read   | fetched
-----------------+----------------------------------------------------+-------+---------+-------------+---------+----------+---------
 mail_messagelog | mail_messagelog_content_type_id                    |   941 | 1290458 | 1.12578e+07 |       0 |        0 |       0
 mail_messagelog | mail_messagelog_email_name_index_dan               |   263 | 1290458 | 1.12578e+07 |       1 |        0 |       0
 mail_messagelog | mail_messagelog_latest_status_595dd7d44fe530a9_idx |   289 | 1290458 | 1.12578e+07 |       1 | 11303158 |  193616
 mail_messagelog | mail_messagelog_message_id_49696302_uniq           |   589 | 1290458 | 1.12578e+07 |       0 |        0 |       0
 mail_messagelog | mail_messagelog_object_id                          |   563 | 1290458 | 1.12578e+07 |       0 |        0 |       0
 mail_messagelog | mail_messagelog_to_address                         |  1009 | 1290458 | 1.12578e+07 |       0 |        0 |       0
(6 rows)

counsyl_product=> \timing
Timing is on.
counsyl_product=> create index mail_messagelog_reference_id_index_dan on mail_messagelog (reference_id);
CREATE INDEX
Time: 94900.382 ms
