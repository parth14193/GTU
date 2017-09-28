echo 'Adding compressed file for following directory'
tar -zcvf test.tar.gz test/

echo 'Uploading file to AWS server'
aws s3 cp bkp.tar.gz  s3://saas-bkp1493118166098/aws/

echo 'Upload completed'

echo 'Please find Download URL'
aws s3 presign s3:///saas-bkp1493118166098/aws/bkp.tar.gz

