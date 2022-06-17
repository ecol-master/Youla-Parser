import requests, json
from .settings import JSON_POST_REQ, URL_ITEM_STRING_TEMPLATE



# def get_monitor_page_info(url_monitor, id_monitor) -> dict:
#     try:
#         response = requests.get(url=f"https://youla.ru{url_monitor}").json()
#         print(response)
#         print("\n")
#         with open(f"reponse_{id_monitor}_one.json", "w") as jsonfile:
#             json.dump(response, jsonfile, ensure_ascii=False)
#         return "YES ITEM"
#     except Exception as error:
#         print(error)
#         return "NO ITEM"

def parse_monitors():
    url = "https://api-gw.youla.io/federation/graphql"
    
    headers = {
        "accept":"*/*",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
    }

    try:
        response = requests.post(url=url, headers=headers, json=JSON_POST_REQ).json()
        
        monitors_datas = response["data"]["feed"]["items"][1:-1]
        all_data = list()
        with open("monitores.json", "w") as jsonfile:
            json.dump(monitors_datas, jsonfile, ensure_ascii=False)
        for one_data in monitors_datas:
            # another_data = get_monitor_page_info(one_data["product"]["url"], one_data["product"]["id"])
            all_data.append(
                {
                    "product_id":one_data["product"]["id"],
                    "product_url":one_data["product"]["url"],
                    "real_price":one_data["product"]["price"]["realPriceText"],
                    "description":one_data["product"]["name"],
                    "city":one_data["product"]["location"]["cityName"]


                }
            )
        
        with open("sorted_monitors.json", "w") as jsonfile:
            json.dump(all_data, jsonfile)
        return "YES"
    except Exception as error:
        print(error)
        return "NO"


