names = ["aixk", "duke", "edik", "tofp", "duke"]
print(list(set(names))) # order is lost

import collections 
print(collections.OrderedDict.fromkeys(names).keys()) # order is kept
