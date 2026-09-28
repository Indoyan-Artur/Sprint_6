import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import HomePage, OrderPage
from selenium.webdriver.common.keys import Keys

BASE_URL = "https://qa-scooter.education-services.ru/"


class TestOrderScooter:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(BASE_URL)
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.home_page = HomePage(cls.driver)
        cls.order_page = OrderPage(cls.driver)
        cls.confirmation_handle = None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 

    ORDER_CASES = [
        {
            "name": "ivan_day",
            "btn": "the_top_button",
            "names": "Иван", "surname": "Иванов",
            "address": "г. Самара, ул. Неверова", "station": "Белорусская",
            "number": "+79179999659", "date": "30.12.2026",
            "day": "rent_for_day", "color": "black_color",
            "comments": "Комментарий",
        },
        {
            "name": "vasya_4days",
            "btn": "the_bottom_button",
            "names": "Вася", "surname": "Сиродоров",
            "address": "г. Воронеж, ул. Неверова", "station": "Черкизовская",
            "number": "+79179999600", "date": "29.12.2026",
            "day": "rent_for_four_days", "color": "gray_color",
            "comments": "комментарий 123",
        },
    ]

    @pytest.mark.parametrize("case", ORDER_CASES, ids=lambda c: c["name"])
    @allure.title("Полный позитивный сценарий заказа")
    def test_order_with_top_button(self, case):
        self.driver.get(BASE_URL)
        self.wait.until(EC.element_to_be_clickable(getattr(self.home_page, case["btn"]))).click()
        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_name)).send_keys(case["names"])
        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_surname)).send_keys(case["surname"])
        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_address)).send_keys(case["address"])
        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_metro_station)).send_keys(case["station"])
        self.wait.until(EC.element_to_be_clickable(self.order_page.metro_option)).click()
        self.wait.until(EC.text_to_be_present_in_element_value(self.order_page.inout_metro_station, case["station"]))

        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_phone_number)).send_keys(case["number"])   
        self.order_page.accept_cookies_if_present()   
        self.wait.until(EC.element_to_be_clickable(self.order_page.button_further)).click()   


        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_delivery_date)).send_keys(case["date"])
        self.wait.until(EC.visibility_of_element_located(self.order_page.inout_delivery_date)).send_keys(Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable(self.order_page.button_rental_period)).click()
        self.wait.until(EC.element_to_be_clickable(getattr(self.order_page, case["day"]))).click()
        self.wait.until(EC.element_to_be_clickable(getattr(self.order_page, case["color"]))).click()
        self.wait.until(EC.visibility_of_element_located(self.order_page.comment)).send_keys(case["comments"])        
        self.wait.until(EC.element_to_be_clickable(self.order_page.button_order)).click()

        self.wait.until(EC.element_to_be_clickable(self.order_page.order_confirmation_button)).click()

        text = self.wait.until(EC.visibility_of_element_located(self.order_page.confirmed_order_identifier)).text
        assert "Заказ оформлен" in text , f"Заказ не оформлен" 

        self.__class__.confirmation_handle = self.driver.current_window_handle

    def _close_modal_if_open(self):
        if self.driver.find_elements(*self.order_page.button_view_status):
            self.wait.until(EC.element_to_be_clickable(self.order_page.button_view_status)).click()

    @allure.title("Логотип Яндекса: новое окно с редиректом")
    def test_yandex_logos(self):
        self.driver.switch_to.window(self.confirmation_handle)
        self._close_modal_if_open()

        handles_before = set(self.driver.window_handles)

        self.wait.until(EC.element_to_be_clickable(self.order_page.yandex_logo)).click()

        self.wait.until(EC.number_of_windows_to_be(len(handles_before) + 1))
        new_handle = (set(self.driver.window_handles) - handles_before).pop()
        self.driver.switch_to.window(new_handle)

        self.wait.until(EC.url_contains("ya.ru"))
        assert self.driver.current_url.startswith("https://ya.ru"), f"Ожидалась главная страница Дзена, открылось: {self.driver.current_url}"

        self.driver.close()
        self.driver.switch_to.window(self.confirmation_handle)

    @allure.title("Логотип «Самокат»: возврат на главную")
    def test_scooter_logos(self):
        self.driver.switch_to.window(self.confirmation_handle)
        self._close_modal_if_open()

        self.wait.until(EC.element_to_be_clickable(self.order_page.scooter_logo)).click()

        assert self.driver.current_url == "https://qa-scooter.education-services.ru/", f"Ожидалась главная страница Самоката, открылось: {self.driver.current_url}"