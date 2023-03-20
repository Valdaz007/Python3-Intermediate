import boto3

session = boto3.session.Session()

client = session.client(
  's3',
  region_name = '<region name>',
  endpoint_url = '<endpoing url>',
  aws_access_key = '<access key>',
  aws_secret_access_key = '<secret key>'
)

with open('<img file name>.<ext>', 'rb') as img:
  client.upload_fileobj(img, '<Space Name>', Key = '<img name>.<ext>')
