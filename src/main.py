from modules.aws.connector import AWSManager
import yaml, os
if __name__ == "__main__":
    buff = AWSManager()
    result = buff.secrets_log_in("config\credentials.yaml")
    print("Main script")