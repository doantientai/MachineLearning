import os
from shutil import copyfile

PATH_TRAIN = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50paired/train/'
PATH_VAL = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50paired/test/'
PATH_TEST = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50paired/val/'
PATH_SOURCE = '/home/tai-databases/CTLymphNodes/PNG/resize_256'
PATH_DEST = '/home/Projects/GANoiseMaker/rival/DnCNN-crisb-DUT/DnCNN-tensorflow/data/CTLymphNodes_256'
PATH_DEST_TRAIN = PATH_DEST + '_train/'
PATH_DEST_TEST = PATH_DEST + '_test/'

# print("list_train", len(list_train))
# print("list_test", len(list_test))
# print("list_val", len(list_val))
# print("list_source", len(list_source))

def CopyImages(list_name, path_source, path_dest):
	# print("fired CopyImages")
	#check if dir exist
	if not os.path.exists(path_dest):
		print(path_dest,' not exits. generating...')
		os.makedirs(path_dest)
	else:
		print("Found", path_dest)

	#copy files
	print("copying files...")
	for a_name in list_name:
		copyfile(path_source + a_name, path_dest + a_name)

	print("Done!")
def main():
	# print("list_train", len(list_train))
	# print("list_test", len(list_test))
	# print("list_val", len(list_val))
	# print("list_source", len(list_source))

	list_train = [fn for fn in next(os.walk(PATH_TRAIN))[2]]
	list_test = [fn for fn in next(os.walk(PATH_TEST))[2]]
	list_val = [fn for fn in next(os.walk(PATH_VAL))[2]]
	list_source = [fn for fn in next(os.walk(PATH_SOURCE))[2]]

	CopyImages(list_train,PATH_TRAIN,PATH_DEST_TRAIN)
	CopyImages(list_test,PATH_TEST,PATH_DEST_TEST)


if __name__ == '__main__':
    main()