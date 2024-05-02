from datetime import date
from datetime import datetime

def genFactura(nombre, cantidad, precio, modelo):
    precioConCantidad = precio*cantidad
    try:
        with open("facturas/"+nombre+ ".txt", "a") as fac:
            fac.write(
f"""======================
Empresa: Piesitos
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
            
    except:
        with open("facturas/"+nombre+".txt", "w") as fac:
            fac.write(
f"""======================
Empresa: Piesitos
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