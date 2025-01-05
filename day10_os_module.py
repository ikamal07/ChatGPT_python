import os
print(os.getcwd())
print(os.listdir())
os.system('mkdir test_dir')
if os.path.isdir('test_dir'):
    print("Directory Exists")
else:
    print("Directory is not created")