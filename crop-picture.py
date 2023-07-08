from PIL import Image
import os
import traceback


def crop_images(folder_path, output_folder, width, height):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为图片
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # 拼接文件路径
            file_path = os.path.join(folder_path, filename)

            # 打开图像文件
            image = Image.open(file_path)

            # 获取图像的尺寸
            image_width, image_height = image.size

            # 计算剪裁的起始坐标和结束坐标
            left = (image_width - width) // 2
            top = (image_height - height) // 2
            right = left + width
            bottom = top + height

            # 剪裁图像
            cropped_image = image.crop((left, top, right, bottom))

            # 保存剪裁后的图像
            output_path = os.path.join(output_folder, filename)
            cropped_image.save(output_path)

            # 关闭图像文件
            image.close()


# 设置输入文件夹路径、输出文件夹路径和剪裁尺寸
# input_folder = r"D:\Users\liuqihang\Desktop\input_folder"
# output_folder =r"D:\Users\liuqihang\Desktop\output_folder"

input_folder = r"D:\Users\liuqihang\Desktop\input_folder\person"
output_folder =r"D:\Users\liuqihang\Desktop\output_folder\person"

# input_folder = r"D:\Users\liuqihang\Desktop\input_folder"
# output_folder =r"D:\Users\liuqihang\Desktop\output_folder"



crop_width = 1280
crop_height = 640

# 调用函数进行剪裁
try:
    crop_images(input_folder, output_folder, crop_width, crop_height)
except Exception as e:
    traceback.print_exc()