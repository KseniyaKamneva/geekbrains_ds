"""
Created on Mon May 23 02:57:16 2022

@author: Ксения Камнева
"""

import json
with open('7.json', 'w') as fw:
    with open('7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'average profit': round(sum([int(i) for i in profit.values() if int(i) > 0])/
                           len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, fw, ensure_ascii=False, indent=4)
