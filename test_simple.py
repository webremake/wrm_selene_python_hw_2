import pytest
import random


@pytest.fixture(scope="session")
def browser(): # print("Открываем браузер") и yield  это предусловие теста
   # print(random.randint(0, 100))
    print("Открываем браузер")
    yield random.randint(0, 100)
    print("Закрываем браузер") # этот оператор выполняется после завершения теста (teardown)

@pytest.fixture
def get_admin(browser): # в эту фикстуру вложена фикстура browser
    return random.randint(0, 100)

def test_simple(get_admin, browser): # фикстуры browser и get_admin будут выполняться перед началом этого теста
    # assert get_admin == 5, "ID администратора ожидется 5"
    # assert browser == "Chrome"
    print(browser)
    assert 1 == 1, "Сообщение которое выводится когда  проверка не прошла"


def test_simple_2(get_admin, browser):
    # assert get_admin == 5
    print(browser)
    assert 1 == 1
