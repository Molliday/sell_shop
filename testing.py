from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

link_produk=None

def SetupSelenium():
    ### Inisialisasi Awal
    binary=FirefoxBinary('system/firefox/firefox.exe')
    selenium=r'system/firefox/geckodriver.exe'
    ### Setup Profile
    firefox_profile = webdriver.FirefoxProfile('system/profile')
    ### Buka Browser
    browser = webdriver.Firefox(executable_path=selenium,firefox_binary=binary,firefox_profile=firefox_profile)
    ### Clear Cache & Cookie
    browser.delete_all_cookies()
    return browser

def InputData():
    global link_produk
    link_produk=input('(#) Link Produk Shopee : ')

InputData()
browser=SetupSelenium()
wait = WebDriverWait(browser, 60)
# cek login
browser.get("https://shopee.co.id/buyer/login")