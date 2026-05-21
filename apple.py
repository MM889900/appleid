import requests
import re
import os
from datetime import datetime

urls = os.getenv('urls', '').split(',')

readme = open('README.md', 'r', encoding='utf-8').read()

start = '<!-- apple starts -->'
end = '<!-- apple ends -->'

new_content = f"{start}\n**正在获取最新账号...**\n{end}"

for url in urls:
    url = url.strip()
    if not url:
        continue
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            text = r.text
            accounts = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+[:：]\s*[\w@#\$%\^&\*\(\)]+', text)
            if accounts:
                new_content = f"{start}\n"
                for acc in accounts[:15]:  # 最多显示15个
                    new_content += f"**账号**：`{acc}`\n\n"
                new_content += f"{end}"
                break
    except:
        continue

readme = re.sub(f'{start}.*?{end}', new_content, readme, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ 更新完成")
