# 🌍📝 Transliteration is the transmission of signs of one writing system
# with the signs of another writing system, where each sign (or sequence of signs)
# of one writing system is transmitted by the corresponding sign (or sequence of signs)
# of another writing system.

# Define transliteration dictionary for lowercase and uppercase Cyrillic letters

# Test _________________________________________________________________
transliteration = {
    'а': 'a', 'А': 'A',
    'б': 'b', 'Б': 'B',
    'в': 'v', 'В': 'V',
    'г': 'g', 'Г': 'G',
    'д': 'd', 'Д': 'D',
    'е': 'e', 'Е': 'E',
    'ё': 'jo', 'Ё': 'Jo',
    'ж': 'zh', 'Ж': 'Zh',
    'з': 'z', 'З': 'Z',
    'и': 'i', 'И': 'I',
    'й': 'j', 'Й': 'J',
    'к': 'k', 'К': 'K',
    'л': 'l', 'Л': 'L',
    'м': 'm', 'М': 'M',
    'н': 'n', 'Н': 'N',
    'о': 'o', 'О': 'O',
    'п': 'p', 'П': 'P',
    'р': 'r', 'Р': 'R',
    'с': 's', 'С': 'S',
    'т': 't', 'Т': 'T',
    'у': 'u', 'У': 'U',
    'ф': 'f', 'Ф': 'F',
    'х': 'h', 'Х': 'H',
    'ц': 'c', 'Ц': 'C',
    'ч': 'ch', 'Ч': 'Ch',
    'ш': 'sh', 'Ш': 'Sh',
    'щ': 'shh', 'Щ': 'Shh',
    'ъ': '*', 'Ъ': '*',
    'ы': 'y', 'Ы': 'Y',
    'ь': "'", 'Ь': "'",
    'э': 'je', 'Э': 'Je',
    'ю': 'ju', 'Ю': 'Ju',
    'я': 'ya', 'Я': 'Ya'
}

with (open("cyrillic.txt", "r", encoding="UTF-8") as file,
      open("transliteration.txt", "w", encoding="UTF-8") as new_file):
    for line in file:
        for s in transliteration:
            while s in line:
                inx = line.find(s)
                line = line[:inx] + transliteration[s] + line[inx + len(s):]

        new_file.write(line)
