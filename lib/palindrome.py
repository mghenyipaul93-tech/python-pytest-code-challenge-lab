def longest_palindromic_substring(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if s == "":
        return ""

    start = 0
    end = 0
    n = len(s)

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(n):
        # Odd palindrome
        l1, r1 = expand_around_center(i, i)
        # Even palindrome
        l2, r2 = expand_around_center(i, i + 1)

        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]