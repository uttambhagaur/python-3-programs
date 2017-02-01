import os

def rename_pic():
    file_list = os.listdir(r"C:\Users\Coder\Desktop\A4A_Program")
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Coder\Desktop\A4A_Program")
    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("1234567890"))
    os.chdir(saved_path)

rename_pic()
