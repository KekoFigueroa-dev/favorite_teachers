# Initialize application and data structure
print("Welcome to my Favorite Teacher program")
fav_teacher = []

# Collect initial teacher rankings with proper case formatting
fav_teacher.append(input("Who is your first favotite teacher: ").title())
fav_teacher.append(input("Who is your second favotite teacher: ").title())
fav_teacher.append(input("Who is your third favotite teacher: ").title())
fav_teacher.append(input("Who is your fourth favotite teacher: ").title())

# Display initial teacher rankings in different sort orders
print(f"\nYour favorite teachers ranked are: {fav_teacher}")
alpha_teachers = sorted(fav_teacher)
print(f"Your favorite teachers alphabetically are: {alpha_teachers}")
rev_alpha = sorted(fav_teacher, reverse=True)
print(f"Your favorite teachers in reverse alphabetical order are: {rev_alpha}")

# Show teacher rankings by groups
print(f"\nYour top two teachers are: {fav_teacher[0]} and {fav_teacher[1]}.")
print(f"Your next two favorite teachers are {fav_teacher[2]} and {fav_teacher[3]}.")
print(f"Your last favorite teacher is {fav_teacher[-1]}")
print(f"You have a total of {len(fav_teacher)} favorite teachers")

# Handle first favorite teacher replacement
no_longer_fav = fav_teacher[0]
print(f"\nOops, {no_longer_fav} is no longer your favorite teacher")
new_fav = input(f"Who is your new favorite teacher: ").title()
fav_teacher.insert(0, new_fav)

# Display updated rankings after replacement
print(f"\nYour favorite teachers ranked are: {fav_teacher}")
alpha_teachers = sorted(fav_teacher)
print(f"Your favorite teachers alphabetically are: {alpha_teachers}")
rev_alpha = sorted(fav_teacher, reverse=True)
print(f"Your favorite teachers in reverse alphabetical order are: {rev_alpha}")
print(f"\nYour top two teachers are: {fav_teacher[0]} and {fav_teacher[1]}.")
print(f"Your next two favorite teachers are {fav_teacher[2]} and {fav_teacher[3]}.")
print(f"Your last favorite teacher is {fav_teacher[-1]}")
print(f"You have a total of {len(fav_teacher)} favorite teachers")

# Remove teacher from list based on user input
print("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ")
remove_teacher = input().title()
fav_teacher.remove(remove_teacher)

# Display final teacher rankings and statistics
print(f"\nYour favorite teachers ranked are: {fav_teacher}")
alpha_teachers = sorted(fav_teacher)
print(f"Your favorite teachers alphabetically are: {alpha_teachers}")
rev_alpha = sorted(fav_teacher, reverse=True)
print(f"Your favorite teachers in reverse alphabetical order are: {rev_alpha}")
print(f"\nYour top two teachers are: {fav_teacher[0]} and {fav_teacher[1]}.")
print(f"Your next two favorite teachers are {fav_teacher[2]} and {fav_teacher[3]}.")
print(f"Your last favorite teacher is {fav_teacher[-1]}")
print(f"You have a total of {len(fav_teacher)} favorite teachers")
