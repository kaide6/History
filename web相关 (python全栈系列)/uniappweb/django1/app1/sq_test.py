
################################################
# #如果外部使用此脚本 则需添加此部分 且文件要从manage.py 同级的位置执行
# import django
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')
# django.setup()
################################################
from app1.models import * #引用

# python manage.py makemigrations app1
# python manage.py migrate

# debug: python manage.py shell

#增
Status.objects.create(name="002")

#查 filter结果调用 .values()->转字典
# Data1.objects.get(name="zhangsan2").age #需要确保只有一个
# Data1.objects.filter()
t1 = Data1.objects.filter(name="zhangsan")[0].age #filter出来是列表  #可跟.order_by('-age') #-表示降序
print(t1)
#按字段查 objects.values('age') or values_list('age')
#聚合查找.略

#删:
#Data1.objects.all().delete() #or xxxx.delete()

#改:
# p = Data1.objects.filter(name="zhangsan")[0]
# p.age=25
# p.save()


####
#Products
# import datetime
# Products.objects.create(name="口罩",numid=0)  #.outtime=datetime.datetime.now()

#查
# Products.objects.filter()
# 转时间
# Products.objects.filter()[0].outtime.strftime("%Y-%m-%d %H:%M:%S")


