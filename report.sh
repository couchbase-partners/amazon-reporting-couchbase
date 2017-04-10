#!/usr/bin/env bash

# You to be logged in as aws_partnership@couchbase.com with the AWS CLI to run this.

# This report isn't available before 2015-01-26
date=2015-01-26T00:00:00.000Z

aws marketplacecommerceanalytics generate-data-set \
--data-set-type daily_business_usage_by_instance_type \
--data-set-publication-date $date \
--role-name-arn arn:aws:iam::728631713266:role/MarketplaceCommerceAnalyticsRole \
--destination-s3-bucket-name marketplacereporting \
--sns-topic-arn arn:aws:sns:us-east-1:728631713266:marketplacereporting
