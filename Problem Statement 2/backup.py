import boto3
import io
import tarfile
from pathlib import Path
from datetime import datetime

SOURCE_DIR = '/path/to/source/directory'
S3_BUCKET_NAME = 'your-s3-bucket-name'
S3_BACKUP_PATH = 'backups/'
BACKUP_FILE_NAME = f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.tar.gz'

def create_backup_in_memory():
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode='w:gz') as tar:
        source_dir_path = Path(SOURCE_DIR)
        for file in source_dir_path.rglob('*'):
            arcname = file.relative_to(source_dir_path)
            tar.add(file, arcname=arcname)
    buffer.seek(0)
    return buffer

def upload_to_s3(file_buffer, file_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_fileobj(file_buffer, S3_BUCKET_NAME, S3_BACKUP_PATH + file_name)
        print(f'Backup uploaded to S3 successfully: {file_name}')
    except Exception as e:
        print(f'Upload to S3 failed: {e}')

if __name__ == '__main__':
    backup_buffer = create_backup_in_memory()
    upload_to_s3(backup_buffer, BACKUP_FILE_NAME)
