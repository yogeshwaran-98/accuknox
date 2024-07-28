
import psutil
import time
import logging


logging.basicConfig(filename='system_config.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


CPU_THRESHOLD = 75
MEMORY_THRESHOLD = 75
DISK_THRESHOLD = 75

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU Usage is above: {cpu_usage}%')
        print(f'CPU Usage Alert: {cpu_usage}%')
    
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'Memory Usage is above: {memory_usage}%')
        print(f'Memory Usage Alert: {memory_usage}%')
    

    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Disk Usage is above: {disk_usage}%')
        print(f'Disk Usage Alert: {disk_usage}%')

def main():
    while True:
        check_system_health()
        time.sleep(10) 

if __name__ == '__main__':
    main()
