1. #### Install Homebrew (if needed)
`curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh`

`echo "Homebrew install complete"`

---

### Install python3
`brew install python3`

`python3 -V`

`pip3 -V`

---

### Install pipenv
`pip3 install pipenv`

`pipenv --version`

---

### Download Chromedriver and move (mv) to /usr/local/bin
###### https://chromedriver.chromium.org/downloads
`mv /path/to/ChromeDriver /usr/local/bin`

---

### Clone this repo

---

### Create `config.json` on local machine with the following template
```
{
	"browser": "Chrome",
	"implicit_wait": 10,
	"email": "",
	"pw": "",
	"url": ""
}
```

---

### Modify conftest.py to change config_local location

---

### Run pipenv install to install dependencies 
`pipenv install`

---

### Run pipenv run python -m pytest to verify that the framework can run tests
`pipenv run python -m`

---

### Run below to run tests
`pipenv run python -m pytest`