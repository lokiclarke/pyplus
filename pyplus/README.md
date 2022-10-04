# PyPremium

PyPremium is a Python library that pushes the boundaries of accessibility for python by emulating batch commands.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pypremium.

```bash
pip install pypremium
```

## Usage

```python
import pypremium

# prints 'Goodbye' over 'Hello' after 3 seconds
pypremium.reprint("Hello","Goodbye",3)

# changes the program title to 'Title'
pypremium.title("Title")

# allows you to write batch code in python
bat_cmd("echo hello")

# pings 'github.com'
pypremium.ping("github.com")

# changes the color of the text to red and makes the background white.
pypremium.color(text="red",bg="white")

# transforms 'Text' into Ascii text art and the prints it
asciiart = pypremium.Ascii("Text")
print(asciiart)

# emulates the '@ECHO OFF' command in batch
pypremium.echooff()

# emulates the 'pause' command in batch and adds '>nul'
pypremium.batpause(nul=True)

# clears the screen, but stores variables in local memory
pypremium.clear()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
