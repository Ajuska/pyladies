import json

retezec_s_jsonem = """{
  "jméno": "Anna",
  "město": "Brno",
  "jazyky": ["čeština", "angličtina", "Python"],
  "věk": 26
}"""

data = json.loads(retezec_s_jsonem)
print(data)
print(data['jméno'])

data['město'] = 'Pardubice'

retezec = json.dumps(data, ensure_ascii=False,
                    indent=4)
print(retezec)
