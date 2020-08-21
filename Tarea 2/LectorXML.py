from xml.dom import minidom
doc = minidom.parse("archivoxml.xml")
empleados = doc.getElementsByTagName("empleado")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    nombre = empleado.getElementsByTagName("nombre")[0]
    apellido = empleado.getElementsByTagName("apellido")[0]
    telefono = empleado.getElementsByTagName("telefono")[0]
    email = empleado.getElementsByTagName("email")[0]
    print("id:%s " % sid)
    print("nombre:%s" % nombre.firstChild.data)
    print("apellido:%s" % apellido.firstChild.data)
    print("telefono:%s" % telefono.firstChild.data)
    print("email:%s" % email.firstChild.data)
    print(type(empleado))
    print("")