def what_to_do_now():
    message = "time to"
    prompt = "enter selection (1, 2, 0r 3):"
    user_choice = int(input(prompt))

    if user_choice == 1:
        print (message, "eat")
    elif user_choice == 2:
        print(message, "play")
    elif user_choice == 3:
        print(message, "sleep")

    else:
        print("incorrect selection!")

what_to_do_now()


# def get_price(child, adult):
#     child_price = 10
#     adult_price = 25
#     group_size = 14
#     group_rate = 0.9

#     cost = (child * child_price + adult * adult_price)

#     if child + adult > group_size:
#         cost = cost * group_rate
#     return cost
# def main():
#     num_child = int(input("Enter the number of children:"))
#     num_adult = int(input("Enter the number of adults:"))
#     cost = get_price(num_child,num_adult)
#     print("The cost of your tickets is : $" + str(cost))
# main()
