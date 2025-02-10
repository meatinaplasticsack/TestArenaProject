import pytest
from selenium.webdriver.common.by import By

from base_pages.login_page import login_page
from test_cases.testconfiguration import setup
from utilities.read_properties import read_config
from utilities.custom_logger import create_logs

class Test_01_Login_Page:
    login_page_url = read_config.get_login_page_url()
    username = read_config.get_username()
    password = read_config.get_password()
    invalid_username = read_config.get_invalid_username()
    logger = create_logs.logs_generator()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_open_login_page(self, setup):
        # Initializing WebDriver and opening login page.
        self.logger.info("Started \"Test_01_Login_Page\" > \"test_open_login_page\".")
        self.driver = setup
        self.driver.get(self.login_page_url)

        # Asserting that login page was successfully loaded.
        expected_title = "TestArena"
        actual_title = self.driver.title

        if actual_title == expected_title:
            self.logger.info(f"Expected title text: \"{expected_title}\", found: \"{actual_title}\". Success!")
            assert True
            self.logger.info("Ended \"Test_01_Login_Page\" > \"test_open_login_page\".")
            self.driver.close()

        else:
            self.logger.info(f"Expected title text: \"{expected_title}\", found: \"{actual_title}\". Failed!")
            self.logger.info("Ended \"Test_01_Login_Page\" > \"test_open_login_page\".")
            self.driver.save_screenshot(".\\screenshots\\test_open_login_page.png")
            self.driver.close()
            assert False

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self, setup):
        # Initializing WebDriver and opening login page.
        self.logger.info("Started \"Test_01_Login_Page\" > \"test_valid_login\".")
        self.driver = setup
        self.driver.get(self.login_page_url)

        self.login_page = login_page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()

        # Asserting that user was successfully logged in.
        expected_dashboard_text = "Zadania przypisane do mnie"
        actual_dashboard_text = self.driver.find_element(By.XPATH, "//*[@id='content']/article/article[2]/div[1]/article/h4").text

        if actual_dashboard_text == expected_dashboard_text:
            self.logger.info(f"Expected dashboard text: \"{expected_dashboard_text}\", found: \"{actual_dashboard_text}\". Success!")
            self.logger.info("Ended \"Test_01_Login_Page\" > \"test_valid_login\".")
            assert True
            self.driver.close()

        else:
            self.logger.info(f"Expected dashboard text: \"{expected_dashboard_text}\", found: \"{actual_dashboard_text}\". Failed!")
            self.logger.info("Ended \"Test_01_Login_Page\" > \"test_valid_login\".")
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_login(self, setup):
            # Initializing WebDriver and opening login page.
            self.logger.info("Started \"Test_01_Login_Page\" > \"test_invalid_login\".")
            self.driver = setup
            self.driver.get(self.login_page_url)

            self.login_page = login_page(self.driver)
            self.login_page.enter_username(self.invalid_username)
            self.login_page.enter_password(self.password)
            self.login_page.click_login()

            # Asserting that user gets correct error message.
            expected_error_message = "Adres e-mail i/lub hasło są niepoprawne."
            actual_error_message = self.driver.find_element(By.XPATH, "//*[@id='text-2']/div/form/div[3]/span/div").text

            if actual_error_message == expected_error_message:
                self.logger.info(f"Expected error message: \"{expected_error_message}\", found: \"{actual_error_message}\". Success!")
                self.logger.info("Ended \"Test_01_Login_Page\" > \"test_invalid_login\".")
                assert True
                self.driver.close()

            else:
                self.logger.info(f"Expected error message: \"{expected_error_message}\", found: \"{actual_error_message}\". Failed!")
                self.logger.info("Ended \"Test_01_Login_Page\" > \"test_invalid_login\".")
                self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
                self.driver.close()
                assert False