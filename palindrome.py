def palindrome():
    phrase = input("Enter a word or phrase: ")
    check = phrase.replace(" ","")
    if check[0::] == check[::-1]:
        print(f"{phrase} is a palindrome")
    else:
        print(f"{phrase} is not a palindrome")


palindrome()