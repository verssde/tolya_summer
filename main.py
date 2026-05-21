import sys
from modules.text_processor import (
    read_text,
    clean,
    get_words,
    count_words,
    top_words,
    ttr,
    find_bigrams,
    average_word_length,
    split_sentences,
    analyze_sentences,
)


def main():
    print("=" * 50)
    print("     ЛИНГВИСТИЧЕСКИЙ АНАЛИЗАТОР ТЕКСТА")
    print("=" * 50)

    # ВВОД ТЕКСТА (только один раз)
    raw_text = read_text()

    if not raw_text.strip():
        print("\n Ошибка: введён пустой текст. Завершение работы.")
        sys.exit(1)

    # АНАЛИЗ ТЕКСТА
    cleaned_text = clean(raw_text)
    words = get_words(cleaned_text)
    word_freq = count_words(words)

    # ВЫВОД РЕЗУЛЬТАТОВ
    print("\n" + "=" * 50)
    print(" РЕЗУЛЬТАТЫ АНАЛИЗА")
    print("=" * 50)

    print("\n10 самых частых слов:")
    for i, (word, freq) in enumerate(top_words(word_freq), 1):
        print(f"   {i}. {word} - {freq}")

    print(f"\n Индекс разнообразия TTR: {ttr(words, word_freq):.4f}")

    bigrams = find_bigrams(words)
    if bigrams:
        print(f"\n Найденные коллокации (биграммы >2 раз):")
        for bigram, count in bigrams[:20]:
            print(f'   "{bigram}": {count} раз')
    else:
        print(f"\n Найденные коллокации (биграммы >2 раз): []")

    avg_word_len = average_word_length(words)
    print(f"\n Средняя длина слова: {avg_word_len:.2f} символов")

    sentences = split_sentences(raw_text)
    if sentences:
        avg_sent_len, longest_sentence, max_len = analyze_sentences(sentences)
        print(f" Средняя длина предложения: {avg_sent_len:.2f} слов")
        print(
            f" Самое длинное предложение: {longest_sentence[:100]}... ({max_len} слов)"
            if len(longest_sentence) > 100
            else f" Самое длинное предложение: {longest_sentence} ({max_len} слов)"
        )
    else:
        print(f" Средняя длина предложения: 0.00")
        print(f" Самое длинное предложение:  (0 слов)")

    print("\n" + "=" * 50)
    print(" Анализ завершён успешно!")
    print("=" * 50)


if __name__ == "__main__":
    main()