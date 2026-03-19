from collections import defaultdict

AVG = "avg"
NUM = "num"
class UndergroundSystem:

    def __init__(self):
        self.customer = defaultdict()
        self.avg_time = defaultdict()
        return

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_t = self.customer[id]
        key = "-".join((checkin_station, stationName))
        time = t - checkin_t
        if key in self.avg_time:
            self.avg_time[key][AVG] = (self.avg_time[key][AVG] * self.avg_time[key][NUM] + time) / (self.avg_time[key][NUM] + 1)
            self.avg_time[key][NUM] += 1
        else:
            self.avg_time[key] = {AVG: time, NUM: 1}
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = "-".join((startStation, endStation))
        return self.avg_time[key][AVG]

# Your UndergroundSystem object will be instantiated and called as such:
ops = ["UndergroundSystem", "checkIn", "checkIn", "checkIn", "checkOut", "checkOut", "checkOut", "getAverageTime", "getAverageTime", "checkIn", "getAverageTime", "checkOut", "getAverageTime"]
v = [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
ans = []
for i, op in enumerate(ops):
    if op == "UndergroundSystem":
        obj = UndergroundSystem()
        ans.append(None)
    elif op == "checkIn":
        obj.checkIn(v[i][0], v[i][1], v[i][2])
        ans.append(None)
    elif op == "checkOut":
        obj.checkOut(v[i][0], v[i][1], v[i][2])
        ans.append(None)
    elif op == "getAverageTime":
        ans.append(obj.getAverageTime(v[i][0], v[i][1]))
print(ans)