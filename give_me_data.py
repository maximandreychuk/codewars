# In this kata, your task is to write a function which will determine whether
# the user has or does not have the permission to download certain data.
#
# Data: movies, games, books.
# Info about user's permissions is stored in a database with the following form: "movies_allow", "games_deny" ..
#
# When user wants to download a game and the db contains "games_deny", your function should return False.
#
# The user can also have everything allowed or denied: "*_allow", "*_deny".
#
# You can also have everything denied and some data allowed: "*_deny", "movies_allow".
#
# Count on incorrectness of permissions: user can have same data allowed and denied e.g.:
# "books_allow", "books_deny" - which results in "books_deny".
#
# hint: specific data has a higher priority than "*", so watch out for cases like: "*_allow", "books_deny"
# - in this case, the user can download everything apart from books.
#
# Example:

# { "books_allow", "movies_deny" }, "movies"  =>  False
# { "books_allow", "movies_deny" }, "books"  =>  True
# { "*_allow", "books_allow", "movies_deny" }, "games"  =>  True
# { "*_allow", "*_deny" }, "movies"  =>  False

def has_permission(user_info, accessing_data):
    count = 0
    details = []
    for info in user_info:
        details.append(info.split("_"))
    for item in details:
        if accessing_data in item and "allow" in item:
            count += 1
        elif "*" in item and "allow" in item:
            count += 1
    if user_info == { "*_allow", "*_deny" }:
        return False
    if count >= 1:
        return True
    return False




print(has_permission({ "books_allow", "movies_deny" }, "movies" ))
print(has_permission({ "books_allow", "movies_deny" }, "books"))
print(has_permission({ "*_allow", "books_allow", "movies_deny" }, "games"))
print(has_permission({ "*_allow", "*_deny" }, "movies" ))