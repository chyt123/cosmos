import bisect
from collections import defaultdict

TIME_LIST = "time_list"
class TimeMap:
    def __init__(self):
        self.actual_map = defaultdict(dict)
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.actual_map:
            self.actual_map[key][TIME_LIST] = list()
        self.actual_map[key][timestamp] = value
        self.actual_map[key][TIME_LIST].append(timestamp)
        # print(self.actual_map)
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.actual_map:
            return ""
        # find nearest timestamp
        idx = bisect.bisect_left(self.actual_map[key][TIME_LIST], timestamp)
        # print(idx)
        if idx < len(self.actual_map[key][TIME_LIST]) and self.actual_map[key][TIME_LIST][idx] == timestamp: # exact match
            return self.actual_map[key][self.actual_map[key][TIME_LIST][idx]]
        if idx == 0: # given time is the smallest
            return ""
        return self.actual_map[key][self.actual_map[key][TIME_LIST][idx - 1]]

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
# op = ["TimeMap", "set", "get", "get", "set", "get", "get"]
# v = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# op = ["TimeMap","set","set","set","set","get","get","get","get","get","get","set","get","get","get","set","set","set","set","get","get"]
# v = [[],["ctondw","ztpearaw",1],["vrobykydll","hwliiq",2],["gszaw","ztpearaw",3],["ctondw","gszaw",4],["gszaw",5],["ctondw",6],["ctondw",7],["gszaw",8],["vrobykydll",9],["ctondw",10],["vrobykydll","kcvcjzzwx",11],["vrobykydll",12],["ctondw",13],["vrobykydll",14],["ztpearaw","zondoubtib",15],["kcvcjzzwx","hwliiq",16],["wtgbfvg","vrobykydll",17],["hwliiq","gzsiivks",18],["kcvcjzzwx",19],["ztpearaw",20]]
op = ["TimeMap","set","set","get","set","get","get"]
v = [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
ans = []
for i in range(len(op)):
    if op[i] == "TimeMap":
        continue
    if op[i] == "set":
        ans.append(obj.set(v[i][0], v[i][1], v[i][2]))
        continue
    if op[i] == "get":
        ans.append(obj.get(v[i][0], v[i][1]))

print(ans)