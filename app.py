import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList,OneLineListItem
from kiteconnect import KiteTicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, SwapTransition
from google.oauth2 import service_account
import gspread
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import requests
import json
import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        instrument_token INTEGER NOT NULL,
        tradingsymbol TEXT NOT NULL,
        candel_high TEXT NOT NULL,
        candel_low TEXT NOT NULL,
        t1 TEXT NOT NULL,
        t1_ltp TEXT,
        t_ltp TEXT,
        Retracement_Point TEXT NOT NULL,
        Retracement_ltp TEXT,
        Quantity TEXT NOT NULL,
        Booking_per TEXT NOT NULL,
        order_placed BOOLEAN Default False,
        booked BOOLEAN Default False
    )''')
conn.commit()
conn.close()

class Stocks(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file('main1.kv'))
        self.screen_manager.add_widget(Builder.load_file('profile.kv'))
        # self.screen_manager.add_widget(Builder.load_file('kiteLogin.kv'))
        return self.screen_manager

Stocks().run()