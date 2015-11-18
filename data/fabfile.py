import csv
import fabric
from fabric.api import *
from fabric.operations import *
import glob
import os

fabric.state.output.status = False

"""
Given a series of xls files with annual refugee data, kick out a single file to upload for Refugee model. List any countries or states that aren't in our lookup. Requires fabric and csvkit.

TO DO
=============
Fetch and resize world flag pics?

"""

COUNTRY_LOOKUP = {
    "Afghanistan": "004",
    "Albania": "008",
    "Algeria": "012",
    "Angola": "024",
    "Armenia": "051",
    "Azerbaijan": "031",
    "Bangladesh": "050",
    "Belarus": "112",
    "Benin": "204",
    "Bhutan": "064",
    "Bosnia and Herzegovina": "070",
    "Bulgaria": "100",
    "Burkina Faso (UVolta)": "854",
    "Burma": "104",
    "Burundi": "108",
    "Cambodia": "116",
    "Cameroon": "120",
    "Canada": "124",
    "Central African Republic": "140",
    "Chad": "148",
    "China": "156",
    "Colombia": "170",
    "Congo": "178",
    "Costa Rica": "188",
    "Croatia": "191",
    "Cuba": "192",
    "Dem. Rep. Congo": "180",
    "Djibouti": "262",
    "Ecuador": "218",
    "Egypt": "818",
    "El Salvador": "222",
    "Equatorial Guinea": "226",
    "Eritrea": "232",
    "Estonia": "233",
    "Ethiopia": "231",
    "France": "250",
    "Gabon": "266",
    "Gambia": "270",
    "Georgia": "268",
    "Germany": "276",
    "Ghana": "288",
    "Guatemala": "320",
    "Guinea": "324",
    "Guinea - Bissau": "624",
    "Haiti": "332",
    "Honduras": "340",
    "India": "356",
    "Indonesia": "360",
    "Iran": "364",
    "Iraq": "368",
    "Israel": "376",
    "Ivory Coast": "384",
    "Jamaica": "388",
    "Jordan": "400",
    "Kazakhstan": "398",
    "Kenya": "404",
    "Kuwait": "414",
    "Kyrgyzstan": "417",
    "Laos": "418",
    "Latvia": "428",
    "Lebanon": "422",
    "Liberia": "430",
    "Libya": "434",
    "Lithuania": "440",
    "Macedonia": "807",
    "Madagascar (Malagasy Republic)": "450",
    "Malaysia": "458",
    "Mali": "466",
    "Mauritania": "478",
    "Moldova": "498",
    "Montenegro": "499",
    "Morocco": "504",
    "Namibia": "516",
    "Nepal": "524",
    "Netherlands": "528",
    "Niger": "562",
    "Nigeria": "566",
    "Korea, North": "408",
    "Pakistan": "586",
    "Palestine": "275",
    "Gaza Strip": "275",
    "Philippines": "608",
    "Republic of South Sudan": "728",
    "Russia": "643",
    "Rwanda": "646",
    "Saudi Arabia": "682",
    "Senegal": "686",
    "Serbia": "688",
    "Sierra Leone": "694",
    "Slovakia": "703",
    "Somalia": "706",
    "South Africa": "710",
    "Sri Lanka (Ceylon)": "144",
    "Sudan": "729",
    "Sweden": "752",
    "Syria": "760",
    "Tajikistan": "762",
    "Tanzania": "834",
    "Thailand": "764",
    "Tibet": "673",
    "Togo": "768",
    "Tunisia": "788",
    "Turkey": "792",
    "Turkmenistan": "795",
    "Uganda": "800",
    "Ukraine": "804",
    "United Arab Emirates": "784",
    "United Kingdom": "826",
    "Uzbekistan": "860",
    "Venezuela": "862",
    "Vietnam": "704",
    "Yemen": "887",
    "Zambia": "894",
    "Zimbabwe": "716",
}

STATE_LOOKUP = {
    "Alabama":"AL",
    "Alaska":"AK",
    "Arizona":"AZ",
    "Arkansas":"AR",
    "California":"CA",
    "Colorado":"CO",
    "Connecticut":"CT",
    "Delaware":"DE",
    "District of Columbia":"DC",
    "Florida":"FL",
    "Georgia":"GA",
    "Guam":"GU",
    "Hawaii":"HI",
    "Idaho":"ID",
    "Illinois":"IL",
    "Indiana":"IN",
    "Iowa":"IA",
    "Kansas":"KS",
    "Kentucky":"KY",
    "Louisiana":"LA",
    "Maine":"ME",
    "Maryland":"MD",
    "Massachusetts":"MA",
    "Michigan":"MI",
    "Minnesota":"MN",
    "Mississippi":"MS",
    "Missouri":"MO",
    "Montana":"MT",
    "Nebraska":"NE",
    "Nevada":"NV",
    "New Hampshire":"NH",
    "New Jersey":"NJ",
    "New Mexico":"NM",
    "New York":"NY",
    "North Carolina":"NC",
    "North Dakota":"ND",
    "Ohio":"OH",
    "Oklahoma":"OK",
    "Oregon":"OR",
    "Pennsylvania":"PA",
    "Puerto Rico":"PR",
    "Rhode Island":"RI",
    "South Carolina":"SC",
    "South Dakota":"SD",
    "Tennessee":"TN",
    "Texas":"TX",
    "Utah":"UT",
    "Vermont":"VT",
    "Virginia":"VA",
    "Washington":"WA",
    "West Virginia":"WV",
    "Wisconsin":"WI",
    "Wyoming":"WY"
}

def parseCSV(year, filename, delim):
    with open(filename, "rb") as ref:
        f = open("refugees-" + year + "-processed.txt", "wb")
        reader = csv.reader(ref, delimiter=delim)
        state = ""
        country = ""
        city = ""
        for row in reader:
            if row[0] != "":
                state = row[0]
                try:
                    stateabbr = STATE_LOOKUP[state]
                except:
                    print state, "not in lookup"
            if row[1] != "":
                country = row[1]
                try:
                    countrycode = COUNTRY_LOOKUP[country]
                except:
                    print country, "not in lookup"
            if row[2] != "":
                city = row[2]
            if row[0] == "" and row[1] == "":
                number = str(int(float(row[3])))
                f.write("|".join(["", countrycode, city, number, year, "", stateabbr]) + "\n")
        f.close()
        
def stackEmUp():
    os.chdir("/home/omaha/webapps/django16/myproject/refugees/data")
    results = [f for f in glob.glob("*.txt") if re.search(r'(20\d\d-processed).*\.txt$', f)]
    s = " ".join(results)
    with hide('running', 'stdout', 'stderr'):
        local('csvstack -d "|" ' + s + ' | csvformat -D "|" > refugee-data-stacked.txt', capture=False)