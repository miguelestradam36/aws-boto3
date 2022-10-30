from modules.aws.connector import AWSManager
import os
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    credentials = current_dir + '\config\credentials.yaml'
    file = current_dir + '\config\requirements.txt'
    buff = AWSManager()
    result = buff.secrets_log_in(credentials)
    upload = buff.upload_file(file,"test_bucket")