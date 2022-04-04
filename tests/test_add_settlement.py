"""
Add settlement test via UI. 
"""

import time
from selenium.webdriver.common.action_chains import ActionChains

def test_add_settlement(browser, config):
    browser.get(config["url"] + "/matters/" + config["matter_id"] + "/settlements")

    browser.find_element_by_xpath('//button[text()="Add Settlement"]').click()

    browser.find_element_by_id("settlement-debtor-offer-settlement-type-lump-sum").click()

    browser.find_element_by_id("settlement-debtor-settlement-accepted").click()

    browser.find_element_by_id("settlement-debtor-offer-settlement-amount").send_keys("99999")

    elem = browser.find_element_by_id("settlement-debtor-offer-payment-start-date")

    ActionChains(browser).move_to_element(elem).click().send_keys("2023/01/01").perform()

    time.sleep(2)

    browser.find_element_by_id("settlement-debtor-contacts--1--contact-status-contact-declined email").click()

    time.sleep(2)

    # put this one here as a hack as it helps bring the page down to access the other debtor contacts (if required)
    browser.find_element_by_id("settlement-note").send_keys("Test Note " + str(time.time()))

    try:
        browser.find_element_by_id("settlement-debtor-contacts--2--contact-status-contact-declined email").click()
    except:
        print("No element found: settlement-debtor-contacts--2--contact-status-contact-declined email")
    
    try:
        browser.find_element_by_id("settlement-debtor-contacts--3--contact-status-contact-declined email").click()
    except:
        print("No element found: settlement-debtor-contacts--3--contact-status-contact-declined email")

    time.sleep(2)

    browser.find_element_by_id("form-submit").click()

    assert browser.find_element_by_xpath("//h2[contains(., 'Workflow')]") 