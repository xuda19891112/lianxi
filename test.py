import os
import pandas
import subprocess

cmd = 'lux https://www.iqiyi.com/v_2993z2f1klc.html'
ret = subprocess.check_output(cmd,shell=True)
ret = ret.decode()
print(type(ret))