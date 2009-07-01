# altere estas variaveis para os nomes verdadeiros dos objetos no dominio
moduleName= "JmsModule"
jmsServerName= "JmsServer"
deploymentName="JmsDeployment"
connectionFactoryJndiName = "JmsConnectionFactory"
connectionFactoryId = "JmsConnectionFactory"

def createJmsQueue(jmsResource, queueName):
    print queueName
    queue = jmsResource.createQueue(queueName)
    queue.setJNDIName(queueName)
    queue.setSubDeploymentName(deploymentName)

try:
    connect("weblogic","weblogic","t3://localhost:7001")
    edit()
    startEdit()
        
    adminServer = getMBean("Servers/AdminServer")
    
    jmsServer = create(jmsServerName, "JMSServer")
    jmsServer.addTarget(adminServer)
    
    jmsSystemResource = create(moduleName, "JMSSystemResource")
    jmsSystemResource.addTarget(adminServer)
    
    jmsResource = jmsSystemResource.getJMSResource()
    
    subDeployment = jmsSystemResource.createSubDeployment(deploymentName)
    subDeployment.addTarget(jmsServer)
    
    connectionFactory = jmsResource.createConnectionFactory(connectionFactoryId)
    connectionFactory.setJNDIName(connectionFactoryJndiName)
    connectionFactory.setSubDeploymentName(deploymentName)
    
    # altere aqui, usando createJmsQueue() para criar as filas 
    createJmsQueue(jmsResource, "JmsQueue01")
    createJmsQueue(jmsResource, "JmsQueue02")
    createJmsQueue(jmsResource, "JmsQueue03")
    
    save()
    activate(block = "true")
    print "----------Muito bom! Funcionou! =)"
except:
    print "----------Xiiii, deu erro: =("
    stopEdit()
    dumpStack()

print "----------Desconectando e saindo fora!"
disconnect()    


