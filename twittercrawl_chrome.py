from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from random import randint

import sys,os

import unittest, time, re

class Sel(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()


        chromeOptions = webdriver.ChromeOptions()
        #optionsOptions.setBinary("/path/to/other/chrome/binary");
        #chromeOptions.binary_location = "/Users/BullzEye/Development/crawl"
        prefs = {"profile.managed_default_content_settings.images":2}
        chromeOptions.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)

        url = self.driver.command_executor._url       #"http://127.0.0.1:60622/hub"
        session_id = self.driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
        print(url)
        print(session_id)

        file_ = open('/Volumes/GAIKAI/sessionconn', 'w')
        file_.write(url)
        file_.write("\n")
        file_.write(session_id)
        file_.close()

        self.driver.implicitly_wait(30)
        self.base_url = "https://twitter.com"

        self.verificationErrors = []
        self.accept_next_alert = True




    def test_sel(self):
        driver = self.driver
        delay = 3
        #Search query
        driver.get(self.base_url + "/search?f=tweets&vertical=default&q=%23ttip since%3A2016-04-27 until%3A2016-05-05&src=typd")
        #driver.find_element_by_link_text("All").click()


        while 1:
          #Versuche fehlermeldung zu umegehen
          #try:
          #  print("Before Timeline-tryAgainMessage"+"\n")
          #  while driver.find_element_by_class_name('Timeline-tryAgainMessage').is_displayed():
          #    print("In Timeline-tryAgainMessage"+"\n")
          #    driver.findElement(By.xpath("//button[contains(.,'Erneut versuchen')]")).click()
          #    time.sleep(randint(6,15))
#
          #except Exception, e:
#
          #Versuche andere fehlermeldung zu umegehen
          #  try:


          lag=0
          presize=0

              #Solange nicht 5 nicht neues geladen wurde
          while lag<2:

            print("In scrape modus")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #print(str(i)+"\n")
            time.sleep(randint(3,6))

            actsize=sys.getsizeof(driver.page_source)

            print(" presize: "+str(presize)+" actsize: "+str(actsize))
            if (presize+500 < actsize):

              presize=actsize

            else:

              lag=lag+1
              print(str(lag)+ " Lag")

              print("Lag! Checke reload funktionen ")

          #write data
          html_source = driver.page_source
          data = html_source.encode('utf-8')
          file_ = open('/Volumes/GAIKAI/twitter2016.2.html', 'w')
          file_.write(data)
          file_.close()




          print("Before stream-end-inner")
          try:
            while driver.find_element_by_class_name('stream-fail-container').is_displayed():
              print("In stream-end-inner"+"\n")
              driver.find_element_by_link_text("Try again").click()
              time.sleep(randint(3,6))
          except Exception, f:
            print("Link: -Probiere es erneut- nicht gefunden!")
           # except Exception, f:
              #for i in range(1,100):
              #Beide Twitter fehlermeldungen nicht gefunden -> seite richtig geladen





if __name__ == "__main__":
    unittest.main()
