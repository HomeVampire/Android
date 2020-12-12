# Write a python code to insert a year of birth and using that calculate that person’s
# current age.
def main():
    birth_year=int(input("Enter your birth year: "))
    from datetime import date
    current_year = date.today().year
    print("Your age is: ",current_year-birth_year)

main()
