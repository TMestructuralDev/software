def calcular_duracion(hora_salida, hora_llegada, hora_termino, hora_regreso):
    # Aquí calculamos el tiempo entre las horas
    formato = "%H:%M"
    salida = datetime.strptime(hora_salida, formato)
    llegada = datetime.strptime(hora_llegada, formato)
    termino = datetime.strptime(hora_termino, formato)
    regreso = datetime.strptime(hora_regreso, formato)
    
    # Calculamos la duración
    duracion_salida_llegada = llegada - salida
    duracion_termino_regreso = regreso - termino
    
    return duracion_salida_llegada.total_seconds() + duracion_termino_regreso.total_seconds()