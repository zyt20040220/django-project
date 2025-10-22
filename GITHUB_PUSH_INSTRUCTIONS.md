# GitHub 远程仓库设置与代码推送指南

本文档提供了在GitHub上创建远程仓库并将本地Django项目代码推送到该仓库的详细步骤。

## 步骤1：在GitHub上创建远程仓库

1. 登录您的GitHub账号
2. 点击右上角的"+"图标，选择"New repository"
3. 填写以下信息：
   - **Repository name**: 输入仓库名称（例如：django-project）
   - **Description**: （可选）添加仓库描述
   - **Visibility**: 选择Public或Private
   - 重要：不要勾选"Add a README file"、"Add .gitignore"或"Choose a license"选项
4. 点击"Create repository"按钮创建仓库

## 步骤2：获取仓库URL

创建仓库后，GitHub会显示仓库的URL。您可以选择使用HTTPS或SSH URL。

### 选项A：使用HTTPS URL

HTTPS URL格式通常为：
```
https://github.com/您的GitHub用户名/您的仓库名.git
```

### 选项B：使用SSH URL（推荐，无需每次输入密码）

SSH URL格式通常为：
```
git@github.com:您的GitHub用户名/您的仓库名.git
```

**注意**：使用SSH URL需要您已在GitHub上配置SSH密钥。如果尚未配置，请参考GitHub官方文档进行设置。

## 步骤3：关联本地仓库与远程仓库

在命令行中，导航到您的项目目录，然后执行以下命令（请确保替换占位符为您实际的URL）：

```bash
# 使用HTTPS URL
git remote add origin https://github.com/您的GitHub用户名/您的仓库名.git

# 或者使用SSH URL
git remote add origin git@github.com:您的GitHub用户名/您的仓库名.git
```

## 步骤4：验证远程仓库配置

执行以下命令验证远程仓库是否正确添加：

```bash
git remote -v
```

您应该会看到类似以下输出：
```
origin  https://github.com/您的GitHub用户名/您的仓库名.git (fetch)
origin  https://github.com/您的GitHub用户名/您的仓库名.git (push)
```

## 步骤5：推送代码到GitHub

执行以下命令将本地代码推送到GitHub远程仓库：

```bash
git push -u origin main
```

如果使用HTTPS URL，系统可能会提示您输入GitHub用户名和密码或个人访问令牌。
如果使用SSH URL，且您已正确配置SSH密钥，则无需输入凭证。

## 常见问题排查

1. **Repository not found** 错误：
   - 确保您输入的URL中的用户名和仓库名完全正确
   - 确保您已经在GitHub上创建了对应的仓库
   - 如果使用SSH，请检查SSH密钥是否正确配置

2. **Permission denied** 错误：
   - 确保您有访问该仓库的权限
   - 如果使用HTTPS，请确认您的凭证正确
   - 如果使用SSH，请检查SSH密钥的权限和配置

3. **Branch not found** 错误：
   - 确认本地分支名称与远程分支名称一致
   - 项目当前默认分支为`main`

4. **网络连接问题**（无法连接到GitHub服务器）：
   - 检查您的网络连接是否正常
   - 尝试使用SSH方式而不是HTTPS方式
   - 如果您在企业网络或学校网络中，可能需要配置代理
   - 尝试临时关闭防火墙或安全软件，看是否是它们阻止了连接

## SSH密钥配置详细步骤（已完成部分）

我们已经为您生成了SSH密钥对，现在需要将公钥添加到GitHub账户中。

### 您的SSH公钥已保存到文件：
我们已经将您的SSH公钥保存到了项目根目录下的 `github_ssh_key.txt` 文件中。

### 将SSH公钥添加到GitHub的详细步骤：

1. **登录GitHub账户**：打开浏览器，访问 [GitHub](https://github.com) 并登录您的账户

2. **进入SSH设置页面**：
   - 点击右上角的个人头像
   - 在下拉菜单中选择"Settings"（设置）

3. **导航到SSH密钥管理**：
   - 在左侧菜单栏中，滚动到"Access"部分
   - 点击"SSH and GPG keys"（SSH和GPG密钥）

4. **添加新密钥**：
   - 点击页面右上角的绿色按钮"New SSH key"（新建SSH密钥）

5. **填写密钥信息**：
   - **Title字段**：添加一个描述性标题，例如"My Windows PC"或其他能帮助您识别此密钥的名称
   - **Key字段**：
     - 打开项目根目录下的 `github_ssh_key.txt` 文件
     - 复制从 `ssh-ed25519` 开始到邮箱地址结束的所有文本
     - 粘贴到GitHub的"Key"字段中

6. **保存密钥**：
   - 点击绿色的"Add SSH key"（添加SSH密钥）按钮
   - 如果系统提示输入GitHub密码进行确认，请输入您的密码

### 确认SSH连接正常工作

添加密钥后，您可以测试SSH连接是否正常：

```bash
ssh -T git@github.com
```

成功连接会显示类似以下消息：
```
Hi zyt20040220! You've successfully authenticated, but GitHub does not provide shell access.
```

### 已完成的步骤

✅ 已创建SSH目录
✅ 已生成SSH密钥对（使用您的邮箱：2974297201@qq.com）
✅ 已将公钥内容保存到 github_ssh_key.txt 文件
✅ 已设置SSH远程仓库（git@github.com:zyt20040220/django-project.git）

### 后续操作

完成公钥添加后，您就可以成功推送代码到GitHub了。推送命令为：

```bash
git push -u origin main
```

## 使用代理设置（如果需要）

如果您在需要代理的网络环境中，可以为Git配置代理：

```bash
# 使用HTTP代理
git config --global http.proxy http://代理服务器:端口

# 使用HTTPS代理
git config --global https.proxy https://代理服务器:端口

# 取消代理设置
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 备选方案：使用GitHub Desktop

如果命令行方式持续遇到问题，您可以尝试使用GitHub Desktop应用程序：

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 登录您的GitHub账号
3. 克隆您的仓库或添加本地仓库
4. 使用图形界面进行提交和推送操作

GitHub Desktop会自动处理认证和许多网络问题，对初学者更为友好。

## 后续操作

推送成功后，您可以：
- 在GitHub上查看和管理您的代码
- 设置分支保护规则
- 邀请协作者
- 配置GitHub Actions进行CI/CD
- 创建Issues和Pull Requests进行协作开发

祝您使用愉快！