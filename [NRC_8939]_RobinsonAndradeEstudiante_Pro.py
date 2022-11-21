from collections import namedtuple

Beneficiario=namedtuple('Beneficiario',['cedula','nombres','apellidos','DNI','edad','NSS'])
Empleado=namedtuple('Empleado',['cedula','nombres','apellidos','DNI','edad','NSS','titulo'])
Riesgo=namedtuple('Riesgo',['nombre_riesgo','tipo_riesgo'])
Agencia=namedtuple('Agencia',['nombre_agencia','direccion','telefono','ciudad'])
Residencia=namedtuple('Residencia',['nombre_residencia','direccion','sector'])
Categoria=namedtuple('Categoria',['nombre_categoria','tipo_sueldo','sueldo_hora'])
Prestamo=namedtuple('Prestamo',['codigo','tipo_interes','periodo','vigencia'])
Fecha=namedtuple('Fecha',['fecha_inicio','fecha_final'])