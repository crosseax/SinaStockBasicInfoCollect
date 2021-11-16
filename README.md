# SinaStockBasicInfoCollect



## Brief

This is a straightforward python implementation to specifically grab basic infos about IPO companies in China from Sina Stock website.

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
python3 InfoCollectro.py
```


Input your desired beginning and ending company stock ID to collect the basic information about all those companies in the middle. 

Example: 1 (equivalent to 000001)

The program will generate a new ```.xlsx``` file in the same root where you saved ```InfoCollector.py```
