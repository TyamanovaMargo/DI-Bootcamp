word_from_user = input("Enter a comma-separated sequence of words: ")


result = [ word for word in word_from_user.split(",")] # type list]

print(",".join(sorted(list(result))))
