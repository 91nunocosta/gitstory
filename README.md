
GitStory is a simple library to tell git commit histories.

#  Pre-requirements

1. python3 installed
2. mongodb installed and running

# How to run
1. install python requirements, `pip install -r requirements.txt`
2. set environment variables:
    1. ensure that the values in `env.sh` are suitable;
    2. run `source env.sh`
3. run the _gitstory_ script, `python3 gitstory <repo url>`

# How to run tests

1. install pytest, `pip install pytest`
2. run `python3 -m pytest`
