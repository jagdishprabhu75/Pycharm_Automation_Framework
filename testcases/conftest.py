import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common import by


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://demo.guru99.com/test/newtours/index.php")
    driver.find_element(by.By.XPATH, "//p[@class='fc-button-label']").click()
    request.cls.driver = driver
