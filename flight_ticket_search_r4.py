#import libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open Latam website
chrome = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
chrome.get('https://www.latam.com/pt_br/voos-destinos/')
chrome.maximize_window()
chrome.execute_script("window.scrollTo(0, 400)")
sleep(20)

#select origin city
origin_city = 'Sao Paulo'
origin_city_field = chrome.find_element_by_xpath('//*[@id="compra-select-origin"]')
origin_city_field.send_keys(origin_city)
sleep(1)
origin_city_confirmation = chrome.find_element_by_link_text('São Paulo (SAO), Guarulhos Intl. (GRU), Brasil')
origin_city_confirmation.click()
sleep(1)

#select destination city
destiny_city = 'Salvador'
destiny_city_field = chrome.find_element_by_xpath('//*[@id="compra-select-destination"]')
destiny_city_field.send_keys(destiny_city)
sleep(1)
destiny_city_confirmation = chrome.find_element_by_link_text('Salvador da Bahia (SSA), Deputado L E Magalhães (SSA), Brasil')
destiny_city_confirmation.click()
sleep(1)

#select departure date
departure_date_field = chrome.find_element_by_xpath('/html/body/main/section/section/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/form/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/input')
departure_date_field.click()
sleep(1)
input_day_departure_date = '29'
selected_day_departure_date = "//table/tbody/tr/td/a[text()='{}']".format(input_day_departure_date)
departure_date_confirmation = chrome.find_element_by_xpath(selected_day_departure_date)
departure_date_confirmation.click()
sleep(1)
print(selected_day_departure_date)

#select return date
return_date_field = chrome.find_element_by_xpath('/html/body/main/section/section/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/form/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[1]/input')
return_date_field.click()
sleep(1)
input_day_return_date = '30'
selected_day_return_date = "//table/tbody/tr/td/a[text()='{}']".format(input_day_return_date)
return_date_confirmation = chrome.find_element_by_xpath(selected_day_return_date)
return_date_confirmation.click()
sleep(1)

#confirm selection
flight_search = chrome.find_element_by_xpath('//*[@id="tab-compra"]/div/div/div/div/div/div/form/div/div[2]/div/div[2]/div[3]/div/div/button')
flight_search.click()
sleep(20)

#select departure flight
departure_flight_selection = chrome.find_element_by_xpath('//*[@id="LA3231"]/div/div')
departure_flight_selection.click()
sleep(1)
departure_flight_selection_proceed = chrome.find_element_by_xpath('//*[@id="main-content"]/div[4]/div/div[2]/section[1]/ul/li[2]/div[2]/div/div[2]/button')
departure_flight_selection_proceed.click()
sleep(10)

#select return flight
return_flight_selection = chrome.find_element_by_xpath('//*[@id="LA3230"]/div/div')
return_flight_selection.click()
sleep(1)
return_flight_selection_proceed = chrome.find_element_by_xpath('//*[@id="submit-flights"]')
return_flight_selection_proceed.click()
sleep(10)

flight_cost = chrome.find_element_by_xpath('//*[@id="toggle-details-button"]/div/div[3]/span[2]/span/span[2]/span')
flight_cost_value = flight_cost.text
print(flight_cost_value)

#https://selenium-python.readthedocs.io/locating-elements.html