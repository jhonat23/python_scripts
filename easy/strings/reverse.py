# return the reverse word if have 5 or more letter, include sentences
def spin_words(sentence=str):
    # Your code goes here
    lst = sentence.split()
    return ' '.join(lst[i][::-1] if len(lst[i]) >= 5 else lst[i] for i in range(len(lst)))
print(spin_words(input()))

