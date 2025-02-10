from selenium.webdriver.common.by import By

class login_page:
    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "//*[@id='login']"

    def __init__ (self, driver):
        self.driver = driver

    # Enetering username.
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    # Enetering password.
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    # Clicking login button.
    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()