class AWSManager():
    ACCESS_KEY = ""
    SECRET_KEY = ""
    SESSION_TOKEN = ""
    logging = __import__('logging')

    def __init__(self):
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='installments.log')
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.logging = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.logging.addHandler(fileHandler)

    def secrets_log_in(self, filepath:str)->None:
        #yaml credentials
        import yaml
        from yaml.loader import SafeLoader
        with open(filepath, 'r') as f:
            self.logging.info('Reading credentials...')
            data = yaml.load(f, Loader=SafeLoader)
            self.ACCESS_KEY = data["aws"]["profiles"]["default"]["primary_key"]
            print("ACCESS KEY: {}".format(self.ACCESS_KEY))
            self.SECRET_KEY = data["default"]["services"]["aws"]["secret_primary_key"]
            print("SECRET ACCESS KEY: {}".format(self.ACCESS_KEY))
        #client

    def establish_connection(self):
        import boto3
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.ACCESS_KEY,
            aws_secret_access_key=self.SECRET_KEY,
            aws_session_token=self.SESSION_TOKEN
        )
        self.logging.info('Estabilished connection with server...')

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
        self.logging.info('Uploaded file to server...')

    @property
    def download_file(self):
        return self.response

    @download_file.setter
    def download_file(self, file_name:str):
        import os
        object_name = os.path.basename(file_name)
        self.response = self.client.download_file(
            self.bucket_name, object_name, file_name
        )
        self.logging.info('Downloaded file to server...')

    @property
    def set_bucket_name(self):
        return self.bucket_name

    @download_file.setter
    def download_file(self, bucket_name:str):
        self.set_bucket_name = bucket_name
        self.logging.info('Changed working S3 Bucket...')