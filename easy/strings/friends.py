"""Only return the names with only 4 characters"""

def friend(x):
    return [i for i in x if len(i) == 4]

print(friend(["Ryan", "Kieran", "Jason", "Yous"]))