Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.

Numeronym: internationalization -> i18n
accessibility -> a11y

word, [list_of_words]
if numeronym(word) not in numeronyms of list_of_words, return numeronym(word)
word = car 
list_of_word =[apple, water, lime]

word = bar -> b1r
list_of_words = [foo, bat, bur] -> [f1o, b1t, b1r]
return = “”

def simple_num (string):
	temp_len = len(string)
	#temp_len = 20
	fir_chr = string[0]
	#fir_chr = i
	last_chr = string[temp_len -1] 
	#last_chr = n
	return(fir_chr+str(len-2)+last_chr)

def simple_num_2(word, list_of_word):
	my_temp_dic = {}
	for item in list_of_word:
		if item is not in my_temp_dic:
			my_temp_dic[item] = simple_num(item)
		else:
			continue
	
	if word in my_temp_dic:
		return(“”)
	else:
		temp_word = simple_num(word)
		for key, value in item(my_temp_dic):
if temp_word == value:
	return(“”)
return(temp_word)

Woogie
