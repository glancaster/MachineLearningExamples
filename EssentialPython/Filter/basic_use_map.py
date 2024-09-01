names = ['Fred', 'Wilma', 'Barney']

map(len, names) # <object>

# above can be replaced
generator = (len(name) for name in names)
