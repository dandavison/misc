-- Converted order patches

select triggering_event::json #>> '{updated_by_endpoint}' as endpoint,
                                  count(*)
from auth_user au
inner join event_log op on op.created_by_id = au.id
where email = 'email@example.com'
group by endpoint;


select email,
       created_at,
       data,
       triggering_event
from auth_user au
inner join event_log op on op.created_by_id = au.id
where email = 'email@example.com'
order by op.id desc
limit 100;

-----------------

select o.type,
       case
           when o.identifier is null then 'null-identifier'
           else 'has-identifier'
       end as has_identifier,
       count(*)
from my_root_objects_table o
inner join my_objects co on co.thing_uuid = o.uuid
where o.created_at > '2020-07-01'
group by o.type,
         has_identifier
order by o.type,
         has_identifier;


select o.uuid
from my_root_objects_table o
inner join my_objects co on co.thing_uuid = o.uuid
where o.created_at > '2020-07-01'
  and o.identifier is null;


select hc.uses_feature,
       count(*)
from my_root_objects_table oo
inner join customer hc on oo.customer_id = hc.id
where (oo.id > 1650000
       and oo.type = 'MY_FEATURE')
group by hc.uses_feature;

with patch_data as
  (select data::json #>> '{linked_items,0,relationship}' as relationship
   from event_log)
select relationship,
       count(relationship)
from patch_data
where relationship != ''
group by relationship
order by count(relationship) desc;

with patch_data as
  (select data::json #>> '{order_product,sub_products,0,test_offering_name}' as test_offering_name
   from event_log
   limit 10000)
select test_offering_name,
       count(test_offering_name)
from patch_data
where test_offering_name != ''
group by test_offering_name
order by count(test_offering_name) desc;

with patch_data as
  (select data::json #>> '{billing_info,0,insurance_cards,0,carrier}' as carrier
   from event_log)
select carrier,
       count(carrier)
from patch_data
where carrier != ''
group by carrier
order by count(carrier) desc;

with patch_data as
  (select thing_id,
          data::json #>> '{patient,sex}' as customer_sex
   from event_log
   limit 10000)
select customer_sex,
       count(*)
from patch_data
group by customer_sex;

with patch_data as
  (select thing_id,
          data::json #>> '{patient,sex}' as customer_sex
   from event_log)
select customer_sex,
       count(*)
from patch_data
group by customer_sex;

with patch_data as
  (select o.type p.data::json #>> '{patient,sex}' as customer_sex
   from event_log p
   inner join my_root_objects_table o on o.id = p.thing_id)
select customer_sex,
       count(*)
from patch_data
group by customer_sex;

-- Now, if this returned zero rows, we want to exit (return empty result)
-- Otherwise, we want to do an UPDATE on the single row to set its status to -- 'processing', and finally return the single row.

COMMIT;


create
temporary table dan_t1 as
create
temporary table dan_t2 as
  (select us.id
   from samples as us
   where not exists
       (select *
        from vendor_sample as s
        where s.identifier = us.identifier) ) t12 as (
                                                        (select id
                                                         from t1)
                                                      union
                                                        (select id
                                                         from t2)),
                n1 as
  (select count(*)
   from t1),
                n2 as
  (select count(*)
   from t2)
select count(*)
from n1;


from vendor_sample
where creation_date > '2019-04-19'
  select creation_date
  from eos_tickets
order by creation_date
select data::json #>> '{providers, 0}'
from event_log
where created_by_url = '/some/url'
limit 10;


select *
from event_log
where created_by_url = '/some/url'
  and data::json #>> '{type}' = 'MY_FEATURE'
limit 1;


select c.name,
       c.id,
       count(*)
from my_root_objects_table as o
inner join customer as c on o.customer_id = c.id
where o.type = 'MY_FEATURE'
  and c.my_feature_enabled_on is null
group by c.name,
         c.id
order by count(*) desc;


select c.name,
       count(*)
from my_root_objects_table as ot.
inner join customer as c on c.id = o.customer_id
left outer join external_identifier as r on r.customer_id = c.id
where o.type = 'MY_FEATURE'
  and c.my_feature_enabled_on is null
  and r.id is null
group by c.name,
         c.id
order by count(*) desc;


select data::json #>> '{linked_items,[0],name,[0]}'
from event_log;

with patch_data as
  (select thing_id,
          data::json #>> '{linked_items,[0],name,[0]}' as first_name
   from event_log)
select thing_id,
       first_name
from patch_data
where first_name is null
limit 1;


select data::json #>> '{linked_items,0,name,0}'
from event_log
where thing_id = 1157397;

# mydb=> with patch_data as (select thing_id, data::json #>> '{linked_items,[0],name,[1]}' as name from event_log) select thing_id, name from patch_data where name = '' limit 1;
#  thing_id | name
 # ------------------+------
 # (0 rows)
 # Time: 65388.703 ms
 # mydb=> with patch_data as (select thing_id, data::json #>> '{linked_items,[0],name,[0]}' as name from event_log) select thing_id, name from patch_data where name = '' limit 1;
 #  thing_id | name
 # ------------------+------
 # (0 rows)

UPDATE 92867 Time: 151797.346 ms Given the JSON value in postgres >
select '["a string", {}]'::json #> '{a,0}' as x;

x ------------
 "a string" >
select '{"key":["a string", {}]}'::json #> '{key,1}' as x;

x ----
 {}