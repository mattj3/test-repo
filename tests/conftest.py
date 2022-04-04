"""
This module contains shared fixtures (setup and teardown of tests)
"""

import json
import pytest
import selenium.webdriver
import time

# Location of local config, change to the location on your local machine 
config_local = '/Users/yourusername/Desktop/config.json'

@pytest.fixture
def config():
    # Read the file
    with open(config_local) as config_file:
        config = json.load(config_file)
        return config

@pytest.fixture
def browser(config):
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Url
    try: 
        b.get(config['url'])
    except:
        print("Invalid URL provided.")

    # Login
    email_id = "user_email"
    pw_id = "user_password"
    next_button_id = "next-button"
    submit_button_id = "submit-log-in"

    try: 
        b.find_element_by_id(email_id).send_keys(config["email"])
        time.sleep(0.25)
        b.find_element_by_id(next_button_id).click()
        time.sleep(0.25)
        b.find_element_by_id(pw_id).send_keys(config["pw"])
        time.sleep(0.25)
        b.find_element_by_id(submit_button_id).click()
    except:
        print("Unable to login.")

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()