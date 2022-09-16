class AWSManager():

    os = __import__('os')
    boto3_ = __import__('boto3')
    botocore = __import__('logging')
    connection_state = False

    def __init__(self):
        print("Initiating connection...")
        self.secrets_log_in(yaml_based=True)

    @property
    def secrets_log_in(self):
        return self.connection_state

    @secrets_log_in.setter
    def secrets_log_in(self, yaml_based:bool=True, access_keys:list=None)->None:
        client = self.boto3_.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN
        )

    @property
    def upload_file(self):
        """
        Getter method, which is used to define the config file path.
        """
        return self.upload_file_state_

    @upload_file.setter
    def upload_file(self, file_name:str, bucket:str, object_name:str=None)->bool:
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
        except ClientError as e:
            self.logging.error(e)
            return False
        return True

    def __del__(self):
        print("Closing connection...")