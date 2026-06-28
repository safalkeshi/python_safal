def main():
    fullname = input("Enter your full name ")
    language = input("enter your favoraite language ")
    greet(fullname,language)

def greet(fullname, language):
  clean_name = fullname.strip().title()
  clean_lang = language.strip().title()

  print(f"Hello {clean_name},its awsome that you love {clean_lang}!")

main()