* [https://github.com/xwisen/ltw/issues/169](https://github.com/xwisen/ltw/issues/169)

```shell
# django-xadmin对不支持python3/django2.x
pip install django-admin # 安装django/django-admin

# 创建项目
mkdir /Users/xwisen.wz/go/src/github.com/xwisen/djangodemo
django-admin startproject -v 3 djangodemo /Users/xwisen.wz/go/src/github.com/xwisen/djangodemo
cd /Users/xwisen.wz/go/src/github.com/xwisen/djangodemo/

# 增加git
git init;git add .;git commit -m "django 命令行初始化项目"

# 
./manage.py migrate --plan # 打印DB变更计划
./manage.py migrate -v 3 # 执行DB变更

./manage.py createsuperuser -v 3 --username admin --email admin@admin.com # 创建admin账号

# 修改支持语言、时区, settings.py
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
STATIC_ROOT = './static/'

./manage.py collectstatic # 把静态文件打包到STATIC_ROOT目录
./manage.py runserver  # run server

```

```shell
# 增加模板, settings.py
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

ln -s adminlte2.3.7 templates
ln -s adminlte2.3.7 static
```

```shell
# ORM 使用，增加数据库变更
./manage.py makemigrations # 生成migrate 语句
./manage.py showmigrations # 查看migrate 语句
./manage.py migrate # 执行migrate

```