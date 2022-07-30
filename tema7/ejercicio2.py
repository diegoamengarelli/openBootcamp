import time

hora = time.strftime('%H')
minutos = time.strftime('%M')


if int(hora) >= 19:
    print("es la hora de ir a casa")
else:
    h_resta = 18-int(hora)
    m_resta = 59-int(minutos)
    print("Quedan {} horas y {} minutos para irse".format(h_resta, m_resta))