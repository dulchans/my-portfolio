from selenium import webdriver

def initialize_browser(browser_name):
    '''
    指定されたブラウザを初期化し、WebDriverのインスタンスを返す関数
    '''

    # 各ブラウザに対応するオプションとドライバーをマッピング
    options_map = {'MicrosoftEdge': webdriver.EdgeOptions(),
                   'chrome': webdriver.ChromeOptions(),
                   'firefox': webdriver.FirefoxOptions()}
    
    # オプションをインスタンス化
    options = options_map.get(browser_name)

    # MicrosoftEdgeの処理
    if  browser_name == 'MicrosoftEdge':
        options = webdriver.EdgeOptions()
        return webdriver.Edge(options=options)
        
    # chromeの処理    
    elif browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(options=options)
        
    # firefoxの処理    
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
        
    # 対応外のブラウザや綴りが間違っている場合の処理  
    else:
        raise ValueError(f'サポートされていないブラウザです: {browser_name}')
