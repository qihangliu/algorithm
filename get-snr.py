from pydub import AudioSegment
import numpy as np
import os

# 定义函数来计算信噪比
def calculate_snr(audio):
    # 转换音频数据到numpy数组
    audio_data = np.array(audio.get_array_of_samples())
    
    # 根据音频数据的平均值计算信号能量
    signal_energy = np.mean(audio_data ** 2)
    
    # 计算噪声能量
    noise_energy = signal_energy / (10 ** (audio.dBFS / 10))
    
    # 返回信噪比
    return 10 * np.log10(signal_energy / noise_energy)

# 遍历文件夹中的所有mp3文件并计算它们的信噪比
folder_path = "C:/Users/LQH/Desktop/test"
for file_path in os.listdir(folder_path):
    if file_path.endswith(".mp3"):
        # 加载mp3文件
        audio_file = AudioSegment.from_file(os.path.join(folder_path, file_path), format="mp3")
        
        # 计算信噪比
        snr = calculate_snr(audio_file)
        
        # 打印结果
        print(f"{file_path}: SNR = {snr:.2f} dB")

