#!/usr/bin/env bash

./generate_reports.sh
aws s3 sync s3://marketplacereporting ./reports
