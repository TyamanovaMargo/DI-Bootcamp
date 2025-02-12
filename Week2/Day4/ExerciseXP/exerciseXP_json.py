#============== 
'''
The python function to save an object into a file is :

    json.dump(object_to_save, destination_file)
'''

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
data = json.loads(sampleJson)
# print(data)

salary = data["company"]["employee"]["payable"]["salary"]
# print(salary)

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key
data["company"]["employee"]["birth_date"] = "10.03.1990"
# print(data)

#Save the dictionary as JSON to a file.
with open("sampleJson.json", "w", encoding="utf-8") as file:
    json.dump(data, file) #which converts the Python objects into appropriate json objects.


#reading JSON file
with open("sampleJson.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON обратно в Python-словарь

print(data)