def main():
    path_to_file = "books/frankenstein.txt"
    char_list = set()
    char_count_dict = {}

    print(f"--- Begin report of {path_to_file} ---")
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"{word_count} words found in the document\n")


        file_contents_lower = file_contents.lower()
        for char in file_contents_lower:
            if char.isalpha():  # Only consider alphabetic characters
                char_count_dict[char] = char_count_dict.get(char, 0) + 1

    char_count_sorted = {}
    char_count_sorted = sorted(char_count_dict.items(), key=lambda a:a[1], reverse=True)
    
    for key, value in char_count_sorted:
        print(f"The {key} character was found {value} times")
        
    print("--- End report ---")

main()