#!/bin/bash

CONTAINER_NAME=${1:-devopsdocker-db-1}

DB_USER="postgres"
DB_NAME="devOps"

echo "Using container: $CONTAINER_NAME"

echo "Copying SQL file to container..."
docker cp ./sql/sh_insert.sql "$CONTAINER_NAME"://tmp/sh_insert.sql

echo "Applying SQL..."
docker exec -i "$CONTAINER_NAME" psql -U "$DB_USER" -d "$DB_NAME" -f //tmp/sh_insert.sql

echo "Done"