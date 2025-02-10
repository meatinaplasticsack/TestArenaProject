import pytest
import time
from selenium.webdriver.common.by import By

from base_pages.login_page import login_page
from base_pages.dashboard_page import dashboard_page
from base_pages.sidebar_page import sidebar_page
from base_pages.tasks_page import tasks_page
from base_pages.add_task_page import add_task_page
from test_cases.testconfiguration import setup
from utilities.read_properties import read_config
from utilities.custom_logger import create_logs

class Test_02_Add_Task_Page:
    login_page_url = read_config.get_login_page_url()
    username = read_config.get_username()
    password = read_config.get_password()
    logger = create_logs.logs_generator()

    existing_project_name = "Amnis [Aktywny]"
    existing_project_xpath = "//*[@id='activeProject']/option[3]"
    sidebar_menu_item_name = "Zadania"

    new_task_title = "New project task"
    new_task_description = "This is description for new project task."
    new_task_release = "Wydanie"
    new_task_environment = "DEV"
    new_task_version = "1.0"
    new_task_priority = "Trywialny"
    new_task_due_date = "2024-01-05 20:20"

    @pytest.mark.regression
    def test_add_new_task(self, setup):
        # Initializing WebDriver and opening login page.
        self.logger.info("Started \"Test_02_Add_Task_Page\" > \"test_add_new_task\".")
        self.driver = setup
        self.driver.get(self.login_page_url)

        # Logging in to the Test Arena Demo.
        self.logger.info("Logging in to the \"Test Arena Demo\".")
        self.login_page = login_page(self.driver)
        self.login_page.enter_username(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()
        self.driver.maximize_window()
        
        # Selecting existing project from the list.
        self.logger.info("Selecting existing project from the list.")
        self.dashboard = dashboard_page(self.driver)
        self.dashboard.select_existing_project(self.existing_project_name)

        # Asserting that correct project was selected.
        project_selected_check = self.driver.find_element(By.XPATH, self.existing_project_xpath).is_selected()
        assert project_selected_check == True

        # Selecting Zadania menu item from the sidebar.
        self.logger.info("Selecting \"Zadania\" from the sidebar.")
        self.sidebar = sidebar_page(self.driver)
        self.sidebar.select_sidebar_item(self.sidebar_menu_item_name)

        # Clicking on "Add task" button.
        self.logger.info("Clicking on \"Dodaj zadanie\" link.")
        self.tasks = tasks_page(self.driver)
        self.tasks.add_task()

        # Entering new task title.
        self.logger.info("Entering title for the new project task.")
        self.add_tasks = add_task_page(self.driver)
        self.add_tasks.enter_new_task_title(self.new_task_title)

        # Entering new task description.
        self.logger.info("Entering description for the new project task.")
        self.add_tasks.enter_new_task_description(self.new_task_description)

        # Entering new task release.
        self.logger.info("Entering release for the new project task.")
        self.add_tasks.enter_new_task_release(self.new_task_release)

        # Entering new task environment.
        self.logger.info("Entering environment for the new project task.")
        self.add_tasks.enter_new_task_environment(self.new_task_environment)

        # Entering new task versions.
        self.logger.info("Entering versions for the new project task.")
        self.add_tasks.enter_new_task_version(self.new_task_version)

        # Selecting new task priority.
        self.logger.info("Selecting priority for the new project task.")
        self.add_tasks.select_new_task_priority(self.new_task_priority)

        # Entering new task due date.
        self.logger.info("Entering due date for the new project task.")
        self.add_tasks.enter_new_task_due_date(self.new_task_due_date)

        # Selecting new task assignee.
        self.logger.info("Selecting assignee for the new project task.")
        self.add_tasks.select_new_task_assignee()

        # Clicking on "Save" button.
        self.logger.info("Saving changes for the new project task.")
        self.add_tasks.click_new_task_save_button()
        time.sleep(3)

        # Asserting that new project task was successfully created.
        expected_message = "Zadanie zostało dodane."
        actual_message = self.driver.find_element(By.XPATH, "//*[@id='j_info_box']/p").text

        if actual_message == expected_message:
            self.logger.info(f"Expected message text: \"{expected_message}\", found: \"{actual_message}\". Success!")
            assert True
            self.logger.info("Ended \"Test_02_Add_Task_Page\" > \"test_add_new_task\".")
            self.driver.close()

        else:
            self.logger.info(f"Expected title text: \"{expected_message}\", found: \"{actual_message}\". Failed!")
            self.logger.info("Ended \"Test_02_Add_Task_Page\" > \"test_add_new_task\".")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_task.png")
            self.driver.close()
            assert False