# Reference : https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks
import pytest
import logging

# Bootstrapping hooks
##
def pytest_load_initial_conftests(early_config, parser, args):
    print("-- pytest_load_initial_conftests")
##
def pytest_cmdline_parse(pluginmanager, args):
    print("-- pytest_cmdline_parse")
##
def pytest_cmdline_main(config):
    print("-- pytest_cmdline_main")
