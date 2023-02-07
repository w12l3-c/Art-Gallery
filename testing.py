import pandas as pd

# pd.options.mode.chained_assignment = None

df = pd.read_csv('class_obj.csv').copy()
x = df[df['name'] == 'The Weeping Women'].index[0]

print(x)
print(type(x))
print(df)

print(df['origin'][1])

# df['origin'][0] = 'spain'
# df.to_csv('class_obj.csv', index=False)
# print(df)

# this is better
# df.loc[2, 'origin'] = 'Hello world'
# print(df.head(5))
# df.to_csv('class_obj.csv', index=False)

something = "hello i am not a person a robot instead and it is something that is not".split()
print(something[6:None])

"""
lst = []
def saving_data(self):
    with open('JSON_saving.json', 'w') as f:
        data_lst = json.load(f)
        art_data = {
            "art": self.name,
            "format": self.__class__.__name__,
            "information": {
                "artist": self._artist,
                "price": self._price,
                "era": {
                    "year": self._year,
                    "period": None
                },
                "origin": {
                    "country": None,
                    "website": None
                },
                "sold": self.sold,
            }
        }
        data_lst.append(art_data)

    with open(f"JSON_saving.json", 'w') as f:
        json.dump(data_lst, f, indent=4)
"""

"""
def update_data(self):
    with open(f"JSON_files/saving_data_{self.name}.json", 'r') as f:
        data = json.load(f)
        data['information']['price'] = self._price
        data['information']['origin']['website'] = self.__website
        data['information']['era']['period'] = self._period

    with open(f"JSON_files/saving_data_{self.name}.json", 'w') as f:
        json.dump(data, f, indent=4)
"""

"""
def update_data(self):
    with open(f"JSON_saving.json", 'r') as f:
        data = json.load(f)

        data['information']['era']['period'] = self._period
        data['information']['origin']['country'] = self.__origin

    with open(f"JSON_saving.json", 'w') as f:
        json.dump(data, f, indent=4)
"""
