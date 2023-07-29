from selenium import webdriver
import chromedriver_autoinstaller

#chrome_driver_path = "C:\Development\chromedriver.exe"
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
assert "Python" in driver.title