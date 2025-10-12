import pandas
data = pandas.read_csv("Squirrel_Data.csv")

color_list = data["Primary Fur Color"].to_list()
gray = color_list.count("Gray")
cinnamon =  color_list.count("Cinnamon")
black = color_list.count("Black")

# or
"""
    gray = len(data[data["Primary Fur Color"]=="Gray"])
    cinnamon = len(data[data["Primary Fur Color"]=="Cinnamon"])
    black = len(data[data["Primary Fur Color"]=="Black"])
"""

final_dict = {"fur color": ["gray","cinnamon","black"],
              "count":[gray,cinnamon,black]}

df = pandas.DataFrame(final_dict)
df.to_csv("color.csv")