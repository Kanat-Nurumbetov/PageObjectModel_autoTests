import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Set browser language (e.g. "en", "fr", "es", etc.)')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    if user_language:
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    else:
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
