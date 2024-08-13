import os
os.system("cls")

sample_st  = {'Yellow', 'Orange','Black'}
sample_lst = ["Blue", 'Green', 'Red']
sample_st2 = set(sample_lst)
result = sample_st | sample_st2

print(result)

