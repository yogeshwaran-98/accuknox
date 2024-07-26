import psutil
import time
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 5
MEMORY_THRESHOLD = 5
DISK_THRESHOLD = 5

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU Usage Alert: {cpu_usage}%')
        print(f'CPU Usage Alert: {cpu_usage}%')
    
    # Check memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'Memory Usage Alert: {memory_usage}%')
        print(f'Memory Usage Alert: {memory_usage}%')
    
    # Check disk usage
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Disk Usage Alert: {disk_usage}%')
        print(f'Disk Usage Alert: {disk_usage}%')

def main():
    while True:
        check_system_health()
        time.sleep(5)  # Check every 5 seconds

if __name__ == '__main__':
    main()
