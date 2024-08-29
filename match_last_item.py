# Match the Last Item
# Create a function that takes a list of items and checks if 
# the last item matches the rest of the list concatenated together.

# Examples
# match_last_item(["rsq", "6hi", "g", "rsq6hig"]) ➞ True
# # The last item is the rest joined.

# match_last_item([1, 1, 1, "11"]) ➞ False
# # The last item should be "111".

# match_last_item([8, "thunder", True, "8thunderTrue"]) ➞ True


def match_last_item(lst):
    lstent= "".join(lst[:len(lst)-1])
    if lstent == lst[-1] :
        return True
    else: return False
print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))

#//////////////////////////////////////////////////////

def match_last_item(lst):
    lstent = "".join(map(str, lst[:len(lst)-1]))
    if lstent == lst[-1]:
        return True
    else:
        return False

print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))  # Output: True

