from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word_python = "Python"
    word_java = "java"

    count_python = count_ocurrences(path, word_python)
    count_java = count_ocurrences(path, word_java)

    assert count_python == 1639
    assert count_java == 676
