from bootstrap import Bootstrap
from config import Config
from logger import Logger
from flask import Flask
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--environment', help="Application environment", default="development", choices=['test','development','production'])
args = parser.parse_args()

app = Flask(__name__)

config = Config(args.environment)
log = Logger(config.get_config())

boot = Bootstrap()

boot.set_logger(log.get_logger())
boot.set_app(app)
boot.set_config(config.get_config())
boot.set_up_routes()

if __name__ == "__main__":
    boot.go()
