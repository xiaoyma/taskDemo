from flask import Flask

from com import taskSDK,task

app = Flask(__name__)

scheduler = task.scheduler
scheduler.init_app(app)
scheduler.start()

app.register_blueprint(taskSDK.taskSDK)
app.register_blueprint(task.task)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)