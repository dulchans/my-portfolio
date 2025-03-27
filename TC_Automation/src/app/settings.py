import os
from datetime import date

'''
プログラムで使用する設定値を一元管理する
'''
# 現在の日付を取得
dt = date.today()
strf_dt = dt.strftime('%y%m%d')

# フォーマットと新規ファイルの名前とパスを取得
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
NEW_FILE = f"{strf_dt}_TC_AmazonOrder.xlsx"
NEW_FILE_PATH = os.path.join(PROJECT_DIR, 'testcase', NEW_FILE)
FORMAT_FILE = 'TC-FORMAT.xlsx'
FORMAT_FILE_PATH = os.path.join(PROJECT_DIR, 'testcase', FORMAT_FILE)

# ログインIDとPASS
USER_ID = 'ユーザーIDを入力してください'
USER_PW = 'passwordを入力してください'

# テストを実行するブラウザを設定（MicrosoftEdge、chrome、firefox）
BROWSER = 'MicrosoftEdge'
# アクセスするURLを設定
URL = 'https://www.amazon.co.jp/'
# 検索する商品名を設定
ITEM = '退屈なことはPythonにやらせよう'