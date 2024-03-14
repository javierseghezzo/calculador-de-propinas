monto_total = float(input("Ingrese el total de la factura: "))
porc_a_dejar = float(input("¿Cual es el porcentaje a otorgar de propinas?: "))
propina = monto_total * porc_a_dejar/100
print(f"El monto total a dejar incluida la propina es de {round(propina)+monto_total} pesos")
