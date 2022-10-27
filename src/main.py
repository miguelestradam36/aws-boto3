from modules.aws.connector import AWSManager
import yaml, os
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir += '\config\credentials.yaml'
    buff = AWSManager()
    result = buff.secrets_log_in(current_dir)
    print("Main script")