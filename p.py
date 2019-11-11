import json
import sys
s = sys.argv[1] #input()
def dosomething():
    print(json.dumps({"ans":s}))
dosomething()
