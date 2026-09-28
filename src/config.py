"""Shared definitions: parties, parliamentary terms, governments.

All rules used to build the analysis sample live here so they are written down once.
"""
import pandas as pd

# Party codes are the usual Finnish abbreviations (the team works in Finnish).
# Reports in English use PARTY_SHORT_EN / PARTY_NAMES_EN.
#
# Parliamentary group code (from the open-data export) -> party code.
# Groups not listed here (one-person groups, Liike Nyt, Valta kuuluu kansalle,
# non-affiliated MPs, ...) are too small to model and are excluded.
PARTY_BY_GROUP = {
    "SD01": "SDP",      # Suomen Sosialidemokraattinen Puolue
    "PS01": "PS",       # Perussuomalaiset
    "KOK01": "KOK",     # Kansallinen Kokoomus
    "KESK01": "KESK",   # Suomen Keskusta
    "VIHR01": "VIHR",   # Vihreä liitto
    "VAS01": "VAS",     # Vasemmistoliitto
    "KD01": "KD",       # Suomen Kristillisdemokraatit
    "R01": "RKP",       # Ruotsalainen eduskuntaryhmä (incl. the Åland MP)
    "UV01": "SIN",      # Uusi vaihtoehto / Sininen eduskuntaryhmä (2017 split from PS)
}

PARTY_NAMES_FI = {
    "SDP": "Sosialidemokraatit",
    "PS": "Perussuomalaiset",
    "KOK": "Kokoomus",
    "KESK": "Keskusta",
    "VIHR": "Vihreät",
    "VAS": "Vasemmistoliitto",
    "KD": "Kristillisdemokraatit",
    "RKP": "RKP",
    "SIN": "Siniset",
}

PARTY_NAMES_EN = {
    "SDP": "Social Democratic Party",
    "PS": "Finns Party",
    "KOK": "National Coalition Party",
    "KESK": "Centre Party",
    "VIHR": "Green League",
    "VAS": "Left Alliance",
    "KD": "Christian Democrats",
    "RKP": "Swedish People's Party",
    "SIN": "Blue Reform",
}
PARTY_NAMES = PARTY_NAMES_EN  # backwards compatibility

# Short English labels for report figures.
PARTY_SHORT_EN = {
    "SDP": "SDP", "PS": "Finns", "KOK": "NCP", "KESK": "Centre", "VIHR": "Greens",
    "VAS": "Left", "KD": "CD", "RKP": "SPP", "SIN": "Blue Reform",
}

# Order used in tables and charts (roughly left to right).
PARTY_ORDER = ["VAS", "SDP", "VIHR", "KESK", "RKP", "KD", "KOK", "SIN", "PS"]

# The 8 parties present in every term (used in the main models).
MAIN_PARTIES = [p for p in PARTY_ORDER if p != "SIN"]

# Official party colours (approximate), for charts.
PARTY_COLORS = {
    "SDP": "#E11931", "PS": "#FFDE55", "KOK": "#006288", "KESK": "#006633",
    "VIHR": "#9ACD32", "VAS": "#F00A64", "KD": "#8E6CC8", "RKP": "#E8A33D",
    "SIN": "#0A2F6B",
}

# A parliamentary term starts on the day the newly elected parliament first convenes.
TERMS = [
    ("2015-2019", pd.Timestamp("2015-04-28", tz="UTC")),
    ("2019-2023", pd.Timestamp("2019-04-24", tz="UTC")),
    ("2023-2027", pd.Timestamp("2023-04-12", tz="UTC")),
]

# Government parties by period (start date of the period, parties in government).
# Caretaker periods after an election are assigned to the outgoing government.
GOVERNMENTS = [
    ("Stubb (caretaker)", pd.Timestamp("2015-04-28", tz="UTC"), {"KOK", "SDP", "RKP", "KD"}),
    ("Sipilä", pd.Timestamp("2015-05-29", tz="UTC"), {"KESK", "PS", "KOK"}),
    # 13 June 2017: PS left government; the split-off group (SIN) stayed.
    ("Sipilä", pd.Timestamp("2017-06-13", tz="UTC"), {"KESK", "SIN", "KOK"}),
    ("Rinne/Marin", pd.Timestamp("2019-06-06", tz="UTC"), {"SDP", "KESK", "VIHR", "VAS", "RKP"}),
    ("Orpo", pd.Timestamp("2023-06-20", tz="UTC"), {"KOK", "PS", "RKP", "KD"}),
]

# The MP for Åland sits in the RKP group but represents a separate province and speaks
# mostly Swedish; Simola et al. exclude this seat. Matched by name.
ALAND_MPS = {("Mats", "Löfström"), ("Anders", "Norrback")}

# Speech type codes -> Finnish labels (varsinainen = regular, vastaus = reply,
# nopeatahtinen = rapid-response, esittely = presentation, ryhmä = group speech).
SPEECH_TYPES = {
    "T": "varsinainen", "V": "vastaus", "N": "nopeatahtinen", "E": "esittely", "R": "ryhmä", "": "määrittelemätön",
}

# Minimum number of MPs a party must have in a term to be modelled.
MIN_MPS_PER_PARTY_TERM = 5


# Main cabinet of each term (PS counted as government in 2015-2019).
MAIN_GOVERNMENT = {
    "2015-2019": {"KESK", "KOK", "PS"},
    "2019-2023": {"SDP", "KESK", "VIHR", "VAS", "RKP"},
    "2023-2027": {"KOK", "PS", "RKP", "KD"},
}


def term_of(ts):
    label = None
    for name, start in TERMS:
        if ts >= start:
            label = name
    return label


def government_of(ts):
    cur = None
    for name, start, parties in GOVERNMENTS:
        if ts >= start:
            cur = (name, parties)
    return cur
