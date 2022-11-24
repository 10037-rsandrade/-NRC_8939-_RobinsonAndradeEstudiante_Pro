from collections import namedtuple #libreria para llamar a las colecciones

Beneficiario=namedtuple('Beneficiario',['cedula','nombres','apellidos','DNI','edad','NSS']) #creacion de la entidad beneficiario
Empleado=namedtuple('Empleado',['cedula','nombres','apellidos','DNI','edad','NSS','titulo']) #creacion de la entidad Empleado
Riesgo=namedtuple('Riesgo',['nombre_riesgo','tipo_riesgo']) #creacion de la entidad Riesgo
Agencia=namedtuple('Agencia',['nombre_agencia','direccion','telefono','ciudad']) #creacion de la entidad Agencia
Residencia=namedtuple('Residencia',['nombre_residencia','direccion','sector']) #creacion de la entidad Residencia
Categoria=namedtuple('Categoria',['nombre_categoria','tipo_sueldo','sueldo_hora']) #creacion de la entidad Categoria
Prestamo=namedtuple('Prestamo',['codigo','tipo_interes','periodo','vigencia']) #creacion de la entidad Prestamo
Fecha=namedtuple('Fecha',['fecha_inicio','fecha_final']) #creacion de la entidad Fecha
