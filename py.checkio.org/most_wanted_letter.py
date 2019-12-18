import string

def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    print(text.count)
    return max(string.ascii_lowercase, key=string.count)

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))