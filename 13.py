__doc__ = '''Write a program to find the biggest of 4 numbers.
   a)  Read 4 numbers from user using Input statement.
   b) extend the above program to find the biggest of 5 numbers.
( PS : Use IF and IF & Else , If and ELIf, and Nested IF )
'''

def biggest_of_N_number(aList):
      max = 0
      for n in aList:
         if n > max:
            max = n
      return max           


if __name__ == '__main__':
       aList = []
       while True:
              n = int(input("Enter the Number: "))
              aList.append(n)
              if len(aList) == 4:
                     print(f"Max of 4 numbers: {biggest_of_N_number(aList)}")
                     s = input("\nDo You want to find the biggest of 5 number: Press Yes/No...")
                     if s == 'Yes' or s == 'yes' or s == 'YES' or s == 'y' or s == 'Y':
                            continue
                     else:
                            break
              if len(aList) == 5:
                     print(f"Max of 5 numbers: {biggest_of_N_number(aList)}")
                     break
              if len(aList) > 5:
                     break
              



       