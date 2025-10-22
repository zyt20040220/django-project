# GitHub远程仓库创建指南

Git已经成功安装（版本2.51.1.windows.1），并且我们已经完成了本地仓库的初始化和提交。以下是在GitHub上创建远程仓库并关联本地项目的详细步骤：

## 步骤1：在GitHub上创建远程仓库

1. 打开[GitHub官网](https://github.com)并登录您的账号
2. 点击右上角的"+"图标，选择"New repository"
3. 在仓库创建页面填写以下信息：
   - **Repository name**: 输入仓库名称，例如 `django-project`
   - **Description**: （可选）输入仓库描述
   - **Public/Private**: 选择仓库的可见性
   - **Initialize this repository with**: 不勾选"Add a README file"（因为我们已经有了）
   - 不勾选其他选项
4. 点击"Create repository"按钮

## 步骤2：关联到GitHub远程仓库

本地仓库已经初始化并完成了首次提交。创建GitHub远程仓库后，请执行以下命令关联并推送代码：

```bash
# 关联到GitHub远程仓库（请将URL替换为您实际的仓库地址）
git remote add origin https://github.com/您的用户名/django-project.git

# 推送到远程仓库
git push -u origin main
```

## 步骤3：设置SSH密钥（推荐）

为了避免每次推送都需要输入用户名和密码，您可以设置SSH密钥：

1. 在本地生成SSH密钥（Git Bash或命令行）：
   ```bash
   ssh-keygen -t ed25519 -C "您的邮箱地址"
   ```
   按照提示操作，保持默认选项即可

2. 复制生成的公钥：
   - Windows: `cat ~/.ssh/id_ed25519.pub`
   - Mac/Linux: `pbcopy < ~/.ssh/id_ed25519.pub`

3. 在GitHub上添加SSH密钥：
   - 进入GitHub的"Settings" → "SSH and GPG keys"
   - 点击"New SSH key"
   - 粘贴您的公钥并保存

4. 将远程仓库URL更改为SSH格式：
   ```bash
   git remote set-url origin git@github.com:您的用户名/django-project.git
   ```

## 注意事项

- 请确保替换所有示例中的用户名和仓库名称为您实际的信息
- 注意：本地仓库默认分支为`main`，与GitHub当前默认分支一致
- 首次推送可能需要输入GitHub账号凭证进行认证

## 后续操作

创建远程仓库后，您可以：
- 邀请协作者参与项目
- 设置GitHub Actions进行持续集成
- 配置分支保护规则
- 创建Issues和Pull Requests进行协作开发