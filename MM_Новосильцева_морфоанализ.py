#Всего токенов
tokens = 0
#Всего словарных словоформ
lemmas = 0
#Всего словарных словоформ, не считая внутри оборотов
lemmas_out_oborot = 0
#Однозначных разборов
odnoznach_slovo = 0
#Многозначных разборов
mnogoznach_slovo = 0
#Многозначных разборов, где многозначность выражается в отнесении слова к разным частям речи (слов)
different_pos = 0
#Всего вариантов анализа
total_ana = 0
#Количество оборотов
total_ob = 0
#число глаголов в в прошедшем времени в единственном числе
verbs_sing_past = 0
#список оборотов
list_ob = []

out_oborot = True

with open('ММ11б_Новосильцева.txt', 'r', encoding='utf-8') as f:

    for line in f:
        #считаем все токены
        if '<w>' in line or '<pun>' in line:
            tokens += 1
        #вход и выход из оборота
        if '<ob>' in line:
            out_oborot = False
            total_ob += 1
            list_ob.append(line[6:].strip())
        elif '</ob>' in line:
            out_oborot = True
        #вход в слово
        if '<w>' in line:
            lemmas += 1
            if out_oborot:
                lemmas_out_oborot += 1
            lemmas_tmp = 0
            different_pos_tmp = set()

        elif '<ana' in line:
            total_ana += 1
            lemmas_tmp += 1
            pos_first_part = line.split('pos="')[1]
            pos_second_part = pos_first_part.split('"')[0]
            different_pos_tmp.add(pos_second_part)

            #ищем прошедшее время, единственное число
            if '"Г"' in line:
                if 'прш' in line and 'ед' in line:
                    verbs_sing_past += 1
        elif '</w>' in line:
            if lemmas_tmp == 1:
                odnoznach_slovo += 1
            elif lemmas_tmp > 1:
                mnogoznach_slovo += 1
            if len(different_pos_tmp) > 1:
                different_pos += 1

print(f'Всего токенов: {tokens}')
print(f'Всего словарных словоформ: {lemmas}')
print(f'Всего словарных словоформ, не считая внутри оборотов: {lemmas_out_oborot}')
print(f'Однозначных разборов(слов): {odnoznach_slovo}')
print(f'Многозначных разборов(слов): {mnogoznach_slovo}')
print(f'Многозначных разборов, где многозначность выражается в отнесении слова к разным частям речи: {different_pos}')
print(f'Всего вариантов анализа: {total_ana}')
print(f'Всего оборотов: {total_ob}')
print(f'Список оборотов: {list_ob}')
print(f'Глаголы в прошедшем единственном числе:{verbs_sing_past}')

