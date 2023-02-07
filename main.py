# -----------------------------------------------------------------------------
# Name:        Data Structure assignment
# Purpose:     Art Gallery to demonstrate my use of data structure
#
# Creator:     Wallace
# Created:     29-Mar-2022
# Updated:     07-Apr-2022
# -----------------------------------------------------------------------------
from Art import ArtPieces
from Classic import Classic
from Digital import Digital
import csv
import random
import pandas as pd


def create_object():
    """
    Create an object in the csv file for later instantiating, and editing data

    Returns
    -------
    str
        A statement where it includes the difference between the price of two
        art pieces after calculations

    Raises
    ------
    FileNotFoundError
        If the file has not created, or it doesn't exist
    """
    with open('class_obj.csv', 'a') as f:
        user_input = input("Input the item(author, year, name, price, website(None or link), origin(None or country))"
                           "\n(ie. Leonardo Da Vinci,1509,Mona Lisa,1000,None,Italy):\n")
        f.write(f'{user_input},None,False\n')


def instantiate_obj() -> list:
    """
    Instantiating all the items in the csv file into class objects depending on
    what attributes they had

    Returns
    -------
    list - Class objects
        A statement where it includes the difference between the price of two
        art pieces after calculations

    Raises
    ------
    FileNotFoundError
        If the file has not created, or it doesn't exist
    """
    df = pd.read_csv('class_obj.csv')
    print("These are the items you are instantiating")
    print(df)

    with open("class_obj.csv", 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    lst = []
    for item in items:
        if int(item.get('year')) < 1980 and str(item.get('website')).lower() == 'none':
            name = Classic(
                artist=item.get('artist'),
                year=int(item.get('year')),
                name=item.get('name'),
                price=float(item.get('price')),
                origin=item.get('origin'),
                sold=False,
            )
            name.checking_art_period()
            name.update_data()
            lst.append(name)
        elif str(item.get('website')).lower != 'none':
            name = Digital(
                artist=item.get('artist'),
                year=int(item.get('year')),
                name=item.get('name'),
                price=float(item.get('price')),
                website=item.get('website'),
                sold=False,
            )
            name.calculate_price()
            name.update_data()
            lst.append(name)
        else:
            name = ArtPieces(
                artist=item.get('artist'),
                year=int(item.get('year')),
                name=item.get('name'),
                price=item.get('price'),
                sold=False,
            )
            lst.append(name)
    random.shuffle(lst)
    return lst


# Main Program
loop = True
while loop:
    try:
        user = int(input("Please put in how many items you want to add: "))
    except Exception as e:
        print(e)
        print('Number please')
    else:
        if user < 0:
            print("It cannot be negative")
        elif user > 5:
            print("Please don't input that much data")
        else:
            while user > 0:
                create_object()
                user -= 1
            loop = False

lst = instantiate_obj()
x = 0
y = 5
money = 5000000
inventory = []
print('-' * 10)
while money >= 0 and x + 5 < len(lst):
    new_lst = lst[x:y].copy()
    for item in new_lst:
        print(item.__str__())
    try:
        buy = input('\nAre you buying any art from these 5?(y/n) ')
        if buy.lower() == 'y':
            art = int(input('Then which number you want to buy?(1-5) '))
            if art <= 0 or art > 5:
                raise ValueError(f"{art} - is not a valid number, please pick 1-5")
            art -= 1
            compare = input(f'\nDo you want to compare the selected art price:{new_lst[art].name}(y/n): ')
            if compare.lower() == 'y':
                compare_item = int(input(f"Which other item? (1-5 exclude {art + 1}): "))
                if compare_item == art + 1:
                    raise NameError(f"You cannot compare the same item")
                if compare_item <= 0 or compare_item > 5:
                    raise ValueError(f"{compare_item} - is not a valid number")
                compare_item -= 1
                print(new_lst[art].compare_price(new_lst[compare_item].name))

            print("You have a 50% chance to get a discount")
            new_lst[art].get_discount()
            money = new_lst[art].buying(money)
            inventory.append(new_lst[art])
            new_lst.pop(art)
        elif buy.lower() == 'n':
            print('Skipping these 5 art, to the next 5')
        else:
            raise ValueError(f"{buy} - input is not valid ")
    except Exception as e:
        print(f"Please try again, Error Message - {e}")
    else:
        x += 5
        y += 5
        print("\nThese are the next five art pieces")
        print("-"*10)

    if x + 5 > len(lst):
        print("\nUnfortunately, these items are not sold today, try next time!")
        for item in lst[x:None]:
            print(item.__str__())
        print("-" * 10)
else:
    if money < 0:
        print(f"Sorry, you have exceed your budget, currently you have ${money}")
    elif x+5 > len(lst)-1:
        print('This is the end of the gallery, thank you!')
    print("-" * 10 + "\nToday you have bought:")
    for bought in inventory:
        print(bought.__str__())
    print('-'*10)

# reversing all the changes so that the program could be run multiple times every time it terminates
save = input("Do you want to save the changes?(y/n)[invalid input will auto select unsaved]: ")
if save.lower() == 'y':
    with open("class_obj.csv", 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    for item in items:
        if int(item.get('year')) > 1980 and str(item.get('website')).lower != 'none':
            name = Digital(
                    artist=item.get('artist'),
                    year=int(item.get('year')),
                    name=item.get('name'),
                    price=float(item.get('price')),
                    website=item.get('website'),
                    sold=item.get('sold'),
                )

            name.reverse_price()
            name.update_data()
else:
    with open("class_obj.csv", 'r') as f:
        reader = csv.DictReader(f)
        items = list(reader)

    for item in items:
        if int(item.get('year')) < 1980 and str(item.get('website')).lower() == 'none':
            name = Classic(
                artist=item.get('artist'),
                year=int(item.get('year')),
                name=item.get('name'),
                price=float(item.get('price')),
                origin=item.get('origin'),
                sold=False,
            )
            name.update_data()
        elif str(item.get('website')).lower != 'none':
            name = Digital(
                    artist=item.get('artist'),
                    year=int(item.get('year')),
                    name=item.get('name'),
                    price=float(item.get('price')),
                    website=item.get('website'),
                    sold=False,
                )
            name.reverse_price()
            name.update_data()
