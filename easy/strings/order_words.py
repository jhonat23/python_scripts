"""Ordering a sentence using the number inside of it"""


def order(sentence):
    phrase = sentence.split()
    lst =[[*phrase[i]] for i in range(len(phrase))]
    order = [str(i) for i in range(1, len(phrase) +1)]    
    def num_pos(elem):
        for i in elem:
            if i in order:
                return i
    lst.sort(key=num_pos)
    sorted_string = ' '.join([''.join(lst[i]) for i in range(len(lst))])

    return sorted_string

order('is2 Thi1s T4est 3a')