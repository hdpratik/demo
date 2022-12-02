import shutil

path = 'D:\Users\Pratik\PycharmProjects\pythonProject\Numbers program\New folder'

src = path + 'lemonade'
dst = path + 'lemonade'

print(shutil.copyfile(src, dst))