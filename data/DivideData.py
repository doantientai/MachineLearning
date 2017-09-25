import os

PATH_TRAIN = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50paired/train/'
PATH_VAL = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50paired/test/'
PATH_TEST = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50paired/val/'
PATH_SOURCE = '/home/tai-databases/CTLymphNodes/PNG/resize_256'

list_train = [os.path.join(PATH_TRAIN,fn) for fn in next(os.walk(PATH_TRAIN))[2]]
list_test = [os.path.join(PATH_TEST,fn) for fn in next(os.walk(PATH_TEST))[2]]
list_val = [os.path.join(PATH_VAL,fn) for fn in next(os.walk(PATH_VAL))[2]]
list_source = [os.path.join(PATH_SOURCE,fn) for fn in next(os.walk(PATH_SOURCE))[2]]

print("list_train", len(list_train))
print("list_test", len(list_test))
print("list_val", len(list_val))
print("list_source", len(list_source))