"""It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic."""

def minimumBribes(q):
    bribes = 0
    Q = [i-1 for i in q]
    for count, i in enumerate(Q):
        if i - count > 2:
            return print('Too chaotic')
        for j in range(max(i-1,0), count):
            if Q[j] > i:
                bribes += 1
    return print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

