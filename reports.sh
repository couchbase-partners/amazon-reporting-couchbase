#!/usr/bin/env bash

./generate_reports.sh

# copy all the reports locally
aws s3 sync s3://marketplacereporting ./reports
