from pydub import AudioSegment
import pesq

# 设置参考音频文件路径
ref_path = 'reference.wav'

# 定义得分字典
scores = {}

# 循环遍历所有的测试音频文件
for degraded_path in ['sample1.wav', 'sample2.wav', 'sample3.wav']:

    # 加载音频
    ref_audio = AudioSegment.from_wav(ref_path)
    degraded_audio = AudioSegment.from_wav(degraded_path)

    # 转换采样率为8000Hz
    ref_audio = ref_audio.set_frame_rate(8000)
    degraded_audio = degraded_audio.set_frame_rate(8000)

    # 将音频数据转换为numpy数组
    ref_data = ref_audio.get_array_of_samples()
    degraded_data = degraded_audio.get_array_of_samples()

    # 计算PESQ分数
    score = pesq.pesq(8000, ref_data, degraded_data, 'wb')

    # 将分数添加到得分字典中
    scores[degraded_path] = score

# 输出得分结果
print(scores)
