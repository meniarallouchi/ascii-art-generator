# ASCII Art Generator

Converts any image into ASCII art using brightness mapping. Each pixel's brightness value gets mapped to a character, where darker characters represent darker areas and lighter characters represent brighter areas. Output is saved as a `.txt` file to your Downloads folder.

## Built With

- [Python 3](https://www.python.org/)
- [Pillow](https://python-pillow.org/) - image loading, resizing, and grayscale conversion
- [NumPy](https://numpy.org/) - pixel array manipulation and brightness-to-character mapping

## Getting Started

### Prerequisites

Make sure you have Python 3 installed, then install the dependencies:

```
pip install pillow numpy
```

### Usage

1. Clone the repo
```
git clone https://github.com/meniarallouchi/ascii-art-generator
```
3. Place your image in the same folder as `asciiArtGenerator.py`

4. Open `asciiArtGenerator.py` and update the config at the top of the file:
```python
imageName= "rei.jpg"
outputFile= "ascii_art.txt"
width= 100
```

5. Run the script
```
python asciiArtGenerator.py
```

6. Find your output in your **Downloads** folder as `ascii_art.txt`

Open the `.txt` file with a monospace font (e.g. Notepad on Windows, TextEdit in plain text mode on Mac) for the best result.

## Configuration

Variable     | Default             | Description                                                        
-------------|---------------------|--------------------------------------------------------------------
`imageName`  | `"rei.jpg"`         | Filename of the image in the same folder as the script
`outputFile` | `"ascii_art.txt"`   | Name of the output file saved to Downloads
`width`      | `100`               | Width of the ASCII output in characters, higher means more detail
`chars`      | `['@','#','S',...]` | Character set ordered dark to light

## How It Works

1. The image is loaded and resized to the target width while preserving aspect ratio
2. Height is scaled by `0.55` to compensate for characters being taller than wide in most fonts
3. The image is converted to grayscale so each pixel has a single brightness value (0–255)
4. Each brightness value is mapped to a character from the `chars` list
5. The result is joined into a string and written to a `.txt` file


## Demo

```
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:::::::::::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::;;::::::::::;:::::::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:;;::::::::::::::::::::::;;:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:;;:::::::::::::::::::::::::::;;::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:++::::::::::::::::::::::::::::::;;;;:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+?*:::::::::::::::::::::::::::;;;::;;;;:,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:*%*:::::::::::::::::::::::::::::::;:::;;:;,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:??*:::+;:::::;::::::::::::::::::::::;;::;;;:,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,:???;,;?+:::::+::::::::::::::::::::::::;;::;;;,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,;?%?*:;%*:::;:;+::::::;::::::::::::::::::;;:::+;,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,;?%%?+:%%;::;*:*+::*;::;::::::::::+;:::::::+::::+,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,??%??;?%?::;%*:?+:;?;::+:::::::;;:;;::::;:::;::::;,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,:?%???*S?*:+?%?;%*:+%+::*;::::::**,+*::::;;::;::::;:,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,;?%?%?%%?*;?*+?**?;?%*::?*::::;+*+:*%*::::;;:;;:::+:,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,+???%?%%????::?%;**?%?::??::::?+*+;,+%+:;::+::;;;:+;,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,+;?%??%%???*,,:?+:????;:+?;::?*;**,.,+%+;+:+;:+:+:+;,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,*%??%%?%%;:::;*;;?*%+;;**:*%*+%*::::+%;;*;;:?;;:+;,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,:%???%??%:,::::+;;+;?;++?+%+;?;::::,::?;+*+;?*;;+:,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,*???%??%::?%#?*++;,;+:;*%+,:;*%*?*;:,+%;*?;*?+++,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,*???%%???:;+##?..,.....::.,,:#@%*,;?:%?;;*:+???:,,,,,,,,,,,,,,,,,,,,,,,,
```
