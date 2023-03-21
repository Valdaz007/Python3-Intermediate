import boto3

session = boto3.session.Session()
client = session.client(
    's3',
    region_name='syd1',
    endpoint_url='https://syd1.digitaloceanspaces.com',
    aws_access_key_id='DO008W4NEKQE3937JCVX',
    aws_secret_access_key='UArU+tbwzNI6vJU7DJge39hid5fY3B5F/UNwZ/YAdro'
)

response = client.list_objects(Bucket='<space name>')
for content in response['Contents']:
    print(content)
