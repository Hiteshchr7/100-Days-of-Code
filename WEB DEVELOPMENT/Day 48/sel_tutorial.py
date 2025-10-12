from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org/")

dates_list = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_list = driver.find_elements(By.CSS_SELECTOR,".event-widget .menu a")
result_dict =  {}
for i in range(len(dates_list)) :
    result_dict[i]={"time" : dates_list[i].text,
        "name" : event_list[i].text}
#prints all upcoming event's and their date's nested dictionary 
print(result_dict)
driver.quit()
