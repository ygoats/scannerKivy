#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:51:01 2020

@ygoats
"""

import apiData
import re
from binance.client import Client
from time import sleep
import datetime
from binance.enums import *

client = Client(apiData.APIKey, apiData.SecretKey) 
interval= Client.KLINE_INTERVAL_5MINUTE
limit=4
y = 0
symbol_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LINKUSDT', 'SXPUSDT', 'UNIUSDT', \
               'SOLUSDT', 'SRMUSDT', 'NEARUSDT']

def timeStamper():
    time_res = client.get_server_time()
    timestamp = (int(time_res['serverTime']/1000))
    datetime_time = datetime.datetime.fromtimestamp(timestamp)
    print(datetime_time)

def is_empty_or_blank(msg):
    """ This function checks if given string is empty
     or contain only shite spaces"""
    return re.search("^\s*$", msg)

def is_usdt(msg):
    return re.search("USDT", msg)
    
        
def strategy_Data():
    PCE = client.get_klines(symbol=symbol_list[0+y], interval=interval, limit=4)
    percentageRise = ((float(PCE[3][4])-float(PCE[3][1]))/float(PCE[3][1]))*100
    lastThreeVol = (float(PCE[2][5])+float(PCE[1][5])+float(PCE[0][5]))
    lastVol = (float(PCE[3][5]))
    print("PercentageRise: ", + round(percentageRise,2))
    volComp = lastVol / lastThreeVol
    print("VolMultiplier: ", + round(volComp,2))
    if volComp > 2.50 and percentageRise > 1.00:
        print('Volume Confirmation')
        print('Price Confirmation Buy')
        placeOpenOrder()
        print('Algorithm Order Has Been Placed')
      
def checkBalance():
    balance = client.get_asset_balance(asset='USDT')
    print('Balance: ' + balance['free'])
    
def checkTradeBalance():
    balance = client.get_asset_balance(asset='USDT')
    PCE = client.get_klines(symbol=symbol_list[0+y],interval=interval, limit=limit)
    balT = balance['free']
    aT = PCE[0][4]
    abT = (float(balT) / float(aT)) * .50
    print('50% Trade Allocation: ' + str(abT))
    
def placeOpenOrder():
    dataC = client.get_klines(symbol=symbol_list[0+y],interval=interval, limit=limit)
    tb  = dataC[0][4]
    priceF = float(tb) * .998
    print(round(priceF,2))
    
    order = client.create_order(
    symbol=symbol,
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=quantity,
    price=round(priceF,2))
    
def placeCloseOrder():
    trades = client.get_margin_trades(symbol=symbol_list[0+y], limit=1)
    tp = trades[0]['price'] 
    targetF = round(float(tp) * 1.05, 2)
    stopF = round(float(tp) * .974, 2)
    stopFL = round(float(stopF) *.976, 2)
    balance = client.get_asset_balance(asset='USDT')
    quantity = balance['free']
    
    print('Target: ' + str(targetF) + ' Stop: ' 
          + str(stopF) + ' StopLimitMin: ' + str(stopFL)
          + ' Quantity: ' + str(quantity))
    
    order = client.create_oco_order(
    symbol=symbol,
    side=SIDE_SELL,
    quantity=quantity,
    price=round(targetF, 2),
    stopPrice=round(stopF, 2),
    stopLimitPrice=round(stopFL, 2),
    stopLimitTimeInForce='GTC')

def cancelOpenOrder():
    orderO = client.get_open_orders(symbol=symbol_list[0+y])
    stopCancel = orderO[0]['orderId']
    result = client.cancel_order(
    symbol=symbol,
    orderId=stopCancel)
