import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenario, given, when, then
import time
import os

# Chemin du dossier des captures d'écran
SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "screenshots")


@pytest.fixture
def browser():
    """Fixture pour le navigateur Selenium."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@scenario('features/modal_dialog.feature', 'Ouvrir le Large Modal et vérifier qu\'il contient 4 fois le terme "lorem ipsum"')
def test_modal_dialog():
    """Scénario pour vérifier le contenu du Large Modal."""
    pass


@given("je suis sur la page Modal Dialogs de DemoQA")
def open_modal_dialog_page(browser):
    """Accéder à la page Modal Dialogs."""
    browser.get('https://demoqa.com/modal-dialogs')
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "showLargeModal"))
    )


@when("je clique sur \"Large Modal\"")
def click_large_modal(browser):
    """Clique sur le bouton pour ouvrir le Large Modal."""
    large_modal_button = browser.find_element(By.ID, "showLargeModal")
    large_modal_button.click()


@then("je vérifie que \"lorem ipsum\" apparaît 4 fois dans le texte du Large Modal")
def verify_lorem_ipsum_in_modal(browser):
    """Vérifie que le terme 'lorem ipsum' apparaît 4 fois dans le texte du Large Modal."""
    # Attendre que le modal large soit visible
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
    )

    # Capture d'écran du modal
    screenshot_path = os.path.join(SCREENSHOT_PATH, "large_modal_screenshot.png")
    browser.save_screenshot(screenshot_path)

    # Récupérer le texte du contenu du modal
    modal_text = browser.find_element(By.CSS_SELECTOR, ".modal-body").text

    # Vérifier combien de fois "lorem ipsum" apparaît
    lorem_count = modal_text.lower().count("lorem ipsum")

    # Vérifier que "lorem ipsum" apparaît exactement 4 fois
    assert lorem_count == 4, f"Erreur : Le terme 'lorem ipsum' apparaît {lorem_count} fois au lieu de 4."
    print(f"Le terme 'lorem ipsum' apparaît {lorem_count} fois dans le Large Modal. Capture d'écran enregistrée à {screenshot_path}.")

