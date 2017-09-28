import os
import boto
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import tarfile

 
AWS_KEY = 'AKIAJ7NLBS7D5HLJPXFA'
AWS_SECRET = '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'
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)

bucket = aws_connection.get_bucket('saas-bkp1493118166098')
bucket_name = 'saas-bkp1493118166098'

source_dir = 'test/'
output_filename= 'bkp.tar.gz'

def tar(source_dir,output_filename):
	tar = tarfile.open(output_filename,"w:gz")
	tar.add(source_dir)
	tar.close()
if tar(source_dir,output_filename) != 'NULL':
	print ('File is taring::')
else:
	print ('Check source_dir and output_filename name and path::')

testfile = output_filename

print 'Uploading %s to Amazon S3 bucket %s' % \
       (testfile, bucket_name)

import sys
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = 'aws/tenant1/' + output_filename
k.set_contents_from_filename(testfile,
        cb=percent_cb, num_cb=10)

download_url = k.generate_url(
        expires_in=60,
        response_headers={
            'response-content-type': 'text/csv',
            'response-content-disposition': 'attachment; filename={}'.format(
                testfile),
        }
    )

print download_url


