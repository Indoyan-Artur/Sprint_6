import allure
import pytest

from config import BASE_URL, YANDEX_MAIN_URL
from test_data.order_cases import ORDER_CASES


class TestOrderScooter:
    @pytest.mark.parametrize("case", ORDER_CASES, ids=lambda c: c["name"])
    @allure.title("Полный позитивный сценарий заказа")
    def test_order(self, case, ready_home_page, order_page):
        ready_home_page.click_order_button(case["btn"])
        order_page.fill_first_step(case)
        order_page.fill_second_step(case)
        order_page.submit_order()

        text = order_page.wait_for_order_confirmation()
        assert "Заказ оформлен" in (text or ""), "Заказ не оформлен"

    @allure.title("Логотип Яндекса: новое окно с редиректом")
    def test_yandex_logo(self, placed_order, order_page):
        order_page.return_to_confirmation_page(placed_order)
        order_page.click_yandex_logo()

        current_url = order_page.wait_until_url(YANDEX_MAIN_URL)
        assert current_url and current_url.startswith(YANDEX_MAIN_URL), (f"Ожидалась главная страница Дзена, открылось: {current_url}")

    @allure.title("Логотип «Самокат»: возврат на главную")
    def test_scooter_logo(self, placed_order, order_page):
        order_page.return_to_confirmation_page(placed_order)
        order_page.click_scooter_logo()

        assert order_page.get_current_url() == BASE_URL, (f"Ожидалась главная страница Самоката, открылось: {order_page.get_current_url()}")