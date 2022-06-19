import time
import platform
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

userSystem = platform.system()

def testCaseStatus(num, numOf):
    if num == 1:
        print("-------------------")
        print("Test Case {}: PASSED".format(numOf))
        print("-------------------")
    elif num == 0:
        print("-------------------")
        print("Test Case {}: Failed".format(numOf))
        print("-------------------")
    elif num == 2:
        print("-----------------------------")
        print("Additional Test Case {}: PASSED".format(numOf))
        print("-----------------------------")

if userSystem == 'Linux':
    profile_path = r'/home/kali/.mozilla/firefox/06au6nqy.default'
    options=Options()

url = "https://nbl.one"
print("URL for quest search: {}".format(url))
r = requests.get(url)
if r.status_code < 400:
    try:
        if userSystem == 'Linux':
            options.set_preference('profile', profile_path)
            service = Service(r'./geckodriver')
            driver = Firefox(service=service, options=options)
        else:
            driver = Firefox()
        driver.get(url)
        print("Python Waiting for web page to finish loading...")
        print("Wait for 5 seconds...")
        time.sleep(5)
        print()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        ids = driver.find_elements(By.TAG_NAME,'section')
        count = 0
        for id in ids:
            if 'quest' in id.get_attribute('id'):
                count+=1
        if count > 0:
            print("{} quests available.".format(count))
        else:
            print("No quest available.")
        testCaseStatus(1,1)
        
    except Exception as e:
        testCaseStatus(0,1)


    try:
        print()
        print("URL for social link search: {}".format(url))
        driver.execute_script("window.scrollTo(0, 0);")
        print()
        driver.find_element(By.XPATH,'//a[text()="Communities"]').click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        socialLinks = driver.find_elements(By.TAG_NAME,'a')
        for social in socialLinks:
            if "linkedin" in social.get_attribute("href"):
                print("Connect with us on LinkedIn   : {}".format(social.get_attribute("href").ljust(17)))
            elif "instagram" in social.get_attribute("href"):
                print("Follow us on Instagram        : {}".format(social.get_attribute("href")))
            elif "twitter" in social.get_attribute("href"):
                print("Connect with us on Twitter    : {}".format(social.get_attribute("href")))
            elif "facebook" in social.get_attribute("href"):
                print("Follow us on Facebook         : {}".format(social.get_attribute("href")))
            elif "youtube" in social.get_attribute("href"):
                print("Subscribe our youtube channel : {}".format(social.get_attribute("href")))
        print()
        testCaseStatus(2,1)
        driver.quit()

    except Exception as e:
        driver.quit()

url = "https://nbl.one/listings"
print("URL for course search: {}".format(url))
r = requests.get(url)
if r.status_code >= 400:
    exit(r.reason)
else:
    try:
        if userSystem == 'Linux':
            options.set_preference('profile', profile_path)
            service = Service(r'./geckodriver')
            driver = Firefox(service=service, options=options)
        else:
            driver = Firefox()
        driver.get(url)
        print("Python Waiting for web page to finish loading...")
        print("Wait for 5 seconds...")
        time.sleep(5)
        print()
        count = 0
        classes = driver.find_elements(By.CLASS_NAME,'gig_cards')
        for i in classes:
            if i.text != '':
                count+=1
        for i in range(count):
            print("Course number : {}".format(i+1))
            classes = driver.find_elements(By.CLASS_NAME,'gig_cards')
            count2 = 0
            for c in classes:
                if c.text != '':
                    if count2 == i:
                        temp = c.text.split('\n')
                        print("Course Name : {}".format(temp[0]))
                        for i in temp:
                            if 'Starts' in i:
                                i = i.split()
                                i = i[len(i)-1].split('$')
                                print("Course Price : Starts at ${}".format(i[len(i)-1]))
                        c.click()
                        time.sleep(2)
                        print("Course URL : {}".format(driver.current_url))
                        driver.execute_script("window.history.go(-1)")
                        print ('--------------------------------------------------')
                        time.sleep(2)
                        break
                    count2+=1
        testCaseStatus(1,2)
        driver.quit()
    except Exception as e:
        driver.quit()
        testCaseStatus(0,2)

url = "https://nby.la/rdJuXp"
print("URL for course booking: {}".format(url))
print()
print("Enter email ID: ", end='')
emailId = input()
print("Enter password: ",end='')
passwd = input()
try:
    if userSystem == 'Linux':
        options.set_preference('profile', profile_path)
        service = Service(r'./geckodriver')
        driver = Firefox(service=service, options=options)
    else:
        driver = Firefox()
    driver.get("https://nby.la/rdJuXp")
    time.sleep(5)
    while (len(driver.find_elements(By.XPATH, '//*[@id="skylift-book-seat"]')) == 0):
        driver.refresh()
        time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="skylift-book-seat"]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR,'''.nsm7Bb-HzV7m-LgbsSe-BPrWId''').click()
    driver.implicitly_wait(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.find_element(By.TAG_NAME,'input').send_keys(emailId)
    driver.find_element(By.XPATH,'//span[text()="Next"]').click()
    time.sleep(8)
    driver.find_element(By.XPATH,'//input[@type="password"]').send_keys(passwd)
    driver.find_element(By.XPATH,'//span[text()="Next"]').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    if len(driver.find_elements(By.XPATH,'//span[text()="Join Conversation with Careers@Nbyula"]')) == 0:
        driver.find_element(By.XPATH,'//span[text()="Proceed"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//p[text()="Choose Billing Country"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//input[@placeholder="Search Billing Country"]').send_keys('India')
        time.sleep(2)
        driver.find_element(By.XPATH,'//button[text()="India"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//p[text()="Choose Billing State"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//input[@placeholder="Search Billing State"]').send_keys('Bihar')
        time.sleep(2)
        driver.find_element(By.XPATH,'//button[text()="Bihar"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//span[text()="Confirm FREE Booking"]').click()
        time.sleep(8)
    else:
        driver.find_element(By.XPATH,'//span[text()="Join Conversation with Careers@Nbyula"]').click()
        time.sleep(4)
    testCaseStatus(1,3)

except Exception as e:
    testCaseStatus(0,3)

try:
    driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys('Preet')
    driver.find_element(By.XPATH,'//input[@placeholder="Search"]').send_keys(Keys.ENTER)
    driver.implicitly_wait(4)
    user = driver.find_elements(By.XPATH,'//p[text()="Preet"]')
    if len(user) > 0:
        user[0].click()
        driver.implicitly_wait(4)
        time.sleep(2)
        driver.find_element(By.XPATH,'//span[text()="Follow"]').click()
        driver.implicitly_wait(4)
        time.sleep(2)
        driver.find_element(By.XPATH,'//span[text()="Following"]').click()
        time.sleep(2)
        testCaseStatus(2,2)
    driver.refresh()
    driver.find_element(By.ID, 'navbar-profile-dropdown').click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, '//span[text()="Log Out"]').click()
    driver.implicitly_wait(5)

except Exception as e:
    driver.quit()

url="https://nbl.one/register?"
try:
    driver.get(url)
    driver.find_element(By.XPATH,"""//input[@placeholder="First name"]""").send_keys('namecheck')
    driver.find_element(By.XPATH,"""//input[@placeholder="Last name"]""").send_keys('lastnamecheck')
    driver.find_element(By.XPATH,"""//input[@type="email"]""").send_keys('bicobib546@mahazai.com')
    driver.find_element(By.XPATH,"""//input[@type="password"]""").send_keys('namecheck')
    driver.find_element(By.CSS_SELECTOR,"button.w-full").click()
    otp=int(input("Please enter the otp : "))
    driver.find_element(By.XPATH,"""//input[@placeholder="Enter OTP..."]""").send_keys(otp)
    driver.find_element(By.XPATH,"""//button[@id="verification-confirm-otp"]""").click()
    testCaseStatus(2,3)
    driver.quit()

except Exception as e:
    driver.quit()