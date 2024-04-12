
# this is kendall's main file

def display_menu():
    print("\nMenu\n"
          "------------- \n")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def decode(encoded_number):
    x = ''
    for i in range(len(encoded_number)):
        b = str(int(encoded_number[i]) - 3)
        x += b
    return x

def main():

    while True:
        display_menu()
        option = input("Please enter an option: ")

        if option == "1":
            choice = input("Please enter the password to encode: ")
            update = 3
            encoded_number = ""
            for each_num in choice:
                updated_num = str(int(each_num) + update % 10)
                encoded_number += updated_num
            print("Your password has been encoded and stored!")



        elif option == "2":
            choice = decode(encoded_number)
            print("The encoded password is " + encoded_number + " and the original password is " + choice + ".")
            continue

        elif option == "3":

            break

if __name__ == '__main__':
    main()



