"""
------------------------------------------------------------------------------------------------------------------
                                            Семинар 4. Задача 27.
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущихподряд, слова 
разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом  тексте.
------------------------------------------------------------------------------------------------------------------
"""
input = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
lst = input.lower().split()
print(len(set(lst)))