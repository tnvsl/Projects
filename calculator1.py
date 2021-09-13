while True:
   num1 = int(input('Введите первое число     '))
   num2 = int(input('Введите второе число     '))
   oper = input('Введите операцию (+-*/) или остановите (стоп)    ')

   #operations
   sum = num1 + num2
   min = num1 - num2
   mul = num1 * num2
   div = num1 / num2

   if oper == '+':
      print(num1, '+', num2,'=', sum)
   elif oper == '-':
      print(num1, '-', num2,'=', min)
   elif oper == '*':
      print(num1, '*', num2,'=', mul)
   elif oper == '/':
      print(num1, '/', num2,'=', div)
   elif oper == 'стоп':
      break
   else:
      print('непонятно')
