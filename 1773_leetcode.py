
def countMatches( items, ruleKey: str, ruleValue: str) -> int:
    track = {
        "type":0,
        "color":1,
        "name":2
    }

    idx = track[ruleKey]
    res = 0
    for item in items:
        if item[idx] == ruleValue: res+=1
    return res


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(countMatches(items,ruleKey,ruleValue))