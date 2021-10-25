1. #### Install Homebrew (if needed)
- `curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh`

- `echo "Homebrew install complete"`

2. #### Install python3
- `brew install python3`

- `python3 -V`

- `pip3 -V`

3. #### Install pipenv
- `pip3 install pipenv`

- `pipenv --version`

4. #### Download Chromedriver and move (mv) to /usr/local/bin
- https://chromedriver.chromium.org/downloads
- `mv /Users/yourusername/Downloads/chromedriver /usr/local/bin/`

5. #### Clone this repo

6. #### Create `config.json` on local machine with the following template
```
{
	"browser": "Chrome",
	"implicit_wait": 10,
	"email": "",
	"pw": "",
	"url": ""
}
```

7. #### Modify conftest.py to change config_local location

8. #### Run pipenv install to install dependencies 
- `pipenv install`

9. #### Run pipenv run python -m pytest to verify that the framework can run tests
- `pipenv run python -m`

10. #### Run below to run tests
- `pipenv run python -m pytest` 

- `pipenv run python -m pytest -s` 