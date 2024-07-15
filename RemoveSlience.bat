@echo off
chcp 65001 >nul
rem https://blog.tubumu.com/2021/12/07/ffmpeg-command-silenceremove/
rem 批处理保存为utf-8编码格式，需要ffmpeg（版本不要太旧）
for /f "delims=" %%i in ('dir /b /s /a-d *.wav') do (
    ffmpeg -hide_banner -loglevel warning -i "%%i" -filter_complex "silenceremove=start_periods=1:start_duration=0:start_threshold=-50dB:detection=peak,areverse,silenceremove=start_periods=1:start_duration=0:start_threshold=-50dB:detection=peak,areverse" -ar 44100 -ac 1 "outx.wav" -y
    move /y outx.wav "%%i"
)
pause
