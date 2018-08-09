from core.conf.environments.base import BaseConfig


class Config(BaseConfig):
    ENVIRONMENT = "default"
    TYPICODE_BASE_URL = "https://jsonplaceholder.typicode.com/"


class Prod(BaseConfig):

    def __init__(self):
        print ""
