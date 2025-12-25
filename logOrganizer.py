import os
import shutil # untility for high-level file operations

#create some example files
#using 'a' mode to create the files if they don't exist
for nome in ["log1.txt", "log2.txt", "backup.zip"]:
    open(nome, 'a').close()

#create destination directories
os.makedirs("Logs", exist_ok=True)
os.makedirs("Backups", exist_ok=True)

archives = os.listdir('.')

for archive in archives:
    #filter .txt files
    if archive.endswith('.txt'):
        shutil.move(archive, os.path.join("Logs", archive))
        print(f"Moved {archive} to Logs/")
    #filter .zip files
    elif archive.endswith('.zip'):
        shutil.move(archive, os.path.join("Backups", archive))
        print(f"Moved {archive} to Backups/")
        