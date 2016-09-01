#!/bin/sh
cd ../
export DATABASE_TEST_URL="postgres://localhost/feature_request_test"
python -m feature-request.tests.app_test
cd feature-request
