import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive plotting
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import warnings
from streamlit_chat import message
import re
import io
import pdfplumber

