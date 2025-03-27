from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_element_clickable(driver, by, value, timeout=10):
    '''
    指定した要素がクリック可能になるまで待機する関数
    '''
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, value)))

def wait_element_visibility(driver, by, value, timeout=10):
    '''
    指定した要素が表示されるまで待機する関数
    '''
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, value)))
