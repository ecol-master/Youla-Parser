MAX_PRICE = 200000

JSON_POST_REQ = {
    "operationName":"catalogProductsBoard",
    "variables":{
        "sort":"DEFAULT",
        "attributes":[
            {"slug":"monitory_diagonal_ekrana","value":["9290"],"from":None,"to":None},
            {"slug":"price","value":None,"from":None,"to":MAX_PRICE},{"slug":"categories","value":["monitory"],"from":None,"to":None}
            ],
        "datePublished":None,
        "location":{"latitude":None,"longitude":None,"city":"576d0617d53f3d80945f942c","distanceMax":None},
        "search":"мониторы","cursor":""},
    "extensions":{"persistedQuery":{"version":1,"sha256Hash":"6e7275a709ca5eb1df17abfb9d5d68212ad910dd711d55446ed6fa59557e2602"}}}

URL_ITEM_STRING_TEMPLATE = "https://api.youla.io/api/v1/product/{}/"


"""https://api.youla.io/api/v1/user/58ca4af00cc3da696b60106d?app_id=web/3&uid=62aad4e398079&timestamp=1655439362871
- получение инфы по id пользователя"""