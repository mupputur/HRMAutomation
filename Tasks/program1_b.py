index_list = [1,2,3,4,5,6,7,8,9,10,11,12]
name_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#
d = {}
for index, name in zip(index_list, name_list):
    d[index] = name
print("Output1: {}".format(d))

x = []
for index, name in zip(index_list, name_list):
    t = index-1,  name
    x.append(t)
print("Output2: {}".format(x))
