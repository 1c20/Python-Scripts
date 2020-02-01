from os import path,system
import sys
try:
    x = path.getsize(sys.argv[1])
except:
    print('[Watcher]: Error,  please make sure that you entered the path correctly')
try:
    while(True):
        if x != path.getsize(sys.argv[1]):
            system(sys.argv[2])
            x = path.getsize(sys.argv[1])
except:
    print('[Watcher]: Error, please make sure that you used " " for command and full file path and run again')

