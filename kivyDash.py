#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:51:01 2020

@ygoats
"""

from kivy.app import App
from kivy.uix.widget import Widget
import time
from kivy.properties import ObjectProperty

from functools import partial
from kivy.lang import Builder
from kivy.clock import Clock

from binance.client import Client
import apiData

from kivy.uix.button import Button
import telegram_send

from buildString import *

from time import sleep

from functions import *
from binance.enums import *

import re

import kivy.utils

client = Client(apiData.APIKey, apiData.SecretKey) 
limit=4

symbol_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LINKUSDT', 'DOTUSDT', 'UNIUSDT', \
               'BATUSDT', 'ADAUSDT', 'NEARUSDT']

#red = [1, 0, 0, 1]  
#green = [0, 1, 0, 1]  
#blue = [0, 0, 1, 1]  
#purple = [1, 0, 1, 1]  

buildString()

class updateData(Widget):
    
    def flashAlgoM(self, x, *args):
        prList = []  
        self.labe50.text = ('Checking Momo Algo')
        for x in range(9):
            klines = client.get_klines(symbol=symbol_list[0+x],interval=KLINE_INTERVAL_5MINUTE, limit=4)
            percentageRise = round(((float(klines[3][4]) - float(klines[2][4])) / float(klines[3][4])) * 100,2)
            prList.append(percentageRise)
            lastThreeVol = (float(klines[2][5])+float(klines[1][5])+float(klines[0][5]))
            lastVol = (float(klines[3][5]))
            volComp = int(lastVol) / int(lastThreeVol)   
            if volComp > 2.00 and percentageRise < -0.05:
                if x == 0:
                    self.labe39.background_color = 1, 0, 0, 1
                    self.labe39.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 1:
                    self.labe40.background_color = 1, 0, 0, 1
                    self.labe40.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 2:
                    self.labe41.background_color = 1, 0, 0, 1
                    self.labe41.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 3:
                    self.labe42.background_color = 1, 0, 0, 1
                    self.labe42.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 4:
                    self.labe43.background_color = 1, 0, 0, 1
                    self.labe43.text = ('Sell  Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 5:
                    self.labe44.background_color = 1, 0, 0, 1
                    self.labe44.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 6:
                    self.labe45.background_color = 1, 0, 0, 1
                    self.labe45.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 7:
                    self.labe46.background_color = 1, 0, 0, 1
                    self.labe46.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                if x == 8:
                    self.labe47.background_color = 1, 0, 0, 1
                    self.labe47.text = ('Sell Signal' + "\n" + symbol_list[0+x])
                    self.labe48.text = ('DropVol ' + symbol_list[0+x])
                    
            if volComp > 2.00 and percentageRise > 0.05:
                if x == 0:
                    self.labe39.background_color = 0, 1, 0, 1
                    self.labe39.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 1:
                    self.labe40.background_color = 0, 1, 0, 1
                    self.labe40.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 2:
                    self.labe41.background_color = 0, 1, 0, 1
                    self.labe41.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 3:
                    self.labe42.background_color = 0, 1, 0, 1
                    self.labe42.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 4:
                    self.labe43.background_color = 0, 1, 0, 1
                    self.labe43.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 5:
                    self.labe44.background_color = 0, 1, 0, 1
                    self.labe44.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 6:
                    self.labe45.background_color = 0, 1, 0, 1
                    self.labe45.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 7:
                    self.labe46.background_color = 0, 1, 0, 1
                    self.labe46.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
                if x == 8:
                    self.labe47.background_color = 0, 1, 0, 1
                    self.labe47.text = ('Buy Signal' + "\n" + symbol_list[0+x])
                    self.labe49.text = ('PopVol' + symbol_list[0+x])
    
    def flashAlgoX(self, x, *args):
        self.labe37.text = ('Checking 521smaX ALGO')
        for v in range(9):
            listA = []
            listB = []
            listC = []
            listD = []
                
            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_5MINUTE, limit=7)
        
            total=0    
            for x in range(5):
                grabData = SCE[5-x][4]
                listA.append(grabData)
            for t in range(5):
                total = total + float(listA[0+t])
            smaFiveClosed = total / 5
        

            total=0
            for x in range(5):
                grabData = SCE[4-x][4]
                listB.append(grabData)
            for t in range(5):
                total = total + float(listB[0+t])
            smaFivePrior = total / 5
        
            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_15MINUTE, limit=23)
        
            total=0
            for x in range(21):
                grabData = SCE[21-x][4]
                listC.append(grabData)
            for t in range(21):
                total = total + float(listC[0+t])
            sma21Closed = total / 21
                
        
            total=0
            for x in range(21):
                grabData = SCE[20-x][4]
                listD.append(grabData)
            for t in range(21):
                total = total + float(listD[0+t])
            sma21Prior = total / 21
    
            if smaFiveClosed > sma21Closed and smaFivePrior < sma21Prior:
                if v == 0:
                    self.labe26.background_color = 0, 1, 0, 1
                    self.labe26.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 1:
                    self.labe27.background_color = 0, 1, 0, 1
                    self.labe27.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 2:
                    self.labe28.background_color = 0, 1, 0, 1
                    self.labe28.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 3:
                    self.labe29.background_color = 0, 1, 0, 1
                    self.labe29.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 4:
                    self.labe30.background_color = 0, 1, 0, 1
                    self.labe30.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 5:
                    self.labe31.background_color = 0, 1, 0, 1
                    self.labe31.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 6:
                    self.labe32.background_color = 0, 1, 0, 1
                    self.labe32.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 7:
                    self.labe33.background_color = 0, 1, 0, 1
                    self.labe33.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                if v == 8:
                    self.labe34.background_color = 0, 1, 0, 1
                    self.labe34.text = ('Cross From Bottom ' + "\n" + symbol_list[0+v])
                    self.labe36.text = ('XBOT ' + symbol_list[0+v])
                         
            if smaFiveClosed < sma21Closed and smaFivePrior > sma21Prior:
                if v == 0:
                    self.labe26.background_color = 1, 0, 0, 1
                    self.labe26.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 1:
                    self.labe27.background_color = 1, 0, 0, 1
                    self.labe27.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 2:
                    self.labe28.background_color = 1, 0, 0, 1
                    self.labe28.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 3:
                    self.labe29.background_color = 1, 0, 0, 1
                    self.labe29.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 4:
                    self.labe30.background_color = 1, 0, 0, 1
                    self.labe30.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 5:
                    self.labe31.background_color = 1, 0, 0, 1
                    self.labe31.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 6:
                    self.labe32.background_color = 1, 0, 0, 1
                    self.labe32.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 7:
                    self.labe33.background_color = 1, 0, 0, 1
                    self.labe33.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
                if v == 8:
                    self.labe34.background_color = 1, 0, 0, 1
                    self.labe34.text = ('Cross From Top ' + "\n" + symbol_list[0+v])
                    self.labe35.text = ('XTOP ' + symbol_list[0+v])
            
    def setTextBack1(self, x, *args):
        self.labe9.text = ('Check Daily % Rise')
        prList = []
        for x in range(9):
            klines = client.get_klines(symbol=symbol_list[0+x],interval=KLINE_INTERVAL_1DAY, limit=limit)
            percentageRise = round(((float(klines[3][4]) - float(klines[2][4])) / float(klines[3][4])) * 100,2)
            prList.append(percentageRise)
            if prList[0+x] > 0.001:
                if x == 0:
                    self.labe.background_color =  0,1,0,1
                if x == 1:
                    self.labe1.background_color = 0,1,0,1
                if x == 2:
                    self.labe2.background_color = 0,1,0,1
                if x == 3:
                    self.labe3.background_color = 0,1,0,1
                if x == 4:
                    self.labe4.background_color = 0,1,0,1
                if x == 5:
                    self.labe5.background_color = 0,1,0,1
                if x == 6:
                    self.labe6.background_color = 0,1,0,1
                if x == 7:
                    self.labe7.background_color = 0,1,0,1
                if x == 8:
                    self.labe8.background_color = 0,1,0,1
            elif prList[0+x] < -0.001:
                if x == 0:
                    self.labe.background_color = 1,0,0,1
                if x == 1:
                    self.labe1.background_color = 1,0,0,1
                if x == 2:
                    self.labe2.background_color = 1,0,0,1
                if x == 3:
                    self.labe3.background_color = 1,0,0,1
                if x == 4:
                    self.labe4.background_color = 1,0,0,1
                if x == 5:
                    self.labe5.background_color = 1,0,0,1
                if x == 6:
                    self.labe6.background_color = 1,0,0,1
                if x == 7:
                    self.labe7.background_color = 1,0,0,1
                if x == 8:
                    self.labe8.background_color = 1,0,0,1
                    
        self.labe.text = symbol_list[0] + "\n" + 'Daily % Rise' + "\n" + str(prList[0]) + ('%')
        self.labe1.text = symbol_list[1] + "\n" + 'Daily % Rise' + "\n" + str(prList[1]) + ('%')
        self.labe2.text = symbol_list[2] + "\n" + 'Daily % Rise' + "\n" + str(prList[2]) + ('%')
        self.labe3.text = symbol_list[3] + "\n" + 'Daily % Rise' + "\n" + str(prList[3]) + ('%')
        self.labe4.text = symbol_list[4] + "\n" + 'Daily % Rise' + "\n" + str(prList[4]) + ('%')
        self.labe5.text = symbol_list[5] + "\n" + 'Daily % Rise' + "\n" + str(prList[5]) + ('%')
        self.labe6.text = symbol_list[6] + "\n" + 'Daily % Rise' + "\n" + str(prList[6]) + ('%')
        self.labe7.text = symbol_list[7] + "\n" + 'Daily % Rise' + "\n" + str(prList[7]) + ('%')
        self.labe8.text = symbol_list[8] + "\n" + 'Daily % Rise' + "\n" + str(prList[8]) + ('%')
        
    def setTextBack2(self, x, *args):
        
        self.labe22.text = ('Trend Bullish or Bearish')
        for v in range(9):
            listA = []
            listB = []

            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_1DAY, limit=7)
        
            total=0    
            for x in range(5):
                grabData = SCE[5-x][4]
                listA.append(grabData)
            for t in range(5):
                total = total + float(listA[0+t])
            smaFiveClosed = total / 5
        
            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_1DAY, limit=23)
        
            total=0
            for x in range(21):
                grabData = SCE[21-x][4]
                listB.append(grabData)
            for t in range(21):
                total = total + float(listB[0+t])
            sma21Closed = total / 21
                
            if smaFiveClosed > sma21Closed:
                if v == 0:
                    self.labe13.background_color = 0,1,0,1
                    self.labe13.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 1:
                    self.labe14.background_color = 0,1,0,1
                    self.labe14.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 2:
                    self.labe15.background_color = 0,1,0,1
                    self.labe15.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 3:
                    self.labe16.background_color = 0,1,0,1
                    self.labe16.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 4:
                    self.labe17.background_color = 0,1,0,1
                    self.labe17.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 5:
                    self.labe18.background_color = 0,1,0,1
                    self.labe18.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 6:
                    self.labe19.background_color = 0,1,0,1
                    self.labe19.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 7:
                    self.labe20.background_color = 0,1,0,1
                    self.labe20.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                if v == 8:
                    self.labe21.background_color = 0,1,0,1
                    self.labe21.text = ('Trend UP ' + "\n" + symbol_list[0+v])
                         
            if smaFiveClosed < sma21Closed:
                if v == 0:
                    self.labe13.background_color = 1,0,0,1
                    self.labe13.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 1:
                    self.labe14.background_color = 1,0,0,1
                    self.labe14.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 2:
                    self.labe15.background_color = 1,0,0,1
                    self.labe15.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 3:
                    self.labe16.background_color = 1,0,0,1
                    self.labe16.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 4:
                    self.labe17.background_color = 1,0,0,1
                    self.labe17.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 5:
                    self.labe18.background_color = 1,0,0,1
                    self.labe18.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 6:
                    self.labe19.background_color = 1,0,0,1
                    self.labe19.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 7:
                    self.labe20.background_color = 1,0,0,1
                    self.labe20.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
                if v == 8:
                    self.labe21.background_color = 1,0,0,1
                    self.labe21.text = ('Trend DOWN ' + "\n" + symbol_list[0+v])
    
    def setTextBack3(self, x, *args):
        
        for v in range(9):
            listA = []
            listB = []

            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_5MINUTE, limit=7)
        
            total=0    
            for x in range(5):
                grabData = SCE[5-x][4]
                listA.append(grabData)
            for t in range(5):
                total = total + float(listA[0+t])
            smaFiveClosed = total / 5
        
            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_15MINUTE, limit=23)
        
            total=0
            for x in range(21):
                grabData = SCE[21-x][4]
                listB.append(grabData)
            for t in range(21):
                total = total + float(listB[0+t])
            sma21Closed = total / 21
            
            smaDiff = round((smaFiveClosed - sma21Closed),2)
            
            if v == 0:
                self.labe26.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 1:
                self.labe27.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 2:
                self.labe28.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 3:
                self.labe29.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 4:
                self.labe30.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 5:
                self.labe31.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 6:
                self.labe32.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 7:
                self.labe33.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
            if v == 8:
                self.labe34.text = (symbol_list[0+v] + "\n" + 'SMA DIFF' + "\n" + str(smaDiff))
                
    def setTextBack4(self, x, *args):
        for y in range(9):
            PCE = client.get_klines(symbol=symbol_list[0+y],interval=KLINE_INTERVAL_5MINUTE, limit=4)
            percentageRise = round(((float(PCE[3][4])-float(PCE[3][1]))/float(PCE[3][1]))*100,2)
            lastThreeVol = (float(PCE[2][5])+float(PCE[1][5])+float(PCE[0][5]))
            lastVol = (float(PCE[3][5]))
            volComp = round(int(lastVol) / int(lastThreeVol),2)
            
            if y == 0:
                self.labe39.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 1:
                self.labe40.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 2:
                self.labe41.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 3:
                self.labe42.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 4:
                self.labe43.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 5:
                self.labe44.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 6:
                self.labe45.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 7:
                self.labe46.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
            if y == 8:
                self.labe47.text = (symbol_list[0+y] + "\n" + 'ROC ' + str(percentageRise) + "\n" + 'VolComp ' + str(volComp))
                
    def setMomo(self, x, *args):
        self.labe49.text = ('No Signal')
        self.labe48.text = ('No Signal')
        for y in range(9):
            PCE = client.get_klines(symbol=symbol_list[0+y],interval=KLINE_INTERVAL_5MINUTE, limit=4)
            percentageRise = ((float(PCE[3][4])-float(PCE[3][1]))/float(PCE[3][1]))*100
            lastThreeVol = (float(PCE[2][5])+float(PCE[1][5])+float(PCE[0][5]))
            lastVol = (float(PCE[3][5]))
            volComp = int(lastVol) / int(lastThreeVol)
            
            if volComp > 2.00 and percentageRise > 0.05:
                telegram_send.send(messages=[symbol_list[0+y] + "Pop on volume!"])
                
            if volComp > 2.00 and percentageRise < -0.05:
                telegram_send.send(messages=[symbol_list[0+y] + "Selling Pressure!"])
                
            if y == 0:
                self.labe39.background_color = 0, 0, 1, 1
            if y == 1:
                self.labe40.background_color = 0, 0, 1, 1
            if y == 2:
                self.labe41.background_color = 0, 0, 1, 1
            if y == 3:
                self.labe42.background_color = 0, 0, 1, 1
            if y == 4:
                self.labe43.background_color = 0, 0, 1, 1
            if y == 5:
                self.labe44.background_color = 0, 0, 1, 1
            if y == 6:
                self.labe45.background_color = 0, 0, 1, 1
            if y == 7:
                self.labe46.background_color = 0, 0, 1, 1
            if y == 8:
                self.labe47.background_color = 0, 0, 1, 1
                
    def smaCrosser(self, x, *args):
        self.labe36.text = ('No Signal')
        self.labe35.text = ('No Signal')
        for v in range(9):
            listA = []
            listB = []
            listC = []
            listD = []
        
            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_5MINUTE, limit=7)
        
            total=0    
            for x in range(5):
                grabData = SCE[5-x][4]
                listA.append(grabData)
            for t in range(5):
                total = total + float(listA[0+t])
            smaFiveClosed = total / 5
        

            total=0
            for x in range(5):
                grabData = SCE[4-x][4]
                listB.append(grabData)
            for t in range(5):
                total = total + float(listB[0+t])
            smaFivePrior = total / 5
        
            SCE = client.get_klines(symbol=symbol_list[0+v], interval=KLINE_INTERVAL_15MINUTE, limit=23)
        
            total=0
            for x in range(21):
                grabData = SCE[21-x][4]
                listC.append(grabData)
            for t in range(21):
                total = total + float(listC[0+t])
            sma21Closed = total / 21
                
        
            total=0
            for x in range(21):
                grabData = SCE[20-x][4]
                listD.append(grabData)
            for t in range(21):
                total = total + float(listD[0+t])
            sma21Prior = total / 21
    
            if smaFiveClosed > sma21Closed and smaFivePrior < sma21Prior:
                print('ok')
                #telegram_send.send(messages=[symbol_list[0+v] + '5 Minute 5SMA Crossing 15M 21SMA from bottom(BULLISH)'])
                timeStamper()
        
            if smaFiveClosed < sma21Closed and smaFivePrior > sma21Prior:
                print('ok')
                #telegram_send.send(messages=[symbol_list[0+v] + '5 Minute 5SMA Crossing 15M 21SMA from top(BEARISH)'])
                timeStamper()
                
            if v == 0:
                self.labe26.background_color = 0, 0, 1, 1
            if v == 1:
                self.labe27.background_color = 0, 0, 1, 1
            if v == 2:
                self.labe28.background_color = 0, 0, 1, 1
            if v == 3:
                self.labe29.background_color = 0, 0, 1, 1
            if v == 4:
                self.labe30.background_color = 0, 0, 1, 1
            if v == 5:
                self.labe31.background_color = 0, 0, 1, 1
            if v == 6:
                self.labe32.background_color = 0, 0, 1, 1
            if v == 7:
                self.labe33.background_color = 0, 0, 1, 1
            if v == 8:
                self.labe34.background_color = 0, 0, 1, 1
            
class scannerCrypto(App):
    def build(self):
        try:
            scan = updateData()
            scan.flashAlgoM(1)
            scan.flashAlgoX(1)
            scan.setTextBack1(1)
            scan.setTextBack2(1)
            scan.setTextBack3(1)
            scan.setTextBack4(1)
            scan.setMomo(1)
            scan.smaCrosser(1)
            
            Clock.schedule_interval(scan.flashAlgoM, 2)
            Clock.schedule_interval(scan.flashAlgoX, 2)
            Clock.schedule_interval(scan.setTextBack1, 4)
            Clock.schedule_interval(scan.setTextBack2, 4)
            Clock.schedule_interval(scan.setTextBack3, 4)
            Clock.schedule_interval(scan.setTextBack4, 4)
            Clock.schedule_interval(scan.setMomo, 60)
            Clock.schedule_interval(scan.smaCrosser, 300)
            return scan
            
        except Exception as e:
            print(e)
            print('Error Occured')
            #telegram_send.send(messages=['Connection Lost, Attempting to connect to server!'])
            timeStamper()
            sleep(60)
            client = Client(apiData.APIKey, apiData.SecretKey)
            print(e)
        
if __name__ == '__main__':
    scannerCrypto().run()
