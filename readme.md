# Script for collecting information about monitors from the Youla marketplace

## Brief description of the project
---
### Libraries for the script

```
pip install requests

pip install xlsxwriter
```

### Brief description of the project

Startup project file - main.py

It creates an object of the Parser class and starts the script.

The requests module sends requests to the server.
xlsriter helps to work with xls format data. 

##

Code examples

```py
# Function for getting product data

def __get_all_monitors_page_data(self, cursor=None) -> list[dict, ...]:
        if cursor is not None:
            JSON_POST_REQUESTS_TO_ALL_MONITORS["variables"]["cursor"] = cursor
        
        url = "https://api-gw.youla.io/federation/graphql"
        headers = {
            "Accept":"*/*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
        }

        response = requests.post(url=url, headers=headers,
            json=JSON_POST_REQUESTS_TO_ALL_MONITORS).json()
        
        return self.__get_filtered_data(response["data"]["feed"]["items"][1:-1])
```

```py
# Function to create a cursor parameter for scrolling the page

def __build_cursor(self, index: int):
    template_cursor = "{\"page\":"+ f"{index}" + ",\"totalProductsCount\":" + f"{index * 30 + 30}" +",\"dateUpdatedTo\":1655622904}"
    return template_cursor
```

```py

# Running a script

from parser import Parser
import datetime


def get_format_date() -> str:
   format_date = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M")
   return format_date

def main():
   format_date = get_format_date()
   parser = Parser(format_date=format_date)
   parser.run_parser()

if __name__ == "__main__":
    main()
```