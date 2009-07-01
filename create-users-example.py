try:
    connect("weblogic","weblogic","t3://localhost:7001")
    
    print "----------Criando usuarios"
    cd("SecurityConfiguration/domain/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator") 
    cmo.createUser("almighty-boss", "12341234", "O todo poderoso chefão absoluto")
    cmo.createUser("peao", "01010101", "Peão. Rala muito e ganha pouco")
    cmo.createUser("estagiario", "blablabla", "Estagiário. Paga contas, tira xerox, faz café")
    
    print "----------Criando as roles e associando-as aos usuarios"
    cd("../../RoleMappers/XACMLRoleMapper")
    cmo.createRole(None, "Administrador", "{Usr(almighty-boss)}")
    cmo.createRole(None, "Peao", "{Usr(peao)}")
    cmo.createRole(None, "Estagiario", "{Usr(estagiario)}")
    
    print "----------Muito bom! Funcionou! =)"
except:
    print "----------Xiiii, deu erro: =("
    dumpStack()

print "----------Desconectando e saindo fora!"
disconnect()
