# desktop-bootstrap
Start and resize applications

## Dependencies

- Python 3.x
- wmctrl 

`sudo apt install wmctrl`

## Usage

The `desktop-bootstrap.py` accepts the following arguments:

- **command**: command to open an application, (e.g, firefox, google-chrome)
- **application name**: name of application, this argument is used to check with `wmctrl` if application has started, some applications has the name different from the command (e.g, Google Chrome (google-chrome)).
- **Axios x**: Which point of axios y the application will be posiotioned.
- **Axios y**: Which point of axios y the application will be posiotioned.
- **Window width**: To which width the application will be resized.
- **Window height**: To which height the application will be resized.
- **-- file**: You can use a configuration file and pass it with this argument instead of execute `desktop-bootstrap.py` file several times.

## Configuration file

Each line receives the same arguments from command line::

`<command> <Application name> <X Axios> <Y Axios> <Window width> <Window height>`

Example of a configuration file:

```
insomnia insomnia 1920 0 1720 1440
dbeaver dbeaver 3640 0 1720 1440
usr/bin/python3.8 google-chrome google 5360 0 1720 1410 https://github.com/ricardo93borges https://dev.to/ricardo93borges
```

## Examples:

The arguments must be in this order:

`/usr/bin/python3.8 <command> <Application name> <X Axios> <Y Axios> <Window width> <Window height>`

Or:

`/usr/bin/python3.8 --file <path/to/configuration/file>`

Using all arguments in the command line:

`insomnia insomnia 1920 0 1720 1440`

Some browsers accepts as argument the websites it will open when start up, each website will be open in a different tab, for example

`/usr/bin/python3.8 google-chrome google 5360 0 1720 1410 https://github.com/ricardo93borges https://dev.to/ricardo93borges`

Using a configuration file:

`/usr/bin/python3.8 /path/to/desktop-bootstrap.py --file /path/to/config-sample.txt`

## Shortcut

The file `desktop-bootstrap.sh` can be executed when a keyboard shortcut is used, the keyboard shortcut setup depends on your OS.
