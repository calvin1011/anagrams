def funWithAnagrams(strings):
    unique_strings = []
    seen_anagrams = set()

    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in seen_anagrams:
            unique_strings.append(s)
            seen_anagrams.add(sorted_s)

    return sorted(unique_strings)

if __name__ == '__main__':
    input_strings = ["code", "aagmnrs", "anagrams", "doce"]
    result = funWithAnagrams(input_strings)
    print([string for string in input_strings if string in result])  # Print selected elements in original order
    
    additional_strings = ["poke", "pkoe", "okpe", "ekop"]
    additional_result = funWithAnagrams(additional_strings)
    print([string for string in additional_strings if string in additional_result])  # Print selected elements in original order
