from utils.json_parser import JSONParser
import os


def set_log_secrets_env():
    """
    Sets logger DB secrets as environment variables
    """
    if os.path.exists(os.path.join(".", "secrets", "logger.json")):
        json_parser = JSONParser(os.path.join(".", "secrets", "logger.json"))
        db_secrets_dict = json_parser.parse_json()
        url = db_secrets_dict['db_url']
        os.environ['LOGGER_URL'] = url
