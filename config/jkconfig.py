base = """<?xml version="1.0" encoding="UTF-8"?>
<flow-definition plugin="workflow-job@2.28">
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties>
        <hudson.model.ParametersDefinitionProperty>
            <parameterDefinitions>
                <hudson.model.StringParameterDefinition>
                    <name>script_path</name>
                    <description>代码路径</description>
                    <defaultValue>10.167.6.154:jimmyya/</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>tag</name>
                    <description>代码tag</description>
                    <defaultValue>CS_web_v1.5.5_TCE_M_v1.6.0_20190626</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>build_image_name</name>
                    <description>生成镜像名</description>
                    <defaultValue>corepro_web</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>build_image_tag</name>
                    <description>生成镜像tag</description>
                    <defaultValue>V1.6.020190704</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>service</name>
                    <description></description>
                    <defaultValue>FII_T_BEACON_COREPRO_WEB</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>git_credentialsid</name>
                    <description></description>
                    <defaultValue>ffe2e3de-cae2-4064-b5c8-865faf304f59</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>haebor</name>
                    <description></description>
                    <defaultValue>10.134.171.175</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>docker_user</name>
                    <description></description>
                    <defaultValue>sqa</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>docker_password</name>
                    <description></description>
                    <defaultValue>Foxconn168!!</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
                <hudson.model.StringParameterDefinition>
                    <name>docker_project</name>
                    <description></description>
                    <defaultValue>devops</defaultValue>
                    <trim>false</trim>
                </hudson.model.StringParameterDefinition>
            </parameterDefinitions>
        </hudson.model.ParametersDefinitionProperty>
    </properties>
    <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps@2.60">
        <script>pipeline {
            agent {label &apos;master&apos;}
            environment {
            e1 = &apos;10.134.171.175&apos;
            e2 =&apos;sqa&apos;
            }
            stages {
            stage(&apos;Get Code&apos;) {
            steps {
            echo &apos;Checking Out..&apos;
            echo &quot;CC&quot;
            sh &apos;&apos;&apos;
            pwd;
            ls;
            rm -rf *;
            ls;
            ps -ef | grep java;
            ps -ef | grep &quot;${CC}&quot;;
            &apos;&apos;&apos;
            }
            }
            stage(&apos;git&apos;) {
            steps {
            echo &apos;Building..&apos;
            git(
                    branch: &quot;master&quot;,
                    credentialsId: &quot;${git_credentialsid}&quot;,
                    url : &quot;git@${script_path}${service}.git&quot;
                    )
            sh &quot;&quot;&quot;
            pwd;
            ls;
            git tag;
            git checkout ${tag};
            ls;
            &quot;&quot;&quot;
            }
            }
            stage(&apos;docker&apos;) {
            steps {
            sh&quot;&quot;&quot;
            pwd;
            ls;
            docker login -u ${docker_user} -p ${docker_password} ${haebor} ;
            docker build -t ${haebor}/${docker_project}/${build_image_name}:${build_image_tag} .;
            docker images | grep ${build_image_name};
            docker push ${haebor}/${docker_project}/${build_image_name}:${build_image_tag};
            &quot;&quot;&quot;
            }
            }
            stage(&apos;Deploy&apos;) {
            steps {
            echo &apos;Deploying....&apos;
            }
            }
            }
            }
        </script>
        <sandbox>true</sandbox>
    </definition>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <builders/>
    <publishers/>
    <buildWrappers/>
</flow-definition>"""

css_config = [
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_web_v1.5.5_TCE_M_v1.6.0_20190626",
        "build_image_name": "corepro_web",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_WEB",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59",
        "haebor": "10.134.171.175",
        "docker_user": "sqa",
        "docker_password": "Foxconn168!!",
        "docker_project": "devops"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_coreprobossapi_v1.5.4_TCE_M_1.6.0_20190612",
        "build_image_name": "boss_api",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_boss_api",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_systemapi_V1.4.5_TCE_M_1.5.8_20190221",
        "build_image_name": "system_api",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_system_api",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "V1.4.1",
        "build_image_name": "api_cboard",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_Cboard",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_eventsub_V1.5.1_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_event_sub",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_event_sub",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_eventhandler_V1.5.6_TCE_M_1.6.0_20190702",
        "build_image_name": "mqtt_event_handler",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_event_handler",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_servicesub_V1.4.2_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_service_sub",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_service_sub",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_thinghander_V1.4.4_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_thing_handler",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_thing_handler",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_topohandler_V1.4.3_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_topo_handler",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_topo_handler",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_shadowsub_V1.5.0_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_shadow_sub",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_shadow_sub",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_shadowhandler_V1.5.2_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_shadow_handler",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_shadow_handler",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_basevermqtt_V1.5.1_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_dataservice",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQTT_baseversion_dataservice",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_baserabbit_dataservice_V1.5.1_TCE_M_1.5.8_20190221",
        "build_image_name": "rabbit_dataservice",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MQ_rabbit_dataservice",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_midwarekafkaproducer_V1.5.1_TCE_M_1.5.8_20190225",
        "build_image_name": "kafkaproducer",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MIDWARE_Kafkaproducer",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro_release/",
        "tag": "CS_cs_midware_devonline_V1.0.1_TCE_M_1.5.8_20190221",
        "build_image_name": "dev_online",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MIDWARE_dev_online",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro_release/",
        "tag": "CS_cs_midware_msgsize_V1.0.1_TCE_M_1.5.8_20190221",
        "build_image_name": "msg_size",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MIDWARE_msg-size",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_dbdatasave_V1.0.0_TCE_M_1.5.8_20190221",
        "build_image_name": "dbdata_save",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MIDWARE_dbdata_save",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_mqttrecord_V1.0.0_TCE_M_1.5.8_20190221",
        "build_image_name": "mqtt_record",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_MIDWARE_mqttrecord",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_activemqplugin_V1.3.5_TCE_M_1.5.8_20190221",
        "build_image_name": "lib_activemq",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_LIB_ACTIVEMQ",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    }
]

tsf_config = [
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_equipment_V1.6.2_TCE_M_1.6.0_20190626",
        "build_image_name": "equipment_api",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_equipment_api",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_proxyapi_TCE_M_1.5.8_20190221",
        "build_image_name": "proxy_api",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_proxy_api",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
    {
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_treeapi_TCE_M_1.5.8_20190221",
        "build_image_name": "tree_api",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_tree_api",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
{
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_deviceauthapi_V1.4.8_TCE_M_1.6.0_20190612",
        "build_image_name": "device_auth",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_device_auth",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
{
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_datadefine_V1.5.1_TCE_M_1.5.8_20190221",
        "build_image_name": "datadefine",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_datadefine",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
{
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_baseversion_recvdataapi_V1.5.1_TCE_M_1.5.8_20190221",
        "build_image_name": "baseversion_recvdata",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_baseversion_recvdata",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
{
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_firmwareapi_V1.4.8_TCE_M_1.5.8_20190221",
        "build_image_name": "firmware_api",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_firmware_api",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
{
        "script_path": "10.167.6.154:jimmyya/",
        "tag": "CS_cs_kafkaaclapi_V1.5.2_TCE_M_1.5.8_20190221",
        "build_image_name": "kafka_acl",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_kafka_acl",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    },
{
        "script_path": "10.167.6.154:CorePro/",
        "tag": "CS_cs_ruleengine_V0.4.3_TCE_M_1.5.8_20190221",
        "build_image_name": "ruleengine",
        "build_image_tag": "V1.6.020190703",
        "service": "FII_T_BEACON_COREPRO_API_ruleEngine",
        "git_credentialsid": "ffe2e3de-cae2-4064-b5c8-865faf304f59"
    }
]

#公有云
public_cloud=[
{
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
]

joblink = "http://10.129.4.189:8080/user/admin/my-views/view/all/job/devops_ate/job/yangjian/"
username = "admin"
password = "ate123456!"
#git@10.167.6.154:corepro-deploy/corepro_b_fs_shadow_handler.git
#sudo docker login --username=100004603023 ccr.ccs.tencentyun.com