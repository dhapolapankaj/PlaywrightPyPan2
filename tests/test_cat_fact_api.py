


import logging
from playwright.sync_api import APIRequestContext


def test_task2(api_request_context: APIRequestContext):
    logging.info("Executing Task2")
    cat_breeds = api_request_context.get("/breeds?limit=100")
    assert cat_breeds.ok

    cat_breeds_json = cat_breeds.json()['data']
    cat_breeds_with_semi_long_coat=[]
    for cat in cat_breeds_json:
        if cat['coat'] == "Semi-long":
            cat_breeds_with_semi_long_coat.append(cat['breed'])

    logging.info("Below are the names of cats with semi long coat")
    logging.info(", ".join(cat_breeds_with_semi_long_coat))




