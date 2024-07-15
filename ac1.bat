@echo off
chcp 65001 >nul
rem 批处理脚本用于将多通道音频文件转换为单通道音频文件，需要ffmpeg
for /f "delims=" %%i in ('dir /b /s /a-d *.wav') do (
    ffmpeg -hide_banner -loglevel warning -i "%%i" -ac 1 "temp.wav" -y
    move /y "temp.wav" "%%i"
)
pause
