# selenium-python-page-object-model
This repository provides some working boilerplate code for building automated test suites on top of the lemoncheesecake test framework for UI-based testing with Selenium.

### Below are some of the features of this test framework:
  - Uses [lemoncheesecake](http://lemoncheesecake.io/) as a core functional test framework
  - Provides awesome and highly readable HTML reports with custom log messages and screenshot hyperlinks
  - Provides pre-configured Slack reporting which posts the report link(s) at suite level to a specific Slack channel; requires only `SLACK_AUTH_TOKEN` and channel name
  - Provides a way to define different base URL based test environment configurations
  - Provides a way to run one or more of your test suites in a single run serially

### Below is the explanation of the key packages/files/directories/modules in the code:
- The `core` package contains various other directories like `common`, `conf`, `utils`, etc.
-- The `common` package contains files like `constants.py` (used to define various constants), `init.py` (used to initialise all the base URLs under test using a `Config` object), etc.
-- The `conf` package contains an `environment` package, which lets you define various test environments (base URLs for the most part). Note that the `config.py` uses Python's `importlib` module to define a `config` object using the `TEST_ENV` environment variable set while running the tests.
-- The `utilities` package defines and lets you define various utility functions.
- As per the page object model, the `pages` package defines various page classes with element locator definitions and functions defining operations on these elements.
- The `scripts` directory contains various ad-hoc scripts, e.g. `test_ping.py` (used to check if one or more URLs pertaining to the application under test are up).
- The `tests` package contains the actual UI-based tests, which use the page class objects for instantiating the webdriver and running tests.
- The `entrypoint.sh` script does reporting related tasks and uses another `run.sh` script which is run per test suite. You must edit various variables like `SLACK_AUTH_TOKEN`, `SLACK_CHANNEL`, `ALL_TEST_SUITES` as per your needs.
- In the `run.sh` script, your must edit various variables like `SERVER_URL`, `WWW_REPORTS_DIR`, `VENV_NAME` as per your needs.

### Getting a Slack API access token
You can obtain a Slack API access token for your workspace by following the steps below:
1. In your Slack Workspace, click the Apps section.
2. In the Apps page, click Manage apps.
3. The App Directory page shows up, in this page, make a search using the keyword “bots” in the top text box Search App Directory.
4. Click Bots app > Add configuration.
5. Set Username and click Add bot integration.
6. You’ll get the API access token in Integration Settings.

### Examples
This repository contains below examples to run some simple UI-based tests from http://automationpractice.com in the test suite file `tests/LoginTests.py`. The required URLs can be found in the `core/conf/environments/default.py` file.
1. `verify_login_failure` - Launches the sign-in page of the website, enters the incorrect username and password and checks whether the login fails and an error message is shown subsequently.
2. `verify_login_success` - Enters the correct username and password and checks whether the login succeeds and the user is taken to the 'My Account' landing page.

### Setting up and running tests
1. Once you have cloned this repository, you should create a virtual environment using the `virtualenv` tool in the root directory of the project. Note that the name of this virtual environment should be the same as that in the `run.sh` and `.gitignore` files.
`$ virtualenv venv_name`
2. Activate the virtual environment with `$ source venv_name/bin/activate`
3. Install all the project dependencies with `$ pip install -r requirements.txt`
4. Set `PYTHONPATH` to the project's root directory.
5. Set `TEST_ENV` to a suitable configuration defined in any of the configuration modules in the `environment` package. Not setting this will make the test framework use the `default` configuration defined in the `environment` package since we have defined this under `config.py`.
6. Run tests with `entrypoint.sh`. Providing no arguments to this script will run all the test suites defined in the `ALL_TEST_SUITES` shell variable in the given order. In order to run one or more test suites in a custom order, you can use `entrypoint.sh my_test_suite_1 my_test_suite_2` (note no `.py` extension in the test suite names).
7. If the `SLACK_AUTH_TOKEN` and `SLACK_CHANNEL` provided in `entrypoint.sh` are valid, you should see a message in your Slack channel with test suite name, number of passed/failed tests and report link.

That's all folks. Happy testing!
