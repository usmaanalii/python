def reverse_string(string):
    reverse = ""
    i = len(string)
    while i > 0:
        reverse += string[i - 1]
        i -= 1
    print(reverse)


reverse_string("hello")


def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]


print(reverse("always"))
