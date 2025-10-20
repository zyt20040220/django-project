# Django项目

这是一个Django项目的基本框架。

## 项目结构

- `mysite/`: Django项目的主目录
- `manage.py`: Django项目管理脚本
- `db.sqlite3`: SQLite数据库文件
- `.gitignore`: Git忽略文件配置

## 如何运行

1. 确保已安装Django：
   ```
   pip install django
   ```

2. 运行开发服务器：
   ```
   python manage.py runserver
   ```

3. 在浏览器中访问：http://127.0.0.1:8000/

## 版本控制设置

注意：如果您想使用Git进行版本控制，请按以下步骤操作：

1. 安装Git（如果尚未安装）
2. 初始化Git仓库：
   ```
   git init
   git add .
   git commit -m "Initial commit"
   ```

## 后续步骤

1. 创建Django应用：
   ```
   python manage.py startapp yourappname
   ```

2. 配置URL路由和视图
3. 创建模型和数据库迁移
4. 开发您的业务逻辑