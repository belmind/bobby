![Python application](https://github.com/BelminD/bobby/workflows/Python%20application/badge.svg?branch=master)
# bobby
The friendly Twitch chatbot! 🤖💬 Bobby helps you moderate your [Twitch.tv](https://twitch.tv) chat! He saves every chat message in a easy to read log file 📄, responds to messages and commands 📩 as well as bans trolls and spammers!🚫

## Features
- [X] Write chatlogs to files
- [X] Logging every chat message (Read chat in your terminal emulator)
- [ ] Respond to messages / commands in chat 
- [ ] Timeout / Ban users in chat for faul language
- [ ] Timeout spammers

## Installation
Open your terminal
```bash
git clone git@github.com/belmind/bobby.git

```
Open the file `config.py` and add your `CHANNEL` name and `OATH` key. If you don't have a oath key you can get one from [twitchapps.com/tmi](https://twitchapps.com/tmi/).

## Usage

```zsh
python3 app.py _name_
```
Where _name_ is the name of the output file. It's not necessary and defaults to `%d-%m-%y.txt`

## Contributing
Pull requests are welcome. Please make sure to update tests as appropriate.

## License
Bobby is open source software licensed as [MIT](https://choosealicense.com/licenses/mit/).
