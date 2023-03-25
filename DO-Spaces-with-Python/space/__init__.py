import boto3

class Space:
    def __init__(self, region, endpoint, access_id, access_secret, space_name):
        session = boto3.session.Session()
        self.client = session.client(
            's3',
            region_name = region,
            endpoint_url = endpoint,
            aws_access_key_id = access_id,
            aws_secret_access_key = access_secret
        )
        self.space_name = space_name
    
    def get_Space_Name(self):
        return self.space_name
    
    def get_Space_File_List(self):
        response = self.client.list_objects(Bucket = self.space_name)
        return response
    
    def download_File(self, filename):
        try:
            self.client.download_file(
            self.space_name,
            filename,
            f"./{filename}"
            )
            return True
        except:
            return False
    
    def upload_File(self, file, filename):
        with open(file, 'rb') as fileobj:
            self.client.upload_fileobj(fileobj, self.space_name, filename)
