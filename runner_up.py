# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_lst = list(arr)
    set_lst = set(arr_lst)
    set_lst.discard(max(arr_lst))
    print(max(list(set_lst)))
    