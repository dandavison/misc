# AABBAAFFF -> AABBAA
# AABBCCFFF -> CCFFF


def max_run(s: str):
    max_substr = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if len(set(substr)) <= 2 and j - i > len(max_substr):
                max_substr = substr
    return max_substr


print(max_run("AABBAAFFF"))
print(max_run("AABBCCFFF"))
