import os
import subprocess

def process_audio(file_path):
    output_file = "outx.wav"
    command = [
        "ffmpeg", 
        "-hide_banner", 
        "-loglevel", "warning", 
        "-i", file_path, 
        "-filter_complex", 
        "silenceremove=start_periods=1:start_duration=0:start_threshold=-50dB:detection=peak,areverse,silenceremove=start_periods=1:start_duration=0:start_threshold=-50dB:detection=peak,areverse", 
        "-ar", "44100", 
        "-ac", "1", 
        output_file, 
        "-y"
    ]
    subprocess.run(command, check=True)
    os.replace(output_file, file_path)

def traverse_and_process(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.wav'):
                file_path = os.path.join(dirpath, filename)
                print(f"Processing {file_path}")
                process_audio(file_path)

if __name__ == "__main__":
    root_directory = "."  # Change this to your target directory
    traverse_and_process(root_directory)
