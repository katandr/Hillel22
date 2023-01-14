import json
import csv
def censor(file, words_to_replace:list):

    words_to_replace.sort(key=len, reverse=True)

    with open(file, 'r') as file:
        stats ={}
        count_word = 0
        text = file.read()
        for word in words_to_replace:

            word_with_capital = word.capitalize()
            word_plural = word+'s'
            word_with_capital_plural = word_with_capital+'s'
            if text.find(word) != -1:
                count_word = text.count(word)

                text = text.replace(word, "***")
                stats[word] = count_word


            if text.find(word_plural) != -1:
                count_word = text.count(word_plural)

                text = text.replace(word_plural, "***")
                stats[word_plural] = count_word


            if text.find(word_with_capital) != -1:
                count_word = text.count(word_with_capital)

                text = text.replace(word_with_capital, "***")
                stats[word_with_capital] = count_word


            if text.find(word_with_capital_plural) != -1:
                count_word = text.count(word_with_capital_plural)
                text = text.replace(word_with_capital_plural, "***")
                stats[word_with_capital_plural] = count_word
            stats[word] = count_word
            count_word = 0

    with open("hw10_newfile.txt", 'w') as new_file:
        new_file.write(text)
    return stats



def dump_to_json_file(file_name,list_of_words_to_replace:list,stats):
    with open('stat.json', 'a') as file:
        to_json = {'file name': file_name, 'list_of_words_to_replace': list_of_words_to_replace,'statistics_of_replacements': stats}
        json.dump(to_json, file, indent=2)

def save_to_csv_file(file_name,list_of_words_to_replace:list,stats):
    with open('stat.csv', 'a', newline="") as file:
        to_csv = [file_name, list_of_words_to_replace, stats]
        writer = csv.writer(file)
        writer.writerow(to_csv)

# подготовка csv файла для записи, запись заголовков
with open('stat.csv', 'w', newline="") as file:
    fieldnames = ['file name','list_of_words_to_replace','statistics_of_replacements']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

# старт основной прогарммы
list_of_words_to_replace = ['friend', 'frendly', 'friendship','gggggggg']
file_name = 'file1.txt'
stats = censor(file_name, list_of_words_to_replace)
dump_to_json_file(file_name,list_of_words_to_replace,stats)
save_to_csv_file(file_name,list_of_words_to_replace,stats)

list_of_words_to_replace2 = ['london', 'paris']
file_name2 = 'file2_london.txt'
stats2 = censor(file_name2, list_of_words_to_replace2)
dump_to_json_file(file_name2,list_of_words_to_replace2,stats2)
save_to_csv_file(file_name2,list_of_words_to_replace2,stats2)




