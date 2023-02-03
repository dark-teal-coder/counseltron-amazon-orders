import pdfplumber
import pandas as pd
from datetime import datetime


order = {}
ca_province_code = {"ALBERTA":"AB", 
    "BRITISH COLUMBIA":"BC", 
    "MANITOBA":"MB", 
    "NEW BRUNSWICK":"NB", 
    "NOVA SCOTIA":"NS", 
    "NEWFOUNDLAND":"NL", 
    "YUKON":"YK", 
    "QUEBEC":"QC", 
    "NUNAVUT":"NU", 
    "ONTARIO":"ON", 
    "PRINCE EDWARD ISLAND":"PE", 
    "SASKATCHEWAN":"SK", 
    "Québec":"QC"}


def get_pdf_page_values(pdf, page_num): 
    page = pdf.pages[page_num]
    page_text = page.extract_text()
    # print(page_text)
    page_text_list = page_text.split('\n')
    # print(page_text_list)
    ## Trim white spaces
    page_text_list = [line.strip() for line in page_text_list]
    # print(page_text_list)
    print("-"*10)
    print(f"Lines on page {page_num + 1}: {len(page_text_list)}")

    ## Customer Name
    i_custname = page_text_list.index("Ship To:") + 1
    v_custname = page_text_list[i_custname].title()
    order.update({"Customer Name": v_custname})
    ## Order ID
    i_order_id = page_text_list.index("Canada") + 1
    v_order_id = page_text_list[i_order_id][-19:] ## 19-digit order ID
    order.update({"Order ID": v_order_id})
    ## SKU 
    result = [s for s in page_text_list if s.startswith("SKU")]
    v_sku = result[0][5:] ## Remove the 1st 5 characters
    order.update({"SKU": v_sku})
    ## Unit Price 
    result = [s for s in page_text_list if s.startswith("Item subtotal")]
    i_item_sub = page_text_list.index(result[0])
    v_unit_price = float(page_text_list[i_item_sub - 1].split("CAD$")[1])
    order.update({"Unit Price (CAD$)": v_unit_price})
    ## Quantity
    # Should use the string before "Item subtotal" instead because there might be more than 1 item in the order
    i_quantity = page_text_list.index("Quantity  Product Details Unit price Order Totals")
    v_quantity = int(page_text_list[i_quantity + 1].split()[0]) 
    order.update({"Quantity": v_quantity})
    ## Grand Total
    result = [s for s in page_text_list if s.startswith("Grand total:")]
    v_grand_total = float(result[0][17:])
    order.update({"Grand Total (CAD$)": v_grand_total})
    ## Address 
    i_canada = page_text_list.index("Canada")
    i_before = i_custname
    i_after = i_canada
    v_address = page_text_list[i_before+1:i_after]
    order.update({"Address": v_address})
    ## Address Line 1
    v_add_line_1 = v_address[0]
    order.update({"Address Line 1": v_add_line_1})
    ## City
    v_city = v_address[-1].split(",")[0].title()
    order.update({"City": v_city})
    
    return order


now = datetime.now()
today_date = now.strftime(r"%Y-%m-%d")
print("Today's date:", today_date)

with pdfplumber.open(f"Amazon Manage Orders {today_date}.pdf") as pdf:
    num_of_pages = len(pdf.pages)
    print(f"Number of pages in the current PDF: {num_of_pages}")
    for i in range(num_of_pages):
        order = get_pdf_page_values(pdf, i)
        for value in order.values(): 
            print(value)
        print("-"*10)
