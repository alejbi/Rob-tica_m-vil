import WebGUI
import HAL
import Frequency
import math
import numpy as np


def absolute2relative (x_abs, y_abs, robotx, roboty, robott):

    # robotx, roboty are the absolute coordinates of the robot
    # robott is its absolute orientation
    # Convert to relatives
    dx = x_abs - robotx
    dy = y_abs - roboty

    # Rotate with current angle
    x_rel = dx * math.cos (-robott) - dy * math.sin (-robott)
    y_rel = dx * math.sin (-robott) + dy * math.cos (-robott)

    return x_rel, y_rel

def distancia(x_rel, y_rel):
    return math.sqrt(x_rel**2 + y_rel**2)


K_atractivo = 1
K_repulsivo = 1.2

while True:
    Frequency.tick()
    currentTarget = WebGUI.getNextTarget()  # el siguiente waypoint
    
    #Objetivo
    x_abs = currentTarget.getPose().x
    y_abs = currentTarget.getPose().y
    robott = HAL.getPose3d().yaw
    robotx = HAL.getPose3d().x
    roboty = HAL.getPose3d().y
    x_rel, y_rel = absolute2relative(x_abs, y_abs, robotx, roboty, robott)

    dist = distancia(x_rel, y_rel)
    if dist < 1:
        currentTarget.setReached(True)
        continue

    #Atractiva
    # así evitamos que frene al acercarse y una vel. constante
    att_x = x_rel/dist
    att_y = y_rel/dist

    #Repulsiva
    rep_x = 0.0
    rep_y = 0.0

    laser_data = HAL.getLaserData()
    for i, valor in enumerate(laser_data.values):
        if valor <= 0 or valor > 7:
            continue
        angle = math.radians(i - 90) #para que vaya de 0º - 180º a -90º - 90º
        if i < 45 or i > 135:
            peso = 1/valor**2
        else:
            peso = 1/valor
        rep_x -= peso * math.cos(angle) 
        rep_y -= peso * math.sin(angle) # así va acumulando fuerza negativa
                                        # como si fuera x +=1 pero restando

    # Normaliza por el número de lecturas (180)
    numero_rayos = len(laser_data.values)
    rep_x = rep_x/numero_rayos
    rep_y = rep_y/numero_rayos

    # Resultante
    res_x = K_atractivo * att_x + K_repulsivo * rep_x
    res_y = K_atractivo * att_y + K_repulsivo * rep_y
    WebGUI.showForces([att_x, att_y], [rep_x, rep_y], [res_x, res_y])

    #Ángulo salida
    if res_x > 0:
        angulo =  math.atan(res_y / res_x)
    elif res_x < 0:
        if res_y >= 0:
            angulo = math.atan(res_y / res_x) + math.pi
        else:                                   
            angulo = math.atan(res_y / res_x) - math.pi
                                                # el +- math.pi es para 
                                                #llevarlo a alguno de los cuadrantes de 0 a pi
    else:  # res_x == 0, no se puede dividir
        if res_y > 0:
            angulo = math.pi / 2
        elif res_y < 0:
            angulo = -math.pi / 2
        else:
            angulo = 0.0

    #Velocidades
    HAL.setW(2*angulo)
    HAL.setV(max(0.5, 3.5 * (1 - abs(angulo)/math.pi))) #hacerlo  unitario
                                                          # y restarlo a 1
                                                          # 1- invertimos (porque 0 recto y 1 atrás) en funcion de cercania
    
