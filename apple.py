import requests
import re
import os
from datetime import datetime

urls = os.getenv('urls', '').split(',')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

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
            accounts = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
            if accounts:
                new_content = f"{start}\n"
                for i, acc in enumerate(accounts[:8], 1):
                    new_content += f"**账号 {i}**<br>Apple ID: <code>{acc}</code><br>\n\n"
                new_content += f"{end}"
                break
    except:
        continue

readme = re.sub(f'{start}.*?{end}', new_content, readme, flags=re.DOTALL)

time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
readme = re.sub(r'<!-- updateTime starts -->.*?<!-- updateTime ends -->', 
                f'<!-- updateTime starts -->{time_str}<!-- updateTime ends -->', readme, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ 更新完成")
