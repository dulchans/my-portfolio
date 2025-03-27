from app.settings import BROWSER, ITEM, URL, USER_ID, USER_PW
from app.initialize_browser import initialize_browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.selenium_utils import wait_element_clickable as wait_c

def run_automation():
    '''
    ログインから決済前までのフローを自動テストし、各STEPの判定結果を返す関数
    '''
    # 各種情報を取得
    browser = BROWSER
    item = ITEM
    url = URL
    judge_results = []  # 判定結果を格納するリスト
    
    # ブラウザの初期化
    driver = initialize_browser(browser)
    # URLにアクセス
    driver.get(url)

    try:
        # STEP 1: 認証ページにアクセス
        wait_c(driver, By.ID, 'nav-link-accountList').click()
        judge_results.append('PASS')
        print('STEP 1/6 COMPLETE')
        
        # STEP 2: ログイン
        wait_c(driver, By.ID, 'ap_email').send_keys(USER_ID)
        wait_c(driver, By.ID, 'continue').click()
        wait_c(driver, By.ID, 'ap_password').send_keys(USER_PW)
        wait_c(driver, By.ID, 'signInSubmit').click()
        judge_results.append('PASS')
        print('STEP 2/6 COMPLETE')
        
        # STEP 3: 商品を検索
        wait_c(driver, By.ID, 'twotabsearchtextbox').send_keys(item)
        wait_c(driver, By.ID, 'nav-search-submit-button').click()
        wait_c(driver, By.XPATH, f"//h2[contains(@aria-label, '{item}')]").click()
        driver.switch_to.window(driver.window_handles[-1])  # タブの切替
        judge_results.append('PASS')
        print('STEP 3/6 COMPLETE')
        
        # STEP 4: カートに追加
        wait_c(driver, By.ID, 'add-to-cart-button').click()
        judge_results.append('PASS')
        print('STEP 4/6 COMPLETE')
        
        # STEP 5: レジ画面に遷移
        wait_c(driver, By.ID, 'sc-buy-box-ptc-button').click()
        driver.switch_to.window(driver.window_handles[0])  # タブの切替
        judge_results.append('PASS')
        print('STEP 5/6 COMPLETE')
        
        # STEP 6: ログアウト
        wait_c(driver, By.ID, 'nav-hamburger-menu').click()
        wait_c(driver, By.XPATH, "//a[contains(text(), 'ログアウト')]").click()
        judge_results.append('PASS')
        print('STEP 6/6 COMPLETE')
    
    # 自動処理中にエラーが発生した場合の処理
    except Exception as e:
        judge_results.append('FAIL')
        print(f'ERROR: {e}')      
    # ブラウザを閉じる
    finally:
        driver.quit()

    # 判定結果を格納したリストを返す
    return judge_results
