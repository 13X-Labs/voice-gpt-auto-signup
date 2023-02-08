#  import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time

def autoVoiceGPT():
	fake = Faker(locale='vi_VN')
	ref_codeText = 'iGLyH4f'
	passwordText = 'autoPassword@2023'
	fullnameText = fake.name()
	emailText = fake.ascii_free_email()
	phoneText = "+849" + str(random.randint(10000000, 99999999))

	with open("registration_info.txt", "a") as file: file.write("\n" + emailText + "|" + passwordText + "|" + phoneText)

	# create a new Chrome session
	driver = webdriver.Chrome()

	# open the website
	driver.get("https://voicegpt.us/auth/signup")

	# get element by id
	fullname = driver.find_element(By.ID, "fullName")
	email = driver.find_element(By.ID, "email")
	phone = driver.find_element(By.ID, "phone")
	password = driver.find_element(By.ID, "password")
	repassword = driver.find_element(By.ID, "re-password")
	referral = driver.find_element(By.ID, "referral")
	submit = driver.find_element(By.XPATH, "//button[@type='submit']")

	# send keys
	fullname.send_keys(fullnameText)
	email.send_keys(emailText)
	phone.send_keys(phoneText)
	password.send_keys(passwordText)
	repassword.send_keys(passwordText)
	referral.send_keys(ref_codeText)
	time.sleep(2)
	submit.click()
	time.sleep(2)

for i in range(1, 100):
	autoVoiceGPT()