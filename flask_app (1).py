# PythonAnywhere WSGI 設定檔
# 這個檔案必須命名為 flask_app.py 並放在 /home/yourusername/mysite/ 資料夾中

import sys
import os

# 加入你的專案路徑 (請將 yourusername 改為你的 PythonAnywhere 用戶名)
path = '/home/011787/mysite'
if path not in sys.path:
    sys.path.append(path)

# 匯入你的 Flask 應用程式
from app import app as application

# 這個檔案會被 PythonAnywhere 自動執行

