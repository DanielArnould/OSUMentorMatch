# OSU Mentor Matcher!
## Unihack 2023 Submission

### How do I run this 🤔 ?

1. First [create OAuth details](https://osu.ppy.sh/home/account/edit#oauth) so the application can access your osu! account and the web API. Not down your `client id` and `client secret`.
2. Download all required dependencies from pip: `pip install customtkinter` `pip install ossapi`, `pip install pillow`
3. Run the program by typing `python3 main.py` in your terminal in the folder of the downloaded project.
4. Input your osu! username, client id, client secret
5. Input your attributes for finding potential mentors

Top Played Beatmaps Scraping Limit = how many of your own top played beatmaps do you wish to scrape in calculating similarity (recommended: 3)

Starting Rank = On average, how high of a range on the scoreboard of individual beatmaps do you want your mentors to be (recommended: 1-50)

Ending Rank = On average, how low of a range on the scoreboard of individual beatmaps do you want your mentors to be (recommended: 5-50)

Playstyle Scraping Limit = How many of other users' top played beatmaps do you wish to be scraped to calculate similarity (recommended: 3-5)

6. Hit Enter and wait for it to load (It may take a while as the osu web api is quite slow)
7. Once it has, you'll see a list of potential mentors, whose profiles you can visit and send a friend request!

### Inspiration
We've all had times where we would be really bad at a game. There are many ways to improve, like to get in a lot of practice, or to get somebody to help you better yourself at the game. We here at Samsung Smart Fridges chose to go with the latter option such that we are able to connect other like-minded individuals together to have fun in a game. 

### What it does
The program is there to help you find the perfect mentor for you, being able to select from the top players of the game. The program is then able to see which categories or genres you like, the difficulty of the game or song that you like, as well as length and many other aspects of the game. This way, we are able to get you matched up with the perfect mentors that have already went through your stages. 

### How we built it
We based the entire code mainly in python, where we would use python gui's for the front end to have the user be able to login, and then find their mentor. Based on our algorithms, we would try to match the user's abilities to one of a suitable mentor. The Python GUI is called CustomTkinter.

### Challenges we ran into
One concurring challenge is from the front end, where we all have little to no experience with GUI's or ways to create user interfaces. Another challenge would be trying to have more effective API calls, because we were facing runtimes of like ~60 seconds 

### Accomplishments that we're proud of
That we were able to finish in a span of 48 hours

### What we learned
We learnt more about OSU's categorizable attributes, OSU's web API, Tkinter which looks awful, and finally we learnt that you shouldn't use python for projects like this. 

### What's next for OSU Mentor Match
The framework or idea of how we can match similar players together like here in OSU, could also work in other games, and outside of games as well. We could try to have the program find or identify patients with similar illnesses or symptoms, or have it find players with similar skill levels in games like League of Legends, Valorant, etc.

