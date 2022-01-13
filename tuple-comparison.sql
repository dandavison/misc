-- atoms
select
    '** Compare atoms';

select
    'Expect 1',
    0 < 1;

select
    'Expect NULL',
    null < 1;

select
    'Expect NULL',
    0 < null;

-- 2-tuples
select
    '** Compare 2-tuples';

select
    'Expect 0',
    (0, 0) < (0, 0);

select
    'Expect 1',
    (0, 0) < (0, 1);

select
    'Expect NULL',
    (0, 1) < (null, 2);

select
    'Expect NULL',
    (0, null) < (0, 1);

select
    'Expect 1',
    (0, null) < (1, 0);

-- 3-tuples
select
    '** Compare 3-tuples';

select
    'Expect 0',
    (0, 0, 0) < (0, 0, 0);

select
    'Expect 1',
    (0, 0, 0) < (0, 0, 1);

select
    'Expect 0',
    (0, 1, 0) < (0, 0, 2);

select
    'Expect NULL',
    (0, 1, 0) < (0, 1, null);

select
    'Expect NULL',
    (0, 1, null) < (0, 1, 2);

select
    'Expect 1',
    (0, 1, null) < (0, 2, 2);