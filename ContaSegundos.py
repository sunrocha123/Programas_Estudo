segundos = input('Por gentileza, entre com o número de segundos que deseja converter: ')
segundos_dia = int(segundos) // 86400
segundos_horas = (int(segundos) % 86400) // 3600
segundos_minutos = ((int(segundos) % 86400) % 3600) // 60
resto_segundo = ((int(segundos) % 86400) % 3600) % 60
print(segundos_dia,'dias,',segundos_horas,'horas,',segundos_minutos,'minutos e',resto_segundo,'segundos.')