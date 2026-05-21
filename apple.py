import os
from datetime import datetime

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

start = '<!-- apple starts -->'
end = '<!-- apple ends -->'

# 如果抓取失败，就显示提示
content = "**正在获取最新账号...**（自动更新中）\n\n**提示**：当前来源暂无可用账号，请稍后刷新或购买独享ID"

new_section = f"{start}\n{content}\n{end}"

# 安全替换
if start in readme and end in readme:
    readme = readme[:readme.find(start)] + new_section + readme[readme.find(end) + len(end):]

# 更新时间
time_str = datetime.now().strftime("%Y-%m-%d %H:%M")
readme = readme.replace('正在获取最新账号...（自动更新中）', f'最后更新：{time_str}')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ Build README 执行完成")
