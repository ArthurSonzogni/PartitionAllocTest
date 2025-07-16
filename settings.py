import os

PARTITION_ALLOC_REPO = "https://chromium.googlesource.com/chromium/src/base/allocator/partition_allocator.git"
START_COMMIT = "087911ce77bce70f277fda09e10db56fe577ed53~"
REPO_DIR = "partition_alloc"
OUTPUT_DIR = "output"
CONFIG_DIR = "configuration"
GN_PATH = os.path.join(os.getcwd(), "gn", "out", "gn")
