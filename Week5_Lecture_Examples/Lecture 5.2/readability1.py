import os

try:
    os.unlink("file.txt")
# raised when file does not exist
except OSError:
    pass