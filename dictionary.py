#Dictionary practice

a = {'hi' : 1, 'hello' :2,'good' :3 }
a.keys()
print(a.keys())

list(a.keys())
print(list(a.keys()))


for k in a.keys():
    print(k)


a.items()
print(a.items())

a['hi']

print(a['hi'])

print(a.get('nokey'))
print(a.get('nokey',"qkqh"))

