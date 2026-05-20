import sys
import os


def pytest_configure(config):
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(here, "..", ".."))
    project_src = os.path.join(root, "src")
    if os.path.isdir(project_src) and project_src not in sys.path:
        sys.path.insert(0, project_src)
