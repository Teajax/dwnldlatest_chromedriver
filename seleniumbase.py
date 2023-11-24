from seleniumbase import Driver
import time

driver = Driver(uc=True)
driver.get("https://www.amazon.in/")
time.sleep(6)
driver.quit()