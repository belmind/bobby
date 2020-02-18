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

> The friendly Twitch chatbot! 🤖💬 Bobby helps you moderate your [Twitch.tv](https://twitch.tv) chat! He saves every chat message in a easy to read log file 📄, send out messages periodically, responds to messages and commands 📩 as well as bans trolls and spammers! 🚫

## Features
- [X] Write chatlogs to files
- [X] Logging every chat message (Read chat in your terminal emulator)
- [ ] Send messages periodically 
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
Bobby is open source software licensed as [MIT](https://github.com/belmind/bobby/blob/master/LICENSE).
