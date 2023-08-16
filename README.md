Forwarding Bot
==============
Description
-----------
This bot can sends your posts to your Telegram channel and then forwards them to 
Telegram groups you want.

Required Python modules
-----------------------
This bot was coded in Python, so it requires some Python modules for work, such as
_aiogram_ and _pyyaml_. To install these modules, write in Python command prompt this:
```
pip install -U aiogram==3.0.0rc1
pip install pyyaml
```
After installing the modules, the bot should work

Bot setup
---------
Bot has almost no commands. In order to use the bot find the `config.yml.origin` file.
The file itself will look like this:
```
token: <Bot token>
main_channel_id: <ID of channel>
group_ids: 
    - <Group ID 1>
    - <Group ID 2>
    ...
    - <Group ID N>
usernames: 
    - <Username 1>
    - <Username 2>
    ...
    - <Username N>
```
Copy this file to the same directory and remove `.origin`. This will create a file
`config.yml` and in this file instead of text in triangle brackets you should write data.
### Bot token
To get bot token you can create your own bot in [BotFather](https://t.me/botfather).
After creating bot, BotFather gives you a token of your bot. This token you should
write in field `token` in `config.yml`.
### Channel ID
If you don't know id of your channel, where you want to post, then this bot can help you:
1. Add the bot to your channel as administrator
2. Write and send in channel "/get_channel_id"
3. Bot deletes your previous message and returns in the channel its ID
4. Click on this ID and paste in field `main_channel_id` in `config.yml`
### Group IDs
There is the almost same thing with groups, where you want to forward your posts:
1. Go to BotFather and check in Bot Settings, that Group Privacy is **disabled**
2. Add the bot to groups you want
3. Write and send in group "/get_group_id"
4. Bot returns to you the group ID
5. Click in this ID and paste in field `group_ids` in `config.yml` as list element (check the example in `config.yml.origin`)
### Usernames
Field `usernames` is needed so that bot knows which users it should accept posts from.
Username is a name of your profile in Telegram. Just find in your Telegram profile field
`username`. Your username must starts from `@` symbol. After that copy your username
**without** `@` symbol and paste in field `usernames` in `config.yml` as list element
(check the example in `config.yml.origin`).

Bot usage
---------
After setting up `config.yml` using the bot is very simple. Just send to bot any post
you want, then the bot sends it to your channel and after that the bot forwards the post
to groups, which IDs you wrote in `config.yml`.