# python_web_pollsite
Polls Demo
-----------------------------------------------------------------------
参考：http://liujiangblog.com/course/django
-----------------------------------------------------------------------
一个新建立的项目结构大概如下：
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
各文件和目录解释：
外层的mysite/目录与Django无关，只是你项目的容器，可以任意命名。
manage.py：一个命令行工具，用于与Django进行不同方式的交互脚本，非常重要！
内层的mysite/目录是真正的项目文件包裹目录，它的名字是你引用内部文件的包名，例如：mysite.urls。
mysite/__init__.py:一个定义包的空文件。
mysite/settings.py:项目的主配置文件，非常重要！
mysite/urls.py:路由文件，所有的任务都是从这里开始分配，相当于Django驱动站点的内容表格，非常重要！
mysite/wsgi.py:一个基于WSGI的web服务器进入点，提供底层的网络通信功能，通常不用关心。
/*-------------------------------------------------------*/
系统会自动生成 polls应用的目录
python manage.py startapp polls

jango的开发服务器（以后简称服务器）默认运行在内部的8000端口
python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000


/*-------------------------------------------------------*/
默认情况，INSTALLED_APPS中会自动包含下列条目，它们都是Django自动生成的：
django.contrib.admin：admin管理后台站点
django.contrib.auth：身份认证系统
django.contrib.contenttypes：内容类型框架
django.contrib.sessions：会话框架
django.contrib.messages：消息框架
django.contrib.staticfiles：静态文件管理框架
上面的一些应用也需要建立一些数据库表，所以在使用它们之前我们要在数据库中创建这些表。使用下面的命令创建数据表：
$ python manage.py migrate。
migrate命令将遍历INSTALLED_APPS设置中的所有项目，在数据库中创建对应的表，并打印出每一条动作信息。
如果你感兴趣，可以在你的数据库命令行下输入：\dt (PostgreSQL)、 SHOW TABLES;(MySQL)或 .schema(SQLite)
来列出 Django 所创建的表。
提示：对于极简主义者，你完全可以在INSTALLED_APPS内注释掉任何或者全部的Django提供的通用应用。这样，
migrate也不会再创建对应的数据表。



python manage.py makemigrations polls
你会看到类似下面的提示：
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice

通过运行makemigrations命令，相当于告诉Django你对模型有改动，
并且你想把这些改动保存为一个“迁移(migration)”。
migrations是Django保存模型修改记录的文件，这些文件保存在磁盘上。
在例子中，它就是polls/migrations/0001_initial.py，你可以打开它看看，
里面保存的都是人类可读并且可编辑的内容，方便你随时手动修改。

接下来有一个叫做migrate的命令将对数据库执行真正的迁移动作。但是在此之前，
让我们先看看在migration的时候实际执行的SQL语句是什么。有一个叫做sqlmigrate
的命令可以展示SQL语句，例如：
$ python manage.py sqlmigrate polls 0001

如果你感兴趣，也可以运行python manage.py check命令，它将检查项目中的错误，
并不实际进行迁移或者链接数据库的操作。
现在，我们可以运行migrate命令，在数据库中进行真正的表操作了。
$ python manage.py migrate
Operations to perform:
    Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
    Rendering model states... DONE
    Applying polls.0001_initial... OK

migrate命令对所有还未实施的迁移记录进行操作，本质上就是将你对模型的修改体现到数据库中具体的表上面。
Django通过一张叫做django_migrations的表，记录并跟踪已经实施的migrate动作，通过对比获得哪些
migrations尚未提交。
migrations的功能非常强大，允许你随时修改你的模型，而不需要删除或者新建你的数据库或数据表，
在不丢失数据的同时，实时动态更新数据库。我们将在后面的章节对此进行深入的阐述，但是现在，
只需要记住修改模型时的操作分三步：
在models.py中修改模型；
运行python manage.py makemigrations为改动创建迁移记录；
运行python manage.py migrate，将操作同步到数据库。
之所以要将创建和实施迁移的动作分成两个命令两步走是因为你也许要通过版本控制系统
（例如github，svn）提交你的项目代码，如果没有一个中间过程的保存文件（migrations），
那么github如何知道以及记录、同步、实施你所进行过的模型修改动作呢？毕竟，github不和数据库直接打交道，
也没法和你本地的数据库通信。但是分开之后，你只需要将你的migration文件（例如上面的0001）上传到github，
它就会知道一切


1. 创建管理员用户
首先，我们需要通过下面的命令，创建一个可以登录admin站点的用户：

$ python manage.py createsuperuser
输入用户名：

Username: admin
输入邮箱地址：

Email address: xxx@xxx.xxx
输入密码：

Password: **********
Password (again): *********
Superuser created successfully.
注意：Django1.10版本后，超级用户的密码强制要求具备一定的复杂性，不能再偷懒了。

2. 启动开发服务器
服务器启动后，在浏览器访问http://127.0.0.1:8000/admin/。你就能看到admin的登陆界面了：

在实际环境中，为了站点的安全性，我们不能将管理后台的url随便暴露给他人，不能用/admin/这么简单的路径。
打开根url路由文件mysite/urls.py，修改其中admin.site.urls对应的正则表达式，换成你想要的，比如：
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    url(r'^my/set/', admin.site.urls),
]
这样，我们必须访问http://127.0.0.1:8000/my/set/才能进入admin界面。



如果你无法找到Django源代码文件的存放位置，可以使用下面的命令：
python -c "import django; print(django.__path__)"






