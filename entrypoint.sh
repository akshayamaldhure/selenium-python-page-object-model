#!/bin/bash
find ./resources -name "*.json" -type f -delete
find ./resources -name "*.html" -type f -delete
export SLACK_AUTH_TOKEN="your_slack_token"
export SLACK_CHANNEL="#yourSlackChannel"
TEST_SKIP_MESSAGE="*[$TEST_ENV] One or more services required for the tests are unavailable, skipping tests.* :sleeping:"
TEST_FAIL_MESSAGE="*[$TEST_ENV] One or more tests from one or more suites have failed.* :cry:"
TEST_PASS_MESSAGE="*[$TEST_ENV] All tests from all suites have passed.* :dancing_panda:"
if [ $# -eq 0 ]; then
    declare -a ALL_TEST_SUITES=("LoginTests")
else
    declare -a ALL_TEST_SUITES=($@)
fi
ALL_TESTS_PASSED=1
if python scripts/test_ping.py; then
    for i in "${ALL_TEST_SUITES[@]}"
    do
        source ./run.sh ${i}
        if [ ${CURRENT_SUITE_EXECUTION_STATUS} == 0 ]; then
            echo "All tests from test suite ${i} passed."
        else
            ALL_TESTS_PASSED=0
        fi
    done
    if [ ${ALL_TESTS_PASSED} -eq 0 ]; then
        python scripts/send_message_to_slack.py -t "${SLACK_AUTH_TOKEN}" -c "${SLACK_CHANNEL}" -m "${TEST_FAIL_MESSAGE}"
    else
        python scripts/send_message_to_slack.py -t "${SLACK_AUTH_TOKEN}" -c "${SLACK_CHANNEL}" -m "${TEST_PASS_MESSAGE}"
    fi
else
    echo ${TEST_SKIP_MESSAGE}
    python scripts/send_message_to_slack.py -t "${SLACK_AUTH_TOKEN}" -c "${SLACK_CHANNEL}" -m "${TEST_SKIP_MESSAGE}"
fi
