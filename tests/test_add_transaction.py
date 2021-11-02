"""
Add transaction test via UI.  
"""

import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_add_transaction(browser, config):
    browser.get(config["url"] + "/matters/" + config["matter_id"] + "/transactions")

    browser.find_element_by_xpath('//button[text()="Add Transaction"]').click()

    browser.find_element_by_id("transaction-amount").send_keys("99999")

    browser.find_element_by_id("transaction-description").send_keys("This is a test transaction" + str(time.time()))

    Select(browser.find_element_by_xpath("//select[@id='transaction-amount-type']")).select_by_visible_text("Chargeable Cost")

    time.sleep(0.75)

    Select(browser.find_element_by_xpath("//select[@id='transaction-neu-payment-method']")).select_by_visible_text("Other")

    time.sleep(0.75)

    elem = browser.find_element_by_id("transaction-transaction-date")

    time.sleep(0.75)

    ActionChains(browser).move_to_element(elem).click().send_keys("2021/01/01", Keys.RETURN).perform()

    time.sleep(0.75)
    
    assert browser.find_element_by_xpath("//p[contains(., 'Transaction created at')]")