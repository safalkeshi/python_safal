def main():
    name , house = get_student()
    print(f"{name} from {house} ")

def get_student():
    name = input("Name :")
    house = input ("House :")
    return (name,house) ##this is tuple returns 2 values returns one tuple its vslue is immutable

if __name__ =="__main__":
    main()