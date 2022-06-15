from selene import be, have
from selene.core.condition import Condition
from selene.support.shared import browser


selene_search_query = 'selene'
invalid_search_query = 'zagadaadada123'
selene_search_result = 'yashaka/selene: User-oriented Web UI browser tests in Python'


def test_search_selene(browser_size):
    search_for(text=selene_search_query, condition=have.text(selene_search_result))


def test_search_selene_fail(browser_size):
    search_for(text=invalid_search_query, condition=have.no.texts())


def search_for(text: str, condition: Condition):
    query = browser.element('[name="q"]')
    query.should(be.blank).type(text).press_enter()
    search = browser.element('#search').should(condition)
