#!/bin/bash

SERVER_URL="http://someserver.com"
WWW_REPORTS_DIR="server_report_dir"
LOCAL_REPORTS_DIR="reports"
VENV_NAME="selenium-pom-python-venv"
REPORT_DIR_NAME=`date +'%d-%m-%Y-%H-%M-%S'`
if test ! -d reports/; then
    echo "reports directory not found, creating the same"
    mkdir -p reports/
fi
echo "Creating directory reports/$REPORT_DIR_NAME"
mkdir -p reports/${REPORT_DIR_NAME}
mkdir -p docker-report/${REPORT_DIR_NAME}
export SLACK_MESSAGE_TEMPLATE="[$TEST_ENV] $1: {passed}/{enabled} passed | $SERVER_URL/$WWW_REPORTS_DIR/$REPORT_DIR_NAME/report/report.html"
${VENV_NAME}/bin/lcc run $1 --enable-reporting slack console html --exit-error-on-failure
export CURRENT_SUITE_EXECUTION_STATUS=$?
echo "Test suite execution completed with exit code" ${CURRENT_SUITE_EXECUTION_STATUS}
echo "Copying the latest report in reports/$REPORT_DIR_NAME"
cp -r report/ ${LOCAL_REPORTS_DIR}/${REPORT_DIR_NAME}
cp -r report/ docker-report/${REPORT_DIR_NAME}
