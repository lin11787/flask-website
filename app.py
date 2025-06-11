from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-this-in-production'

# 資料檔案路徑
DATA_FILE = '/home/011787/mysite/messages.json'  # 請將 yourusername 改為你的用戶名

# 初始化留言列表
messages = []

def load_messages():
    """從檔案載入留言"""
    global messages
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                messages = json.load(f)
    except Exception as e:
        print(f"載入留言失敗: {e}")
        messages = []

def save_messages():
    """儲存留言到檔案"""
    try:
        # 確保目錄存在
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"儲存留言失敗: {e}")

# 啟動時載入現有留言
load_messages()

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    name = request.form.get('name', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not message:
        flash('請填寫姓名和留言內容！', 'error')
        return redirect(url_for('index'))

    # 新增留言
    new_message = {
        'id': len(messages) + 1,
        'name': name,
        'message': message,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    messages.insert(0, new_message)  # 新留言顯示在最前面
    save_messages()  # 儲存到檔案

    flash('留言新增成功！', 'success')
    return redirect(url_for('index'))

@app.route('/clear_messages', methods=['POST'])
def clear_messages():
    global messages
    messages = []
    save_messages()  # 儲存變更
    flash('所有留言已清空！', 'info')
    return redirect(url_for('index'))

# PythonAnywhere 不需要這個部分，因為會通過 WSGI 運行
# 以下程式碼僅用於本地開發測試
if __name__ == '__main__':
    app.run(debug=True)