import time
import pytest
import keyboard
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Assurez-vous que le pilote est installé et configuré correctement.
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    #driver.quit()

# 1er Scenario, je teste la présence des éléments dans ma page
@scenario('features/contact_form.feature', "Vérifie la présence du formulaire de contact")
def test_input_field_presence():
    pass


@given('Je suis sur la page de contact')
def open_contact_page(browser):
    browser.get('https://demoqa.com/automation-practice-form')


@when('Je veux compléter les champs requis')
def input_field_presence(browser):
    pass
    assert browser.find_element(By.ID, 'firstName').is_displayed()
    assert browser.find_element(By.ID, 'lastName').is_displayed()
    assert browser.find_element(By.ID, 'userEmail').is_displayed()
    assert browser.find_element(By.XPATH, '(//label[text()="Reading"])').is_displayed()
    assert browser.find_element(By.XPATH, '(//label[text()="Music"])').is_displayed()
    assert browser.find_element(By.XPATH, '(//label[text()="Sports"])').is_displayed()
    assert browser.find_element(By.ID, 'userNumber').is_displayed()
    assert browser.find_element(By.ID, 'dateOfBirthInput').is_displayed()
    assert browser.find_element(By.ID, 'uploadPicture').is_displayed()
    assert browser.find_element(By.ID, 'currentAddress').is_displayed()
    assert browser.find_element(By.ID, 'state').is_displayed()
    assert browser.find_element(By.ID, 'city').is_displayed()
    assert browser.find_element(By.ID, 'submit').is_displayed()
    

@then('Je devrais pouvoir remplir tous les champs')
def fill_input_fields(browser):
    firstname = "John"
    lastname = "Doe"
    userMail = "johndoe@example.com"
    number_phone = "1234567890"
    reading_checkbox = browser.find_element(By.XPATH, '(//label[text()="Reading"])')
    music_checkbox = browser.find_element(By.XPATH, '(//label[text()="Music"])')
    sports_checkbox = browser.find_element(By.XPATH, '(//label[text()="Sports"])')


    browser.find_element(By.ID, 'firstName').send_keys(firstname)
    browser.find_element(By.ID, 'lastName').send_keys(lastname)
    browser.find_element(By.ID, 'userEmail').send_keys(userMail)
    browser.find_element(By.XPATH, '//label[text()="Male"]').click()
    browser.find_element(By.ID, 'userNumber').send_keys(number_phone)

    browser.execute_script("window.scrollTo(0, 500);")

    browser.find_element(By.ID, 'dateOfBirthInput').click()    
    browser.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select').click()    
    browser.find_element(By.CSS_SELECTOR, "[value='1']").click()    
    browser.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select').click()    
    browser.find_element(By.CSS_SELECTOR, "[value='2023']").click()    
    browser.find_element(By.CSS_SELECTOR, '.react-datepicker__day--001').click()

    browser.execute_script("window.scrollTo(0, 500);")

    reading_checkbox.click()
    music_checkbox.click()
    sports_checkbox.click()

    browser.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys("Maths")
    browser.find_element(By.XPATH, '//input[@id="subjectsInput"]').send_keys("\n")



    time.sleep(4)

    browser.execute_script("window.scrollTo(0, 500);")
    # browser.find_element(By.ID, 'uploadPicture').send_keys("C:/Users/DELL/Downloads/1.jpg")
    browser.find_element(By.ID, 'currentAddress').send_keys("123 Main Street")

    browser.find_element(By.ID, 'state').click()
    browser.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()
    browser.find_element(By.ID, 'city').click()
    browser.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()

@then('Je devrais pouvoir soumettre le formulaire')
def submit_form(browser):
    browser.find_element(By.ID, 'submit').click()

    time.sleep(15)






    



# 2ème Scenario, je teste la présence des éléments dans ma page


# @scenario('features/contact_form.feature', "Verify the presence of the textarea field")
# def test_textarea_field_presence():
#     pass



