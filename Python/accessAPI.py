import requests

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

print ("Welcome to the Book of Mormon Summary Tool!")
book = ""
data = {}
done = False
while done == False:
    while True:
        try:
            book = input('Which book of the Book of Mormon would you like?  ')
            bookcheck = book.replace(" ", "").lower()
            response = requests.get(base_url + bookcheck)
            response.raise_for_status()
            break
        except requests.exceptions.HTTPError as err:
            print("Please provide a valid book.")
            continue
    while True:
        try:
            chapter = input('Which chapter of %s are you interested in?  ' % book)
            response = requests.get(base_url + book.replace(" ", "").lower() + '/' + chapter)
            response.raise_for_status()
            data = response.json()
            break
        except requests.exceptions.HTTPError as err:
            print("Please provide a valid chapter.")
            continue
    print('Summary of %s chapter %d: ' % (book, int(chapter)))
    print(data['chapter']['summary'])
    while True:
        inp = input("Would you like to view another (Y/N): ")
        if inp.lower() == "n":
            print("Thank you for using Book of Mormon Summary Tool!")
            done = True
            break
        elif inp.lower() == "y":
            break
        else:
            print("Invalid choice")