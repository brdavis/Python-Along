def pig_latin_translator():
	original_word = raw_input("Enter a word to be translated into pig latin: ")
	if len(original_word) > 0 and original_word.isalpha():
		#translate
		original_word.lower()
		first_letter = original_word[0]
		remainder_of_word = original_word[1:len(original_word)]
		pig_latin_suffix = "ay"
		pig_latin_translation = remainder_of_word + first_letter + pig_latin_suffix
		#print resulti
		print original_word + " in pig latin is: " + pig_latin_translation
	else:
		print "Invalid input: Please try again"
		pig_latin_translator()

pig_latin_translator()
