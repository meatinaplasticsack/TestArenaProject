import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_metadata.plugin import metadata_key

# Setup Chrome driver with some custom options related to invalid SSL certificates.
@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--allow-running-insecure-content")  # Allow insecure content.
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://beta.demo.testarena.pl/") # Force TestArena to be treated as secure site.
    driver = webdriver.Chrome(options=chrome_options)    

    return driver

# Hook for adding custom info to HTML report.
def pytest_configure(config):
    config.stash[metadata_key]["Project name"] = "TestArena project for mBank recrutation process"
    config.stash[metadata_key]["Test module name"] = "Login page tests"
    config.stash[metadata_key]["Tester name"] = "Bartosz"

# Hook for removing unwanted info from HTML report.
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)