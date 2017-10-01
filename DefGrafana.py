#!/usr/bin/python3
# -*- coding: utf-8 -*-

# [ES] DefGrafana.py - Script para capturar imagenes dentro de Grafana.
#
# Modo de uso: - Modificar seccion "VARS"
#              - Ejecutar: python3 DefGrafana.py '<URL Dashboard>'
#
# https://github.com/andoniaf

#### VARS ####
username = 'admin'
password = 'secret'
# Necesario sobretodo en consultas pesadas
timeout = 5
imgName = 'grafImg_'
# Resolucion de la "ventana"
hWin = 1200
wWin = 800
##############
import sys
from graf2png import graf2png


if len(sys.argv) == 1:
    mensaje = "Uso:\n - Modificar seccion \"VARS\"\n"
    mensaje += " - Ejecutar: python3 DefGrafana.py '<URL Dashboard>'"
    print(mensaje)

else:
    if (sys.argv[1] == '--cut-panel'):
        onlyPanel = True
        webUrl = sys.argv[2]
    else:
        onlyPanel = False
        webUrl = sys.argv[1]

    print("URL a capturar: " + webUrl)

    graf2png(webUrl, username, password, timeout, imgName, hWin, wWin, onlyPanel)
