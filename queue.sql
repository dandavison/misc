-- https://stackoverflow.com/questions/11532550/atomic-update-select-in-postgres
-- https://dba.stackexchange.com/questions/69471/postgres-update-limit-1/69497#69497
-- set up data

drop table if exists myqueuetable;


create table myqueuetable (id serial, status varchar);


insert into myqueuetable (status)
values ('processing');


insert into myqueuetable (status)
values ('enqueued');


insert into myqueuetable (status)
values ('processing');


insert into myqueuetable (status)
values ('enqueued');

-- -- dequeue (should return row 2)

update myqueuetable
set status = 'processing'
where id =
        (select id
         from myqueuetable
         where status = 'enqueued'
         order by id
         limit 1
         for update skip locked) RETURNING id;

-- alternatively, using a CTE
with dequeued as
    ( select id
     from myqueuetable
     where status = 'enqueued'
     order by id
     limit 1)
UPDATE myqueuetable
set status = 'processing'
from dequeued
where myqueuetable.id = dequeued.id returning dequeued.id;

