#Задача «Шифр Цезаря»
#2.Напишите программу «Шифр Цезаря»
#   a.Шифр Цезаря — это вид шифра подстановки, в котором каждый символ
#   в открытом тексте заменяется символом, находящимся на некотором постоянном
#   числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом
#   вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.
#   b.Вам необходимо реализовать две функции.
#   I.Первая, принимает исходную строку и возвращает зашифрованную.
#   II.Вторая, принимает зашифрованную и возвращает дешифрованную.
#   III.Также можете продумать и реализовать механизм задания ключа
#   (передавать в функцию шифрования, а в функции дешифровки извлекает этот ключ из строки)
#Функция принимает два агрумента, 1-ий аргумет (Text) текст что необходимо зашифровать,
# второй аргумет число целое (kod) - здвига в право на и список в котором можно предварительно смешать порядок
def My_Kod_Encrypt(Text,kod,myListAlphabet):
    myListMyText =list(Text) # варант цикл myListMyText = [char for char in Text]
    b=len(myListMyText)
    myListMyTextKod = []
    a = len(myListAlphabet)
    myListAlphabet = myListAlphabet*kod
    if kod>0:
        for i in range (b):
            for j in range(a-1):
                if myListMyText[i]==myListAlphabet[j]:  
                    myListMyTextKod.append(i)
                    myListMyTextKod[i] = myListAlphabet[j+kod]
    textEncrypt = ''.join(str(m) for m in myListMyTextKod) # в кавычках ставим любой знак ион будет между буквами,сейчас между буквами ничего не будет
    return textEncrypt,myListMyTextKod
# функция My_Kod_Decipher Расшифрованный текст , принимает три переменне сам текст, код, и список в котором можно предварительно смешать порядок
def My_Kod_Decipher(Text,kod,myListAlphabet):
    myListMyText =list(Text) # варант цикл myListMyText = [char for char in Text]
    b=len(myListMyText)
    myListMyTextKod = []
    a = len(myListAlphabet)
    myListAlphabet = myListAlphabet*kod
    if kod>0:
        for i in range (b):
            for j in range(a-1):
                if myListMyText[i]==myListAlphabet[j]:  
                    myListMyTextKod.append(i)
                    myListMyTextKod[i] = myListAlphabet[j-kod] # меняя знак в обратную сторону мы разшифровуем функцию
                        #print ('Зашифрованный текст',myListMyTextKod)
        textEncrypt = ''.join(str(m) for m in myListMyTextKod) # в кавычках ставим любой знак ион будет между буквами, 
    return textEncrypt,myListMyTextKod
#Дано: Список можно дополнить символами ит загавными буквами и тд, при єтом нужно менять 
myListA = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
MyT = str (input("введите текст---> "))
MyK=4 #больше нуля, пробел также шишруем
#Вызов функций 
My_fun_print = My_Kod_Encrypt(MyT,MyK,myListA)
MyText2 = My_fun_print[0]
My_fun_print2 = My_Kod_Decipher(MyText2,MyK,myListA)
#Вывод результата
print ('Зашифрованный текст:',My_fun_print[0])
print ('Расшифрованный текст:',My_fun_print2[0])












