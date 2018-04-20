
# Git
1. 克隆代码
    - git clone 地址
    - ctrl + insert 复制
    - shift + insert 粘贴
2. 删除分支
    - git branch -D 分支名 删除对应分支
3. 创建分支
    - git checkout -b 分支名 
4. 查看分支
    - git branch 查看所有分支
5. 切换分支
    - git checkout 分支名 切换分支
6. 查看状态
    - git status
7. 添加修改的数据到缓存区
    - git add . 把所有文件添加
    - git add 文件名 把指定文件添加
8. 提交修改到本地分支
    - git commit -m'注解'
9. 提交本地分支到远程分支上
    - git push origin 分支名 
10. 设置全局变量
    - git config --global user.email "sss@qq.com"
    - git config --global user.name "69"
11. 合并add和commit操作
    - git commit -am''
12. 创建秘钥
    - ssh-keygen -t rsa -C 账号
    - 电脑上文件位置C:\Users\Administrator\.ssh
13. 将远程拉到本地
    - git pull origin 分支名 
14. 比较分支之间的不同
    - git diff 分支1 分支2
15. 合并
    - git merge 分支名 在当前分支上合并目标分支
16. 上线代码需要打tag,在master分支打tag打版本v1.0.0.0注意一定要在主分支下打版本号
    - git tag -a 版本号 -m'注解'
17. 上传版本号
    - git push origin 版本号
18. 删除git远程分支
    - git push origin --delete 分支名 
19. 查看tag
    - git tag 
20. 删除tag 
    - git tag -d 版本号
21. 删除远程tag
    - git push origin --delete tag 版本号
22. 缓存本地修改的代码
    - git stash
    - git stash list 查看当前缓存
23. 还原缓存
    - git stash apply stash@{x}    x --> 缓存号
24. 清除缓存
    - git stash clear 清除所有缓存
25. 查看提交日志
    - git log
26. 查看某次提交内容
    - git show 版本id
27. 返回历史版本
    - git reset --hard 版本ID 
