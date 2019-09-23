# -*- coding: utf-8 -*-
import time
from flask import Flask,request,jsonify,json
import jenkins_demo
import config.jkconfig

app= Flask(__name__)

@app.route("/")
def index():
    return '<h1> hello flask !</h1>'

@app.route("/build")
def build_webhook():
    params = request.json if request.method == "POST" else request.args
    create_config = {
        #源码信息
        "script_path": "10.167.6.154:corepro-deploy/",
        "service": "corepro_b_fs_shadow_handler",
        "tag": "master",
        "git_credentialsid": "gitlab-yangjian-id",
        #docker镜像存储信息
        "build_image_name": "corepro_web",
        "build_image_tag": "V20190712",
        "image_hub":"ccr.ccs.tencentyun.com",
        "image_project":"sqacorepro",
        "hub_user":"100007687948",
        "hub_password":"ate.sqa123"
    }
    task_build(params,create_config)
    jk = jenkins_demo.Myjenkins(jkconfig.joblink, jkconfig.username,jkconfig.password)
    jk.build_job("corepro_common_job", params=create_config)

def task_build(git_params,default_params):
    project_mapping = {'corepro':['push','tag_push'],'boss':['tag_push']}
    if git_params["event_name"] in project_mapping[git_params["project"]["name"]]:
        default_params["service"] = git_params["project"]["name"]
        default_params["tag"] = git_params["ref"].split('/')[-1]
        default_params["build_image_name"] = git_params["project"]["name"]
        default_params["build_image_tag"] = git_params["ref"].split('/')[-1]+"_"+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    else:
        print("event not to build task")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
