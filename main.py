from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

url = 'https://login.microsoftonline.com/common/oauth2/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&resource=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DeyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBWVpmbnJHS2g5ZVZBcW0wSm5OZDNUN1lYaE5oQzk1eWpPc25pVDd4MmRsNHFJMTl5ZzhpV0s0S0dHUGRrbDBuemJBREppOGhGN0w5bzd2bzJVbUNGd3ciLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vUGFnZXMvUmVzcG9uc2VQYWdlLmFzcHg_aWQ9dG0zbVdCc2hOMHEzNkE3MmxuUWd3WnI1M1c0WXE0aENpNFVjWDA0YTh1TlVSRXRXTlRGRVZrVkRVa0kyUkZsRFZ6VldVRGhFTWtzMVNDNHUmc2lkPTJhZDlmYjUyLTdmYTUtNDgzMC1iMzY3LTM3NDFmYmNmNzNlNyJ9fQ&response_mode=form_post&nonce=637777121623264482.ZTM5ZGY5YmMtN2MyYS00MDU5LTg1YTAtZTc4OTViN2QwNjczMjY5OTNiODktNGQ3OS00NjI4LWJiY2MtN2M2NjY2N2IwNWY1&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&msafed=0&x-client-SKU=ID_NET472&x-client-ver=6.14.1.0'
email = 'sreissc241@ops.org'
password = '505241'

driver.get(url)

def sign_in():
    driver.find_element_by_xpath('//*[@id="i0116"]').send_keys(email) # sends user email to email input
    sleep(2) # gives time for page to load
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click() # clicks on the next button
    sleep(5) # gives time for page to load
    driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(password) # types in the password
    sleep(2) # gives time for page to load
    driver.find_element_by_xpath('//*[@id="submitButton"]').click() # clicks sign in
    sleep(2) # gives time for page to load
    driver.find_element_by_xpath('//*[@id="idBtn_Back"]').click() # clicks no for (reduce number of times signing in)

def fill_in_form():
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input').send_keys(password) # types in the password
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div/label/input').click() # clicks "lunch"
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/label/input').click() # clicks "yes"
    driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[4]/div[1]/button/div').click() # clicks "submit"

sign_in()
sleep(5)
fill_in_form()
sleep(2)
driver.close()
