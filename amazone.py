import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAJ7NLBS7D5HLJPXFA'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name =  'saas-bkp1493118166098'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

bucket = conn.get_bucket('saas-bkp1493118166098')

testfile = "test.py"

print 'Uploading %s to Amazon S3 bucket %s' % \
       (testfile, bucket_name)

import sys
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

from boto.s3.key import Key
k = Key(bucket) 
k.key   = 'my test file'
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



