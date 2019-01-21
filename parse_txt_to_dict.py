dict={}

with open('data.txt', encoding='utf-8') as f:
    data =f.read().splitlines()
    for element_pair in data :
        elements = element_pair.split(",")
        element_key = elements[0]
        element_value = elements[1]
        dict[element_key] = element_value

print(dict)


data.txt:
kulcs1,ertek1
kulcs2,ertek2
