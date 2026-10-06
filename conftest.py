import pytest
from selenium import webdriver

from page_objects import HomePage, OrderPage
from test_data.order_cases import PLACED_ORDER_CASE


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def home_page(browser):
    return HomePage(browser)


@pytest.fixture(scope="class")
def order_page(browser):
    return OrderPage(browser)


@pytest.fixture
def ready_home_page(home_page):
    home_page.open()
    home_page.accept_cookies_if_present()
    return home_page


@pytest.fixture(scope="class")
def placed_order(home_page, order_page):
    home_page.open()
    home_page.accept_cookies_if_present()
    home_page.click_order_button("the_top_button")

    order_page.fill_first_step(PLACED_ORDER_CASE)
    order_page.fill_second_step(PLACED_ORDER_CASE)
    order_page.submit_order()

    return order_page.get_order_confirmation_handle()