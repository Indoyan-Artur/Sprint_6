from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Сколько это стоит? И как оплатить?
    cost_of_scooter = (By.XPATH, ".//div[@id='accordion__heading-0' and @class='accordion__button']")
    answer_cost_of_scooter = (By.XPATH, ".//div[@id='accordion__panel-0']/p")

    # Хочу сразу несколько самокатов! Так можно?
    several_scooters = (By.XPATH, ".//div[@id='accordion__heading-1' and @class='accordion__button']")
    answer_several_scooters = (By.XPATH, ".//div[@id='accordion__panel-1']/p")

    # Как рассчитывается время аренды?
    time_calculation = (By.XPATH, ".//div[@id='accordion__heading-2' and @class='accordion__button']")
    answer_time_calculation = (By.XPATH, ".//div[@id='accordion__panel-2']/p")

    # Можно ли заказать самокат прямо на сегодня?
    order_scooter_today = (By.XPATH, ".//div[@id='accordion__heading-3' and @class='accordion__button']")
    answer_order_scooter_today = (By.XPATH, ".//div[@id='accordion__panel-3']/p")

    # Можно ли продлить заказ или вернуть самокат раньше?
    extend_return_earlier = (By.XPATH, ".//div[@id='accordion__heading-4' and @class='accordion__button']")
    answer_extend_return_earlier = (By.XPATH, ".//div[@id='accordion__panel-4']/p")

    # Вы привозите зарядку вместе с самокатом?
    charging_and_scooter = (By.XPATH, ".//div[@id='accordion__heading-5' and @class='accordion__button']")
    answer_charging_and_scooter = (By.XPATH, ".//div[@id='accordion__panel-5']/p")

    # Можно ли отменить заказ?
    cancel_the_order = (By.XPATH, ".//div[@id='accordion__heading-6' and @class='accordion__button']")
    answer_cancel_the_order = (By.XPATH, ".//div[@id='accordion__panel-6']/p")

    bring_beyond_mkad = (By.XPATH, ".//div[@id='accordion__heading-7' and @class='accordion__button']")
    answer_bring_beyond_mkad = (By.XPATH, ".//div[@id='accordion__panel-7']/p")

    # Кнопка верхняя
    the_top_button = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]")

    # Кнопка нижняя
    the_bottom_button = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[contains(@class,'Button_Button')]")

    