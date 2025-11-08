def number_of_words(text):
  words = text.split()
  return len(words)

def number_of_characters(text):
  characters = {}
  for char in text:
    if char.lower() in characters:
      characters[char.lower()] += 1
    else:
      characters[char.lower()] = 1
  return characters

def filter_alpha(list):
  alpha_only = []
  for item in list:
    if item['name'].isalpha() == True:
      alpha_only.append(item)
  return alpha_only

def print_chars(chars):
  for char in chars:
    print(f"{char['name']}: {char['num']}")

def character_count_sorted(text):
  sorted_list = []

  def sort_on(items):
    return items["num"]

  chars_with_count = number_of_characters(text)

  for char in chars_with_count:
    sorted_list.append({"name": char, "num": chars_with_count[char]})

  sorted_list.sort(reverse=True, key=sort_on)

  return filter_alpha(sorted_list)
