# pipeline.py -- Nuestro pipeline de datos básico

def extraer_datos():
    """Simula extraer datos de una fuente."""
    datos = [
        {"producto": "Laptop", "precio": 999, "cantidad": 5},
        {"producto": "Mouse", "precio": 29, "cantidad": 50},
        {"producto": "Teclado", "precio": 79, "cantidad": 30},
    ]
    return datos

def calcular_iva(precio, tasa=0.21):
    """Calcula el IVA de un precio."""
    return precio * tasa

def calcular_ipsi(precio, tasa=0.11):
    """Calcula el IVA de un precio."""
    return precio * tasa

def aplicar_descuento(precio, descuento=0.10):
    """Calcular el descuento para los mayoristas."""
    return precio * descuento

def calcular_total(datos):
    """Calcula el total de ventas."""
    total = sum(item["precio"] * item["cantidad"] for item in datos)
    return total

if __name__ == "__main__":
    datos = extraer_datos()
    total = calcular_total(datos)
    iva = calcular_iva(total)
    ipsi = calcular_ipsi(total)
    descuento = aplicar_descuento(total)
    print(f"Total de ventas: {total:,.2f} €")
    print(f"Total de IVA: {iva:,.2f} €")
    print(f"Total de IPSI: {ipsi:,.2f} €")
    print(f"Descuento mayorista: {descuento:,.2f} €")