import os
import sys
import threading

class ProgressPercentage(object):
    """
    Built-in Methods
    """
    def __init__(self, filename):
        """
        
        """
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        """
        
        """
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

class AWSManager():
    """
    Attributes
    """
    ACCESS_KEY = "" # access key for AWS
    SECRET_KEY = "" # secret key for AWS
    SESSION_TOKEN = "" # session token for AWS
    logging = __import__('logging') # attribute using imported module
    response = 'Action not performed' # flag for request
    """
    Methods
    """
    def __init__(self):
        """
        
        """
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='services.log')
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.logging = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.logging.addHandler(fileHandler)
        from boto3.s3.transfer import TransferConfig
        GB = 1024 ** 3
        self.config = TransferConfig(multipart_threshold=3*GB)

    def secrets_log_in(self, filepath:str)->None:
        #yaml credentials
        import yaml
        from yaml.loader import SafeLoader
        with open(filepath, 'r') as f:
            self.logging.info('Reading credentials...')
            data = yaml.load(f, Loader=SafeLoader)
            self.ACCESS_KEY = data["aws"]["profiles"]["default"]["primary_key"]
            print("ACCESS KEY: {}".format(self.ACCESS_KEY))
            self.SECRET_KEY = data["aws"]["profiles"]["default"]["secret_primary_key"]
            print("SECRET ACCESS KEY: {}".format(self.ACCESS_KEY))
        #client

    def establish_connection(self):
        from botocore.exceptions import ClientError
        try:
            import boto3
            self.client = boto3.client(
                's3',
                aws_access_key_id=self.ACCESS_KEY,
                aws_secret_access_key=self.SECRET_KEY,
                aws_session_token=self.SESSION_TOKEN
            )
            self.logging.info('Estabilished connection with server...')
        except ClientError as e:
            self.logging.error(e)

    def upload_file(self, file_name:str):
        try:
            import os
            # If S3 object_name was not specified, use file_name
            object_name = os.path.basename(file_name)
            # Upload the file
            self.client.upload_file(file_name, self.bucket_name, object_name, Config=self.config, Callback=ProgressPercentage(file_name))
            self.response = "Successfully downloaded file..."
            self.logging.info('Uploaded file to server...')
            return self.response
        except Exception as e:
            self.response = 'ERROR'
            self.logging.info('ERROR: {}'.format(e))

    @property
    def download_file(self):
        return self.response

    @download_file.setter
    def download_file(self, file_name:str):
        try:
            import os
            object_name = os.path.basename(file_name)
            self.client.download_file(
                self.bucket_name, object_name, file_name
            )
            self.response = "Successfully downloaded file..."
            self.logging.info('Downloaded file to server...')
        except Exception as e:
            self.response = 'ERROR'
            self.logging.info('ERROR: {}'.format(e.message))

    @property
    def set_bucket_name(self):
        return self.bucket_name

    @set_bucket_name.setter
    def set_bucket_name(self, bucket_name:str):        
        self.bucket_name = bucket_name
        self.logging.info('Changed working S3 Bucket...')

    @property
    def create_bucket(self):
        return self.response

    @set_bucket_name.setter
    def create_bucket(self, bucket_name:str):        
        self.client.create_bucket(Bucket=bucket_name)
        self.response = "Successfully created bucket"
        self.logging.info('Creating S3 Bucket...')

    def list_buckets(self)->dict:        
        response = self.client.list_buckets()
        self.logging.info('Listing S3 Buckets...')
        return response