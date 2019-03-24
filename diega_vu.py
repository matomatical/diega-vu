import re
import random

def main():
    print("Diega Vu: I'm feeling a sense of Deja vu, can YOU feel it too?")
    you_say = input("Says you: ")
    while you_say:
        quotes  = segment(transform(you_say.strip()))
        vu_says = pre()+" "+start()+" "+", and ".join(map(prep, quotes))+" "+end()
        print("Diega Vu: " + vu_says)
        you_say = input("Says you: ")
    print("Diega Vu: Oh... Now the feeling has gone... And you too?")

def prep(quote):
    """naive sentence type detection (handles ?, !, ., and none."""
    if quote.endswith('?'):
        return "asking " + quote.rstrip('.?!')
    else:
        return "saying " + quote.rstrip('.?!')

def pre():
    return random.choice([
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
def start():
    return random.choice([
        "I remember, last time, you were",
        "I remember this! You were",
        "It was just like this last time! You were",
        "Just like last time... You were"])
def end():
    return random.choice([
        "too!",
        "then, too!",
        "back then, too!"])

def segment(reply):
    """naive sentence segmentation on ., !, ?."""
    sentences = reply.replace(". ", ".|") \
                     .replace("! ", ".|") \
                     .replace("? ", "?|") \
                     .split('|')
    return sentences

def transform(reply):
    """
    TODO: replace I, me, my mine myself, you, yours your yourself,
    i'm, i am, i was, you're, you are, you were, etc.
    then others like i've and you've, i'll, you'll, etc. should be caught
    somewhere within that
    """
    #todo: consider word boundaries using re module
    reply = reply.lower()
    reply = re.sub(r"\bmyself\b", "YOURSELF", reply)
    reply = re.sub(r"\byourself\b", "MYSELF", reply)
    reply = re.sub(r"\bmine\b", "YOURS", reply)
    reply = re.sub(r"\byours\b", "MINE", reply)
    reply = re.sub(r"\bmy\b", "YOUR", reply)
    reply = re.sub(r"\byour\b", "MY", reply)
    reply = re.sub(r"\bi'm\b", "YOU'RE", reply)
    reply = re.sub(r"\bi am\b", "YOU ARE", reply)
    reply = re.sub(r"\bi was\b", "YOU WERE", reply)
    reply = re.sub(r"\byou're\b", "I'M", reply)
    reply = re.sub(r"\byou are\b", "I AM", reply)
    reply = re.sub(r"\byou were\b", "I WAS", reply)
    reply = re.sub(r"\bi\b", "YOU", reply)
    reply = re.sub(r"\bme\b", "YOU", reply)
    reply = re.sub(r"\byou\b", "I", reply) # or is it me?
    reply = reply.upper()
    return reply

if __name__ == '__main__':
    main()
