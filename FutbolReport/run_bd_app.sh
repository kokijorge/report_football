
docker rm postgres

cat << EOF > pg-env.list
PG_MODE=primary
PG_PRIMARY_USER=postgres
PG_PRIMARY_PASSWORD=yoursecurepassword
PG_DATABASE=testdb
PG_USER=yourusername
PG_PASSWORD=yoursecurepassword
PG_ROOT_PASSWORD=yoursecurepassword
PG_PRIMARY_PORT=5432
EOF

docker run --publish 5432:5432 \
  --volume=pgvolume:/pgdata \
  --env-file=pg-env.list \
  --name="postgres" \
  --hostname="postgres" \
  --detach \
crunchydata/crunchy-postgres:centos7-9.6.17-4.1.2

rm pg-env.list

docker run --rm -p 8080:8000 --name fut -e SQLALCHEMY_DATABASE_URI='postgresql://postgres:yoursecurepassword@172.17.0.1:5432/testdb' futbolreport 