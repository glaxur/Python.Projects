"""silly sentences sent by using random words in a formatting template
Isaiah Santillan
7/25/18
"""
import random
# sample_list = [x for x in range(10)]
# random.choice(sample_list)

template = "%s %s the %s %s."
BASE_SENTENCE = "My python teacher wrote the python book."

persons = ["My python teacher", "My brother", "Foxy", "Isaiah"]
verbs = ["wrote", "licked", "hugged", "ate"]
adjectives = ["python", "funniest", "big", "small"]
nouns = ["book", "computer", "socks", "bed"]

# Main section

if __name__ == "__main__":
    person = random.choice(persons)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    format_values = (person, verb, adjective, noun)

    # print(BASE_SENTENCE)
    print(template%format_values)
   # print(BASE_SENTENCE == template%format_values)
    
