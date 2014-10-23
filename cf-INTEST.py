import sys
class Main(object):
    def __init__(self):
        n,k = map(int,next(sys.stdin.buffer).split())
        strings = sys.stdin.buffer.read().split()
        stats={}
        for item in strings:
            try:
                stats[item]+=1
            except KeyError:
                stats[item]=1
                result = 0
        for item,count in stats.items():
            if not int(item)%k:
                result += count
                print(result)
hef = Main()