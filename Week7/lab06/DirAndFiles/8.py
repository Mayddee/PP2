import os
path = input()
if os.path.exists(path):
    os.remove(path)
else:
    print("Path does not exist!")