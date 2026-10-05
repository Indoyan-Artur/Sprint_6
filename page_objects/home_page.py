from selenium.webdriver.support import expected_conditions as EC

from locators.home_page_locators import HomePageLocators
from page_objects.base_page import BasePage


class HomePage(BasePage, HomePageLocators):

    def click_order_button(self, button_locator_name="the_top_button"):
        button = getattr(self, button_locator_name)
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def click_faq_question(self, heading_locator_name):
        heading = getattr(self, heading_locator_name)
        self.scroll_to_element(heading)
        self.wait.until(EC.element_to_be_clickable(heading)).click()

    def get_faq_answer_text(self, answer_locator_name):
        return self.wait.until(
            EC.visibility_of_element_located(getattr(self, answer_locator_name))
        ).text
