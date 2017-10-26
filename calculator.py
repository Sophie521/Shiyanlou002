#!/usr/bin/env python3

import sys
import csv


class Config(object):
    def __init__(self, configfile):
        self.configfile = configfile
        self.config = {}
        fd = open(configfile, 'r')
        for line in fd.readlines():
            tmp = line.split('=')
            #self.config[tmp[0].strip()] = float(tmp[1].strip())
            name = tmp[0].strip()
            value = tmp[1].strip()
            self.config[name] = float(value)

    def get_config(self, config_key):
        return self.config[config_key]

class UserData(object):
    def __init__(self, userdatafile):
        self.userdata = {}
        fd = open(userdata, 'r')
        for line in fd.readlines():
            tmp = line.split(',')
            #self.userdata[tmp[0].strip()] = float(tmp[1].strip())
            num = tmp[0].strip()
            salary = tmp[1].strip()
            self.userdata[num] = salary

class Calculator(object):
    def __init__(self, userdatafile):
        self.userdata = {}


    def taxable_income(self, salary, insurance):
        return salary - float(insurance) - 3500

    def taxpayable(self, taxable_income):
        tax_payable = 0
        if taxable_income < 0:
            tax_payable = 0
        elif taxable_income < 1500:
            tax_payable = taxable_income * 0.03
        elif taxable_income < 4500:
            tax_payable = (taxable_income * 0.1) - 105
        elif taxable_income < 9000:
            tax_payable = (taxable_income * 0.2) - 555
        elif taxable_income < 35000:
            tax_payable = (taxable_income * 0.25) - 1005
        elif taxable_income < 55000:
            tax_payable = (taxable_income * 0.3) - 2755
        elif taxable_income < 80000:
            tax_payable = (taxable_income * 0.35) - 5505
        else:
            tax_payable = (taxable_income * 0.450) - 13505
        return tax_payable


    def min_max(self, num, salary):
        min_insurance = float(Config.get_config("JiShuL"))
        max_insurance = float(Config.get_config('JiShuH'))
        #for num, salary in UserData.userdata.items():
        if salary < min_insurance:
            insurance = min_insurance * 0.165
        elif salary > max_insurance:
            insurance = max_insurance * 0.165
        else:
            insurance = salary * 0.165
        return insurance
'''
    def sum_rate(self):
        rate_name = ['YangLao', 'YiLiao', 'ShiYe', 'GongShang', 'ShengYu', 'GonJiJin']
        sum_rate = 0
        for i in rate_name:
            sum_rate = Config.get_config(i) + sum_rate
        return sum_rate
'''

    def final_salary(self, num, salary):
	insurance = self.min_max(salary)
        tax_payable = self.taxpayable(salary)
        final_salary = salary - insurance - tax_payable
	output = "{},{},{:.2f},{:.2f},{:.2f}".format(num, salary, insurance,\
tax_payable, final_salary)
        # print(output)
        self.output += output

class Output(object):

    output = ''
    userdata = {}
    for i in userdata:
        final_salary(i,int(userdata[i]))

    def dumptofile(self, outfile):
        with open(outfile, 'a') as file:
            file.write(self.output)



if __name__ == '__main__':
    args = sys.argv[1:]
    index_c = args.index('-c')
    index_d = args.index('-d')
    index_o = args.index('-o')
    configfile = args[index_c + 1]
    userdata = args[index_d + 1]
    outfile = args[index_o + 1]

    config = Config(configfile)
    user = UserData(userdata)
    user = Calculator(userdata)
    user = UserData(outfile)
    
   # UserData.dumptofile(outfile)
    out = Output(outfile)
    Output.dumptofile(outfile)








