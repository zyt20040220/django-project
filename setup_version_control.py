import os
import subprocess
import sys

# 创建一个简单的版本控制设置脚本
print("设置版本控制系统...")

# 创建.gitignore文件
print("创建.gitignore文件...")
gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
ENV/
env.bak/
venv/

# Django
*.log
*.pot
*.pyc
__pycache__/
local_settings.py

# Database
*.sqlite3

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS files
.DS_Store
Thumbs.db
"""

with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write(gitignore_content)

print(".gitignore文件已创建")

# 检查是否有Git可用的替代方案
try:
    # 尝试检查PowerShell是否有Git模块
    result = subprocess.run([sys.executable, '-c', 'import sys; print(sys.version)'], 
                          capture_output=True, text=True)
    print(f"Python版本: {result.stdout.strip()}")
    print("版本控制设置脚本完成")
except Exception as e:
    print(f"错误: {e}")

print("注意: 由于Git命令不可用，无法初始化Git仓库。您可以之后手动安装Git并运行'git init'。")