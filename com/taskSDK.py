import sys,json,requests
from past.builtins import apply
from flask import request,Blueprint


'''
author: sunqin
    fun: post/get
    type: json
    example:
    {
        "classfile": "com.ywwl.Services.faker.impl.fakerDataImpl", #目录
        "className": "fakerDataImpl", #类名
        "funcName": "getFakerPwd", #方法名
        "param": {"len": "10"} #方法传参
        "actionId": "23232323" #任务日志ID
    }
'''

taskSDK = Blueprint("taskSDK",__name__)
@taskSDK.route('/recieveTask',methods=['GET','POST'])
def recieveTask():
    try:
        data = request.get_json(force=True)
        ret = execTask(**data)
        return json.dumps({'resultCode': 1, 'result': ret})
    except Exception as e:
        print(e)
        return json.dumps({'resultCode': 1, 'result': str(e)})

def execTask(**kwargs):
    classfile =kwargs['classfile']
    className =kwargs['className']
    funcName = kwargs['funcName']
    params = kwargs['params']
    actionId = kwargs['actionId']

    #注意，params可能是json字符串，所以paramdict可能是嵌套字典
    paramdict = {}
    paramdict['actionId'] = actionId
    paramdict['params'] = params

    #动态初始化对象
    aMod = sys.modules[classfile]
    aClass = getattr(aMod, className)
    a = aClass()

    #动态执行方法
    func = a.__getattribute__(funcName)
    ret = apply(func,**paramdict)
    return ret

class taskResult():
    def respResult(self,actionId,result):
        #调用任务系统提供的接口，根据actionId查询对应日志，并修改其结果
        url = 'http://qc-job.test.ywwl.com/logResult'
        payload = {
            'actionId': actionId,
            'result': result,
        }
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return response.text