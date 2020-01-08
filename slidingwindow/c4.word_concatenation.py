# Given a string and a list of words, find all the starting indices of
# substrings in the given string that are a concatenation of all the given
# words exactly once without any overlapping of words. It is given that all
# words are of the same length.


def find_word_concatenation(s, words):
    res = []
    if not words or not s:
        return res

    words_dict = {}
    for w in words:
        if w not in words_dict:
            words_dict[w] = 0
        words_dict[w] += 1

    word_len = len(words[0])
    words_len = len(words)
    window_len = word_len * words_len

    for i in range(word_len):
        freq = words_dict.copy()
        count = 0
        start, end = i, i
        # not traverse the whole list but m / l
        while end <= len(s) - word_len:
            curr = s[end: end + word_len]
            if curr in freq:
                freq[curr] -= 1
                if freq[curr] >= 0:
                    count += 1
                if count == words_len:
                    res.append(start)

            if end - start >= window_len - word_len:
                prev = s[start: start + word_len]
                if prev in freq:
                    freq[prev] += 1
                    if freq[prev] >= 1:
                        count -= 1
                start += word_len

            end += word_len

    return res


if __name__ == "__main__":
    print(find_word_concatenation("cabbcatjfoxcatfoxcat", ["cat", "fox", "cat"]))
    print(find_word_concatenation("catcatfoxcatfoxcatfox", ["cat", "fox", "fox"]))
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
