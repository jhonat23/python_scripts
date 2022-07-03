def get_count(sentence):
    count = 0
    for i in sentence:
        if i in 'aeiou':
            count +=1
    return count

print(get_count(input()))