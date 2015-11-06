import os

def get_folder(f):
    if f == 0:
        return "000"
    folder = str(f)
    length = 0
    while f != 0:
        length += 1
        f /= 10
        f = int(f)
    while length != 3:
        folder = "0" + folder
        length += 1
    return folder

def rename():
    cur_path = os.getcwd()
    for f in range(0, 182):
        folder = get_folder(f)
        folder += "/Trajectory/"
        path = "/home/zishan/development/minor/data/"
        path += folder
        os.chdir(path)
        files = os.listdir()
        files.sort()
        j = 1
        for i in files:
            os.rename(i, str(j)+".plt")
            j += 1
        print("File rename complete in folder {0}. Number of files renamed: {1}".format(folder, len(files)))
    os.chdir(cur_path)

if __name__ == '__main__':
    rename()