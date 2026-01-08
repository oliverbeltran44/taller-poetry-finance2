def convertir_usd_a_cop(lista_precios_usd, tasa_cambio=4100):
    """
    Convierte una lista de precios de dólares a pesos colombianos.
    
    Args:
        lista_precios_usd (list): Lista de precios en USD.
        tasa_cambio (float): Tasa de cambio fija (default 4100).
        
    Returns:
        list: Lista de precios convertidos a COP.
    """
    precios_cop = []
    for precio in lista_precios_usd:
        # Lógica simple de conversión
        nuevo_precio = precio * tasa_cambio
        precios_cop.append(nuevo_precio)
    
    return precios_cop