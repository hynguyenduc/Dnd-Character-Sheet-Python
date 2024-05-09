#this is just to play around with code

dict_ex = [{1: 'he.json', 2: 'je.json', 3: 'hy.json'}]

selection = "1"

profile_name = {k:v for (k,v) in dict_ex if k == int(selection)}
print(profile_name)