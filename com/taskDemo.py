import time,json
from concurrent.futures import ThreadPoolExecutor
from com.taskSDK import taskResult

#创建线程池
executor = ThreadPoolExecutor(1)

class taskDemo():
    '''注意：此模块需要在项目中任意py文件from com.route.job.taskDemo import taskDemo，否则SDK动态动态初始化对象会报错'''
    def insideDemo(self,**kwargs):
        '''
        接入SDK的函数，在任务调度平台，保存以下信息：
        {
            "classfile": "com.route.job.taskDemo", #目录
            "className": "taskDemo", #类名
            "funcName": "insideDemo", #方法名
            "param": {"len": "10"} #方法传参
            "actionId": "23232323" #任务日志ID,自动生成传入
        }
        '''
        #提交一个线程执行具体的项目函数
        executor.submit(self.test1,**kwargs)
        print("项目已开始执行，请等待结果")
        #先返回正在执行的信息
        return "项目已开始执行，请等待结果"

    def test1(self,**kwargs):
        '''
            各自项目具体要执行的函数
        '''
        actionId = kwargs['actionId']
        params = kwargs['params']
        params = json.loads(params)
        len = params['len']
        time.sleep(5)
        print("执行一次aaa" + len)
        result = "执行一次aaa"
        #调用taskSDK的respResult方法，将执行结果传过去
        sdk = taskResult()
        ret = sdk.respResult(actionId,result)
        return "执行完毕"