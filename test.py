parts_of_speech = {
    "adverbs": ['seldom', 'nicely', 'rudely', 'loudly', 'differently', 'quickly', 'Meanwhile', 'actually', 'instead', 'happily', 'quietly', 'Suddenly', 'rarely', 'generally', 'loudly', 'finally', 'accidentally', 'now', 'Once', 'softly', 'how'],
    "determiners": ['the', 'The', 'a', 'an', 'A', 'An', 'this', 'This', 'that', 'That', 'these', 'These'],
    "nouns": ['turtle', 'fox', 'horse', 'kangaroo', 'Samantha', 'Bob', 'Manhattan', 'birds', 'chess', 'rabbits', 'sea', 'stand', 'lamb', 'watermelon', 'mountains', 'ants', 'crab', 'song', 'elephant', 'mouse', 'apple', 'house', 'winner', 'tea', 'blew', 'karate', 'rooftop', 'map', 'penguin', 'crocodile', 'letter', 'car', 'rocks', 'snow', 'field', 'village', 'kangaroo', 'zebra', 'turtles', 'chickens', 'cars', 'Back', 'squirrel', 'clever', 'tiger', 'cupcakes', 'contest', 'mountain', 'fedora', 'race', 'flamingo', 'giraffe', 'leg', 'cows', 'cup', 'orchestra', 'tree', 'pancakes', 'bees', 'crumbs', 'dog', 'magician', 'parade', 'unicorns', 'talent', 'wise', 'cheetah', 'tomorrow', 'fox', 'cookbook', 'goat', 'fruit', 'pillow', 'everyone', 'poems', 'stars', 'skyscraper', 'octopus', 'sloth', 'colors', 'meadow', 'world', 'library', 'panda', 'marshmallows', 'elephants', 'top', 'banana', 'pizza', 'monkey', 'cheese', 'moon', 'sunset', 'lion', 'hippo', 'bakery', 'brighter', 'group', 'chocolate', 'show', 'pink', 'moves', 'brave', 'forest', 'sleepy', 'eagle', 'balloon', 'time', 'owl', 'butterfly', 'book', 'rock', 'clouds', 'coconut', 'bamboo', 'ice', 'shade', 'marathon', 'breeze', 'sun', 'speedy', 'sky', 'drops', 'debate', 'brown', 'guitar', 'cream', 'bars', 'parrot', 'Nearby', 'roll', 'president', 'river', 'city', 'cat', 'fence', 'robot', 'jumping', 'cones', 'sunflowers', 'case', 'disappear', 'cloud'],
    "adjectives": ['cold', 'energetic', 'upcoming', 'rainbow-colored', 'curious', 'same', 'joyful', 'sleepy', 'lemon', 'fish', 'mischievous', 'detective', 'stylish', 'tired', 'nervous', 'adventurous', 'yellow', 'gigantic', 'giant', 'polite', 'annual', 'purple', 'ninja', 'tiny', 'lazy', 'fluffy', 'tallest', 'thoughtful', 'studious', 'sheep', 'distant', 'little', 'quick', 'full', 'golden', 'rusty', 'cool', 'next', 'cheese', 'bus', 'blue', 'happy', 'serious', 'nearby', 'bright', 'legendary', 'old', 'hot', 'new', 'fresh', 'stale', 'fast', 'slow', 'tall', 'short', 'bright', 'dark'],
    "verbs": ['flew', 'danced', 'ended', 'painted', 'deliver', 'please', 'began', 'talking', 'parked', 'holding', 'held', 'made', 'dreaming', 'stolen', 'floated', 'shine', 'climbed', 'sing', 'using', 'drew', 'offered', 'investigated', 'buzzing', 'look', 'practiced', 'learning', 'blew', 'smiling', 'wearing', 'singing', 'rolled', 'chase', 'tried', 'make', 'bake', 'asking', 'dancing', 'was', 'listening', 'fell', 'built', 'stole', 'studied', 'bounced', 'sat', 'blooming', 'juggle', 'stretched', 'turned', 'wrote', 'sang', 'worried', 'played', 'swimming', 'landed', 'jumped', 'drove', 'fly', 'reading', 'flying', 'were', 'having', 'yawned', 'watching', 'cried', 'roared'],
    "pronouns": ['their', 'who', 'it', 'we', 'you', 'us', 'he', 'she', 'they', 'them']
}

paragraph = "Once upon a time, the lazy dog sat on a bright blue tree while dreaming about swimming in the city. The quick brown fox danced happily around the old rusty car parked next to the jumping cows. Suddenly, a cold breeze blew through the forest, and a giant talking apple began to sing loudly. The sleepy cat tried to chase a butterfly but ended up reading a book instead. Across the river, the curious penguin wrote poems about flying cars and purple clouds. The lazy squirrel built a tiny house out of ice cream cones and chocolate bars. Meanwhile, in the distant mountains, a group of ninja turtles practiced their karate moves in the snow. Back in the city, the brave giraffe drove a bus full of singing rabbits and dancing elephants. On the rooftop, a tired magician tried to make the moon disappear but accidentally turned it into a giant pizza. The wise owl sat quietly on the fence, watching a parade of rainbow-colored unicorns fly by. Nearby, the energetic kangaroo bounced happily over a field of blooming sunflowers. In the sky, a happy cloud painted the sunset with bright pink and yellow colors. Under the sea, the fish played chess with the crab while the octopus played the guitar. The mischievous monkey stole a watermelon from the fruit stand and offered it to the smiling tiger. At the library, the studious turtle was reading a cookbook about how to make pancakes out of stars. At the same time, a robot was learning how to bake cupcakes for the annual bakery contest. The sleepy sloth yawned and rolled over, dreaming of a race with the speedy cheetah. Over in the meadow, the sheep held a talent show, and the winner was a lamb who could juggle three rocks. The joyful flamingo danced on one leg while the parrot sang a rock 'n' roll song from the top of the coconut tree. Suddenly, a gigantic banana fell from the sky and landed softly on a pillow made of marshmallows. In the nearby village, the chickens were having a serious debate about whether the sun was actually made of lemon drops. The detective panda investigated a case of stolen bamboo while wearing a stylish fedora. The polite crocodile offered a cup of tea to the nervous zebra who was worried about the upcoming zebra marat."

import random

words = paragraph.replace(",","").replace(".","").split()
#print(word)

nouns = set(parts_of_speech['nouns'])
pronouns = set(parts_of_speech['pronouns'])
verbs = set(parts_of_speech['verbs'])
adverbs = set(parts_of_speech['adverbs'])
adjectives = set(parts_of_speech['adjectives'])
determiners = set(parts_of_speech['determiners'])

for word in words:
    if word in nouns:
        nouns.add(word)
    elif word in pronouns:
        pronouns.add(word)
    elif word in verbs:
        verbs.add(word)
    elif word in adverbs:
        adverbs.add(word)
    elif word in adjectives:
        adjectives.add(word)
    elif word in determiners:
        determiners.add(word)
    else :
        print("unknown word %s"%(word))
        

print("nouns:", nouns)
print("prounous:", pronouns)
print("verbs:", verbs)
print("adverbs:", adverbs)
print("abjectives:", adjectives)
print("determiners:", determiners)

if determiners and adjectives and nouns and verbs and adverbs:
    sentence = f"{random.choice(list(determiners))} {random.choice(list(adjectives))} {random.choice(list(nouns))} {random.choice(list(verbs))} {random.choice(list(adverbs))}."
    print("sentence:", sentence)
else:
    print("disability")
