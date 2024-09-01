from collections import defaultdict

state_capitals = {
        "Arkansas": "Little Rock",
        "Colorado": "Denver",
        "California":"Sacramento",
        "Georgia":"Atlanta"
        }

# state_capitals["Alabama"] -> KeyError

state_capitals_default = defaultdict(lambda : "Placeholder City")
for k in state_capitals:
    state_capitals_default[k] = state_capitals[k]
print(state_capitals_default["Colorado"])
print(state_capitals_default["South Carolina"])
