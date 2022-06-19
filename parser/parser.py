import requests, json
from .settings import JSON_POST_REQUESTS_TO_ALL_MONITORS, YOULA_PREFIX_URL
from .xls_writer import XlsWriter


class Parser:
    """
        Class for sending requests to youla-api and sorting data for writing to xls file
    """
    def __init__(self, format_date: str):

        self.__format_date = format_date

        self.__xls_writer = None

    def run_parser(self):
        data = self.__get_json_data()
        
        self.__xls_writer = XlsWriter(self.__format_date, data=data)

        self.__xls_writer.run_xls_writer()
    
    """
        The function generates a cursor parameter for the request until the cards on the page run out.
    """
    def __get_json_data(self) -> list[dict, ...]:
        all_data = self.__get_all_monitors_page_data()        
        run, index = True, 0
        
        while run:
            try:
                cursor = self.__build_cursor(index)
                data = self.__get_all_monitors_page_data(cursor=cursor)
                
                if data == []:
                    raise Exception

                for item in data:
                    all_data.append(item)
                
                index += 1
            except Exception as error:
                run = False

        return all_data


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

    """
        Function build special parameter (cursor) for post request to scroll the page and collect more data
    """
    def __build_cursor(self, index: int):
        template_cursor = "{\"page\":"+ f"{index}" + ",\"totalProductsCount\":" + f"{index * 30 + 30}" +",\"dateUpdatedTo\":1655622904}"
        return template_cursor

    """
        Selects and returns the required fields from the object
    """
    def __get_filtered_data(self, data: list[dict, ...]):
        all_filtered_data = list()

        for product in data:
            try:
                all_filtered_data.append(
                    {
                        "Наименование":product["product"]["name"],
                        "Ссылка на товар":"{}{}".format(YOULA_PREFIX_URL, product["product"]["url"]),
                        "Цена (значение)":product["product"]["price"]["realPrice"]["price"] / 100,
                        "Цена (текст)":product["product"]["price"]["realPriceText"],
                        "Id товара на Юле":product["product"]["id"],
                        "Город":product["product"]["location"]["cityName"]
                    }
                )
            except Exception as error:
                pass

        return all_filtered_data


