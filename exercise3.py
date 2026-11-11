def average(numbers):
    """Average of a list. An empty list has average 0"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    words = text.split()
    if len(words) == 0:
        return ""
    return words[0]


def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    if total == 0:
        return 0
    return part / total * 100