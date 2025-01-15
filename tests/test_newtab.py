import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenario, given, when, then
import time


@pytest.fixture
def browser():
    """Fixture pour le navigateur Selenium."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@scenario('features/newtab.feature', 'Ouvrir et fermer la fenêtre NewTab')
def test_newtab():
    """Scénario pour ouvrir et fermer la fenêtre NewTab."""
    pass


@given("je suis sur la page DemoQA")
def open_demoqa_page(browser):
    """Accéder à la page DemoQA."""
    browser.get('https://demoqa.com/browser-windows')
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "tabButton"))
    )


@when("je clique sur le lien 'New Tab'")
def click_new_tab_link(browser):
    """Clique sur le lien 'New Tab' pour ouvrir une nouvelle fenêtre."""

    new_tab_button = browser.find_element(By.ID, "tabButton")
    new_tab_button.click()
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)

@then("je vérifie que la nouvelle fenêtre est ouverte")
def verify_new_tab_opened(browser):
    """Vérifier que la nouvelle fenêtre a été ouverte."""
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))
    assert len(
        browser.window_handles) == 2, "Erreur : La nouvelle fenêtre n'a pas été ouverte."


@then("je ferme la fenêtre")
def close_new_tab(browser):
    """Fermer la nouvelle fenêtre ouverte."""
    main_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.close()
    browser.switch_to.window(main_window)


@then("je reviens à la fenêtre principale")
def return_to_main_window(browser):
    """Revenir à la fenêtre principale."""
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(1))
    main_window = browser.window_handles[0]
    browser.switch_to.window(main_window)
    assert browser.current_window_handle == main_window, "Erreur : La fenêtre principale n'est pas active."
