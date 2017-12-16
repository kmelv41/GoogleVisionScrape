from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import bs4 as bs
import urllib, sys
import csv

hdr = {'User-Agent':'Mozilla/5.0'}

# Functions

# Retrieves link to URL
def getURL(url):
    try:
        page = urllib.request.Request(url,headers=hdr)
        source = urllib.request.urlopen(page).read()
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = bs.BeautifulSoup(source,'lxml')
    except AttributeError as e:
        print(e)
        return None
    return soup

def fb_login():
    driver.get('https://www.facebook.com')
    time.sleep(2)
    assert "Facebook" in driver.title
    elem=driver.find_element_by_id('email')
    elem.send_keys('k-melville@hotmail.com')
    time.sleep(1)
    elem=driver.find_element_by_id('pass')
    elem.send_keys('WharF41OuT;')
    time.sleep(1)
    elem.send_keys(Keys.RETURN)

def screenshot_test():
    driver.get('https://www.youtube.com/watch?v=XWzYOpWi65E')
    time.sleep(15)
    for i in range(100):
        driver.save_screenshot(r'C:\Users\KMelville\Desktop\Screenshots\shot'+str(i)+'.png')
        time.sleep(0.1)

    

def play_game():
    # Loads home page for game
    driver.get('https://www.ruffgalaxy.com/')
    # Sleep for a full minute to allow time to login with Facebook
    time.sleep(120)

    # Click on video game to begin playing
    gameElem = driver.find_element_by_xpath("//div[@class='gameContainer']")
    gameElem.click()
    # Let intro video play through
    time.sleep(70)

    # Click to start game
    gameElem.click()
    time.sleep(4)

    # Loop 1000 click and holds
    for _ in range(1000):
        ActionChains(driver).click_and_hold(gameElem).perform()
        time.sleep(0.25)
        ActionChains(driver).release(gameElem).perform()
        time.sleep(0.25)

def collect_photos():
    urls = list()
    driver.get('https://www.facebook.com/mallory.mckewen/photos?lst=513419974%3A523870044%3A1512608723&source_ref=pb_friends_tl')
    time.sleep(2)
    firstPicture = driver.find_element_by_xpath('//*[@id="pic_1403514083098925"]/div/i')
    firstPicture.click()
    time.sleep(5)
    for i in range(1000):
        time.sleep(1)
        if driver.current_url in urls:
            break
        else:
            urls.append(driver.current_url)
            driver.save_screenshot(r'C:\Users\KMelville\Desktop\Screenshots\shot'+str(i)+'.png')
            nextPicture = driver.find_element_by_xpath('//*[@id="facebook"]')
            nextPicture.send_keys(Keys.RIGHT)

    return urls

def search_Springsteen():
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    site = 'https://www.stubhub.com/find/s/?q=springsteen%20on%20broadway'
    req = urllib.request.Request(site, headers=headers)
    html = urllib.request.urlopen(req)
    soup = bs.BeautifulSoup(html)
    prices = soup.find_all("div", class_="price")
    print(prices)

def write_to_csv(urlList):
    with open("urls.csv",'w') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows([urlList])


# Disable pop-up notifications
options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(chrome_options=options)

fb_login()
time.sleep(1)
urlList = collect_photos()
print(urlList)

write_to_csv(urlList)

# Firebase user_id for game: J9lfbLQ8H1MWfmlcUPxVnp1x7Cw2

# Last photo
# https://www.facebook.com/photo.php?fbid=10151173802923184&set=t.523870044&type=3&theater