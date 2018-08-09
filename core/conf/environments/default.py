from core.conf.environments.base import BaseConfig


class Config(BaseConfig):
    ENVIRONMENT = "default"
    AUTOMATION_PRACTICE_URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"


class Prod(BaseConfig):

    def __init__(self):
        print ""
