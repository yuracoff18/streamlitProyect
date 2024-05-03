from datetime import date
from datetime import datetime

def genFactura(nombre, cantidad, precio, modelo):
    precioConCantidad = precio*cantidad
    try:
        with open("facturas/"+nombre+ ".txt", "a") as fac:
            fac.write(
f"""======================
Empresa: Piecitos
Fecha: {date.today()}
Hora: {datetime.now().hour}:{datetime.now().minute}
                    
Nombre: {nombre}
Cantidad: {cantidad}
                    
Modelo: {modelo}
Valor unitario: {precio}
                    
Valor sin IVA: {precioConCantidad}
Valor total: {precioConCantidad + (precioConCantidad* 0.19)}
======================
""")
            fac.close()
            
    except:
        with open("facturas/"+nombre+".txt", "w") as fac:
            fac.write(
f"""======================
Empresa: Piecitos
Fecha: {date.today()}
Hora: {datetime.now().hour}:{datetime.now().minute}
                    
Nombre: {nombre}
Cantidad: {cantidad}
                    
Modelo: {modelo}
Valor unitario: {precio}
                    
Valor sin IVA: {precioConCantidad}
Valor total: {precioConCantidad + (precioConCantidad* 0.19)}
======================
    """)
            fac.close()

def genInfo(nombre, cantidad, precio, modelo):
    with open("actual_info/info.txt", "w") as arch:
        arch.write(f"{nombre},{cantidad},{precio},{modelo}")
        arch.close()
        