import re

def check_character(string):
    rule = re.compile(r'\W')
    string = rule.search(string)
    return not bool(string)

print(check_character("ksfjksjfosfiejfijefaefsdsdSDSD1423"))
print(check_character("sjkjskjfkjsf#"))
#[^a-zA-Z0-9]