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
