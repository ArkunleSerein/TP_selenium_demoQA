import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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


@scenario('features/widgets.feature', 'Vérifier que le bouton Start atteint 100%')
def test_progress_bar():
    """Scénario pour vérifier que la barre de progression atteint 100%."""
    pass

@given("je suis sur la page des widgets de DemoQA")
def open_widgets_page(browser):
    """Accède à la page des widgets de DemoQA."""
    browser.get('https://demoqa.com/progress-bar')
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "startStopButton"))
    )


@when("je clique sur le bouton \"Start\"")
def click_start_button(browser):
    """Clique sur le bouton Start pour démarrer la barre de progression."""
    start_button = browser.find_element(By.ID, "startStopButton")
    start_button.click()


@then("je vérifie que la barre de progression atteint 100%")
def verify_progress_bar(browser):
    """Vérifie que la barre de progression atteint 100%."""
    # Attendre que la barre de progression atteigne 100%
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".progress-bar"), "100%"
        )
    )
    # Vérifier que la barre est bien à 100%
    progress_bar = browser.find_element(By.CSS_SELECTOR, ".progress-bar")
    assert "100%" in progress_bar.text, f"Erreur : la barre de progression n'a pas atteint 100%."


