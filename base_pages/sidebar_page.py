from selenium.webdriver.common.by import By

class sidebar_page:
    logo_testarena_id = "header_logo"
    list_dashboard_xpath = "//*[@id='wrapper']/ul/li[1]"
    list_project_xpath = "//*[@id='wrapper']/ul/li[2]"
    list_releases_xpath = "//*[@id='wrapper']/ul/li[3]"
    list_environments_xpath = "//*[@id='wrapper']/ul/li[4]"
    list_versions_xpath = "//*[@id='wrapper']/ul/li[5]"
    list_tags_xpath = "//*[@id='wrapper']/ul/li[6]"
    list_tasks_xpath = "//*[@id='wrapper']/ul/li[7]"
    list_tickets_xpath = "//*[@id='wrapper']/ul/li[8]"
    list_test_db_xpath = "//*[@id='wrapper']/ul/li[9]"
    list_files_xpath = "//*[@id='wrapper']/ul/li[10]"

    def __init__ (self, driver):
        self.driver = driver

    # Selecting menu items from the sidebar.
    def select_sidebar_item(self, sidebar_menu_item_name):

        if sidebar_menu_item_name == "Zadania" or "zadania":
           self.driver.find_element(By.XPATH, self.list_tasks_xpath).click()
        
        elif sidebar_menu_item_name == "Kokpit" or "kokpit":
            self.driver.find_element(By.XPATH, self.list_dashboard_xpath).click()

        elif sidebar_menu_item_name == "Projekt" or "projekt":
            self.driver.find_element(By.XPATH, self.list_project_xpath).click()

        elif sidebar_menu_item_name == "Wydania" or "wydania":
            self.driver.find_element(By.XPATH, self.list_releases_xpath).click()

        elif sidebar_menu_item_name == "Środowiska" or "Srodowiska" or "środowiska" or "srodowiska":
            self.driver.find_element(By.XPATH, self.list_environments_xpath).click()

        elif sidebar_menu_item_name == "Wersje" or "wersje":
            self.driver.find_element(By.XPATH, self.list_versions_xpath).click()

        elif sidebar_menu_item_name == "Tagi" or "tagi":
            self.driver.find_element(By.XPATH, self.list_tags_xpath).click()

        elif sidebar_menu_item_name == "Zgłoszenia" or "zgloszenia":
            self.driver.find_element(By.XPATH, self.list_tickets_xpath).click()

        elif sidebar_menu_item_name == "Baza testów" or "Baza testow" or "baza testów" or "baza testow":
            self.driver.find_element(By.XPATH, self.list_test_db_xpath).click()

        elif sidebar_menu_item_name == "Pliki" or "pliki":
            self.driver.find_element(By.XPATH, self.list_files_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.logo_testarena_id).click()
        