簡易留言板

## ✨ 功能特色

- 📝 **新增留言**：用戶可以輸入姓名和留言內容
- 👀 **檢視留言**：所有留言按時間倒序顯示
- 🗑️ **清空留言**：管理員可以清空所有留言
- 💾 **持久化儲存**：使用JSON檔案儲存留言數據
- 📱 **響應式設計**：支援桌面和手機裝置
- 🎨 **現代化UI**：漸層背景和動畫效果

1. *複製專案**
   ```bash
   git clone https://github.com/yourusername/flask-guestbook.git
   cd flask-guestbook
   ```

2. **安裝依賴**
   ```bash
   pip install flask
   ```

3. **運行應用程式**
   ```bash
   python app.py
   ```

4. **訪問網站**
   開啟瀏覽器訪問 `http://127.0.0.1:5000`

### PythonAnywhere 部署

1. **上傳檔案**
   - 將所有檔案上傳到 `/home/yourusername/mysite/`
   - 修改 `app.py` 中的 `DATA_FILE` 路徑
   - 修改 `flask_app.py` 中的用戶名

2. **設定Web App**
   - 在PythonAnywhere的Web頁面建立新的web app
   - 選擇 "Manual configuration"
   - 設定Source code路徑和WSGI檔案

3. **重新載入**
   - 點擊 "Reload" 按鈕

## 📁 專案結構

```
flask-guestbook/
├── app.py              # 主要Flask應用程式
├── flask_app.py        # PythonAnywhere WSGI設定檔
├── templates/
│   └── index.html      # HTML模板
├── requirements.txt    # Python依賴套件
├── README.md          # 專案說明文件
├── .gitignore         # Git忽略檔案
└── messages.json      # 留言數據檔案（自動生成）
```

## 🛠️ 技術棧

- **後端**: Python Flask
- **前端**: HTML5, CSS3, JavaScript
- **樣式**: 自定義CSS（漸層設計）
- **儲存**: JSON檔案
- **部署**: PythonAnywhere

## 📸 功能截圖

### 主頁面
- 美觀的漸層背景設計
- 簡潔的留言表單
- 響應式佈局

### 留言顯示
- 卡片式留言設計
- 顯示發布時間
- 留言統計資訊

## 🔧 自定義設定

### 修改樣式
在 `templates/index.html` 中的 `<style>` 區塊可以自定義：
- 顏色主題
- 字體設定
- 佈局樣式

### 修改功能
在 `app.py` 中可以：
- 新增留言驗證
- 修改儲存格式
- 添加更多功能
