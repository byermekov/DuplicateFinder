import os
import tqdm
from pathlib import Path
import zlib
# from PIL import Image
import pickle

HASH_CACHE_FILE = 'img_hash_cache.pkl'

ARG_HASH_SIZE = 5 # less strict
ARG_HASH_SIZE = 6 # strict
ARG_HASH_SIZE = 8 # super strict


## SEARCH PATH
ARG_SEARCH_FOLDERS = [
    '/abc/xyz/xyz/' ## Set search path here
]



g_hash_cache = dict()

image_files = []
for folder in ARG_SEARCH_FOLDERS:
    img_files = [ str(x) for x in Path(folder).rglob('*.*') ]
    img_files = list(filter(lambda x: x.rsplit('.', 1)[-1].lower() in ['png', 'jpeg', 'jpg', 'bmp'], img_files))
    image_files.extend(img_files)


def crc32(fileName):
    with open(fileName, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(65536)
            if not s:
                break
            hash = zlib.crc32(s, hash)
        return "%08X" % (hash & 0xFFFFFFFF)

def crc32_test(image_files):
    files_by_hash = dict()
    for img_file in (pbar := tqdm.tqdm(image_files)):
        pbar.set_description("[CRC32 TEST]")
        h = try_get_value((img_file, 'crc'), lambda: crc32(img_file))
        if h not in files_by_hash:
            files_by_hash[h] = []
        files_by_hash[h].append(img_file)

    print("#"*50)
    print("[CRC32 TEST]")
    print("#"*50)
    for h, files in files_by_hash.items():
        if len(files) <= 1:
            continue

        print(f"Hash: {h}, Found {len(files)}")
        for f in files:
            print(f"    {f}")
        print('-'*50)



def load_hash_cache():
    global g_hash_cache
    if os.path.exists(HASH_CACHE_FILE):
        with open(HASH_CACHE_FILE, 'rb') as fp:
            g_hash_cache = pickle.load(fp)

def save_hash_cache():
    global g_hash_cache
    if os.path.exists(HASH_CACHE_FILE):
        with open(HASH_CACHE_FILE, 'wb') as fp:
            pickle.dump(g_hash_cache, fp)

def try_get_value(key, or_not):
    global g_hash_cache
    if key not in g_hash_cache:
        g_hash_cache[key] = or_not()
    return g_hash_cache[key]

load_hash_cache()

crc32_test(image_files)


save_hash_cache()