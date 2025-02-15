import os


path = 'Possible_trash_on_platforms/'

for i in range(1, 108):

    src = 'platform' + str(i) + '.jpg'
    dst = 'platform_' + str(i) + '.jpg'

    os.rename(path + src, path + dst)


