# python3

def read_input():
    input_type = input()
    if 'I' in input_type:
        pattern = input().rstrip()
        text = input().rstrip()
    elif 'F' in input_type:
        filename = "06"
        with open("tests/" + filename, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text

def print_occurrences(positions):
    print(' '.join(map(str, positions)))

def get_occurrences(pattern, text):
    pattern_hash = hash(pattern)
    text_hash = hash(text[:len(pattern)])
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            positions.append(i)
        if i < len(text) - len(pattern):
            text_hash = hash(text[i+1:i+len(pattern)+1])
    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))