#basftest_1.py

A = "JJJJJJJABCDUIBAZDBSIAHFB"
B = "ABCD"
C = "QIDBCZDBKABCD"

result = ""
print("Substring matches in all sequences: ")
for segment_len in range(2, len(A)):
    for start_letter in range(0, len(A) - (segment_len - 1)):
        search_str = A[start_letter : start_letter + segment_len]
        if (search_str in B) and (search_str in C):
            print(f"Substring: {search_str} \t Length: {len(search_str)}")
            result = search_str

print(f"(One of the) Longest length strings: {result}")

# function
def exercise_1(string_1, string_2, string_3, verbose=False):
    result = ""
    if verbose:
        print("Substring matches in all sequences: ")
    for segment_len in range(2, len(A)):
        for start_letter in range(0, len(A) - (segment_len - 1)):
            search_str = A[start_letter : start_letter + segment_len]
            if (search_str in B) and (search_str in C):
                if verbose:
                    print(f"Substring: {search_str} \t Length: {len(search_str)}")
                result = search_str

    return result

exercise_1(A, B, C, verbose=False)