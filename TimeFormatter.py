def  main():
    initial_time = input("enter Your time ")
    twenty_four_hour = convert(initial_time)
    return twenty_four_hour
def convert(twenty_four_hour):
    cleaned_time =twenty_four_hour.strip().upper()
    am_or_pm =cleaned_time[-2:].strip()
    hours,minutes = time_digits.split(":")
    print(f"the period is {am_or_pm}")


main()