# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome()


def login(driver):
    driver.get('https://passport.jd.com/uc/login')
    driver.find_elements_by_link_text("账户登录")[0].click()
    return driver


def buy_mi8():
    driver.get('https://item.jd.com/7437788.html')
    driver.find_element_by_link_text("加入购物车").click()
