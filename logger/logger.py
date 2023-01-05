import pymongo
from datetime import datetime
from utils.set_log_secrets_env import set_log_secrets_env
import os


class MongoLogger:
    """
    Custom logger that inserts logs into MongoDB
    """
    def __init__(self):
        set_log_secrets_env()
        self.url = os.getenv('LOGGER_URL')
        self.database = "bbc_logger_db"
        self.collection = "bbc_logger"
        self.__client = None
        self.__error = 0

    def __connect(self):
        try:
            self.__client = pymongo.MongoClient(self.url)
            _ = self.__client.list_database_names()
        except Exception as conn_exception:
            self.__error = 1
            self.__client = None
            raise

    def __insert(self, json_log):
        try:
            db = self.__client[self.database]
            coll = db[self.collection]
            coll.insert_one(json_log)
        except Exception as insert_err:
            self.__error = 1
            raise

    def __close_connection(self):
        if self.__client is not None:
            self.__client.close()
            self.__client = None

    def log_to_db(self, level: str, message: str):
        if self.url is not None:
            if self.__error == 0:
                self.__connect()
            if self.__error == 0:
                json_log = {"time": str(datetime.now()), "level": level, "message": message}
                self.__insert(json_log)
            if self.__client is not None:
                self.__close_connection()
