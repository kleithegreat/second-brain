import pandas as pd


def make_cols(df: pd.DataFrame):
    df.columns = ["Book", "Chapter", "Verse", f"{df}".upper()]


amp = pd.read_csv("AMP_fixed.csv")
# esv = pd.read_csv("ESV_fixed.csv")
kjv = pd.read_csv("KJV_fixed.csv")
# niv = pd.read_csv("NIV_fixed.csv")
nkjv = pd.read_csv("NKJV_fixed.csv")

bible = pd.read_csv("NASB_fixed.csv")
bible.columns = ["Book", "Chapter", "Verse", "NASB"]

bible["UUID"] = (bible['Book'].astype(str).str.zfill(2) + bible['Chapter'].astype(str).str.zfill(3) + bible['Verse'].astype(str).str.zfill(3))
col = bible.pop('UUID')
bible.insert(0, 'UUID', col)

# bible["AMP"] = 

print(bible.describe())
print(bible)
