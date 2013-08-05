try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

def progress_bar_downloader(url, fname, progress_update_every=5):
    #from http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python/22776#22776
    u = urlopen(url)
    f = open(fname, 'wb')
    meta = u.info()
    file_size = int(meta.get("Content-Length"))
    print("Downloading: %s Bytes: %s" % (fname, file_size))
    file_size_dl = 0
    block_sz = 8192
    p = 0
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        if (file_size_dl * 100. / file_size) > p:
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            print(status)
            p += progress_update_every
    f.close()
