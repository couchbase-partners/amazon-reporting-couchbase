#!/usr/bin/env bash

# You to be logged in as aws_partnership@couchbase.com with the AWS CLI to run this.
# This script was written on a Mac.  Date seems to behave differently on Linux.

# This report isn't available before 2015-01-26

start_date=20150126
end_date=`date +%Y%m%d`

i=0
while [[ $current_date < $end_date ]]
do
   current_date=`date -j -v +${i}d -f "%Y%m%d" ${start_date} +%Y%m%d`
   timestamp=`date -j -v +${i}d -f "%Y%m%d" ${start_date} +%Y-%m-%d`T00:00:00.000Z
   echo $timestamp
   i=`expr $i + 1`

   aws marketplacecommerceanalytics generate-data-set \
   --data-set-type daily_business_usage_by_instance_type \
   --data-set-publication-date $timestamp \
   --role-name-arn arn:aws:iam::728631713266:role/MarketplaceCommerceAnalyticsRole \
   --destination-s3-bucket-name marketplacereporting \
   --sns-topic-arn arn:aws:sns:us-east-1:728631713266:marketplacereporting
done
