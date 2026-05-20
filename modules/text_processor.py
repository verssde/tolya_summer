# ФУНКЦИЯ ДЛЯ ВВОДА МНОГОСРОЧНОГО ТЕКСТА
def read_text():

    text = ""

    print("Введите текст (пустая строка завершает ввод):")
    while True:
        line = input()

        if line == "":
            break

        text = text + line + "\n"

    return text


# ОЧИСТКА ТЕКСТА
def clean_text(text):

    text = text.lower()
    punctuation = '.,!?;:-()[]{}"'
    cleaned = ""

    for char in text:
        if char not in punctuation:
            cleaned = cleaned + char

    return cleaned


# РАЗДЕЛЕНИЕ НА СЛОВА
def get_words(text):

    words = text.split()
    return words


# ПОДСЧЕТ ЧАСТОТЫ СЛОВ
def count_words(words):

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count


# ТОП 10 СЛОВ
def top_words(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]


# ФУНКЦИЯ TTR
def calculate_ttr(words, word_count):
    return len(word_count) / len(words)


# ФУНКЦИЯ БИГРАММ
def find_bigrams(words):

    bigram_count = {}

    for i in range(len(words) - 1):
        bigram = words[i] + " " + words[i + 1]

        if bigram in bigram_count:
            bigram_count[bigram] += 1
        else:
            bigram_count[bigram] = 1

    result = []
    for bigram in bigram_count:
        if bigram_count[bigram] > 2:
            result.append((bigram, bigram_count[bigram]))

    return result


# ФУНКЦИЯ ДЛИНЫ СЛОВА
def average_word_length(words):

    total_length = 0

    for word in words:
        total_length += len(word)

    if len(words) == 0:
        return 0

    return total_length / len(words)


# РАЗБИЕНИЕ НА ПРЕДЛОЖЕНИЯ
def split_sentences(original_text):

    sentences = []
    current = ""

    for char in original_text:
        current += char

        if char in ".!?":
            sentence = current.strip()

            if sentence != "":
                sentences.append(sentence)

            current = ""

    return sentences


# СРЕДНЯЯ ДЛИНА ПРЕДЛОЖЕНИЯ И ПОИСК САМОГО ДЛИННОГО
def average_sentence_length(sentences):

    total_words = 0
    max_length_sentence = ""
    max_length = 0

    for sentence in sentences:

        cleaned = clean_text(sentence)
        words = get_words(cleaned)
        total_words += len(words)

        if len(words) > max_length:
            max_length = len(words)
            max_length_sentence = sentence

    if len(sentences) == 0:
        return 0

    return total_words / len(sentences), max_length_sentence, max_length
