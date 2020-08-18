#!/bin/bash

# https://info.crunchydata.com/blog/easy-postgresql-10-and-pgadmin-4-setup-with-docker


docker volume create --driver local --name=pgvolume
#docker volume create --driver local --name=pga4volume

docker network create --driver bridge pgnetwork



if [ ! "$(docker ps -q -f name=postgres)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=postgres)" ]; then
        # cleanup
        docker rm postgres
    fi
    # run your container

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

	docker run --rm --publish 5432:5432 \
	  --volume=pgvolume:/pgdata \
	  --volume=$(pwd):/mydata \
	  --env-file=pg-env.list \
	  --name="postgres" \
	  --hostname="postgres" \
	  --detach \
	crunchydata/crunchy-postgres:centos7-9.6.17-4.1.2

	rm pg-env.list
fi




#docker run --publish 5050:5050 \
#  --volume=pga4volume:/var/lib/pgadmin \
#  --env-file=pgadmin-env.list \
#  --name="pgadmin4" \
#  --hostname="pgadmin4" \
#  --detach \
#crunchydata/crunchy-pgadmin4:centos7-11.6-4.1.1

docker run --rm -p 80:80 --name fut \
   --volume=$(pwd)/../FutbolReport:/src \
   -e SQLALCHEMY_DATABASE_URI='postgresql://postgres:yoursecurepassword@172.17.0.1:5432/testdb' \
   futbolreport 