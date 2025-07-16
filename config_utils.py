import os
import glob
from settings import CONFIG_DIR

def get_configurations():
    """
    Returns a list of (configuration_name, configuration_path) tuples.
    """
    configs = []
    for config_path in glob.glob(os.path.join(CONFIG_DIR, "*.gn")):
        config_name = os.path.splitext(os.path.basename(config_path))[0]
        configs.append((config_name, config_path))
    return configs
