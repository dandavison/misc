#!/bin/bash -u

echo MySQL
echo "-----"
cat tuple-comparison.sql | mysql --skip-column-names

echo
echo SQLite
echo "------"
cat tuple-comparison.sql | sqlite3

echo
echo Postgres
echo "--------"
cat tuple-comparison.sql | psql --tuples-only -d db1

echo
echo CockroachDB
cat tuple-comparison.sql | psql --tuples-only "postgresql://dan:$COCKROACH_PASSWORD@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=$HOME/.postgresql/root.crt&options=--cluster%3Droyal-bear-3614"
