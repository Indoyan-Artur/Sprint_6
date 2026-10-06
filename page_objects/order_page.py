from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage, OrderPageLocators):
    def fill_first_step(self, case):
        self.send_keys(self.inout_name, case["names"])
        self.send_keys(self.inout_surname, case["surname"])
        self.send_keys(self.inout_address, case["address"])
        self.send_keys(self.inout_metro_station, case["station"])
        self.click(self.metro_option)
        self.wait_until_text_in_element(self.inout_metro_station, case["station"])

        self.send_keys(self.inout_phone_number, case["number"])
        self.accept_cookies_if_present()
        self.click(self.button_further)

    def fill_second_step(self, case):
        self.send_keys(self.inout_delivery_date, case["date"])
        self.send_keys(self.inout_delivery_date, Keys.ENTER)
        self.click(self.button_rental_period)
        self.click(getattr(self, case["day"]))
        self.click(getattr(self, case["color"]))
        self.send_keys(self.comment, case["comments"])

    def submit_order(self):
        self.click(self.button_order)
        self.click(self.order_confirmation_button)

    def wait_for_order_confirmation(self):
        return self.get_text_or_none(self.confirmed_order_identifier)

    def get_order_confirmation_handle(self):
        return self.get_current_window_handle()

    def close_modal_if_open(self):
        if self.is_element_present(self.button_view_status):
            self.click(self.button_view_status)

    def return_to_confirmation_page(self, confirmation_handle):
        self.switch_to_window(confirmation_handle)
        self.close_modal_if_open()

    def click_yandex_logo(self):
        handles_before = self.get_window_handles()
        self.click(self.yandex_logo)
        self.switch_to_new_window(handles_before)

    def click_scooter_logo(self):
        self.click(self.scooter_logo)
