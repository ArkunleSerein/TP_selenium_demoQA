import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """
    Fixture pour le navigateur Selenium.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@scenario('features/checkbox.feature', "Sélectionner et vérifier un élément")
def test_checkbox_selection():
    """
    Scénario pour la sélection d'un élément de checkbox.
    """
    pass


@given("je suis sur la page des checkboxes")
def open_checkbox_page(browser):
    """
    Ouvre la page des checkboxes.
    """
    browser.get('https://demoqa.com/checkbox')


@when("je sélectionne tous, sauf Excel File.doc et Office")
def select_checkbox(browser):
    """
    Sélectionne les cases "Notes", "Commands", "React", "Angular", "Veu", "Word File.doc" soit cochées.
    """
    # Attendre que le bouton pour développer toutes les options soit visible et cliquer dessus
    expand_all_checkbox = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-icon-expand-all"))
    )
    expand_all_checkbox.click()

    # Faire défiler la page vers le bas pour s'assurer que les éléments sont visibles
    browser.execute_script("window.scrollTo(0, 500);")

    # Attente pour garantir que toutes les cases sont visibles
    WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".rct-checkbox"))
    )

    # Sélectionner les cases à cocher sauf celles spécifiées
    checkboxes_to_select = [
        "Notes", "Commands", "React", "Angular", "Veu", "Word File.doc"
    ]

    for checkbox_text in checkboxes_to_select:
        checkbox = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[. = '{checkbox_text}']/preceding-sibling::span"))
        )
        checkbox.click()

    # Attendre que les cases soient cochées
    WebDriverWait(browser, 10).until(
        EC.visibility_of_any_elements_located(
            (By.CSS_SELECTOR, ".rct-icon-check")
        )
    )


@then("je dois voir le message 'You have selected : desktop notes commands workspace react angular veu wordFile' soit affiché")
def check_selected_checkboxes(browser):
    """
    Vérifier si le message "You have selected : desktop, notes, commands, workspace, react, angular, veu, wordFile" est affiché.
    """
    result_div = browser.find_element(By.ID, "result")
    message = "You have selected :\ndesktop\nnotes\ncommands\nworkspace\nreact\nangular\nveu\nwordFile"
    assert message in result_div.text


