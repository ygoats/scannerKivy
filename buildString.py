#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:01:35 2020

@ygoats
"""
from kivy.lang import Builder
#red = [1, 0, 0, 1]
#green = [0, 1, 0, 1]
#blue = [0, 0, 1, 1]
#purple = [1, 0, 1, 1]

def buildString():

    Builder.load_string('''
<updateData>:
    labe:lab
    Button:
        id: lab
        font_size: 12
<updateData>:
    labe1:lab1
    Button:
        id: lab1
        font_size: 12
        center_x: 150
<updateData>:
    labe2:lab2
    Button:
        id: lab2
        font_size: 12
        center_x: 250
<updateData>:
    labe3:lab3
    Button:
        id: lab3
        font_size: 12
        top: 200
<updateData>:
    labe4:lab4
    Button:
        id: lab4
        font_size: 12
        center_x: 150
        top: 200
<updateData>:
    labe5:lab5
    Button:
        id: lab5
        font_size: 12
        center_x: 250
        top: 200
<updateData>:
    labe6:lab6
    Button:
        id: lab6
        font_size: 12
        top: 300
<updateData>:
    labe7:lab7
    Button:
        id: lab7
        font_size: 12
        center_x: 150
        top: 300
<updateData>:
    labe8:lab8
    Button:
        id: lab8
        font_size: 12
        center_x: 250
        top: 300
<updateData>:
    labe9:lab9
    Label:
        id: lab9
        font_size: 16
        center_x: 150
        top: 400
<updateData>:
    labe10:lab10
    Label:
        id: lab10
        font_size: 16
        center_x: 150
        top: 500
<updateData>:
    labe11:lab11
    Label:
        id: lab11
        font_size: 16
        center_x: 150
        top: 600
<updateData>:
    labe12:lab12
    Label:
        id: lab12
        font_size: 20
        center_x: 150
        top: 650
        text: str("Simple Scanner")
<updateData>:
    labe13:lab13
    Button:
        id: lab13
        font_size: 12
        center_x: 375
<updateData>:
    labe14:lab14
    Button:
        id: lab14
        font_size: 12
        center_x: 475
<updateData>:
    labe15:lab15
    Button:
        id: lab15
        font_size: 12
        center_x: 575
<updateData>:
    labe16:lab16
    Button:
        id: lab16
        font_size: 12
        top: 200
        center_x:375
<updateData>:
    labe17:lab17
    Button:
        id: lab17
        font_size: 12
        top: 200
        center_x: 475
<updateData>:
    labe18:lab18
    Button:
        id: lab18
        font_size: 12
        top: 200
        center_x: 575
<updateData>:
    labe19:lab19
    Button:
        id: lab19
        font_size: 12
        top: 300
        center_x: 375
<updateData>:
    labe20:lab20
    Button:
        id: lab20
        font_size: 12
        top: 300
        center_x: 475
<updateData>:
    labe21:lab21
    Button:
        id: lab21
        font_size: 12
        top: 300
        center_x: 575
<updateData>:
    labe22:lab22
    Label:
        id: lab22
        font_size: 16
        center_x: 475
        top: 400
<updateData>:
    labe23:lab23
    Label:
        id: lab23
        font_size: 16
        center_x: 475
        top: 500
<updateData>:
    labe24:lab24
    Label:
        id: lab24
        font_size: 16
        center_x: 475
        top: 600
<updateData>:
    labe25:lab25
    Label:
        id: lab25
        font_size: 20
        center_x: 475
        top: 650
        text: str("Bot Control 2")
<updateData>:
    labe26:lab26
    Button:
        id: lab26
        font_size: 12
        center_x:700
<updateData>:
    labe27:lab27
    Button:
        id: lab27
        font_size: 12
        center_x: 800
<updateData>:
    labe28:lab28
    Button:
        id: lab28
        font_size: 12
        center_x: 900
<updateData>:
    labe29:lab29
    Button:
        id: lab29
        font_size: 12
        top: 200
        center_x:700
<updateData>:
    labe30:lab30
    Button:
        id: lab30
        font_size: 12
        top: 200
        center_x: 800
<updateData>:
    labe31:lab31
    Button:
        id: lab31
        font_size: 12
        top: 200
        center_x: 900
<updateData>:
    labe32:lab32
    Button:
        id: lab32
        font_size: 12
        top: 300
        center_x: 700
<updateData>:
    labe33:lab33
    Button:
        id: lab33
        font_size: 12
        top: 300
        center_x: 800
<updateData>:
    labe34:lab34
    Button:
        id: lab34
        font_size: 12
        top: 300
        center_x: 900
<updateData>:
    labe35:lab35
    Label:
        id: lab35
        font_size: 16
        center_x: 800
        top: 400
<updateData>:
    labe36:lab36
    Label:
        id: lab36
        font_size: 16
        center_x: 800
        top: 500
<updateData>:
    labe37:lab37
    Label:
        id: lab37
        font_size: 16
        center_x: 800
        top: 600
<updateData>:
    labe38:lab38
    Label:
        id: lab38
        font_size: 20
        center_x: 800
        top: 650
        text: str("Bot Control 3")
<updateData>:
    labe39:lab39
    Button:
        id: lab39
        font_size: 12
        center_x: 1025
<updateData>:
    labe40:lab40
    Button:
        id: lab40
        font_size: 12
        center_x: 1125
<updateData>:
    labe41:lab41
    Button:
        id: lab41
        font_size: 12
        center_x: 1225
<updateData>:
    labe42:lab42
    Button:
        id: lab42
        font_size: 12
        top: 200
        center_x: 1025
<updateData>:
    labe43:lab43
    Button:
        id: lab43
        font_size: 12
        top: 200
        center_x: 1125
<updateData>:
    labe44:lab44
    Button:
        id: lab44
        font_size: 12
        top: 200
        center_x: 1225
<updateData>:
    labe45:lab45
    Button:
        id: lab45
        font_size: 12
        top: 300
        center_x: 1025
<updateData>:
    labe46:lab46
    Button:
        id: lab46
        font_size: 12
        top: 300
        center_x: 1125
<updateData>:
    labe47:lab47
    Button:
        id: lab47
        font_size: 12
        top: 300
        center_x: 1225
<updateData>:
    labe48:lab48
    Label:
        id: lab48
        font_size: 16
        center_x: 1125
        top: 400
<updateData>:
    labe49:lab49
    Label:
        id: lab49
        font_size: 16
        center_x: 1125
        top: 500
<updateData>:
    labe50:lab50
    Label:
        id: lab50
        font_size: 16
        center_x: 1125
        top: 600
<updateData>:
    labe51:lab51
    Label:
        id: lab51
        font_size: 20
        center_x: 1125
        top: 650
        text: str("Bot Control 4")
''')

