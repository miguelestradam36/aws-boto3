from modules.aws.connector import AWSManager
from modules.config.setup import SetUpExecuter
import os
if __name__ == "__main__":
    #Setting up and installing modules/libraries
    env_setup = SetUpExecuter()
    #Current directory full path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    credentials = current_dir + '\\config\\defaults.yaml'
    file = current_dir + '\\config\\requirements.txt'
    #AWS Created Object
    buff = AWSManager()
    result = buff.secrets_log_in(credentials)
    buff.establish_connection()
    buff.create_bucket = "testbucket788bsdf"
    buff.set_bucket_name = "testbucket788bsdf"
    upload = buff.upload_file(file)
    print(upload)