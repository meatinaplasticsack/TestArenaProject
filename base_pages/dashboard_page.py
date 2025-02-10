import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class dashboard_page:
    droplist_project_selector_xpath = "/html/body/header/div[1]/span/div[1]"
    droplist_project_selector_search_xpath = "//*[@id='activeProject_chosen']/div/div/input"

    def __init__ (self, driver):
        self.driver = driver

    # Selecting element from dropdown list.
    def select_existing_project(self, existing_project_name):

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.droplist_project_selector_xpath).click()
        self.driver.find_element(By.XPATH, self.droplist_project_selector_search_xpath).send_keys(existing_project_name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.droplist_project_selector_search_xpath).send_keys(Keys.RETURN)

        """
        # Alternative version of selecting elements from dropdown list.
        droplist_project_selector = self.driver.find_element(By.ID, self.droplist_project_selector_id)
        select_existing_project = Select(droplist_project_selector)
        select_existing_project.select_by_visible_text(existing_project_name)
        """
        
        