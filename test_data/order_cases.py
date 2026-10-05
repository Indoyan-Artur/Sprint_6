#Тестовые данные заказа самоката.

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

# Данные для предусловия, заказ оформляется один раз
PLACED_ORDER_CASE = {
    "names": "Тест", "surname": "Тестов",
    "address": "г. Москва, ул. Ленина", "station": "Белорусская",
    "number": "+79179999659", "date": "30.12.2026",
    "day": "rent_for_day", "color": "black_color",
    "comments": "Предусловие для проверки логотипов",
}
