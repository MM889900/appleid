import os
from datetime import datetime

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

start = '<!-- apple starts -->'
end = '<!-- apple ends -->'

new_content = f"""{start}
**正在获取最新账号...**（自动更新中）
{end}"""

readme = readme.split(start)[0] + new_content + readme.split(end)[1] if end in readme else readme

time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
readme = readme.replace('更新中', time_str)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ 更新完成")
