import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_github():
    with allure.step('открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').type('eroshenkoam/allure-example')  # send_keys
        s('.header-search-input').press_enter() # send_keys

    with allure.step('переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('открывает таб Isseus'):
        s('#issues-tab').click()

    with allure.step('проверяет наличие Isseus с номером 76'):
        s(by.partial_text('#76')).should(be.visible)