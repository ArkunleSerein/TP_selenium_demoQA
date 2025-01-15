import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
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


@scenario('features/webtable.feature', 'Supprimer les deux dernières lignes et modifier le salaire de la première ligne')
def test_webtable():
    """Scénario pour supprimer les deux dernières lignes et modifier le salaire."""
    pass


@given("je suis sur la page Web Tables")
def open_webtables_page(browser):
    """Accéder à la page Web Tables."""
    browser.get('https://demoqa.com/webtables')
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".rt-tbody"))
    )


@when("je supprime les deux dernières lignes et modifie le salaire de la première ligne")
def delete_rows_and_modify_salary(browser):
    """Supprimer les deux dernières lignes et modifier le salaire de la première ligne."""
    WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".rt-tbody .rt-tr"))
    )

    delete_buttons = browser.find_elements(By.XPATH, "//span[@title='Delete']")

    for _ in range(2):
        delete_buttons = browser.find_elements(By.XPATH, "//span[@title='Delete']")
        delete_buttons[-1].click()
        time.sleep(1)

    first_row = browser.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr")[0]
    edit_button = first_row.find_element(By.ID, "edit-record-1")
    edit_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "salary"))
    )

    salary_input = browser.find_element(By.ID, "salary")
    salary_input.click()
    salary_input.clear()
    salary_input.send_keys("4300")

    save_button = browser.find_element(By.ID, "submit")
    save_button.click()

@then("je vérifie que le salaire a bien été mis à jour à 4300")
def check_updated_salary(browser):
    WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".rt-tbody .rt-tr"))
    )

    first_row = browser.find_elements(By.CSS_SELECTOR, ".rt-tbody .rt-tr")[0]
    salary_cell = first_row.find_elements(By.CSS_SELECTOR, ".rt-td")[4]
    salary = salary_cell.text
    assert salary == "4300"

    print("Le salaire a bien été mis à jour à 4300.")


