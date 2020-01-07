# Given a string and a list of words, find all the starting indices of
# substrings in the given string that are a concatenation of all the given
# words exactly once without any overlapping of words. It is given that all
# words are of the same length.


def find_word_concatenation(s, words):
    words_dict = {}
    for w in words:
        if w not in words_dict:
            words_dict[w] = 0
        words_dict[w] += 1

    origin_dict = words_dict.copy()

    word_len = len(words[0])
    start, end = 0, 0
    count = 0
    res = []
    while end < len(s):
        curr = s[end: end + word_len]
        if curr not in words_dict:
            end += 1
            start = end
            count = 0
            words_dict = origin_dict.copy()
            continue
        words_dict[curr] -= 1
        if words_dict[curr] == 0:
            count += 1
            if count == len(words_dict):
                res.append(start)
                words_dict[s[start: start + word_len]] += 1
                count -= 1
                start += word_len
        elif words_dict[curr] < 0:
            while start < end and s[start: start + word_len] != curr:
                words_dict[s[start: start + word_len]] += 1
                if words_dict[s[start: start + word_len]] == 1:
                    count -= 1
                start += word_len
            words_dict[curr] += 1
            start += word_len
        end += word_len
    return res


if __name__ == "__main__":
    print(find_word_concatenation("cabbcatjfoxcatfoxcat", ["cat", "fox", "cat"]))
    print(find_word_concatenation("catcatfoxcatfoxcatfox", ["cat", "fox", "fox"]))
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
