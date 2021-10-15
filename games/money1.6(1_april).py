import time
import random
print ('добро пожаловать в "деньги и экономия"! ваша цель - заработать 100 миллионов за 30 лет.')
time.sleep (2)
a = 0
p = 1
money = 10000
time_until_death = 360
cotton_price = 64
oil_price = 18
gold_price = 30600
cotton_have = 0
oil_have = 0
gold_have = 0
biruza_devidents = 0
montr_devidents = 0
lubashino_devidents = 0
biruza_price = 1000
montr_price = 1000
lubashino_price = 1000
while (a == 0):
   if (p == 0):
      print('у вас ', money , ' рублей')
      print('цена нефти за литр: ', oil_price, '. цена хлопка за килограмм: ', cotton_price, '. цена золота за слиток: ', gold_price, '.')
      print('Вы имеете ', oil_have , ' литров нефти, ', cotton_have ,' килограммов хлопка и ', gold_have ,' слитков золота. доход с девидендов за 1 ход: ', biruza_devidents + montr_devidents + lubashino_devidents)
      print('осталось ходов: ', time_until_death , ' , использовано ходов: ', 360 - time_until_death , '.')
   if (p == 1):
      p = 0
   choose = input('что вы хотите сделать: купить, продать, закончить месяц.')
   if (choose == 'закончить месяц'):
      print('заканчиваем...')
      if (time_until_death == 0):
         print('к сожалению, вы проиграли.')
      if (money == 100000000 or money > 100000000):
         print('вы выиграли! поздравляю!')
      time_until_death = time_until_death - 1
      cotton_price += random.randrange(-251, 251)
      oil_price += random.randrange(-251, 251)
      gold_price += random.randrange(-501, 501)
      if (cotton_price < 64):
         cotton_price += 300
      if (oil_price < 10):
         oil_price += 300
      if (gold_price < 20000):
         gold_price += 700
      if (cotton_price > 1250):
         cotton_price = cotton_price - 300
      if (oil_price > 1250):
         oil_price = oil_price - 300
      if (gold_price > 62000):
         gold_price = gold_price - 700
      time.sleep(1)
   if (choose == 'продать'):
      resourse = input('какие ресурсы вы хотите продать: хлопок, нефть, золото.')
      if (resourse == 'хлопок'):
         print('цена хлопка за килограмм: ', cotton_price , '.Сколько килограмм хлопка вы хотите продать?')
         buy = int(input())
         if (buy > cotton_have):
            print('у вас недостаточно хлопка!')
         if (buy == cotton_have or buy < cotton_have):
            print('вы успешно продали ', buy , ' килограммов хлопка за ', buy * cotton_price ,' рублей! у вас осталось ', cotton_have - buy , ' хлопка!')
            money = money + buy * cotton_price
            cotton_have = cotton_have - buy
      if (resourse == 'нефть'):
         print('цена нефти за литр: ', oil_price , '.Сколько литров нефти вы хотите продать?')
         buy = int(input())
         if (buy > oil_have):
            print('у вас недостаточно нефти!')
         if (buy == oil_have or buy < oil_have):
            print('вы успешно продали ', buy , ' литров нефти за ', buy * oil_price ,' рублей! у вас осталось ', oil_have - buy , ' нефти!')
            money = money + buy * oil_price
            oil_have = oil_have - buy
      if (resourse == 'золото'):
         print('цена золота за слиток: ', gold_price , '.Сколько слитков золота вы хотите продать?')
         buy = int(input())
         if (buy > gold_have):
            print('у вас недостаточно золота! (нужно больше золота! :-D )')
         if (buy == gold_have or buy < gold_have):
            print('вы успешно продали ', buy , ' слитков золота за ', buy * gold_price ,' рублей! у вас осталось ', gold_have - buy , ' золота!')
            money = money + buy * gold_price
            gold_have = gold_have - buy
   if (choose == 'купить'):
      resourse = input('какие ресурсы вы хотите купить: хлопок, нефть, золото.')
      if (resourse == 'хлопок'):
         print('цена хлопка за килограмм: ', cotton_price , '.Сколько килограмм хлопка вы хотите купить?')
         buy = int(input())
         if (buy > -1):
            if (buy * cotton_price > money):
               print('у вас недостаточно денег! вам не хватает ', buy * cotton_price - money , ' рублей!')
            if (buy * cotton_price < money or buy * cotton_price == money):
               print('вы успешно купили ', buy , ' килограммов хлопка за ', buy * cotton_price ,' рублей!')
               money = money - buy * cotton_price
               cotton_have = cotton_have + buy
      if (resourse == 'нефть'):
         print('цена нефти за литр: ', oil_price , '.Сколько литров нефти вы хотите купить?')
         buy = int(input())
         if (buy > -1):
            if (buy * oil_price > money):
               print('у вас недостаточно денег! вам не хватает ', buy * oil_price - money , ' рублей!')
            if (buy * oil_price < money or buy * oil_price == money):
               print('вы успешно купили ', buy , ' литров нефти за ', buy * oil_price ,' рублей!')
               money = money - buy * oil_price
               oil_have = oil_have + buy
      if (resourse == 'золото'):
         print('цена золота за слиток: ', gold_price , '.Сколько слитков золота вы хотите купить?')
         buy = int(input())
         if (buy > -1):
            if (buy * gold_price > money):
               print('у вас недостаточно денег! вам не хватает ', buy * gold_price - money , ' рублей!')
            if (buy * gold_price < money or buy * gold_price == money):
               print('вы успешно купили ', buy , ' слитков золота за ', buy * gold_price ,' рублей!')
               money = money - buy * gold_price
               gold_have = gold_have + buy
