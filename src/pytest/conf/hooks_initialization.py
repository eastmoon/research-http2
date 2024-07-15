# Reference : https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks
import pytest
import logging

# Initialization hooks
##
def pytest_addoption(parser, pluginmanager):
    print("-- pytest_addoption")
##
def pytest_addhooks(pluginmanager):
    print("-- pytest_addhooks")
##
@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    # Retrieve logging plugin object
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    # Change color on existing log level
    logging_plugin.log_cli_handler.formatter.add_color_level(logging.INFO, "cyan")
    print("-- pytest_configure")
##
@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    print("-- pytest_unconfigure")
##
@pytest.hookimpl(trylast=True)
def pytest_sessionstart(session):
    print("-- pytest_sessionstart")
##
@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    print("-- pytest_sessionfinish")
##
@pytest.hookimpl(trylast=True)
def pytest_plugin_registered(plugin, plugin_name, manager):
    print("-- pytest_plugin_registered")
