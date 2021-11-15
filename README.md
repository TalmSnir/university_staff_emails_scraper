# Staff emails scraper

Automatically scrape given staff's emails from the TAU phone-book and write them into a csv file.

## Resources

- [selenium with python docs](https://selenium-python.readthedocs.io/)

## Tech Stack

**Client:** Python, Selenium

## Run Locally

Clone the project

```bash
  git clone git@github.com:TalmSnir/university_staff_emails_scraper.git
```

Go to the project directory

```bash
  cd university_staff_emails_scraper
```

install requirments

```bash
pip install -r requirments
```

[Download selenium web driver](https://selenium-python.readthedocs.io/installation.html) and add the exe file to the project directory

Add the desired staff names from TAU University in the emails_scraper.py file

```python
  teachers_list = ['']
```

Run the script

```bash
  python -m emails_scraper
```
