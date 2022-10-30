class AWSManager():
    ACCESS_KEY = ""
    SECRET_KEY = ""
    SESSION_TOKEN = ""
    def secrets_log_in(self, filepath:str)->None:
        #yaml credentials
        import yaml
        from yaml.loader import SafeLoader
        with open(filepath, 'r') as f:
            data = yaml.load(f, Loader=SafeLoader)
            self.ACCESS_KEY = data["default"]["services"]["aws"]["aws_access_key_id"]
            print("ACCESS KEY: {}".format(self.ACCESS_KEY))
            self.SECRET_KEY = data["default"]["services"]["aws"]["aws_secret_access_key"]
            print("SECRET ACCESS KEY: {}".format(self.ACCESS_KEY))
            self.SESSION_TOKEN = data["default"]["services"]["aws"]["aws_session_token"]
            print("SESSION TOKEN: {}".format(self.ACCESS_KEY))
        #client

    def establish_connection(self):
        import boto3
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.ACCESS_KEY,
            aws_secret_access_key=self.SECRET_KEY,
            aws_session_token=self.SESSION_TOKEN
        )

    @property
    def upload_file(self):
        """
        Getter method, which is used to define the config file path.
        """
        return self.response

    @upload_file.setter
    def upload_file(self, file_name:str):
        import os
        # If S3 object_name was not specified, use file_name
        object_name = os.path.basename(file_name)
        # Upload the file
        self.response = self.client.upload_file(file_name, self.bucket_name, object_name)

    @property
    def download_file(self):
        return self.response

    @download_file.setter
    def download_file(self, file_name:str, bucket:str, object_name:str=None):
        self.response = self.client.download_file(
            "bucket-name", "key-name", "tmp.txt",
            ExtraArgs={"VersionId": "my-version-id"}
        )

    @property
    def set_bucket_name(self):
        return self.bucket_name

    @download_file.setter
    def download_file(self, bucket_name:str):
        self.set_bucket_name = bucket_name
        