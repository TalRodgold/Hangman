def func(num1, num2):
    """checks if two numbers equal to each other
     :param num1: input of any number
     :param num2: input of any number
     :type num1: int
     :type num2: int
     :return: if numbers are equal SAME
              if numbers are diffrent DIFFRENT
     :rtype: int  """
    if num1 == num2:
        return "same"
    else: return "diffrent"
def main():
    func(5, 5)
if __name__ == "__main__":
    main()