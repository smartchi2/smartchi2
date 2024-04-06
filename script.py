
def arithmetic():
  product = str(input("Enter product name: "));
  number1 = int(input("Enter input: "));
  number2 = int(input("Enter second input: "));
  number3 = int(input("Enter third input: "));

  sum = number1 + number2 + number3
  print("The sum of the aritmetic is", sum,  product);

  print('The average of the aritemetic is' ,sum/3);
  
  smallest = 0;
  largest = 0;
  
  if number1 <= number2 and number1 <= number3:
    smallest = number1;
  if number2 <= number1 and number2 <= number3:
    smallest = number2;
  if number3 <= number1 and number3 <= number2:
    smallest = number3;

  print('The smallest of the integers is ',smallest)

  if number1 >= number2 and number1 >= number3:
     largest = number1
  if number2 >= number1 and number2 >= number3:
     largest = number2
  if number3 >= number1 and number3 >= number2:
     largest = number3;

  print("The largest of integers is", largest)

arithmetic();