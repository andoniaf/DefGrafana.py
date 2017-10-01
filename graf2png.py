#!/usr/bin/python3
# -*- coding: utf-8 -*-


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image


def graf2png(weburl, username, password, timeout, imgname, hwin, wwin, onlypanel):
    driver = webdriver.PhantomJS()
    driver.set_window_size(hwin, wwin)
    driver.get(weburl)

    # Introducimos username
    in_user = driver.find_element_by_name('username')
    in_user.clear()
    in_user.send_keys(username)

    # Introducimos password
    in_pass = driver.find_element_by_id('inputPassword')
    in_pass.clear()
    in_pass.send_keys(password)
    in_pass.send_keys(Keys.ENTER)

    # Espera a que cargue la consulta
    time.sleep(timeout)

    # Timestamp para evitar sobreescribir capturas
    currtime = time.strftime("%y%m%d%H%M%S", time.localtime())
    imgname = imgname + currtime + '.png'
    # Realizar screenshot
    driver.save_screenshot(imgname)
    print("Screen guardada como: " + imgname)
    # Recortar panel(?)
    #   Solo funciona con los paneles cuya clase sea 'panel-fullscreen',
    #     esta es la clase que tiene por defecto los paneles cuando
    #     generas un enlace para compartir. (Share Panel > Link > Copy)
    if (onlypanel):
        panel = driver.find_element_by_class_name('panel-fullscreen')
        plocation = panel.location
        psize = panel.size

        left = plocation['x']
        top = plocation['y']
        right = plocation['x'] + psize['width']
        bottom = plocation['y'] + psize['height']

        pimg = Image.open(imgname)
        pimg = pimg.crop((left, top, right, bottom))
        pimgname = 'panel_' + imgname
        pimg.save(pimgname)
        print("Panel recortado guardado como: " + pimgname)
