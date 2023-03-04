# import the neccessary libraries to open webpages
import requests
import webbrowser
# import json #only if the user's details need to be written to a file.


# !!! Not familiar with tkinter; unsure of integration into tag.py

def check_OAuth():
    check = False   # currently, the user has not checked if they have an OAuth

    while check == False:
        oauth_exist = input("Do you have an osu! OAuth token? (y/n): ")
        if oauth_exist.lower() == 'n':
            # if the user replies 'n' (no), they will be taken to the website below to create OAuth.
            print("You need a osu! OAuth Token to access this program")
            print("You will be redirected to the osu! website to create an osu! OAuth token")
            webbrowser.open_new_tab("https://osu.ppy.sh/home/account/edit#oauth")
            continue

        elif oauth_exist.lower() == 'y':
            # the user has OAuth, retrieve their OAuth details.
            get_OAuth()
            check = True

        else:
            # the user input was invalid.
            print("Please enter 'y' for YES, and 'n' for NO")


def get_OAuth():
    # this function asks the user for their OAuth id, secret and their osu! user ID.
    client_id = input("Enter your osu! OAuth client ID: ")
    client_secret = input("Enter your osu! OAuth client secret: ")
    user_id = input("Enter your osu! ID:")
    user_info = [client_id,client_secret,user_id]
    print(user_info) # for testing


# FOR TESTING PURPOSES
#if __name__ == "__main__":
#    check_OAuth()