from function import amount_of_sentences, \
    amount_of_non_declarative_sentences, \
    average_length_of_sentences, \
    average_word_length, \
    top_k_repeated_n_grams

str_ = input("Enter text: ")

script1 = amount_of_sentences(str_)
script2 = amount_of_non_declarative_sentences(str_)
script3 = average_length_of_sentences(str_)
script4 = average_word_length(str_)
script5 = top_k_repeated_n_grams(str_)

print("Amount of sentences: ", script1,
      "\nAmount od non-declarative sentences: ", script2,
      "\nAverage length of the sentences in characters: ", script3,
      "\nAverage length of the world in the text in characters: ", script4,
      "\nTop-K repeated N-grams in the text (K=10, N=4): ", script5)
