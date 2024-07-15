# Reference : https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks
import pytest
import logging

# Reporting hooks
##
def pytest_collectstart(collector):
    print("-- pytest_runtestloop")
##
def pytest_make_collect_report(collector):
    print("-- pytest_runtest_protocol")
##
def pytest_itemcollected(item):
    print("-- pytest_runtest_logstart")
##
def pytest_collectreport(report):
    print("-- pytest_runtest_logfinish")
##
def pytest_deselected(items):
    print("-- pytest_runtest_setup")
##
def pytest_report_header(config, start_path):
    print("-- pytest_runtest_call")
##
def pytest_report_collectionfinish(config, start_path, items):
    print("-- pytest_runtest_teardown")
##
def pytest_report_teststatus(report, config):
    print("-- pytest_pyfunc_call")
##
def pytest_report_to_serializable(config, report):
    print("-- pytest_runtest_teardown")
##
def pytest_report_from_serializable(config, data):
    print("-- pytest_pyfunc_call")
##
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    print("-- pytest_runtest_teardown")
##
def pytest_fixture_setup(fixturedef, request):
    print("-- pytest_pyfunc_call")
##
def pytest_fixture_post_finalizer(fixturedef, request):
    print("-- pytest_runtest_teardown")
##
def pytest_warning_recorded(warning_message, when, nodeid, location):
    print("-- pytest_pyfunc_call")
##
def pytest_runtest_logreport(report):
    print("-- pytest_runtest_teardown")
##
def pytest_assertrepr_compare(config, op, left, right):
    print("-- pytest_pyfunc_call")
##
def pytest_assertion_pass(item, lineno, orig, expl):
    print("-- pytest_runtest_teardown")
