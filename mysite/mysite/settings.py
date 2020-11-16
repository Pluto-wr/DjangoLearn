"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sn*3y-*4%rzxnd8tq0r1$d&p*h8_g0axy_yaqe2r@fp)1xxz3g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# APP列表（应用）
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',   # 记录所有Django用到的所有模型 ContentType表
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 注册上传图片应用
    'article',
    'blog',
    'read_statistics',
    'comment',
    'likes',
]

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
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# media配置，配置上传文件的保存目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 配置cdeditor 上传图片的路径
CKEDITOR_UPLOAD_PATH = 'upload/'

CKEDITOR_CONFIGS = {
    'default': {},
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}

# 自定义参数
# 页面分页数
NUMBER_OF_BLOGS_PAGES = 10


# 缓存设置--> 数据库高速缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

# # 设置日志
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
#     'formatters': {  # 日志信息显示的格式
#         'verbose': {
#             'format': '%(levelname)s -- %(asctime)s - %(name)s - %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s -- %(asctime)s - %(name)s - %(message)s'
#         },
#     },
#     'filters': {  # 对日志进行过滤
#         'require_debug_true': {  # django在debug模式下才输出日志
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {  # 日志处理方法
#         'console': {  # 向终端中输出日志
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'file': {  # 向文件中输出日志，日志会以文件的方式保存到项目目录下的 logs 文件夹下面；
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/blog.log'),  # 日志文件的位置
#             'maxBytes': 300 * 1024 * 1024,
#             'backupCount': 10,
#             'formatter': 'verbose',
#             'encoding': 'utf-8'
#         },
#     },
#     'loggers': {  # 日志器
#         'django': {  # 定义了一个名为django的日志器
#             'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
#             'propagate': True,  # 是否继续传递日志信息
#             'level': 'INFO',  # 日志器接收的最低日志级别为 INFO
#         },
#     }
# }

# import os
# import os.path, time, datetime
#
# logdir = "/data0/www/applogs"
#
# for parent, dirnames, filenames in os.walk(logdir):
#     for filename in filenames:
#         fullname = parent + "/" + filename  # 文件全称
#         createTime = int(os.path.getctime(fullname))  # 文件创建时间
#         nDayAgo = (datetime.datetime.now() - datetime.timedelta(days=2))  # 当前时间的n天前的时间
#         timeStamp = int(time.mktime(nDayAgo.timetuple()))
#         if createTime < timeStamp:  # 创建时间在n天前的文件删除
#             os.remove(os.path.join(parent, filename))
