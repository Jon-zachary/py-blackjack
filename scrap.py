# def arg_lister(**kwarg):
#     for foo in kwarg:
#         print(foo, kwarg[foo])
        
# arg_lister(name='dan', job='prof' )

# d = {'name': 'dan', 'job': 'prof'}

# for k in d:
#     print( k, d[k])

# l = [1, 2, 3]
# print(l)
# l[0] = 20
# print(l)

# t = (1, 2, 3)
# t[0] = 20

# l = [1, 2, 3, 4, 4, 4, 5, 5, 6]
# print(l)
# s = set(l)
# print(s)

# Write a function that takes three strings
#  and prints out the length of each of them

# def print_len(w1, w2, w3):
#     return len(w1), len(w2), len(w3)

# len1, len2, len3 = print_len('hello', 'python', 'foobarquin')

# print(len1, len2, len3)



# def vowel_count(s):
#     vowels = ['a','e','i','o','u']
#     count = 0
#     for chr in s:
#         if chr in vowels:
#             count += 1
#     return count
# v = vowel_count('hello')
# print(v)

class Nums:
    def __init__(self, nums):
        self.n = nums
    
    @property
    def total(self):
        return sum(self.n)
        
N = Nums([1,2,3])
print(N.n)
print(N.total)

N.n.append(4)
print(N.total)
print(N.n)
