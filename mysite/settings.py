"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')4o++4=p(-9vw65-nrwp)=b5sbvq2#^j)%6rm85n^h#o_ylx)%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
]
# 请注意settings文件中顶部的INSTALLED_APPS设置项。它列出了所有的项目中被激活的Django应用（app）。
# 你必须将你自定义的app注册在这里。每个应用可以被多个项目使用，并且可以打包和分发给其他人在他们的项目中使用。
# 默认情况，INSTALLED_APPS中会自动包含下列条目，它们都是Django自动生成的：
# django.contrib.admin：admin管理后台站点
# django.contrib.auth：身份认证系统
# django.contrib.contenttypes：内容类型框架
# django.contrib.sessions：会话框架
# django.contrib.messages：消息框架
# django.contrib.staticfiles：静态文件管理框架


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]  # 要有这一行，如果已经存在请保持原样
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ENGINE（引擎）：可以是django.db.backends.sqlite3、django.db.backends.postgresql、
# django.db.backends.mysql、django.db.backends.oracle，当然其它的也行。
# NAME（名称）：类似Mysql数据库管理系统中用于保存项目内容的数据库的名字。如果你使用的是默认的SQLite，
# 那么数据库将作为一个文件将存放在你的本地机器内，此时的NAME应该是这个文件的完整绝对路径包括文件名，
# 默认值os.path.join(BASE_DIR, ’db.sqlite3’)，将把该文件储存在你的项目目录下。

# import pymysql         # 一定要添加这两行！通过pip install pymysql！
# pymysql.install_as_MySQLdb()
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysite',
#         'HOST': '192.168.1.1',
#         'USER': 'root',
#         'PASSWORD': 'pwd',
#         'PORT': '3306',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/


LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
# 在修改settings文件时，请顺便将TIME_ZONE设置为国内所在的时区Asia/Shanghai
#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     'D://static/',
#     # os.path.join(BASE_DIR, "static"),
#     # '/var/www/static/',
