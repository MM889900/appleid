import requests
import re
import os
from datetime import datetime

# 获取账号源
urls = [u.strip() for u in os.getenv('urls', '').split(',') if u.strip()]

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

start = '<!-- apple starts -->'
end = '<!-- apple ends -->'

content = "**正在获取最新账号...**（自动更新中）"

for url in urls:
    try:
        r = requests.get(url, timeout=12)
        if r.status_code == 200:
            # 加强匹配
            accounts = re.findall(r'[\w\.-]+@[\w\.-]+\.(com|net|org|cn)', r.text)
            if len(accounts) >= 2:
                content = ""
                for i, acc in enumerate(accounts[:8], 1):
                    content += f"**账号 {i}**<br>Apple ID: <code>{acc}</code><br><br>"
                print(f"✅ 从 {url} 抓取到 {len(accounts)} 个账号")
                break
    except Exception as e:
        print(f"跳过 {url}: {e}")
        continue

# 更新内容
new_section = f"{start}\n{content}\n{end}"
readme = re.sub(f'{start}.*?{end}', new_section, readme, flags=re.DOTALL)

# 更新时间
time_str = datetime.now().strftime("%Y-%m-%d %H:%M")
readme = re.sub(r'正在获取最新账号\.\.\.|更新中', f'最后更新：{time_str}', readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ 自动抓取完成")
