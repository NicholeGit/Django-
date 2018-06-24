[TOC]
# Django示例
这是一个基于Python 3.6.4+Django 2.0.5的示例。

admin账号：root

admin密码：root!234

## 项目配置

- 配置静态目录
```python
在settings.py中添加
STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),  #实际的目录地址
)
```
- 配置模板目录
```python
在settings.py中TEMPLATES添加 
'DIRS': [os.path.join(BASE_DIR,'templates')],
```
- 界面汉化
```python
在settings.py修改
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```

- 查看执行的sql

```python
在settings.py中增加
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```


## admin

创建超级用户

python manage.py createsuperuser

## 配置路由

```pyt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('waterfall/', include('waterfall.urls')),  # 给waterfall设置子路由
]
```

## APP

- [waterfall 瀑布流示例](/Django_sample/Django_sample/waterfall/README.md)

