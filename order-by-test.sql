drop table if exists birds;

-- "family" is a reserved word in CockroachDB
create table birds (
    species varchar(32),
    _family varchar(32),
    wingspan float,
    frequency float
);

insert into
    birds
values
    ('Avocet', 'Avocets', 1, 1),
    ('Bittern', 'Herons', 2, 1),
    ('Chaffinch', 'Finches', 3, 1),
    ('Tawny Owl', 'Owls', 3, 1),
    ('Little Owl', 'Owls', 3, 2),
    ('Short-eared Owl', 'Owls', 3, 3),
    ('Null-wingspan Owl', 'Owls', 3, 4),
    ('Long-eared Owl', 'Owls', 4, 7),
    ('Barn Owl', 'Owls', 5, 7);

WITH user_query as (
    SELECT
        species,
        wingspan,
        frequency
    FROM
        birds
    WHERE
        _family = 'Owls'
    ORDER BY
        wingspan,
        frequency DESC
)
SELECT
    *
FROM
    user_query
LIMIT
    4;