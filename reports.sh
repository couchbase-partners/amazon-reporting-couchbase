#!/usr/bin/env bash

aws s3 rm s3://marketplacereporting --recursive
./generate_reports.sh

rm -rf ./reports
aws s3 sync s3://marketplacereporting ./reports

python consolidate.py
