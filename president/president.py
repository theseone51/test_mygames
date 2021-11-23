import json
import sys

try:
    with open("blob.json", "r") as file:
        data = json.load(file)

    president = " ".join(sys.argv[1:])
    mathching = next(item for item in data if item['president'] == president)
    print(f"Номер: { mathching['number'] }\n"
          f"Имя: { mathching['president'] }\n"
          f"Дата рождения: { mathching['birth_year'] }\n"
          f"Дата смерти: { mathching['death_year'] }\n"
          f"Дата начала правления: { mathching['took_office'] }\n"
          f"Дата окончания правления: { mathching['left_office'] }\n"
          f"Партия: { mathching['party'] }")
except IOError:
    print("Can not read file blob.json =(")
except StopIteration:
    print("President not found =(")
