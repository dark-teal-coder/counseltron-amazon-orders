<!-- README file for projects-->

# Counseltron Data Entry Automation

## Metadata

- <ins>Project Owner</ins>: [@dark-teal-coder](github.com/dark-teal-coder)
- <ins>First Published Date</ins>: 2023-02-03

## Project

- **Title**: *Counseltron Data Entry Automation*
- **Difficulty**:
  - [ ] Beginner
  - [x] Intermediate
  - [ ] Advanced
- **Scale**:
  - [x] Small
  - [ ] Medium
  - [ ] Big

## Repository Description

This project is for my data entry job. The job involves an extensive amount of manual repetitive daily tasks. To manage Amazon orders, we need to type in data from papers into or copy and paste data into different apps. Therefore, this project is to automate some of these manual tasks in order to save some time. 

### Manual Daily Task to Manage Amazon Orders

1. Log in to [Amazon Seller Central](https://sellercentral.amazon.ca)
2. Select all orders of the day
3. Print 2 copies of picking slips
4. Order the paper picking slips in both piles so that those under CAD$30 to be sent as 1st class mail by Canada Post come before those as regular parcels
5. Put 1 copy aside
6. Open "E-commerce Spec File" Excel file (see [E-commerce Spec File 2022.JPG](./images/E-commerce%20Spec%20File%202022.JPG))
7. For 1st class mails, use the SKU code on each order to check the shipping cost for a certain quantity of the product/item from the "E-commerce Spec File" Excel file
8. Jot down the shipping cost on the picking slips one by one
9. For regular parcels, use the item code (SKU) on each order to check the dimension (depth x width x height) and weight of the product/item from the "E-commerce Spec File" Excel file
10. Jot down the dimension and weight on the picking slips one by one
11. Open Adagio Order Entry desktop application
12. Create an order list and enter details (product/item info) (see [Adagio Order Details.JPG](./images/Adagio%20Order%20Details.JPG))
13. Check availability of each item in the [Details] tab in the order list (see [Adagio Order Details Availability.JPG](./images/Adagio%20Order%20Details%20Availability.JPG))
14. If some items are out of stock, cancel the corresponding orders on [Amazon Seller Central](https://sellercentral.amazon.ca)
15. Post the new order in Adagio Order Entry
16. Open "E-commerce Calculator" Excel file (see [E-commerce Calculator.JPG](./images/E-commerce%20Calculator.JPG))
17. Choose "AMA00M" spreadsheet
18. Enter Canada's province code, item code (SKU), quantity and "Cost" (unit price)
19. Check if the total before selling fees and sales taxes equals the "Order amount" at the end of the [Details] tab of Adagio Order Entry (see [Adagio Order Details.JPG](./images/Adagio%20Order%20Details.JPG))
20. Print the "AMA00M" spreadsheet result
21. Open "EST Desktop" application (see [Canada Post EST Desktop App.JPG](./images/Canada%20Post%20EST%20Desktop%20App.JPG))
22. Enter login credential
    - Username: Counseltron_LTD
    - Password: **********
23. Click [New] or Press [Ctrl] + [N] to create a new shipping label
24. Enter "Reference #", "Name", "Address Line 1", "Address Line 2" (if any), "City", "Province", "Postal Code", "Contact Phone", "Weight", "Length", "Width", "Height" and "Cost Centre" as "Amazon Marketplace" to create a shipping label
25. Upon entering the information on each label, click [Pricing] to check the shipping price and save it before creating a new one
26. After receiving confirmation from the warehouse, confirm shipment against each other on [Amazon Seller Central](https://sellercentral.amazon.ca)
27. Click [End of Day] to print the shipping labels
28. For those regular parcel shipments, enter the tracking ID  generated by "EST Desktop" on the paper shipping labels

The difference between "Steps to Print Amazon Packing Slips" and "Steps to Print Amazon Packing Slips to PDF" is the printer in Step 9.

### Steps to Print Amazon Packing Slips

1. Go to [Amazon Seller Central](https://sellercentral.amazon.ca)
2. Click [Log in]
3. Fill in the login credential
4. Click the 3-line menu icon in the top left corner
5. Choose [Orders]
6. Choose [Manage Orders]
7. Click [Order date] to select all orders
8. Click [Print Packing Slip(s)]
9. Choose [Kyocera TASKalfa 3500i KX] under "Printer"
10. Click [More settings]
11. Change the settings according to the following:
  - Paper size: A4
  - Scale: 100%
  - Pages per sheet: 1
  - Margins: Default
12. Click [Save]
13. Choose the directory to save the file to
14. Use the file name format "Amazon Manage Orders 2023-02-03"
15. Change the date in the file name to today's date
16. Click [Save]

### Steps to Print Amazon Packing Slips to PDF

1. Go to [Amazon Seller Central](https://sellercentral.amazon.ca)
2. Click [Log in]
3. Fill in the login credential
4. Click the 3-line menu icon in the top left corner
5. Choose [Orders]
6. Choose [Manage Orders]
7. Click [Order date] to select all orders
8. Click [Print Packing Slip(s)]
9. Choose [Save as PDF] under "Printer"
10. Click [More settings]
11. Change the settings according to the following:
  - Paper size: A4
  - Scale: 100%
  - Pages per sheet: 1
  - Margins: Default
12. Click [Save]
13. Choose the directory to save the file to
14. Use the file name format "Amazon Manage Orders 2023-02-03"
15. Change the date in the file name to today's date
16. Click [Save]

## Installation 

### Tools

- Text Editor or Integrated Development Environment (IDE)
  - You can [download the famous text editor Notepad++](https://notepad-plus-plus.org/downloads). 
  - Or, you can [download the popular IDE Visual Studio Code (VS Code)](https://code.visualstudio.com/download). 
- Python 3
  - You can [install Python 3 from python.org](https://www.python.org/downloads). 
- Python Package Installer/Manager `pip`
  - If you installed Python from [python.org](https://www.python.org), you should already have `pip`. If it is not installed, you can use the command `py -m ensurepip --default-pip` to bootstrap it from the standard library. If you are using Linux, you will have to [install the package manager separately](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/). You can find out more about the `pip` tool [here](https://pip.pypa.io/en/stable/getting-started/). 
- Command-line interface (CLI) 
  - You can [install the open-source PowerShell on Windows, Linux and macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) if you do not have or want to use a pre-installed CLI on your local machine. 

### Description

Check if you have Python installed using the command `python --version`, or simply, `python version`, in the CLI. [Git-clone the project repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the local machine. Use the command `py -m pip install package_name` to install the necessary Python libraries. Check out [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) to learn more about `pip install`. Check the top part of the `.py` script file for the list of libraries required. For example, you may need `requests` and `beautifulsoup4` libraries if you see the following lines in the top part of the script file: 
```
import requests
from bs4 import BeautifulSoup
```
If `pip` fails to locate the relevant packages, you may find it at [Python Package Index (PyPI)](https://pypi.org/). Use `python file_name.py` to run the script in a CLI. Or, use an IDE, such as VS Code, to run the script. There will usually be a [Run] button in the top right corner of the opened script file. 

## Credits 

### Contributors 

- [@dark-teal-coder](github.com/dark-teal-coder)

### References 

- [Python Unicode Encode Error](https://blog.finxter.com/python-unicode-encode-error)

&nbsp;

*1st Completion Date: Feb 15, 2023*&emsp;
