#!/bin/bash

set -e

# TODO: in each env (L3, L2, L1) get its own secret.
# Fetch secret from AWS Secrets Manager
#DB_CREDS=$()

# Extract values using jq (ensure jq is installed)
#DB_USERNAME=$(echo "${DB_CREDS}" | jq -r '.username')
#DB_PASSWORD=$(echo "${DB_CREDS}" | jq -r '.password')
#DB_HOST=$(echo "${DB_CREDS}" | jq -r '.host')
#DB_PORT=$(echo "${DB_CREDS}" | jq -r '.port')

# https://www.odoo.com/documentation/18.0/developer/reference/cli.html#cmdoption-odoo-bin-d
odoo \
  --db_user odoo \
  --db_password odoo123 \
  --db_host localhost \
  --db_port 5432 \
  --database custom \
  --addons-path /usr/lib/python3/dist-packages/odoo/addons,/mnt/custom-addons
