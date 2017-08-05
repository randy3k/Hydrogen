import sys
import os

pkg_path = os.path.dirname(__file__)
vendor = os.path.join(pkg_path, "vendor")

if vendor not in sys.path:
    sys.path.append(vendor)
