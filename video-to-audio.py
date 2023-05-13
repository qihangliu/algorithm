from moviepy.editor import *

# 设置MP4文件所在的文件夹路径
input_folder = "D:\\Users\\liuqihang\\Desktop\\Pictures"

# 设置保存音频文件的文件夹路径
output_folder = "D:\\Users\\liuqihang\\Desktop\\Audio"

# 循环遍历文件夹中的所有MP4文件
for file_name in os.listdir(input_folder):
    if file_name.endswith(".mp4"):
        # 读取MP4文件并提取音频
        video = VideoFileClip(os.path.join(input_folder, file_name))
        audio = video.audio
        
        # 构造输出文件路径和名称
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".mp3")
        
        # 保存音频文件
        audio.write_audiofile(output_file)