class AWSManager():
    ACCESS_KEY = ""
    SECRET_KEY = ""
    SESSION_TOKEN = ""
    os = __import__('os')
    boto3_ = __import__('boto3')
    botocore = __import__('logging')
    connection_state = False

    def __init__(self):
        print("Initiating connection...")
        self.secrets_log_in()

    @property
    def secrets_log_in(self)->bool:
        return self.connection_state

    @secrets_log_in.setter
    def secrets_log_in(self, access_keys:str)->None:
        try:
            #yaml credentials
            import yaml
            from yaml.loader import SafeLoader
            with open('Userdetails.yaml') as f:
                data = yaml.load(f, Loader=SafeLoader)
                self.ACCESS_KEY = data["default"]["services"]["aws"]["aws_access_key_id"]
                self.SECRET_KEY = data["default"]["services"]["aws"]["aws_secret_access_key"]
                self.SESSION_TOKEN = data["default"]["services"]["aws"]["aws_session_token"]
            #client
            self.client = self.boto3_.client(
                's3',
                aws_access_key_id=self.ACCESS_KEY,
                aws_secret_access_key=self.SECRET_KEY,
                aws_session_token=self.SESSION_TOKEN
            )
            self.connection_state = True
        except Exception as error:
            self.connection_state = False

    @property
    def upload_file(self)->bool:
        """
        Getter method, which is used to define the config file path.
        """
        return self.upload_file_state_

    @upload_file.setter
    def upload_file(self, file_name:str, bucket:str, object_name:str=None)->None:
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = self.os.path.basename(file_name)

        # Upload the file
        s3_client = self.boto3.client('s3')
        from botocore.exceptions import ClientError
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
            self.upload_file_state_ = True
            return self.upload_file_state_
        except ClientError as e:
            self.logging.error(e)
            self.upload_file_state_ = False

    def __del__(self):
        print("Closing connection...")