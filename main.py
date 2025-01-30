with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
count = len(words)

char_count = {}
lowered_contents = file_contents.lower()

for char in lowered_contents:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

highlow = {
    key: val
    for key, val in sorted(char_count.items(), key=lambda ele: ele[1], reverse=True)
}

filtered = []
for i in highlow:
    if i.isalpha():
        filtered.append({i: highlow[i]})


if __name__ == "__main__":
    print("--- Begin Report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print("")
    for i in filtered:
        for key, val in i.items():
            print(f"The '{key}' character was found {val} times")
    print("--- End Report ---")
