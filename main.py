# Random word
import random

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
following_letters = {
    "a": consonants,
    "b": vowels + ["l", "r"],
    "c": vowels + ["h", "l", "r", "k"],
    "d": vowels + ["r"],
    "e": consonants + ["e"],
    "f": vowels + ["l", "r"],
    "g": vowels + ["h", "l", "r"],
    "h": vowels,
    "i": consonants,
    "j": vowels,
    "k": vowels,
    "l": vowels + ["l", "d", "f", "k", "m", "n", "p", "s", "t", "y"],
    "m": vowels + ["m", "b", "p"],
    "n": vowels + ["n", "c", "d", "g", "k", "s", "t"],
    "o": consonants + ["o"],
    "p": vowels + ["h", "l", "r"],
    "q": ["u"],
    "r": vowels + ["r", "b", "c", "d", "f", "g", "k", "l", "m", "n", "p", "s", "t", "v", "w", "y"],
    "s": vowels + ["s", "c", "h", "k", "l", "m", "n", "p", "t", "w"],
    "t": vowels + ["h", "r"],
    "u": consonants,
    "v": vowels,
    "w": vowels + ["h"],
    "x": vowels + ["c", "p", "t"],
    "y": vowels,
    "z": vowels
}

real_words = ["graze"]
almost_real_words = ["prefin", "frammola", "qudiz", "genuho", "cuxilsaw", "diwompic", "oxtone", "prizode", "metables",
                     "mersager", "fobuxcer", "julpuking", "boblanka", "pabloofed", "melmamug", "solnomesion", "nasca",
                     "ponific", "blackobu", "vabate"]

def random_letter():
  if random.randint(0, 5) == 0:
    return random.choice(vowels)
  else:
    return random.choice(consonants)

def generate_ending(last_letter):
  consonant_endings = ["ing", "ion", "ed", "es", "er", "sion", "e", "", "", ""]
  vowel_endings = ["s", "tion", "sion", "r", "", "", ""]
  if last_letter in consonants:
    return random.choice(consonant_endings)
  else:
    return random.choice(vowel_endings)

def generate_random_word(starting_letter = "random"):
  word = ""
  if starting_letter == "random":
    word = random_letter()
  else:
    if starting_letter.isalpha():
      word = starting_letter.lower()
    else:
      word = random_letter()
  while word[0] == "x":
    word = random_letter()

  while len(word) < 8:
    possible_upcomings = following_letters[word[-1]]
    letter = random.choice(possible_upcomings)

    # Refined the condition to avoid IndexError when len(word) < 2
    if len(word) >= 2:
      while True:
        if word[-1] == letter and word[-2] == letter:
          letter = random.choice(possible_upcomings)
        elif word[-1] in consonants and word[-2] in consonants and letter in consonants:
          letter = random.choice(possible_upcomings)
        elif word[-1] in vowels and word[-2] in vowels and letter in vowels:
          letter = random.choice(possible_upcomings)
        else:
          break

    word += letter


    if len(word) > 4:
      if random.randint(0, 10 - len(word)) == 0:
        word += generate_ending(word[-1])
        break
  return word

for i in range(0, 10):
  print(generate_random_word())
print("")
