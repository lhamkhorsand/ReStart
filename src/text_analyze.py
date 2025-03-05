txt= ('The rapid advancement of technology has significantly changed the way we live,'
      ' work, and interact with the world around us.'
      ' From artificial intelligence to the internet of things,'
      ' these innovations are reshaping industries and driving global economies.'
      ' While some may fear the disruption caused by these advancements,'
      ' others see immense opportunities for growth and improvement.'
      ' Embracing technology with a mindful approach can lead to a future'
      ' where human potential is enhanced and new possibilities arise.'
      ' It is essential to strike a balance between innovation and ethical responsibility'
      ' to ensure that technology benefits society as a whole')


list_of_words = txt.split(' ')
print(f'Total number of words: {len(list_of_words)}')



list_of_unique_words = set(list_of_words)
print(f'Total number of unique words: {len(list_of_unique_words)}')


tobe= ['am', 'is', 'are', 'was', 'were']
total_tobe=0
for word in list_of_words:
    if word in tobe:
        total_tobe+=1
print(f'Total number of to be verbs: {total_tobe}')



tobe_dict = dict.fromkeys(tobe, 0)
for word in list_of_words:
    if word in tobe:
        tobe_dict[word]+=1
print(f'To be verbs frequency: {tobe_dict}')