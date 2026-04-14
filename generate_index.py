import os

# 定義要掃描的資料夾
folders = ['Ubuntu', '2.5.3', 'VFIFE']
html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>Truchas-Lab 文件導覽</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; padding: 40px; max-width: 900px; margin: auto; background-color: #0d1117; color: #ffffff; }
        h1 { border-bottom: 1px solid #30363d; }
        h2 { color: #58a6ff; margin-top: 30px; }
        li { margin-bottom: 10px; padding: 15px; border: 1px solid #30363d; border-radius: 8px; background-color: #161b22; }
        a { text-decoration: none; color: #58a6ff; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Truchas-Lab 模擬與研究筆記 (自動更新版)</h1>"""

for folder in folders:
    if os.path.exists(folder):
        html_content += f"<h2>{folder}</h2><ul>"
        files = sorted([f for f in os.listdir(folder) if f.endswith('.html') and f != 'tmp'])
        for f in files:
            html_content += f'<li><a href="{folder}/{f}">{f}</a></li>'
        html_content += "</ul>"

html_content += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
