#!/usr/bin/env python3
import psutil
import shutil
import datetime
import os

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

LOG_FILE = "logs/system_health.log"

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_message(message):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{time_stamp} - {message}\n")
    print(f"{time_stamp} - {message}")

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    issues = False

    if cpu_usage > CPU_THRESHOLD:
        log_message(f"WARNING: High CPU usage detected: {cpu_usage}%")
        issues = True

    if memory.percent > MEMORY_THRESHOLD:
        log_message(f"WARNING: High Memory usage detected: {memory.percent}%")
        issues = True

    disk_usage_percent = (disk.used / disk.total) * 100
    if disk_usage_percent > DISK_THRESHOLD:
        log_message(f"WARNING: High Disk usage detected: {disk_usage_percent:.2f}%")
        issues = True

    if not issues:
        log_message("System is healthy.")

if __name__ == "__main__":
    check_system_health()
