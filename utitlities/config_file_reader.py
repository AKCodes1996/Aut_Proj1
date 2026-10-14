


'''This file code used to read data from config.ini file '''


import configparser             # this built-in module used to read config.ini file
from pathlib import Path        # handle path or folder


'''config parsser object read ini file'''
config = configparser.ConfigParser()

config_path = Path(__file__).parent.parent / "config" / "config.ini"
config.read(config_path)


'''Reading url and browser'''
BASE_URL = config["DEFAULT"]["base_url"]
BROWSER = config["DEFAULT"]["browser"]