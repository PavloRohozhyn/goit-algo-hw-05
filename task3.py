import timeit

# Читаємо статтю
def get_article(file_name):
    article = open(file_name, "r")
    return article.read()

# Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    def build_prefix_function(pattern):
        m = len(pattern)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    lps = build_prefix_function(pattern)
    i = j = 0
    n, m = len(text), len(pattern)
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Боєра-Мура (BM)
def bm_search(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    bad_char_table = bad_character_table(pattern)
    s = 0  # зміщення для тексту
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            char_shift = bad_char_table.get(text[s + j], -1)
            s += max(1, j - char_shift)
    return -1

# Рабіна-Карпа (RK)
def rk_search(text, pattern, prime=101):
    n, m = len(text), len(pattern)
    hpattern = sum(ord(pattern[i]) * pow(256, m - i - 1, prime) for i in range(m)) % prime
    htext = sum(ord(text[i]) * pow(256, m - i - 1, prime) for i in range(m)) % prime
    h = pow(256, m - 1, prime)
    
    for i in range(n - m + 1):
        if htext == hpattern:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            htext = (htext - ord(text[i]) * h) * 256 + ord(text[i + m])
            htext %= prime
    return -1

# Статті
article_one = get_article('task3_article_one.txt')
article_two = get_article('task3_article_one.txt')
# 
existing_str_in_article_one = "опг"
non_existing_str_in_article_one = "aaaa"
#
existing_substr_in_article_two = "варіа"
non_existing_substr_in_article_two = "aaaa"

# Для 10
print('Numbers: 10')
results = []
results.append(('Article One (existing substring):',
    timeit.timeit(lambda: kmp_search(article_one, existing_str_in_article_one), number=10),
    timeit.timeit(lambda: bm_search(article_one, existing_str_in_article_one), number=10), 
    timeit.timeit(lambda: rk_search(article_one, existing_str_in_article_one), number=10)))
results.append(("Article Two (existing substring):", 
    timeit.timeit(lambda: kmp_search(article_two, existing_substr_in_article_two), number=10),
    timeit.timeit(lambda: bm_search(article_two, existing_substr_in_article_two), number=10),
    timeit.timeit(lambda: rk_search(article_two, existing_substr_in_article_two), number=10)))
results.append(("Article One (non-existing substring):",
    timeit.timeit(lambda: kmp_search(article_one, non_existing_str_in_article_one), number=10),
    timeit.timeit(lambda: bm_search(article_one, non_existing_str_in_article_one), number=10),
    timeit.timeit(lambda: rk_search(article_one, non_existing_str_in_article_one), number=10)))
results.append(("Article Two (non-existing substring):",
    timeit.timeit(lambda: kmp_search(article_two, non_existing_str_in_article_one), number=10),
    timeit.timeit(lambda: bm_search(article_two, non_existing_str_in_article_one), number=10),
    timeit.timeit(lambda: rk_search(article_two , non_existing_str_in_article_one), number=10)))
print(f"{'Case: ':<40}{'Knuth Morris Pratt: ':<23}{'Boyer Moore: ':<15}{'Rabin Karp: ':<15}")
for case, kmp, bm, rk in results:
    print(f"{case:<40}{kmp:<23.6f}{bm:<15.6f}{rk:<15.6f}")


# Для 100
print('Numbers: 100')
results = []
results.append(('Article One (existing substring):',
    timeit.timeit(lambda: kmp_search(article_one, existing_str_in_article_one), number=100),
    timeit.timeit(lambda: bm_search(article_one, existing_str_in_article_one), number=100), 
    timeit.timeit(lambda: rk_search(article_one, existing_str_in_article_one), number=100)))
results.append(("Article Two (existing substring):", 
    timeit.timeit(lambda: kmp_search(article_two, existing_substr_in_article_two), number=100),
    timeit.timeit(lambda: bm_search(article_two, existing_substr_in_article_two), number=100),
    timeit.timeit(lambda: rk_search(article_two, existing_substr_in_article_two), number=100)))
results.append(("Article One (non-existing substring):",
    timeit.timeit(lambda: kmp_search(article_one, non_existing_str_in_article_one), number=100),
    timeit.timeit(lambda: bm_search(article_one, non_existing_str_in_article_one), number=100),
    timeit.timeit(lambda: rk_search(article_one, non_existing_str_in_article_one), number=100)))
results.append(("Article Two (non-existing substring):",
    timeit.timeit(lambda: kmp_search(article_two, non_existing_str_in_article_one), number=100),
    timeit.timeit(lambda: bm_search(article_two, non_existing_str_in_article_one), number=100),
    timeit.timeit(lambda: rk_search(article_two , non_existing_str_in_article_one), number=100)))
print(f"{'Case: ':<40}{'Knuth Morris Pratt: ':<23}{'Boyer Moore: ':<15}{'Rabin Karp: ':<15}")
for case, kmp, bm, rk in results:
    print(f"{case:<40}{kmp:<23.6f}{bm:<15.6f}{rk:<15.6f}")


# Для 1000
print('Numbers: 1000')
results = []
results.append(('Article One (existing substring):',
    timeit.timeit(lambda: kmp_search(article_one, existing_str_in_article_one), number=1000),
    timeit.timeit(lambda: bm_search(article_one, existing_str_in_article_one), number=1000), 
    timeit.timeit(lambda: rk_search(article_one, existing_str_in_article_one), number=1000)))
results.append(("Article Two (existing substring):", 
    timeit.timeit(lambda: kmp_search(article_two, existing_substr_in_article_two), number=1000),
    timeit.timeit(lambda: bm_search(article_two, existing_substr_in_article_two), number=1000),
    timeit.timeit(lambda: rk_search(article_two, existing_substr_in_article_two), number=1000)))
results.append(("Article One (non-existing substring):",
    timeit.timeit(lambda: kmp_search(article_one, non_existing_str_in_article_one), number=1000),
    timeit.timeit(lambda: bm_search(article_one, non_existing_str_in_article_one), number=1000),
    timeit.timeit(lambda: rk_search(article_one, non_existing_str_in_article_one), number=1000)))
results.append(("Article Two (non-existing substring):",
    timeit.timeit(lambda: kmp_search(article_two, non_existing_str_in_article_one), number=1000),
    timeit.timeit(lambda: bm_search(article_two, non_existing_str_in_article_one), number=1000),
    timeit.timeit(lambda: rk_search(article_two , non_existing_str_in_article_one), number=1000)))
print(f"{'Case: ':<40}{'Knuth Morris Pratt: ':<23}{'Boyer Moore: ':<15}{'Rabin Karp: ':<15}")
for case, kmp, bm, rk in results:
    print(f"{case:<40}{kmp:<23.6f}{bm:<15.6f}{rk:<15.6f}")