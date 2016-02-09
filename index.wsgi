import os
import sys

root = os.path.dirname(__file__)

# 两者取其一
# sys.path.insert(0, os.path.join(root, 'site-packages'))
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))