# convert string with Chinese number into pure number
def chinese_number_convert(inputStr):
    if '万' in inputStr:
        inputStr = inputStr.replace('万', '')
        inputStr = str(int(float(inputStr) * 10000))
    if '亿' in inputStr:
        inputStr = inputStr.replace('亿', '')
        inputStr = str(int(float(inputStr) * 100000000))
    return inputStr

# specifically getting rid of one unit character in xueqiu data
def xueqiu_data_adjustment(inputStr):
    result = inputStr.split('：')[1]
    if '手' in result:
        result = result.replace('手', '')
    result = chinese_number_convert(result)
    return result