"""Code to understand tuples"""

if __name__ == '__main__':
   n = int(input())
   integer_list = list(map(int, input().split()))
   hash_tup = hash(tuple(integer_list))
   print(hash_tup)
#print(input()==0 or hash(tuple(map(int,input().strip().split()))))
    