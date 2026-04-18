import shutil

source = input("Enter source folder path: ")
backup = input("Enter backup folder path: ")

shutil.copytree(source, backup)

print("Backup completed successfully")