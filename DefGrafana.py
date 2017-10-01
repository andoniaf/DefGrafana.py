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
passGraf = 'secret'
# Necesario sobretodo en consultas pesadas
timeout = 10
imgName = 'webScreen_'
#Resolucion de la "ventana"
hWin = 1200
wWin = 800
##############
import sys
import time
from selenium import webdriver   
from selenium.webdriver.common.keys import Keys

if len(sys.argv) == 1:
  mensaje = "Uso:\n - Modificar seccion \"VARS\"\n"
  mensaje += " - Ejecutar: python3 DefGrafana.py '<URL Dashboard>'"
  print(mensaje)

else:
  webUrl = sys.argv[1] 
  print("URL a capturar: " + webUrl)

  driver = webdriver.PhantomJS()
  driver.set_window_size(hWin, wWin)
  driver.get(webUrl)
  
  ## Introducimos username
  user_name=driver.find_element_by_name('username')
  user_name_text = user_name.text
  user_name.clear()
  user_name.send_keys(username)
  
  ## Introducimos password
  password=driver.find_element_by_id('inputPassword')
  password.clear()
  password.send_keys(passGraf)
  password.send_keys(Keys.ENTER)
  
  ## Espera a que cargue la consulta
  time.sleep(timeout)
  
  ## Screenshot
  # Timestamp para evitar sobreescribir capturas
  currTime = time.strftime("%y%m%d%H%M%S", time.localtime())
  imgName = imgName + currTime + '.png'
  driver.set_window_size(600, 600)
  driver.save_screenshot(imgName)
  print("Screen guardada como: " + imgName)

