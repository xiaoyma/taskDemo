from flask import Blueprint
import datetime, pickle
from flask_apscheduler import APScheduler
from com.taskDemo import taskDemo

#创建一个调度器
scheduler = APScheduler()

#创建一个task蓝图对象
task = Blueprint("task", __name__)

def task_print_date():
    now_time = datetime.datetime.now()
    print("当前时间为" + str(now_time))


#北务接口
@task.route('/task1', methods=['GET'])
def task1():
    '''http://192.168.59.94:9000/task1"'''
    '''动态添加任务'''
    # scheduler.add_job(id="一次性任务",func=task_print_date,trigger= 'date',next_run_time=datetime.datetime.now())
    scheduler.add_job(id="循环任务",func=task_print_date,trigger='interval',seconds=3)
    # scheduler.add_job(id="定时任务" ,func=task_print_date,trigger='cron ',second='*/5')
    return "打印当前时间"

@task.route('/pause', methods=['GET'])
def pause_job():#暂停任务
    job_id = "循环任务"
    scheduler.pause_job(str(job_id))
    return '暂停成功'

@task.route('/get_jobs', methods=['GET'])
def get_task():#获取任务列表
    jobs = scheduler.get_jobs()
    print(jobs)
    return 'jobs:' + str(pickle.dumps(jobs))

@task.route('/get_job', methods=['GET'])
def get_task_detail():#获取任务详情
    job = scheduler.get_job(id='循环任务')
    print(job)
    return 'job:' + str(pickle.dumps(job))

@task.route('/resume', methods=['GET'])
def resume_job():#恢复被暂停的任务
    job_id = "循环任务"
    scheduler.resume_job(str(job_id))
    return 'Success!'

@task.route('/remove_job', methods=['GET'])
def remove_job():#删除任务
    job_id = '循环任务'
    scheduler.remove_job(str(job_id))
    return 'remove success!'