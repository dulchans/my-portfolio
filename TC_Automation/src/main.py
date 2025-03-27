import os
from app.settings import NEW_FILE, NEW_FILE_PATH
import tkinter as tk
from tkinter import messagebox
from app.automation import run_automation
from app.generate_xl import run_generate_xl

def main():
    tk.Tk().withdraw()
    askokcancel = messagebox.askokcancel('テスト開始', 'テストを実行しますか？')

    if askokcancel:

        # 同じ名前のファイルが存在する場合は処理を中止
        if os.path.exists(NEW_FILE_PATH):
            messagebox.showwarning('テスト中止', f'同じ名前のファイルが存在します。\nファイル名: {NEW_FILE}')

        # 同じ名前のファイルが存在しない場合は処理を続行
        else:
            # 自動処理を実行して、判定結果を取得
            judge_result = run_automation()
            # Excelファイルを生成して、テストカバレッジを取得
            test_coverage = run_generate_xl(judge_result)
            # 通知後にExcelファイルを開く
            messagebox.showinfo('自動テスト終了', f'テストが終了しました。\n合格率は {test_coverage} です。')
            os.startfile(NEW_FILE_PATH)

    else:
        pass

if __name__ == '__main__':
    main()
