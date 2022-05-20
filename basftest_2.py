#basftest_2.py

# function
def exercise_2(input_string, verbose=False):
    print("input string: ",input_string)
    L = len(input_string)
    rgb_equal_representations = 0
    for segment_len in range(3, L + 1):
        for start_letter in range(0, L - (segment_len - 1)):
            search_str = input_string[start_letter : start_letter + segment_len]
            if search_str.count("R") == search_str.count("G") == search_str.count("B"):
                rgb_equal_representations = rgb_equal_representations + 1
                if verbose:
                    print(f"Substring: {search_str}  \t Found match")
            else:
                if verbose:
                    print(f"Substring: {search_str}")
    print("output: ",rgb_equal_representations)
    return rgb_equal_representations

exercise_2("RRBBGG", verbose=False)
exercise_2("RRBBG", verbose=False)
exercise_2("RBGGBR", verbose=False)
exercise_2("RBGRBG", verbose=False)
exercise_2("RRBBGG", verbose=False)