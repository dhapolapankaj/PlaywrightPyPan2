from playwright.sync_api import Playwright
import libraries.test_data as data
import libraries.locators as locators
from decimal import Decimal
from re import sub

def sort_products_according_to(page,sort_value):
    page.locator(locators.inventory_page["products_sorter"]).select_option(sort_value)

def get_price_of_first_inventory(page):
    return page.query_selector(locators.inventory_page["first_inventory_price"]).text_content()

def click_add_to_cart_for_first_inventory(page):
    page.query_selector(locators.inventory_page["first_inventory_add_to_cart"]).click()

def get_price_of_last_inventory(page):
    return page.query_selector(locators.inventory_page["last_inventory_price"]).text_content()

def click_add_to_cart_for_last_inventory(page):
    page.query_selector(locators.inventory_page["last_inventory_add_to_cart"]).click()

def goto_cart(page):
    page.query_selector(locators.inventory_page["cart"]).click()

def checkout(page):
    page.query_selector(locators.cart_page["checkout_button"]).click()

def checkout_step_one_continue(page,first_name,last_name, zip):
    page.query_selector(locators.check_out_step_one["first_name_textbox"]).fill(first_name)
    page.query_selector(locators.check_out_step_one["last_name_textbox"]).fill(last_name)
    page.query_selector(locators.check_out_step_one["zip_textbox"]).fill(zip)
    page.query_selector(locators.check_out_step_one["continue_button"]).click()



def get_total_amount_from_checkout_step_two(page):
    return Decimal(sub(r'[^\d.]','',page.query_selector(locators.check_out_step_two["total_amount"]).text_content())) 

def get_products_amount_with_tax(product_prices:list[str]):
    products_amount = sum([ Decimal(sub(r'[^\d.]','',p)) for p in product_prices ])
    products_amount = products_amount + (products_amount * Decimal(data.tax_percent) / Decimal('100'))
    return products_amount

