import re
import random


def main():
    print("Diega Vu: I'm feeling a sense of Déjà vu, can YOU feel it too?")
    you_say = what_do_you_say()
    while you_say:
        vu_says = what_does_vu_say(you_say)
        print("Diega Vu: " + vu_says)
        you_say = what_do_you_say()
    print("Diega Vu: Oh... Now the feeling has gone... And you, too?")

def what_do_you_say():
    try:
        return input("Says you: ")
    except EOFError:
        print("")
        return "" # signals end of conversation
def what_does_vu_say(you_say):
    quotes = segment(transform(you_say.strip()))
    vu_says = start()+" "+", and ".join(map(prep, quotes))+" "+end()
    return vu_says


SUBSTITUTION_PAIRS = [
        ("myself", "yourself"),      ("mine", "yours"),     ("my", "your"),
        ("i'm", "you're"),           ("i am", "you are"),   ("am i", "are you"),
        ("i was", "you were"),       ("was i", "were you"),
        ("i wasn't", "you weren't"), ("wasn't i", "weren't you"),
        ("i", "you"), ("me", "you"), # <-- double-up! prefer you --> i (-/> me)
    ]
SUBSTITUTIONS = []
for _1st_person, _2nd_person in SUBSTITUTION_PAIRS:
    for find, repl in [(_1st_person, _2nd_person), (_2nd_person, _1st_person)]:
        SUBSTITUTIONS.append(
            # look for word(s) matching the pattern in `find`
            # (surround with r"\b" and replace whitespace with r"\s+")
            ( re.compile(r"\b" + re.sub(r"\s+", r"\\s+", find) + r"\b")
            # replace them with the target word `repl`
            # (uppercased to prevent repeated replacement)
            , repl.upper()
            )
        )
def transform(reply):
    """
    Replace I, me, my, mine, myself, you, yours, your, yourself, i'm, i am,
    i was, you're, you are, you were, etc. then others like i've and you've, 
    i'll, you'll, etc. should be caught somewhere within that.
    """
    reply = reply.lower()
    for find, replace in SUBSTITUTIONS:
        reply = find.sub(replace, reply)
    reply = reply.upper()
    return reply

def segment(reply):
    """naive sentence segmentation on ., !, ?."""
    sentences = reply.replace(". ", ".|") \
                     .replace("! ", ".|") \
                     .replace("? ", "?|") \
                     .split('|')
    return sentences

def prep(quote):
    """naive sentence type detection (handles ?, !, ., and none)."""
    if quote.endswith('?'):
        return "asking " + quote.rstrip('.?!')
    else:
        return "saying " + quote.rstrip('.?!')

def start():
    part1 = random.choice([
        "Oh!",
        "Ah!",
        "Hey!",
        "Wow!",
        "Wow...",
        "This is crazy!",
        "No way!",
        "No way..."
        "Ooh!",
        "Ooh..."])
    part2 = random.choice([
        "I remember, last time, you were",
        "I remember this! You were",
        "It was just like this last time! You were",
        "Just like last time... You were"])
    return f"{part1} {part2}"
def end():
    return random.choice([
        "too!",
        "then, too!",
        "back then, too!"])


if __name__ == '__main__':
    main()
