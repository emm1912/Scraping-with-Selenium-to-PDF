# Scraping with Selenium and saving info to PDF's 30-MAY-2023
Doing some freelance jobs, a customer asked me to retrieve the articles of a web page for research puposes (circa. 100+ articles) and save all the individual articles with
the corresponding title inside individual PDF files.
So here is the code I used, the code has some comments for help understanding what's going on.

###### Note. The body of the articles is missing here because I used the premium account of the customer to login, for this version instead of the whole body of the article I used the little summary that is readable (with no premium account) as the article itself.

## Description

For this project I used selenium to get to the page and obtain all the url's of every article and then with reportlab I saved the gathered info into several
pdf files (you can find them inside the pdf folder), I just include 2 pdf's but feel free to run the script if you want the get the whole list.

Next, the structure of the project:


<code>
├── main.py
├── pdf
│   ├── 1-1815, slag bij Waterloo
│   └── 2-Aan dek
├── README.md
└── requirements.txt
</code>


### Folder description

#### pdf:
Here you can find all the created pdf's


## How to use it?
With requirements.txt create your venv and run main.py.


###### Selenium info links
1. [Selenium Documentation](https://www.selenium.dev/selenium/docs/api/py/api.html)
2. [Page Objects](https://selenium-python.readthedocs.io/page-objects.html)
3. [Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)


###### Reportlabs Info/Documentation
[Reportlabs pdf](https://docs.reportlab.com/reportlab/userguide/ch1_intro/)
