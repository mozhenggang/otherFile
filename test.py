# -*- coding: utf-8 -*-
import os
import shutil

def copy_and_rename_files(source_folder, destination_folder, source_extension, destination_extension):
    try:
        # 确保目标文件夹存在，如果不存在则创建
        os.makedirs(destination_folder, exist_ok=True)

        # 遍历源文件夹中的所有文件
        for file_name in os.listdir(source_folder):
            # 判断文件是否是源后缀名的文件
            if file_name.endswith(source_extension):
                source_path = os.path.join(source_folder, file_name)

                # 构造目标文件名（修改后缀名）
                destination_name = os.path.splitext(file_name)[0] + destination_extension
                destination_path = os.path.join(destination_folder, destination_name)

                # 复制并重命名文件
                shutil.copy2(source_path, destination_path)
                print(f"文件复制成功: {file_name} -> {destination_name}")

        print("所有匹配文件复制并重命名完成！")
    except Exception as e:
        print(f"文件复制失败: {e}")

if __name__ == '__main__':
    source_folder_path = "E:/pythonProject/source"
    destination_folder_path = "E:/pythonProject/decrypted"
    source_extension = ".h"  # 源文件后缀名
    destination_extension = ".hxxx"  # 目标文件后缀名

    copy_and_rename_files(source_folder_path, destination_folder_path, source_extension, destination_extension)
