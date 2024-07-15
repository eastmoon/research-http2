# Reference : https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks
import pytest
import logging

# Collection hooks
##
def pytest_collection(session):
    print("-- pytest_collection")
##
def pytest_ignore_collect(collection_path, config):
    print("-- pytest_ignore_collect")
##
def pytest_collect_directory(path, parent):
    print("-- pytest_collect_directory")
##
def pytest_collect_file(file_path, parent):
    print("-- pytest_collect_file")
##
def pytest_pycollect_makemodule(module_path, parent):
    print("-- pytest_pycollect_makemodule")
##
def pytest_pycollect_makeitem(collector, name, obj):
    print("-- pytest_pycollect_makeitem")
##
def pytest_generate_tests(metafunc):
    print("-- pytest_generate_tests")
##
def pytest_make_parametrize_id(config, val, argname):
    print("-- pytest_make_parametrize_id")
##
def pytest_markeval_namespace(config):
    print("-- pytest_markeval_namespace")
##
def pytest_collection_modifyitems(session, config, items):
    print("-- pytest_collection_modifyitems")
##
def pytest_collection_finish(session):
    print("-- pytest_collection_finish")
