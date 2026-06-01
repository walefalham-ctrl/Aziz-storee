import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8836273594:AAH6F1PtB1LG0nLR-Ofe-Jvv_9tCMaecLQY"
WEB_APP_URL = "https://walefalham-ctrl.github.io/Aziz-store/"

class Handler(BaseHTTPRe
