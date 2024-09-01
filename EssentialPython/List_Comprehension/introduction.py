lists = {
"basiclist":[x + 1 for x in (1,2,3)], # [2,3,4]
"generator":(x + 1 for x in (1,2,3)), # 2 -> 3 -> 4
"filterlist":[x + 1 for x in (1,2,3) if x % 2 == 0], # 3
"ternarylist":[x + 1 if x % 2 == 0 else x for x in (1,2,3)], # [1,3,3]
"ternaryfilterlist":[x+1 if x%2 == 0 else x for x in range(-3,4) if x > 0], # [1,3,3]
"setcomp":{x for x in (1,2,2,3)}, # {1,2,3}
"dictcomp":{k:v for k,v in [('a',1),('b',2)]}, # {'a':1,'b':2}
"nestedlist":[ x + y for x in [1,2] for y in [10,20]], # [11,21,12,22]
"firstloopfilter":[ x + y for x in [1,2,3] if x > 2 for y in [3,4,5]], # [6,7,8]
"secondloopfilter":[ x + y for x in [1,2,3] for y in [3,4,5] if x > 2] # [6,7,8]
         }
for l in lists.values():
    print(l)
