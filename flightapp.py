from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def flight_app():
    leave_slc = input("Departure date: ")
    leave_uk = input("Return date: ")

    driver = webdriver.Chrome()
    driver.get(f"https://www.kayak.com/flights/SLC-LON/2024-{leave_slc}/2024-{leave_uk}?sort=bestflight_a")
    page_source = driver.page_source
    flight_options = driver.find_elements(By.CLASS_NAME, "Hv20-content")
    flights = ['','','']
    i = 0

    print('')
    print('')
    print("Flights from Salt Lake City to London")

    print(f'Departure from SLC {leave_slc}. Leave London {leave_uk}')
    
    for flight in flight_options:
         flights[i] = flight_options[i].text
         i += 1

    print('')
    print(flights[0])
    print('')
    print(flights[1])
    print('')
    print(flights[2])
    print('')
    
    driver.close()

if __name__ == '__main__':
    while True:
        flight_app()
        time_wait = 30
        print('')
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
        