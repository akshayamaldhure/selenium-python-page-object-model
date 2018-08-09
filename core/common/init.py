from core.conf.environments.config import get_config_object


class Base:
    ENVIRONMENT = None
    USER_BASE_URL = None


def init_session():
    config = get_config_object()
    print "Test environment: {}".format(config.ENVIRONMENT)
    print "URL under test: {}".format(config.AUTOMATION_PRACTICE_URL)
    Base.ENVIRONMENT = config.ENVIRONMENT
    Base.USER_BASE_URL = config.AUTOMATION_PRACTICE_URL
