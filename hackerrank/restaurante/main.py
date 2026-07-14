# 1. Menú del restaurante
menu = {
    "1. Hamburguesa con queso": 250.00,
    "2. Papas fritas": 120.00,
    "3. Pizza personal": 350.00,
    "4. Refresco": 75.00,
    "5. Helado de vainilla": 90.00
}

# Tasas de impuestos y propina
TASA_IMPUESTO = 0.18  # 18%
PROPINA_SUGERIDA = 0.10  # 10%

print("--- ¡BIENVENIDO AL RESTAURANTE! ---")
print("Este es nuestro menú de hoy:")
for producto, precio in menu.items():
    print(f"{producto} - ${precio:.2f}")
print("-----------------------------------")

subtotal = 0.0
productos_elegidos = []

# --- PASO 1: AGREGAR AL CARRITO (BOLSA) ---
while True:
    seleccion = input("\nIngresa el número del producto (o escribe 'pagar' para ir a la caja): ").strip().lower()
    
    if seleccion == 'pagar':
        break
        
    encontrado = False
    for producto, precio in menu.items():
        if producto.startswith(seleccion):
            subtotal += precio
            # Guardamos el nombre limpio del producto en la bolsa
            nombre_limpio = producto.split(". ")[1]
            productos_elegidos.append(f"{nombre_limpio} (${precio:.2f})")
            print(f"-> ¡Agregado a la bolsa! Total acumulado: ${subtotal:.2f}")
            encontrado = True
            break
            
    if not encontrado:
        print("Opción no válida. Digita un número del 1 al 5, o escribe 'pagar'.")

# --- PASO 2: MOSTRAR LA BOLSA Y CALCULAR TOTALES ---
if subtotal > 0:
    impuesto_total = subtotal * TASA_IMPUESTO
    propina_total = subtotal * PROPINA_SUGERIDA
    gran_total = subtotal + impuesto_total + propina_total

    print("\n===================================")
    print("         DETALLE DE TU BOLSA       ")
    print("===================================")
    for prod in productos_elegidos:
        print(f" * {prod}")
    print("-----------------------------------")
    print(f"Subtotal:            ${subtotal:.2f}")
    print(f"Impuestos (18%):     ${impuesto_total:.2f}")
    print(f"Propina (10%):       ${propina_total:.2f}")
    print("-----------------------------------")
    print(f"TOTAL NETO A PAGAR:  ${gran_total:.2f}")
    print("===================================")

    # --- PASO 3: PROCESO DE PAGO Y DEVOLUCIÓN ---
    print("\n--- PROCESO DE COBRO ---")
    while True:
        try:
            pago_cliente = float(input(f"¿Con cuánto dinero va a pagar? (Total: ${gran_total:.2f}): $"))
            
            if pago_cliente >= gran_total:
                cambio = pago_cliente - gran_total
                print("\n===================================")
                print("         PAGO PROCESADO             ")
                print("===================================")
                print(f"Recibido:            ${pago_cliente:.2f}")
                print(f"Total de la cuenta:  ${gran_total:.2f}")
                print(f"Su cambio/devuelta:  ${cambio:.2f}")
                print("===================================")
                print("¡Pago exitoso! Gracias por su compra.")
                break
            else:
                faltante = gran_total - pago_cliente
                print(f"Dinero insuficiente. Le faltan ${faltante:.2f}. Intente de nuevo.")
        except ValueError:
            print("Por favor, introduce una cantidad de dinero válida (solo números).")

else:
    print("\nNo agregaste nada a la bolsa. ¡Vuelve pronto!")