#!/usr/env/python

import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('lazydinners')
my_bucket.download_file('recipes.json', 'localrecipes.json')

