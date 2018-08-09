import importlib
import os


def get_config_object():
    environment = os.environ.get('TEST_ENV', 'default')
    module_name = 'core.conf.environments.{}'.format(environment)
    config_module = importlib.import_module(module_name)
    class_ = getattr(config_module, 'Config')
    return class_()


project_dir = os.path.dirname(__file__)
