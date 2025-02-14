from datetime import datetime

class Calculos():

    def calcular_total_horas(hora_salida, hora_regreso):
        """Calcula la diferencia en horas decimales entre la hora de salida y regreso."""
        try:
            formato = "%H:%M"
            salida = datetime.strptime(hora_salida, formato)
            regreso = datetime.strptime(hora_regreso, formato)
            diferencia = regreso - salida
            total_horas = diferencia.total_seconds() / 3600  # Convertir a horas decimales
            return round(total_horas, 2)  # Redondear a 2 decimales
        except ValueError:
            return None  # Retorna None si el formato de hora es incorrecto

    def calcular_total_sin_iva(total_horas, costo_hora):
        """Calcula el total sin IVA multiplicando el total de horas por el costo por hora."""
        try:
            return round(total_horas * float(costo_hora), 2)
        except ValueError:
            return None  # Retorna None si el costo_hora no es un número válido

    def calcular_total_con_iva(total_sin_iva):
        """Calcula el total con IVA (16%)."""
        return round(total_sin_iva * 1.16, 2)