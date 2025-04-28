# System Health Monitoring and Backup Automation Project

## Overview
This project contains two major scripts:
- **System Health Monitor**: Monitors CPU, Memory, and Disk usage.
- **Automated Backup Solution**: Automatically backs up a specified folder.

## Folder Structure
```
scripts/
    health_monitor.py
    backup_script.py
logs/
backups/
screenshots/
README.md
requirements.txt
```

## Requirements
- Python 3
- psutil library

Install dependencies:
```bash
pip install -r requirements.txt
```

## How to run

### Monitor System Health
```bash
python3 scripts/health_monitor.py
```

### Backup Directory
Edit `SOURCE_DIR` path in `scripts/backup_script.py` and then run:
```bash
python3 scripts/backup_script.py
```

## Screenshots
*Coming Soon*

## Author
Developed by [Your Name]
