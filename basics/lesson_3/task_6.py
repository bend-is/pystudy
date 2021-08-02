"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def capitalize_word(word: str) -> str:
    """Capitalize word

    :param word: Any word
    :type word: str
    :return: Capitalized word
    :rtype: str
    """

    return word.lower().capitalize()


def capitalize_text(sentence: str) -> str:
    """Capitalize all words in sentence

    :param sentence: Any sentence
    :type sentence: str
    :return: Sentence with capitalized words
    :rtype: str
    """

    return " ".join(map(capitalize_word, sentence.split()))


if __name__ == '__main__':
    print(capitalize_text(input("Enter a word or a text to capitalize: ")))
