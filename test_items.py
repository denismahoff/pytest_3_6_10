from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(0)

    button = browser.find_elements(By.CSS_SELECTOR,
                                   "#add_to_basket_form > button"
                                   )

    assert button, "Button has not been found."
    # print('Button is name:' + button)
