**Basic Packages**

- aiogram - 3.0.0b4
- googletrans

**Install dependencies**

```
pip3 install -r requirements.txt
```

**Launching the bot**

Make sure that you have created and activated a virtual environment! You also need to register the bot token in the file `config.py` This option of storing the token is not safe. It will be changed in the future.

To launch the bot, enter the command:

```
python bot.py
```

**Description**

The bot works via the google translate API. At the first launch, with the start command, the bot offers to select the target translation language (into which language to translate).

![Launch Bot](https://i.ibb.co/FnkrDBW/1.png)

At the moment, there is a choice of two target translation languages: Russian and English. In the upcoming updates, the number of languages will expand.

You can change the translation language with the setting command, or again with the start command.

Next, the bot translates all messages coming to it.

![Working Bot](https://i.ibb.co/yyQx1jV/2.png)

Which is cool! The language written by the user for translation is determined automatically!

**Database**

In addition, the bot works with a database based on the built-in sqlite3 module. When the bot is first launched, the user's name, his telegram ID and the translation language are recorded in the database.

**Update Bot "China" - 29.09**
1. Removed functions that were at the development stage
2. A new "Registration date" field has been added to the database
At the moment, the client update also updates this field.
3. Added Chinese language translate 🔥

![China](https://i.ibb.co/26Lj2Y9/upd.png)
