# Reference : https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks
import pytest
import logging

# Test running (runtest) hooks
##
def pytest_runtestloop(session):
    print("-- pytest_runtestloop")
##
def pytest_runtest_protocol(item, nextitem):
    print("-- pytest_runtest_protocol")
##
def pytest_runtest_logstart(nodeid, location):
    print("-- pytest_runtest_logstart")
##
def pytest_runtest_logfinish(nodeid, location):
    print("-- pytest_runtest_logfinish")
##
def pytest_runtest_setup(item):
    print("-- pytest_runtest_setup")
##
def pytest_runtest_call(item):
    print("-- pytest_runtest_call")
##
def pytest_runtest_teardown(item, nextitem):
    print("-- pytest_runtest_teardown")
##
def pytest_pyfunc_call(pyfuncitem):
    print("-- pytest_pyfunc_call")
