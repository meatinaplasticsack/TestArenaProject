from selenium.webdriver.common.by import By

class tasks_page:
    link_add_task_xpath = "//*[@id='content']/article/div[1]/nav/ul/li/a"

    def __init__ (self, driver):
        self.driver = driver

    # Clicking Add task button.
    def add_task(self): 
        self.driver.find_element(By.XPATH, self.link_add_task_xpath).click()

        