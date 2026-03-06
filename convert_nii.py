import subprocess
import os
from tqdm import tqdm

if __name__ == "__main__":
    path = os.path.join('data', 'testing')

    for folder in tqdm(os.listdir(path)):
        folder_path = os.path.join(path, folder)
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            cmd = ['gzip', f"{file_path}"]
            subprocess.run(cmd, check=True, text=True)
    
