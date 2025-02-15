import os


path = 'cardboard_2/'

for i in range(0, 17000):

    src = os.listdir(path)[i]
    dst = 'cardboard' + str(i+1000) + '.jpg'

    os.rename(path + src, path + dst)


