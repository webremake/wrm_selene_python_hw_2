from selene import be, have
from selene.support.shared import browser


def test_search_result_not_empty(config_browser):
    browser.open_url('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="links"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.save_screenshot('search_result_not_empty_screenshot.png')


def test_search_result_empty(config_browser):
    browser.open_url('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('гнг8нсрппс шр8гуацг -0у9кцук').press_enter()
    assert browser.element('.no-results__title').should(have.text('результаты не найдены.'))
    browser.save_screenshot('search_result_empty_screenshot.png')
