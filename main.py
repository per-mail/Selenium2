'''
from selenium import webdriver
import time

url = "https://www.instagram.com/"
driver = webdriver.Chrome("C:\\Users\\dfg\\Desktop\\Selenium\\chromedriver\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

url = "https://www.instagram.com/"




'''
try:
    user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]
'''
# options
options = webdriver.ChromeOptions()

# change useragent
#useragent = UserAgent()

options.add_argument("Explanation=HelloWorld:)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
#options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")

#proxy_options = {
#    "proxy": {
#        "https": f"http://{login}:{password}@138.128.91.65:8000"
#    }
#}

# устаревший метод запуска webdriver
# driver = webdriver.Chrome(
#     executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
#     options=options
# )

# новый метод запуска webdriver нужно ипортировать библиотеку from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\dfg\\Desktop\\Selenium\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(
    service=s,
    options=options
#    seleniumwire_options=proxy_options
)
# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    #driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    driver.get(url="https://peter.sh/experiments/chromium-command-line-switches/")
    time.sleep(10)
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

    #driver.get("https://2ip.ru")
    #time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


