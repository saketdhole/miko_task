import configparser
import os.path


class NoSuchKeyError(configparser.Error):
    def _init_(self, key, section):
        self.key = key
        self.section = section


class ReadConfig:
    def __init__(self, filePath):
        self.filePath = filePath
        self.config = None
        self.config = configparser.RawConfigParser()
        if os.path.exists(self.filePath):
            self.config.read(self.filePath)

    def api_url(self):
        for sec in self.config.sections():
            if sec == 'environment.stagging':
                URL = self.config.get('environment.stagging', 'api_url')
                return URL
