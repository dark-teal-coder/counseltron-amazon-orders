<!-- README file for projects-->

# Amazon Order Data Entry Automation

## Metadata

- <ins>Project Owner</ins>: [@dark-teal-coder](github.com/dark-teal-coder)
- <ins>First Published Date</ins>: 2023-02-03

## Project

- **Title**: *Amazon Order Data Entry Automation*
- **Difficulty**:
  - [ ] Beginner
  - [x] Intermediate
  - [ ] Advanced
- **Scale**:
  - [x] Small
  - [ ] Medium
  - [ ] Big

## Repository Description

In Canada, there are a number of small companies who sell products on Amazon Seller Central and hire data entry clerks to help them input and process order data. Many of these small companies cannot afford to use technological tools to process orders and require manual work. To manage Amazon orders, these companies require data entry clerks to type in data from paper orders into or copy and paste the data into different applications, such as Canada Post EST Desktop App, for further processing. However, we have free open-source tools like Python to help us automate some tasks and make our work more efficient and simpler. This project is for the data entry job which involves an extensive amount of manual repetitive data entry tasks on a daily basis. It aims to automate some of these manual tasks in order to save some time.

### General Procedures

This section shows what the job is about in general. The following are the general procedures to process Amazon orders on a daily basis:

#### Steps to Manage Daily Amazon Orders Maually

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
    - Username: Company_Name
    - Password: **********
23. Click [New] or Press [Ctrl] + [N] to create a new shipping label
24. Enter "Reference #", "Name", "Address Line 1", "Address Line 2" (if any), "City", "Province", "Postal Code", "Contact Phone", "Weight", "Length", "Width", "Height" and "Cost Centre" as "Amazon Marketplace" to create a shipping label
25. Upon entering the information on each label, click [Pricing] to check the shipping price and save it before creating a new one
26. After receiving confirmation from the warehouse, confirm shipment against each other on [Amazon Seller Central](https://sellercentral.amazon.ca)
27. Click [End of Day] to print the shipping labels
28. For those regular parcel shipments, enter the tracking ID  generated by "EST Desktop" on the paper shipping labels

### Packing Slips

On "Manage Orders" page of [Amazon Seller Central](https://sellercentral.amazon.ca), we can print packing slips. We have to print the packing slips for the warehouse as they have to include the paper packing slips in the shipments. This cannot be done by computer. But we also have to print another set to write pricing and dimension information on. For both sets, we have to order each so that those orders to be sent as 1st class mail (under CAD$30; no tracking ID required by Amazon) by Canada Post come before those as regular parcels (over CAD$30; tracking ID required by Amazon). See the illustration below.

**Illustration**

Original order (from Amazon):

- Order 01: CAD$34.99
- Order 02: CAD$20.67
- Order 03: CAD$20.67
- Order 04: CAD$36.77
- Order 05: CAD$33.53
- Order 06: CAD$50.83
- Order 07: CAD$316.32
- Order 08: CAD$29.32
- Order 09: CAD$335.92
- Order 10: CAD$41.34

New order:
- Order 02: CAD$20.67
- Order 03: CAD$20.67
- Order 08: CAD$29.32
- Order 01: CAD$34.99
- Order 04: CAD$36.77
- Order 05: CAD$33.53
- Order 06: CAD$50.83
- Order 07: CAD$316.32
- Order 09: CAD$335.92
- Order 10: CAD$41.34

The difference between "Steps to Print Amazon Packing Slips" and "Steps to Print Amazon Packing Slips to PDF" is the printer in Step 9.

#### Steps to Print Amazon Packing Slips

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

#### Steps to Print Amazon Packing Slips to PDF

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

### Python Development Tools

- Python 3
  - [Download and install Python 3 from python.org](https://www.python.org/downloads). 
- Python Package Installer/Manager `pip`
  - If you installed Python from [python.org](https://www.python.org), you should already have `pip`. If it is not installed, you can use the command `py -m ensurepip --default-pip` to bootstrap it from the standard library. If you are using Linux, you will have to [install the package manager separately](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/). You can find out more about the `pip` tool [here](https://pip.pypa.io/en/stable/getting-started/). 
- Text Editor and Integrated Development Environment (IDE)
  - [Download and install the text editor Notepad++](https://notepad-plus-plus.org/downloads). 
  - [Download and install the IDE Visual Studio Code (VS Code)](https://code.visualstudio.com/download). 
  - [Install the web-based app Jupyter Notebook with pip](https://jupyter.org/install#jupyter-notebook)
  - [Install the web-based IDE JupyterLab with pip](https://jupyter.org/install#jupyterlab)
  - [Install Anaconda to get Jupyter Notebook](https://docs.jupyter.org/en/latest/install/notebook-classic.html#installing-jupyter-using-anaconda-and-conda)
- Command-line interface (CLI) 
  - You can [install the open-source PowerShell on Windows, Linux and macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) if you do not have or want to use a pre-installed CLI on your local machine. 

### Python Libraries

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
- [GUI Automation using Python](https://www.geeksforgeeks.org/gui-automation-using-python)

&nbsp;

*1st Completion Date: Feb 15, 2023*&emsp;
