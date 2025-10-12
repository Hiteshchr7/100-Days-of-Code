import requests
import os
import dotenv 
from datetime import datetime
dotenv.load_dotenv()

'''Created a user account on pixela using post req'''
pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token" : os.environ.get("pixela_token"),
    "username" : os.environ.get("pixela_username"),
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(pixela_url,json=user_param)


"""Creating a graph for habit tracking """
graph_endpoint = f"{pixela_endpoint}/{os.environ.get("pixela_username")}/graphs"
graph_param = {
    "id" : "graph7" ,
    "name" : "Study/Coding Graph",
    "unit" : "hour",
    "type" : "float",
    "color" : "sora"
}
headers = {
    "X-USER-TOKEN" : os.environ.get("pixela_token")
}
#response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)


today = datetime.now()
pixel_param = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you study/code today? ")
}
pixel_endpoint = f"{pixela_endpoint}/{os.environ.get("pixela_username")}/graphs/graph7"
response = requests.post(url=pixel_endpoint,json=pixel_param,headers=headers)


pixel_put_endpoint = f"{pixela_endpoint}/{os.environ.get('pixela_username')}/graphs/graph7/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity" : "1.5"
}
# response = requests.put(url=pixel_put_endpoint,json=new_pixel_data,headers=headers)


pixel_del_endpoint = f"{pixela_endpoint}/{os.environ.get('pixela_username')}/graphs/graph7/{today.strftime('%Y%m%d')}" 
# response = requests.delete(url=pixel_del_endpoint,headers=headers)
print(response.text)