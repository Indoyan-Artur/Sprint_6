from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage, OrderPageLocators):

    def fill_first_step(self, case):
        self.wait.until(EC.visibility_of_element_located(self.inout_name)).send_keys(case["names"])
        self.wait.until(EC.visibility_of_element_located(self.inout_surname)).send_keys(case["surname"])
        self.wait.until(EC.visibility_of_element_located(self.inout_address)).send_keys(case["address"])
        self.wait.until(EC.visibility_of_element_located(self.inout_metro_station)).send_keys(case["station"])
        self.wait.until(EC.element_to_be_clickable(self.metro_option)).click()
        self.wait.until(EC.text_to_be_present_in_element_value(self.inout_metro_station, case["station"]))

        self.wait.until(EC.visibility_of_element_located(self.inout_phone_number)).send_keys(case["number"])
        self.accept_cookies_if_present()
        self.wait.until(EC.element_to_be_clickable(self.button_further)).click()

    def fill_second_step(self, case):
        self.wait.until(EC.visibility_of_element_located(self.inout_delivery_date)).send_keys(case["date"])
        self.wait.until(EC.visibility_of_element_located(self.inout_delivery_date)).send_keys(Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable(self.button_rental_period)).click()
        self.wait.until(EC.element_to_be_clickable(getattr(self, case["day"]))).click()
        self.wait.until(EC.element_to_be_clickable(getattr(self, case["color"]))).click()
        self.wait.until(EC.visibility_of_element_located(self.comment)).send_keys(case["comments"])

    def submit_order(self):
        self.wait.until(EC.element_to_be_clickable(self.button_order)).click()
        self.wait.until(EC.element_to_be_clickable(self.order_confirmation_button)).click()

    def wait_for_order_confirmation(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.confirmed_order_identifier)
            ).text
        except TimeoutException:
            return None

    def get_order_confirmation_handle(self):
        return self.driver.current_window_handle

    def close_modal_if_open(self):
        if self.is_element_present(self.button_view_status):
            self.wait.until(EC.element_to_be_clickable(self.button_view_status)).click()

    def return_to_confirmation_page(self, confirmation_handle):
        self.switch_to_window(confirmation_handle)
        self.close_modal_if_open()

    def click_yandex_logo(self):
        handles_before = self.get_window_handles()
        self.wait.until(EC.element_to_be_clickable(self.yandex_logo)).click()
        self.switch_to_new_window(handles_before)

    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.scooter_logo)).click()

    def close_current_window(self):
        self.driver.close()
