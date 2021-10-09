from helpers.environ import Environ 
import os 
fp = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(fp, '.env')
env = Environ(fp, raise_file_error=True)

print(f"XDING: {env.get('xing', True)}")

