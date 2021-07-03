import collections
import re


def missing(first, second):
    first_dict = collections.defaultdict()
    ans = []
    for i, j in first:
        first_dict[i] = j
    for i, j in second:
        if i not in first_dict:
            ans.append([i, j])
    ans.sort(key=lambda x:x[1])
    return [i[0] for i in ans]


first = [[1234, 532632], [2354, 732634]]
second = [[1234, 532632], [234, 632633], [458, 642633], [2354, 732634]]
# print(missing(first, second))


def employeeWithLesser(employeeCalls, k):
    ans = []
    employees = collections.defaultdict(list)
    for i, j, l in employeeCalls:
        employees[i].append([j, l])
    for i in employees:
        cnt = 0
        for j in range(1, len(employees[i])):
            if employees[i][j][0] > employees[i][j - 1][1]:
                cnt += 1
        if cnt < k:
            ans.append("{} {}".format(i, cnt))
    return ans

employeeCalls = [
    [1, 1481122000, 1481122020],
    [3, 1481122000, 1481122020],
    [1, 1481122020, 1481122040],
    [2, 1481122020, 1481122040],
    [3, 1481122040, 1481122060],
    [1, 1481122050, 1481122060],
    [3, 1481122070, 1481122090]
]
k = 2
# print(employeeWithLesser(employeeCalls, k))

def awardTopK(positive, negative, hotelIds, reviews, k):
    positive_set = set(positive.lower().split())
    negative_set = set(negative.lower().split())
    pts = collections.defaultdict()
    for i in range(len(hotelIds)):
        hotel_id = hotelIds[i]
        if hotel_id not in pts:
            pts[hotel_id] = 0
        pt = 0
        for word in re.split('[^a-zA-Z]', reviews[i].lower()):
            if word in positive_set:
                pt += 3
            elif word in negative_set:
                pt -= 1
        pts[hotel_id] += pt
    pt_list = [[i, j] for i, j in pts.items()]
    pt_list.sort(key=lambda x: (-x[1], x[0]))
    return [i[0] for i in pt_list[:k]]


positive = "BREAKFAST BEACH CITYCENTER LOCATION METRO VIEW STAFF PRICE"
negative = "NOT"
hotelIds = [3, 4, 3, 3, 4]
reviews = ['THIS HOTEL HAS A NICE VIEW OF THE CITYCENTER. THE LOCATION IS PERFECT.', 'THE BREAKFAST IS OK. REGARDING LOCATION, IT IS QUITE FAR FROM CITYCENTER BUT PRICE IS CHEAP SO IT IS WORTH.', 'LOCATION IS EXCELLENT, 5 MINUTES FROM CITYCENTER. THERE IS ALSO A METRO STATION VERY CLOSE TO THE HOTEL.', "THEY SAID I COULDN'T TAKE MY DOG AND THERE WERE OTHER GUESTS WITH DOGS! THAT IS NOT FAIR.", 'VERY FRIENDLY STAFF AND GOOD COST-BENEFIT RATIO. LOCATION IS A BIT FAR FROM CITYCENTER.']
k = 2

positive = "breakfast beach citycenter location metro view staff price"
negative = "not"
hotelIds = [1, 2, 1, 1, 2]
reviews = [
    "This hotel has a nice view of the citycenter. The location is perfect.",
    "The breakfast is ok. Regarding location, it is quite far from citycenter but price is cheap so it is worth.",
    "Location is excellent, 5 minutes from citycenter. There is also a metro station very close to the hotel.",
    "Good price but I couldn't take my dog and there were other guests with dogs!",
    "Very friendly staff and good cost-benefit ratio. Its location is a bit far from citycenter.",
]
k = 2
print(awardTopK(positive, negative, hotelIds, reviews, k))
