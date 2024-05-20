from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import base64

# Detect cover text as Sinhala
def detect_sinhala_text(open_text, threshold=0.5):
    try:
        lang_list = detect_langs(open_text)
        for item in lang_list:
            if item.lang == 'si' and item.prob > threshold:
                return True
        return False
    except LangDetectException:
        # Treat short text as Sinhala by default
        return True
