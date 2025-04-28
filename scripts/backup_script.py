#!/usr/bin/env python3
import os
import shutil
import datetime

SOURCE_DIR = "C:/Users/reyansh mishra/OneDrive/Documents/wisecow-main"
BACKUP_DIR = "backups/"

os.makedirs(BACKUP_DIR, exist_ok=True)

def create_backup():
    time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"backup_{time_stamp}.zip")

    try:
        shutil.make_archive(backup_file.replace('.zip', ''), 'zip', SOURCE_DIR)
        print(f"Backup successful: {backup_file}")
    except Exception as e:
        print(f"Backup failed: {str(e)}")

if __name__ == "__main__":
    create_backup()
