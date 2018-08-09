import os.path

from lemoncheesecake.project import SimpleProjectConfiguration, HasPreRunHook

try:
    from core.common.init import init_session
except:
    print("Error! Please ensure following:\n- PYTHONPATH/TEST_ENV environment variables are set properly before"
          " running any tests.\n- All test URLs are valid and reachable.")
    exit(1)


class MyProjectConfig(SimpleProjectConfiguration, HasPreRunHook):
    def pre_run(self, cli_args, report_dir):
        init_session()


project_dir = os.path.dirname(__file__)
project = MyProjectConfig(
    suites_dir=os.path.join(project_dir, "tests"),
    fixtures_dir=os.path.join(project_dir, "core/fixtures"),
)
