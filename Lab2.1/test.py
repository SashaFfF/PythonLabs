import unittest
import function


class TestCountSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = function.amount_of_sentences('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = 3
        actual = function.amount_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Abbreviations test: number of sentences not ' + str(expected))

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        expected = 3
        actual = function.amount_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Sample text test: number of sentences not ' + str(expected))


class TestCountNonDeclarativeSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = function.amount_of_non_declarative_sentences('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = 1
        actual = function.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
                         'Abbreviations test: number of non decl. sentences not' + str(expected))

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        expected = 1
        actual = function.amount_of_non_declarative_sentences(text)
        self.assertEqual(actual, expected,
                         'Sample text test: number of non decl. sentences not ' + str(expected))


class TestGetAverageSentenceLength(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = function.average_length_of_sentences('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = round(47 / 3, 2)
        actual = function.average_length_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_numbers(self):
        text = 'Oh!!! 4 Heloo aaaa. asd6laa, 777; word?'
        expected = round(22 / 3, 2)
        actual = function.average_length_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Average len with numbers test: result isn\'t ' + str(expected))


class TestAvgWordLength(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = function.average_word_length('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - its greate text!!'
        expected = round(47 / 14, 2)
        actual = function.average_word_length(text)
        self.assertEqual(actual, expected,
                         'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_numbers(self):
        text = 'Oh!!! 4 Heloo aaaa. asd6laa, 777; word?'
        expected = round(22 / 5, 2)
        actual = function.average_word_length(text)
        self.assertEqual(actual, expected,
                         'Average len with numbers test: result isn\'t ' + str(expected))


class TestGetTopKRepeatedNgram(unittest.TestCase):
    def test_empty_text(self):
        expected = []
        actual = function.top_k_repeated_n_grams('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_text_without_repeated_anagrams(self):
        text = 'It is without words which can repeat'
        expected = [('it is without', 1), ('is without words', 1), ('without words which', 1)]
        actual = function.top_k_repeated_n_grams(text, 3, 3)
        self.assertListEqual(actual, expected,
                             'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_repeated_sequence(self):
        text = 'aaa bbb ccc aaa bbb ccc aaa bbb ccc'
        expected = [('aaa bbb ccc', 3), ('bbb ccc aaa', 2), ('ccc aaa bbb', 2)]
        actual = function.top_k_repeated_n_grams(text, 3, 3)
        self.assertListEqual(actual, expected,
                             'Average len with numbers test: result isn\'t ' + str(expected))


if __name__ == '__main__':
    unittest.main()
