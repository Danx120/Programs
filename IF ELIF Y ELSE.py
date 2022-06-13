
acl=int(input('Ingrese el # de ACL: '))
if acl >=1 and acl <=199:
    print('ACL es estandar')
elif acl>=100 and acl <=199:
    print('ACL es extendido')
else:
    print('El dato ingresado no es un ACL')