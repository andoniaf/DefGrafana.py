#!/usr/bin/python3
# -*- coding: utf-8 -*-


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def graf2png(weburl, username, password, timeout, imgname, hwin, wwin):
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
