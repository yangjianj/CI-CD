# -*- coding: utf-8 -*-
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build
from  jconfig import jkconfig

class Myjenkins():
    def __init__(self,url,username,password):
        self.server=Jenkins(url, username=username, password=password)

    def get_job_details(self):
        for job_name,job_instance in self.server.get_jobs():
            print(job_instance.name)
            print(job_instance.get_description())
            print(job_instance.is_running())
            print(job_instance.is_enabled())
            print("######")

    def create_job(self,**config):
        curr_con=open(config['xml'],'r+',encoding='utf-8')
        cc=curr_con.read()
        self.server.create_job(config["jobname"],cc.encode('utf-8'))

    def create_job_str(self,**config):
        cc=jkconfig.base
        self.server.create_job(config["jobname"],cc.encode('utf-8'))

    def build_job(self,jobname,params=None):
        self.server.build_job(jobname,params)

if __name__=='__main__':
    #url实例化jenkins对象时url 决定了创建目录的路径；可以新建url
    jk=Myjenkins("http://10.129.4.189:8080/user/admin/my-views/view/all/job/devops_ate/job/yangjian/","admin","ate123456!")
    print(jk.server.version)
    #jk.get_job_details()
    #print(jk.server['core'].get_config())  #获取已存在job配置文件，可通过配置文件创建job
    create_config={
        "jobname":"corepro_common_job",
         "script_path":"jimmyya/",
         "tag": "CS_web_v1.5.6_TCE_M_v1.6.0_20190627",
         "build_image_name": "test",
         "build_image_tag": "V1.6.0201907035",
         "service": "FII_T_BEACON_COREPRO_WEB"
    }

    #jk.create_job(**create_config)
    #jk.create_job_str(**create_config)
    #jk.server.build_job("job_6")
    #jk.delete_job("job_6")
    #jk.build_job(build_config["jobname"], params=jkconfig.tsf_config[8])


    for i in jkconfig.public_cloud:
        #jk.create_job_str(**i)
        jk.build_job("corepro_common_job",params=i)
        #jk.server.delete_job(i["jobname"])
        #pass




