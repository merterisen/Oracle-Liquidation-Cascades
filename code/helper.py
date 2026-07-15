import pandas as pd
import numpy as np

# Split ABI-encoded data into 32-byte words
def split_abi_words(data):
    if pd.isna(data):
        return []

    data = str(data).strip()

    if data.startswith("0x"):
        data = data[2:]

    if len(data) == 0:
        return []

    return ["0x" + data[i:i+64] for i in range(0, len(data), 64)]

def first_data_word(data):
    if pd.isna(data):
        return np.nan

    data = str(data).strip()

    if data.startswith("0x"):
        data = data[2:]

    if len(data) < 64:
        return np.nan

    return "0x" + data[:64]

def hex_to_uint(x):
    if pd.isna(x):
        return np.nan

    x = str(x).strip()

    if x.startswith("0x"):
        x = x[2:]

    if x == "":
        return np.nan

    return int(x, 16)

# Unsigned integer decoder
def hex_to_uint(x):
    try:
        if pd.isna(x):
            return np.nan

        x = str(x).strip()

        if x.startswith("0x"):
            x = x[2:]

        if len(x) == 0:
            return np.nan

        return int(x, 16)

    except Exception:
        return np.nan

# Signed integer decoder for Chainlink OCR int192/int256-like values
def hex_to_int_signed_256(x):
    try:
        if pd.isna(x):
            return np.nan

        x = str(x).strip()

        if x.startswith("0x"):
            x = x[2:]

        if len(x) == 0:
            return np.nan

        value = int(x, 16)

        # Interpret as signed 256-bit integer
        if value >= 2**255:
            value = value - 2**256

        return value

    except Exception:
        return np.nan

def detect_time_unit_from_value(value):
    """
    Detect timestamp unit from magnitude.
    seconds:      ~1e9
    milliseconds: ~1e12
    microseconds: ~1e15
    nanoseconds:  ~1e18
    """
    if pd.isna(value):
        return "unknown"

    value = float(value)

    if value > 1e17:
        return "ns"
    elif value > 1e14:
        return "us"
    elif value > 1e11:
        return "ms"
    elif value > 1e8:
        return "s"
    else:
        return "unknown"


def symbol_from_filename(path):
    upper = path.upper()

    for sym in ["BTCUSDT", "ETHUSDT", "USDCUSDT", "LINKUSDT"]:
        if sym in upper:
            return sym

    return "unknown"