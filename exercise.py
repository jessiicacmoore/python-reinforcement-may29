seating_plan = [
    [None, "Pumpkin", None, None],
    ["Socks", None, "Mimi", None],
    ["Gismo", "Shadow", None, None],
    ["Smokey", "Toast", "Pacha", "Mau"],
]


def display_available_seats(list):
    for row in range(0, len(seating_plan)):
        for seat in range(0, len(seating_plan[row])):
            if seating_plan[row][seat] == None:
                print(
                    f"Row {row+1} Seat {seat+1} is available - Do you want to sit there y/n?"
                )
                user_answer = input()
                if user_answer == "y":
                    print("What is your name?")
                    user_name = input()
                    seating_plan[row][seat] = user_name
                    return


display_available_seats(seating_plan)
print(seating_plan)
