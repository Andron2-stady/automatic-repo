from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_field = driver.find_element(By.NAME, 'custname')
    name_field.send_keys('Иван Иванов')

    submit_button = driver.find_element(
        By.XPATH,
        '//input[@type="submit"] | //button[text()="Submit"]'
    )
    submit_button.click()

    assert '/post?' in driver.current_url, \
        f"URL не изменился после отправки формы! Текущий: {driver.current_url}"

    driver.quit()
