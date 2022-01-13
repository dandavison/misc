#!/bin/bash -u

echo "** MySQL: $(mysql --version)"
cat order-by-test.sql | mysql -D db1 --table

echo
echo "** SQLite: $(sqlite3 --version)"
cat order-by-test.sql | sqlite3 -column -header

echo
echo "** Postgres: $(postgres --version)"
cat order-by-test.sql | psql --quiet -d db1

echo
echo "** CockroachDB"
cat order-by-test.sql | psql --quiet "postgresql://dan:$COCKROACH_PASSWORD@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=$HOME/.postgresql/root.crt&options=--cluster%3Droyal-bear-3614"
