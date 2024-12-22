from django.conf import settings
from apps.gwm.models import Apk
import logging
from pathlib import Path
import hashlib
import os
import uuid

logger = logging.getLogger(__name__)


def human_file_size(size):
    power = 2 ** 10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size = size / power
        n += 1
    size = round(size, 1)
    return f"{size}{power_labels[n]}B"


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def collect_apk_files():
    apk_list = []
    current_web = os.environ.get('ENTRY_IP', 'Unknown')
    web_base_url = f"http://{current_web}/dl"
    download_dir = settings.APK_DL_DIR
    directory_path = Path(download_dir)
    for file_path in directory_path.rglob("*.apk"):
        file_size_raw = file_path.stat().st_size
        file_size = human_file_size(file_size_raw)
        file_md5 = calculate_md5(file_path)
        name = str(file_path).split('/')[-1]
        print(name)
        id = str(uuid.uuid4())
        apk_list.append({
            'id': id,
            'name': name,
            'url': web_base_url + '/' + name,
            'md5': file_md5,
            'size': file_size
        })
    return apk_list


def insert_or_update_apk(val):
    logger.info("insert or update apk instance: {}".format(val))

    try:
        apk = Apk.objects.get(name=val['name'])
    except Apk.DoesNotExist:
        apk = Apk(name=val['name'])
    if "version" in val.keys():
        apk.version = val['version']
    if "describe" in val.keys():
        apk.describe = val['describe']
    if "file_url" in val.keys():
        apk.file_url = val['file_url']
    if "file_md5" in val.keys():
        apk.file_md5 = val['file_md5']
    if "file_size" in val.keys():
        apk.file_size = val['file_size']
    if "comment" in val.keys():
        apk.comment = val['comment']
    apk.save()
    return "apk instances update -> OK"
