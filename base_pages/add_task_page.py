import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class add_task_page:
    textbox_title_id = "title"
    textbox_description_id = "description"
    textbox_release_id = "token-input-releaseId"
    textbox_environments_id = "token-input-environments"
    textbox_versions_id = "token-input-versions"
    dropdown_priority_id = "priority"
    calendar_due_date_id = "dueDate"
    list_assignee_name_id = "assigneeName"
    link_assign_to_me_xpath = "//*[@id='j_assignToMe']"
    textbox_tags_id = "token-input-tags"
    button_save_id = "save"
    button_cancel_xpath = "//*[@id='content']/article/form/div[13]/span[2]/a"

    def __init__ (self, driver):
        self.driver = driver

    # Adding new task title.
    def enter_new_task_title(self, new_task_title):
        self.driver.find_element(By.ID, self.textbox_title_id).click()
        self.driver.find_element(By.ID, self.textbox_title_id).send_keys(new_task_title)
        
    # Adding new task description.
    def enter_new_task_description(self, new_task_description):
        self.driver.find_element(By.ID, self.textbox_description_id).click()
        self.driver.find_element(By.ID, self.textbox_description_id).send_keys(new_task_description)

    # Adding new task release.
    def enter_new_task_release(self, new_task_release):
        self.driver.find_element(By.ID, self.textbox_release_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.textbox_release_id).send_keys(new_task_release)
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_release_id).send_keys(Keys.RETURN)

    # Adding new task environment.
    def enter_new_task_environment(self, new_task_environment):
        self.driver.find_element(By.ID, self.textbox_environments_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.textbox_environments_id).send_keys(new_task_environment)
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_environments_id).send_keys(Keys.RETURN)

    # Adding new task version.
    def enter_new_task_version(self, new_task_version):
        self.driver.find_element(By.ID, self.textbox_versions_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.textbox_versions_id).send_keys(new_task_version)
        time.sleep(1)
        self.driver.find_element(By.ID, self.textbox_versions_id).send_keys(Keys.RETURN)

    # Selecting new task priority.
    def select_new_task_priority(self, new_task_priority):
        self.driver.find_element(By.ID, self.dropdown_priority_id).click()
        select_task_priority = Select(self.driver.find_element(By.ID, self.dropdown_priority_id))
        select_task_priority.select_by_visible_text(new_task_priority)

    # Adding new task due date.
    def enter_new_task_due_date(self, new_task_due_date):
        self.driver.find_element(By.ID, self.calendar_due_date_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.calendar_due_date_id).send_keys(new_task_due_date)
        time.sleep(1)
        self.driver.find_element(By.ID, self.calendar_due_date_id).send_keys(Keys.RETURN)

    # Adding new task assignee.
    def select_new_task_assignee(self):
        self.driver.find_element(By.XPATH, self.link_assign_to_me_xpath).click()

    # Clicking on "Save" button.
    def click_new_task_save_button(self):
        self.driver.find_element(By.ID, self.button_save_id).click()