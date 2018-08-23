from __future__ import absolute_import, unicode_literals
from celery import task
from .models import TodoList,Alert
import datetime

@task()
def task_perm_delete():
    print "Perm_del task executed"
    deldate = datetime.date.today() - datetime.timedelta(days=30)
    perm_del_lists = TodoList.objects.filter(deleted_on__lt = deldate)
    perm_del_lists.delete()

# @task()
# def task_alert():
#     print "User alerted"
    
