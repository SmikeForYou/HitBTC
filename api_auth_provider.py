import os, requests
from configparser import ConfigParser
session = requests.session()

config_parser = ConfigParser()
config_parser.read(os.path.join(os.path.dirname(__file__), '.env'))
session.auth = (config_parser.get("keys", "API_KEY"), config_parser.get("keys", "API_SECRET"))