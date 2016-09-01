#!/usr/bin/python

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# connect to database
conn = connect("dbname=postgres user=postgres")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

# create development and test databases
dev_name = "feature_request_development"
test_name = "feature_request_test"
cur.execute("CREATE DATABASE " + dev_name + ";")
cur.execute("CREATE DATABASE " + test_name + ";")
conn.commit()

cur.close()
conn.close()
