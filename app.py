from flask import Flask
from com import taskSDK,task

#创建一个app
app = Flask(__name__)

#引用调度器
scheduler = task.scheduler
#将调度器加载到应用中
scheduler.init_app(app)
#启动调度器
scheduler.start()

#在应用中注册task蓝图对象
app.register_blueprint(task.task)
#在应用中注册taskSDK蓝图对象
app.register_blueprint(taskSDK.taskSDK)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)