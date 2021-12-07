# SinaStockBasicInfoCollect



## Brief

This program scrapes informations about Chinese stocks online.
Include basic company informations from Sina Stock website and current Price information from Xueqiu website.

## Dependencies

Before using, make sure you have installed [python](https://www.python.org/downloads/) (version 3.6 or newer).

The program requires some python libraries to be installed before run. 

Run following commands using to install dependencies:

1. requests
```sh
pip3 install -r requirements.txt
```
## Instruction of use

1. Clone the repo

2. To run the program, use command 
```sh
python3 run.py
```


Input your desired beginning and ending company stock ID to collect the basic information about all those companies in the middle. 

Example: 1 (equivalent to 000001)

The program will generate a new ```.xlsx``` file in the same root where you saved ```InfoCollector.py```


## UPDATES 12/07/2021

Added Xueqiu website for current date's price info