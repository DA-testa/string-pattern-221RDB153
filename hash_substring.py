# python3

def read_input():
    input_choice, pattern, text = input().rstrip().split()
    if input_choice.upper() == 'F':
        with open(pattern) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(*output)

def get_occurrences(pattern, text):
    occurrences = []
    if len(pattern) > len(text):
        return occurrences
    pattern_hash = hash(pattern)
    text_hash = hash(text[:len(pattern)])
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash == text_hash:
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = hash(text[i+1:i+len(pattern)+1])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))