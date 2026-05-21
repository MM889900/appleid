import requests
import re
import os
from datetime import datetime

urls = [u.strip() for u in os.getenv('urls', '').split(',') if u.strip()]

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

start = '<!-- apple starts -->'
end = '<!-- apple ends -->'

content = "**正在获取最新账号...**（自动更新中）"

for url in urls:
    try:
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            continue
        text = r.text

        # 加强匹配规则，适配 fanqiangnan 等网站
        accounts = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        if len(accounts) > 3:
            content = ""
            for i, acc in enumerate(accounts[:12], 1):
                content += f"**账号 {i}**<br>Apple ID: <code>{acc}</code><br><br>"
            break
    except:
        continue

new_section = f"{start}\n{content}\n{end}"
readme = re.sub(f'{start}.*?{end}', new_section, readme, flags=re.DOTALL)

time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
readme = re.sub(r'正在获取最新账号\.\.\.|更新中', time_str, readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ 更新完成")
