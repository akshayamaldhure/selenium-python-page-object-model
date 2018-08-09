from core.conf.environments.config import get_config_object


class Base:
    ENVIRONMENT = None
    USER_BASE_URL = None


def init_session():
    config = get_config_object()
    print "Test environment: {}".format(config.ENVIRONMENT)
    print "Users base URL: {}".format(config.TYPICODE_BASE_URL)
    Base.ENVIRONMENT = config.ENVIRONMENT
    Base.USER_BASE_URL = config.TYPICODE_BASE_URL
