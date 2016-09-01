#!/usr/bin/python

import os
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# connect to database
conn = connect("dbname=postgres user=postgres")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

dev_name = "feature_request_development"
test_name = "feature_request_test"

# create development and test databases
cur.execute("CREATE DATABASE " + dev_name + ";")
cur.execute("CREATE DATABASE " + test_name + ";")
conn.commit()

cur.close()
conn.close()

# configure enviornment
