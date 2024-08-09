import duckduckpy

for r in duckduckpy.query('Sausages').related_topics:
    print(r.first_url," - ",r.text)



""" 
More Abstract than urllib,requests, three lines,io";../o; and you get the same data out
"""