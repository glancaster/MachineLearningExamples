filter_list = list(filter(None, [1,0,2,[],'','a'])) # ['1,2,'a']
listcomp = [i for i in  [1,0,2,[],'','a'] if i]
generator = ( i for i in  [1,0,2,[],'','a'] if i )
