# CI-CD    
持续集成-持续发布    
1.git代码更新==webhook==>自定义web服务提取更新信息（[webhook post参数](gitlab_webhook.json)）     
2.web服务根据gitlab post参数调用指定jenkins api接口执行相关任务（参数化build，[demo](/jenkins_demo.py)）    
3.jenkins任务执行流水线：拉取git代码--切换到应tag/branch--docker build -- docker push([jenkins job pipeline](/config/git_in_pipeline.xml))    
4.jenkins任务执行流水线：kubectl/docker命令更新集群中相关服务的镜像到最新版本    
5.web服务根据发布的代码信息启动自动化测试    
6.根据自动化测试结果选择是否发布代码    

![image](/image/流水线.png)
