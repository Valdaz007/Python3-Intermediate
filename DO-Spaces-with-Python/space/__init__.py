import boto3

class Space:
    def __init__(self, region: str, endpoint: str, access_id: str, access_secret: str, space_name: str):
        session = boto3.session.Session()
        self.client = session.client(
            's3',
            region_name = region,
            endpoint_url = endpoint,
            aws_access_key_id = access_id,
            aws_secret_access_key = access_secret
        )
        self.space_name = space_name
    
    def get_Space_Name(self) -> str:
        return self.space_name
    
    def get_Space_File_List(self) -> list:
        response = self.client.list_objects(Bucket = self.space_name)
        return response
    
    def download_File(self, filename: str) -> bool:
        try:
            self.client.download_file(
            self.space_name,
            filename,
            f"./{filename}"
            )
            return True
        except:
            return False
    
    def upload_File(self, file: str, filename: str):
        with open(file, 'rb') as fileobj:
            self.client.upload_fileobj(fileobj, self.space_name, filename)
    
    def delete_File(self, filename: str):
        self.client.delete_object(Bucket = self.space_name, Key = filename)
