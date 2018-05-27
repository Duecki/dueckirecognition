#!/usr/bin/python
# -*- encoding: utf-8 -*-
# https://pypi.python.org/pypi/geocoder/
import boto3
from pprint import pprint
import sys

session = boto3.Session(profile_name='default')
rek = session.client('rekognition')

imgfile = open(sys.argv[1], 'rb')
imgbytes = imgfile.read()
imgfile.close()

imgobj = {'Bytes': imgbytes}
imgattrs = ['ALL']

rekresp = rek.detect_faces(Image=imgobj, Attributes=imgattrs)

pprint (rekresp)
