## radist - A Bot You Can Talk to Like a Human
This bot uses the Ollama model, and you can choose any model you like, with or without censorship, and so on. The functionality of this bot includes pinging it, replying to its messages with simple commands, interacting with it, obtaining information, and more.

## Usage
Currently, we have only one command for usage:

`/ask_radist ask_string_text: str` - Ask something from Ollama. It also works with `@bot` and with replies as well.

You can change the model and settings in `configuration.py` and the bot token in `.env`.

## Installation
To install, you will need Python 3.11 or higher and create a `.env` file based on `.env.example`. Here is the instruction on how to install locally without `docker`:

> [!NOTE]  
> You must have Ollama installed locally and the model you want to use.

### Windows
```sh
$ git clone https://github.com/risknu/radist.git
$ cd radist; pip install -r requirements.txt
```

### MacOS, Linux
```sh
$ git clone https://github.com/risknu/radist.git
$ cd radist && pip install -r requirements.txt
```

### License
Licensed under the `Apache License 2.0`
