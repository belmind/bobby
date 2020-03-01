# bobby

<div align="center">
    <div align="center">
    <a href="https://www.flaticon.com/authors/icongeek26">
        <img src="assets/chatbot.svg" width="25%">
    </a>
</div>

</div>

<br />

<div align="center">

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
<br />
![Python application](https://github.com/BelminD/bobby/workflows/Python%20application/badge.svg?branch=master)
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/belmind/bobby/graphs/commit-activity)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/belmind/bobby/blob/master/LICENSE)

</div>

> The friendly Twitch chatbot! 🤖💬 Bobby helps you moderate your [Twitch.tv](https://twitch.tv) chat! He saves every chat message in a easy to read log file 📄, sends out messages periodically, responds to messages and commands 📩 as well as bans trolls and spammers! 🚫

## Features
- [X] Write chatlogs to files
- [X] Logging every chat message (Read chat in your terminal emulator)
- [X] Respond to messages in chat
- [X] Respond to commands such as `!roll`
- [X] Timeout / Ban users in chat for faul language
- [ ] Send messages periodically
- [ ] Timeout spammers

## Installation
> Make sure to have Python3 installed on your machine.

Clone the repository and install packages.
```zsh
git clone https://www.github.com/belmind/bobby
cd bobby
pip3 install -r requirements.txt
```

Open the file `config.py` and add your `CHANNEL` name and `OATH` key. If you don't already have a oath key you can get one from [twitchapps.com/tmi](https://twitchapps.com/tmi/).

## Usage

```zsh
python3 app.py -f name
```
Where `name` is the name of the output file. It's not necessary and defaults to `%d-%m-%y.txt`

### Chat Responses
It's simple to edit the chat responses! Simply, open the file `responses.txt` and modify it!
```
!rank, Diamond IV (44 LP)
!highscore, My highscore is exactly 113 312 413 100!
```
**NOTE that the values are being separated by a comma `,`.**

Bobby will then respond with the following format: `@{user} {msg}` in a few milliseconds.

### Faul Language
There is a file named `bannable_words.txt` which you can fill out with words you would neve want to see in a chat room.
```
badword1
badword2
badword3
```
Bobby will instantly ban these users from chat. Make sure that you give the bot moderator privileges if you are running it from a seperate account.

## Contributing
Pull requests are welcome. Please make sure to update tests as appropriate.

## License
Bobby is open source software licensed as [MIT](https://github.com/belmind/bobby/blob/master/LICENSE).
