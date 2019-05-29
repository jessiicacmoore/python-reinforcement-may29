seating_plan = [
    [None, "Pumpkin", None, None],
    ["Socks", None, "Mimi", None],
    ["Gismo", "Shadow", None, None],
    ["Smokey", "Toast", "Pacha", "Mau"],
]


def display_available_seats(list):
    done = False
    for row in range(0, len(seating_plan)):
        for seat in range(0, len(seating_plan[row])):
            if seating_plan[row][seat] == None:
                print(
                    f"Row {row+1} Seat {seat+1} is available - Do you want to sit there y/n?"
                )
                user_answer = input()
                if user_answer == "y":
                    done = True
                    print("What is your name?")
                    user_name = input()
                    seating_plan[row][seat] = user_name
                    break
                if done:
                    break
            if done:
                break


display_available_seats(seating_plan)
print(seating_plan)

# Row 1 Seat 1 is available - Do you want to sit there y/n?
# n
# Row 1 Seat 3 is available - Do you want to sit there y/n?
# y
# What is your name?
# Jess
# [
#     [None, "Pumpkin", "Jess", None],
#     ["Socks", None, "Mimi", None],
#     ["Gismo", "Shadow", None, None],
#     ["Smokey", "Toast", "Pacha", "Mau"],
# ]
