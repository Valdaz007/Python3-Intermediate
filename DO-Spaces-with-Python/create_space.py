import boto3

session = boto3.session.Session()
client = (
  's3',
  region= '<Spacec-Region>',
  endpoint_url = 'https://<Space-Region>.digitalocean.com',
  aws_access_key_id = '<Key-ID>'
  aws_secret_access_key = '<Secret-Key>'
)

client.create_bucket(Bucket = '<Bucket-Name>')
