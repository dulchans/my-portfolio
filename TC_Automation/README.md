TCA(TestCase_Automation with Amazon)
-----------------------------------
Amazonの購入フローを自動でテストし、結果をExcelファイルに出力する

-----------------------------------
検知できるバグ
-----------------------------------
- ページのリンク切れ
- UI崩れ
- 機能単位の動作チェック（ログイン、検索機能、カート機能）
- 商品の出品確認など

-----------------------------------
使い方
-----------------------------------
1. TC_Automationフォルダを任意のパスに格納
2. \TC_Automation\src\main.pyを実行         # Jupyterから実行したい場合はmain.ipynbを実行
3. 実行可否のダイアログで「はい」を選択
4. プログラムが実行される
5. 処理が終了後、生成したExcelファイルが表示される
6. 担当者名を入力して保存

-----------------------------------
補足
-----------------------------------
- フォルダ内に仮想環境を用意しているので、仮想環境を起動してプログラムを実行させること

- インストールしたライブラリはseleniumとopenpyxlだけなので、
　2つが入っている環境であれば、仮想環境下でなくても動作する想定です。

- WEBの自動操作中に、Bot回避のためのCAPTCHAが表示されることがあります。
　その場合は、手入力で値を入力して認証させてください。

- アカウント情報、検索したい商品、テストで使用するブラウザなど各種設定を変更したい場合は、
　以下ファイル内の設定値を変更してください。
　\TC_Automation\app\src\
　└settings.py

-----------------------------------
注意点
-----------------------------------

- ファイル、フォルダの名前変更はNG
  プログラムがパスを参照できず、機能しなくなります

- 生成したファイル名を変更しない
  テスト結果の異なるファイルが存在する原因となり、テストの一貫性が担保できなくなります
