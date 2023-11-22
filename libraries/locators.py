login_page = {
    "username_textbox" : "//input[@id='user-name']",
    "password_textbox": "//input[@id='password']",
    "login_button":"//*[@id='login-button']"
}

inventory_page = {
    "products_header" : "//div[@id='inventory_filter_container']//div[@class='product_label']",
    "products_sorter" : "//select[@class='product_sort_container']",
    "first_inventory_price" : "//div[@class='inventory_item']//div[@class='inventory_item_price']",
    "first_inventory_add_to_cart":"//div[@class='inventory_item']//button[string()='ADD TO CART']",
    "cart":"//div[@id='shopping_cart_container']/a",
    "last_inventory_price" : "(//div[@class='inventory_item']//div[@class='inventory_item_price'])[last()]",
    "last_inventory_add_to_cart":"(//div[@class='inventory_item']//button[string()='ADD TO CART'])[last()]"

}

cart_page = {
    "checkout_button" : "//a[string()='CHECKOUT']"

}

check_out_step_one = {
    "first_name_textbox" : "//input[@id='first-name']",
    "last_name_textbox" : "//input[@id='last-name']",
    "zip_textbox" : "//input[@id='postal-code']",
    "continue_button":"//input[@value='CONTINUE']"
}

check_out_step_two = {
    "total_amount" : "//div[@id='checkout_summary_container']//div[@class='summary_total_label']"

}
