import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mysql-connector-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ipwhois'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-dotenv'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'googlesearch-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'geopy'])

print("Installations Complete!")