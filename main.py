# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements)
print("carbon" in elements)
print(elements.get("dilithium"))


n = elements.get("dilithium")
print(n is None)
print(n is not None)

elea = {"hydrogen": 1, "helium": 2, "carbon": 6}
print("______________")



a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
# TODO: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't


elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
