A simple Python script, which prints a random command, installed on the system, but not yet documented by the tldr project. To prevent the "Rerun the command until a fitting command appears"-effect, the seed for the random numbers only changes every 24 hours.

```
Usage: tldrOfTheDay [options]

Options:
  -h, --help            Display this help.
  -v, --version         Display version information.
      --please          Print a new random command, independent of time and day.
```
