import zipfile

import os

cwd = os.getcwd()
os.chdir(cwd)
zfile = zipfile.ZipFile('py_archive_file.zip', 'w')

for file in cwd:
    if file.endswith("py"):
        zfile.write(file, compress_type=zipfile.ZIP_DEFLATED)
zfile.close()