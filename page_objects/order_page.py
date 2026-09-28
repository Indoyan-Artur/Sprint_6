from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies_if_present(self):
        if self.driver.find_elements(*self.cookies_button):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cookies_button)).click()

    inout_name = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    inout_surname = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    inout_address = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    inout_metro_station = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    metro_option = (By.CSS_SELECTOR, "button.select-search__option") 
    inout_phone_number = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")

    button_further = (By.XPATH, "//button[normalize-space()='Далее']")

    cookies_button = (By.ID, "rcc-confirm-button")

    inout_delivery_date = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")
    button_rental_period = (By.CLASS_NAME, "Dropdown-placeholder")
    rent_for_day = (By.XPATH, "//div[contains(@class,'Dropdown-option') and normalize-space()='сутки']")
    rent_for_four_days = (By.XPATH, "//div[contains(@class,'Dropdown-option') and normalize-space()='четверо суток']")
    black_color = (By.ID, "black")
    gray_color = (By.ID, "grey")
    comment = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")

    button_order = (By.XPATH, ".//div[contains (@class, 'Order_Buttons')]/button[text()='Заказать']")

    order_confirmation_button = (By.XPATH, "//button[normalize-space()='Да']")

    confirmed_order_identifier = (By.XPATH, "//*[contains(@class,'Order_ModalHeader') and contains(text(),'Заказ оформлен')]")
    button_view_status = (By.XPATH, "//button[normalize-space()='Посмотреть статус']")

    scooter_logo = (By.CSS_SELECTOR, "[alt='Scooter']")
    yandex_logo = (By.CSS_SELECTOR, "[alt='Yandex']")

