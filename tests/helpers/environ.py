import os 
from yaml import safe_load, Loader 
class Environ(dict):
    def __init__(self, env_file_path=None, raise_file_error=False):
        # get os.environs 
        for key,value in os.environ.items():
            self[key] = value 
        
        # get file environs
        if env_file_path and os.path.exists(env_file_path) and os.path.isfile(env_file_path):
            with open(env_file_path) as env_file:
                envs = safe_load(env_file)
                if type(envs) != dict: 
                    raise TypeError("Requires YAML data to be of dict!")
                for key, value in envs.items():
                    self[key] = value 
        elif env_file_path and raise_file_error and (not os.path.exists(env_file_path) or not os.path.isfile(env_file_path)):
            raise Exception(f"Error loading: {env_file_path}")

    def get(self, key, default=None):
        value = default 
        try: 
            value = self[key]
        except KeyError:
            pass 
        return value 
