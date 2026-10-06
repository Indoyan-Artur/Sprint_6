from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL


class BasePage:
    cookies_button = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url=None):
        self.driver.get(url or BASE_URL)

    def accept_cookies_if_present(self):
        if self.is_element_present(self.cookies_button):
            self.click(self.cookies_button)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_text_or_none(self, locator):
        try:
            return self.get_text(locator)
        except TimeoutException:
            return None

    def wait_until_text_in_element(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element_value(locator, text))

    def is_element_present(self, locator):
        return bool(self.driver.find_elements(*locator))

    def get_window_handles(self):
        return self.driver.window_handles

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def switch_to_new_window(self, handles_before):
        self.wait.until(EC.number_of_windows_to_be(len(handles_before) + 1))
        new_handle = (set(self.driver.window_handles) - set(handles_before)).pop()
        self.driver.switch_to.window(new_handle)
        return new_handle

    def close_current_window(self):
        self.driver.close()

    def get_current_url(self):
        return self.driver.current_url

    def wait_until_url(self, url_part):
        try:
            self.wait.until(EC.url_contains(url_part))
            return self.driver.current_url
        except TimeoutException:
            return None