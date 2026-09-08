class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d={}
        bulbs.sort()
        for bulb in bulbs:
            if bulb not in d:
                d[bulb]=1
            else:
                d[bulb]+=1
        j=[]
        for k,v in d.items():
            if v%2!=0:
                j.append(k)
        return j
        
