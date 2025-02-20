"""
ISR
"""

# Entradas
sueldo = float(input("Sueldo:"))

# Proceso
if sueldo >= 0.01 and sueldo <= 3644.94 : 
    excedente = sueldo - 0.01  
    impuestoM = excedente * 0.10
    ISR = impuestoM + 12.88
if sueldo >= 3644.95 and sueldo <= 7446.19 : 
    excedente = sueldo - 3644.95
    impuestoM = excedente * 0.20
    ISR = impuestoM + 303.76
if sueldo >= 7466.20 and sueldo <= 10298.35:
    excedente = sueldo - 7466.20 
    impuestoM = excedente * 0.30
    ISR = impuestoM + 1063.92
if sueldo >= 10298.36:
    excedente = sueldo - 10298.36
    impuestoM = excedente * 0.35
    ISR = impuestoM + 3327.42
# Salidas
print(ISR)
