import random
import time
import urllib.request
from selenium import webdriver
import os
import pydub
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
import speech_recognition as sr
from selenium.webdriver.common.keys import Keys
from urllib3.filepost import choose_boundary


username = "" # your steam username
password = "" #your steam password

def delay():
    time.sleep(random.randint(1,2))
firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument("--window-size=1920,1080")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--proxy-server='direct://'")
firefox_options.add_argument("--proxy-bypass-list=*")
firefox_options.add_argument("--start-maximized")
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--ignore-certificate-errors')
#driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(executable_path="C:/Users/Ufuk_karabag/Desktop/TradingWiev/chromedriver.exe", options=firefox_options)
#driver = webdriver.Firefox(options=firefox_options)
driver.get("https://www.rustreaper.com/login")
def login():
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(Keys.ENTER)

    guardKod = input("Steam Guard : ")

    driver.find_element_by_class_name("twofactorauthcode_entry_input").send_keys(guardKod)
    driver.find_element_by_class_name("twofactorauthcode_entry_input").send_keys(Keys.ENTER)

    time.sleep(10)
    driver.get("https://www.rustreaper.com/")
    time.sleep(5)
"""driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/div").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[1]").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[2]/div[4]").click()
time.sleep(3)"""
def rain():
    coin = driver.find_element_by_xpath("/html/body/div[1]/div/header/nav/div/div[3]/ul[2]/li[4]/a/div/span").get_attribute('innerHTML')
    print("Coins: ", coin)
    

    driver.find_element_by_xpath("/html/body/div[1]/div/footer/div/div[3]/div[1]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[2]/div/input").send_keys("kod")


    """while True:
        try:
            driver.find_element_by_xpath("//a[@class='claimRain']").click()
            break
        except:
            time.sleep(1)

    time.sleep(5)"""
    #!!!!!! RECAPTCHA BYPASS STARTS !!!!!
    frames = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[0])
    delay()

    driver.find_element_by_class_name("recaptcha-checkbox-border").click()
    time.sleep(2)
    # switch to recaptcha audio control frame
    driver.switch_to.default_content()
    frames = driver.find_element_by_xpath("/html/body/div[last()]/div[4]").find_elements_by_tag_name("iframe")
    #frame = driver.find_element_by_xpath("/html/body/div[last()]/div[4]").
    delay()
    driver.switch_to.frame(frames[0])
    delay()

    # click on audio challenge
    driver.find_element_by_id("recaptcha-audio-button").click()

    # switch to recaptcha audio challenge frame
    driver.switch_to.default_content()
    frames = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[-1])
    delay()

    # get the mp3 audio file
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print("[INFO] Audio src: %s" % src)

    # download the mp3 audio file from the source
    print(os.getcwd())
    urllib.request.urlretrieve(src, os.path.normpath(os.getcwd() + "\\sample.mp3"))
    delay()
    text = os.getcwd() + "\sample.mp3"
    print(text)
    try:
        sound = pydub.AudioSegment.from_mp3(os.path.normpath(text))
        sound.export(os.path.normpath(os.getcwd() + "\\sample.wav"), format="wav")
        sample_audio = sr.AudioFile(os.path.normpath(os.getcwd() + "\\sample.wav"))
    except Exception:
        print("[ERR] Please run program as administrator or download ffmpeg manually, "
            "http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/")
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    print("[INFO] Recaptcha Passcode: %s" % key)
    delay()
    # key in results and submit
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    delay()
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    delay()

login()
while True:
    rain()
        
