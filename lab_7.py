# task1
# def read_display_text_file(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#          for line in file: #последовательное прохождение через каждую строку внутри файла
#             print(line, end='')#вывод текущей строки на экран без символа новой строки \n
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# read_display_text_file(file_path)

# task2
# import random
#
# def random_line_read(file_path):
#       with open(file_path, 'r') as file:  #открывает файл по указанному пути в режиме чтения
#          lines = file.readlines() #читает все строки файла и сохраняет их в список
#          print(random.choice(lines).strip()) #использует функцию random.choice() для случайного выбора одной строки. strip() убирает все возможные символы новой строки или пробелы с начала и конца строки
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# random_line_read(file_path)

# task 3
# def number_uppercase_symbols(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       content = file.read() #читает содержимое файла
#       uppercase_count = sum(1 for char in content if char.isupper()) #char.isupper() функция, которвя возвращает Truе, если символ в верхнем регистре, sum() подстчитывает значения Truе
#       print(uppercase_count) #выводит на консоль количество true, то есть кол-во символов в верхнем регистре
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# number_uppercase_symbols(file_path)

# task 4
# def lines_not_start_D(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       count = sum(1 for line in file if not line.strip().startswith('D'))#подсчет количества строк, которые не начинаются с D
#       print(count) #вывод числа строк
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# lines_not_start_D(file_path)

# task 5
# def words_end_F(file_path):
#       with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#          words = file.read().split() #читает содержимое файла и разбивает его на слова
#          count = sum(1 for word in words if word.endswith(('F', 'f'))) #подсчет количества слов, оканчивающихся на 'F' или 'f
#          print(count)
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# words_end_F(file_path)

# task 6
# def count_all_none_words(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       content = file.read() #читает содержимое файла
#       count_all = content.lower().split().count('all') #преобразует текст в нижний регистр, разбивает его на слова и считает слова 'all'
#       count_none = content.lower().split().count('none') #аналогично тому, что выше
#       print(count_all)
#       print(count_none)
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\all.none.txt"#путь к файлу
# count_all_none_words(file_path)

# task 7
# def count_word_frequency(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       content = file.read().lower() #читает содержимое файла, преобразуя символы в нижний регистр
#       words = content.split() #разбивает текст на слова
#       word_frequency = {} #dictionary, который нужен для отслеживания частоты встречающихся слов
#
#       for word in words: #проходится по каждому слову в файле
#          word_frequency[word] = word_frequency.get(word, 0) + 1 #если слово уже присутствует в словаре, то частота увеличивается на 1, если нет, то устанавливает частоту 1
#       for word, frequency in word_frequency.items(): #проходится по паре ключ значение
#          print(f"{word}: {frequency}")
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# count_word_frequency(file_path)

# task 8
# def longest_word(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       content = file.read().lower()  #читает содержимое файла, преобразуя символы в нижний регистр
#       words = content.split() #разбивает текст на слова
#       long_word = max(words, key=len) #находит максимально длинное слово
#
#       print(long_word)
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# longest_word(file_path)

# task 9
# def replace_symb(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       content = file.read() #читает содержимое файла
#       correct_cont = content.replace('B', 'J').replace('b', 'j') #замена символов
#       print(correct_cont)
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# replace_symb(file_path)

# task 10
# def count_a_b_occur(file_path):
#    with open(file_path, 'r') as file: #открывает файл по указанному пути в режиме чтения
#       content = file.read().lower()  #читает содержимое файла, преобразуя символы в нижний регистр
#       count_a = content.count('a') #подсчет символа а
#       count_b = content.count('b') #подсчет символа b
#       print(f"a={count_a}, b={count_b}")
#
# file_path = r"C:\Users\Ильяс\Desktop\lab_7\lab_7.txt"#путь к файлу
# count_a_b_occur(file_path)