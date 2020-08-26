#importing
from speedtest import Speedtest
spd= Speedtest()
spd_dwn=spd.download()
print(f'Your Download Speed is: {spd_dwn}')
spd_up=spd.upload()
print(f"Your Upload Speed is: {spd_up}")
