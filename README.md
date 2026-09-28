Sprint_6

Автотесты сайта [qa-scooter.education-services.ru](https://qa-scooter.education-services.ru/)
на Python + Selenium (Firefox) + pytest, отчёт — Allure.

Покрытие

- «Вопросы о важном»: 8 тестов через параметризацию — по клику
  на вопрос открывается нужный текст.
- "Заказ самоката": позитивный сценарий с 2 наборами данных
  (параметризация), обе кнопки «Заказать» (вверху и внизу),
  проверка модалки «Заказ оформлен», клик по логотипу «Самокат»
  (возврат на главную) и логотипу Яндекса (новое окно, редирект
  ya.ru → главная Дзена).

Установка

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
+ установленные Mozilla Firefox и GeckoDriver

Запуск
python -m pytest test/ -v

Allure
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report

