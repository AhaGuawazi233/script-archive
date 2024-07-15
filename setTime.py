import os
import subprocess

# 获取当前目录下的所有.wav文件
wav_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.wav')]

input_time = input("请输入需要统一化的时间长度（单位为秒）（要求要大于最长音频的长度）:")
input_time = float(input_time)

for wav_file in wav_files:
    # 获取音频长度
    duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', wav_file]))

    # 计算需要添加的静音长度
    pad_duration = max((input_time - duration) / 2, 0) 

    # 在音频的首尾添加等长的静音
    subprocess.call([
        'ffmpeg', '-i', wav_file, '-af',
        f'adelay={pad_duration*1000}|{pad_duration*1000},apad',
        '-t', str(input_time), 'temp.wav'
    ])

    # 将处理后的音频文件移动到原始音频文件的位置，覆盖原始文件
    os.replace('temp.wav', wav_file)