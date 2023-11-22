import logging
from playwright.sync_api import Page
from libraries.utils import get_price_of_first_inventory,sort_products_according_to,click_add_to_cart_for_first_inventory,goto_cart,get_price_of_last_inventory,click_add_to_cart_for_last_inventory
from libraries.utils import checkout,checkout_step_one_continue,get_total_amount_from_checkout_step_two,get_products_amount_with_tax


def test_task1(page: Page):
    logging.info("Executing Task1 test")
    product_prices = []
    sort_products_according_to(page, "hilo")
    product_prices.append(get_price_of_first_inventory(page))
    click_add_to_cart_for_first_inventory(page)
    product_prices.append(get_price_of_last_inventory(page))
    click_add_to_cart_for_last_inventory(page)
    goto_cart(page)
    checkout(page)
    checkout_step_one_continue(page,"Hridhay","Dhapola","404040")
    actual_amount = get_total_amount_from_checkout_step_two(page)
    expected_amount = get_products_amount_with_tax(product_prices)

    assert actual_amount == expected_amount



