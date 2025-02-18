import requests
import json


l = []
w = []
p = []
final_dict = {}

# TGA1LLY1VH95IET0


def get_funds():
    url1 = 'http://api.stockfluence.com/fund/type/losers?apikey=9d60023d5b5de98eeede2393edb7dc7f'
    losers = requests.get(url1).json()

    url2 = 'http://api.stockfluence.com/fund/type/gainers?apikey=9d60023d5b5de98eeede2393edb7dc7f'
    winners = requests.get(url2).json()

    url3 = 'http://api.stockfluence.com/fund/type/popular?apikey=9d60023d5b5de98eeede2393edb7dc7f'
    populars = requests.get(url3).json()

    for loser in losers:
        url4 = 'http://api.stockfluence.com/fund/{}?apikey=469979b39e7c3b6a312579c4d092f6a5'.format(
            loser["symbol"])
        data4 = requests.get(url4).json()
        l.append({"name": loser["name"], "symbol": loser["symbol"]})

    # for winner in winners:
    #     url5 = 'https://www.alphavantage.co/query?function=ROC&symbol={}&interval=weekly&time_period=10&series_type=close&apikey=TGA1LLY1VH95IET0'.format(winner["symbol"])
    #     data5 = requests.get(url5).json()
    #     w.append({"name": winner["name"], "symbol": winner["symbol"], "roc": data5["Technical Analysis: ROC"][next(iter(data5["Technical Analysis: ROC"]))]["ROC"]})

    # for popular in populars:
    #     url6 = 'https://www.alphavantage.co/query?function=ROC&symbol={}&interval=weekly&time_period=10&series_type=close&apikey=TGA1LLY1VH95IET0'.format(popular["symbol"])
    #     data6 = requests.get(url6).json()
    #     p.append({"name": popular["name"], "symbol": popular["symbol"], "roc": data6["Technical Analysis: ROC"][next(iter(data6["Technical Analysis: ROC"]))]["ROC"]})

    final_dict = {"losers": l, "winners": w, "popular": p}
    return (final_dict)

# def data_process():
#     with open('data.json', 'r') as f:
#         data = json.load(f)
#     return data


symbols = ['ABT', 'ABBV', 'ACN', 'ACE',
           'ADBE', 'ADT', 'AAP', 'AES',
           'AET', 'AFL', 'AMG', 'A',
           'GAS', 'APD', 'ARG', 'AKAM',
           'AA', 'AGN', 'ALXN', 'ALLE',
           'ADS', 'ALL', 'ALTR', 'MO',
           'AMZN', 'AEE', 'AAL', 'AEP',
           'AXP', 'AIG', 'AMT', 'AMP',
           'ABC', 'AME', 'AMGN', 'APH',
           'APC', 'ADI', 'AON', 'APA',
           'AIV', 'AMAT', 'ADM', 'AIZ',
           'T', 'ADSK', 'ADP', 'AN',
           'AZO', 'AVGO', 'AVB', 'AVY',
           'BHI', 'BLL', 'BAC', 'BK',
           'BCR', 'BXLT', 'BAX', 'BBT',
           'BDX', 'BBBY', 'BRK-B',
           'BBY', 'BLX', 'HRB', 'BA',
           'BWA', 'BXP', 'BSK', 'BMY',
           'BRCM', 'BF-B', 'CHRW',
           'CA', 'CVC', 'COG', 'CAM',
           'CPB', 'COF', 'CAH', 'HSIC',
           'KMX', 'CCL', 'CAT', 'CBG',
           'CBS', 'CELG', 'CNP', 'CTL',
           'CERN', 'CF', 'SCHW', 'CHK',
           'CVX', 'CMG', 'CB', 'CI',
           'XEC', 'CINF', 'CTAS', 'CSCO',
           'C', 'CTXS', 'CLX', 'CME', 'CMS',
           'COH', 'KO', 'CCE', 'CTSH', 'CL',
           'CMCSA', 'CMA', 'CSC', 'CAG',
           'COP', 'CNX', 'ED', 'STZ', 'GLW',
           'COST', 'CCI', 'CSX', 'CMI',
           'CVS', 'DHI', 'DHR', 'DRI',
           'DVA', 'DE', 'DLPH', 'DAL',
           'XRAY', 'DVN', 'DO', 'DTV',
           'DFS', 'DISCA', 'DISCK', 'DG',
           'DLTR', 'D', 'DOV', 'DOW',
           'DPS', 'DTE', 'DD', 'DUK',
           'DNB', 'ETFC', 'EMN', 'ETN',
           'EBAY', 'ECL', 'EIX', 'EW',
           'EA', 'EMC', 'EMR', 'ENDP',
           'ESV', 'ETR', 'EOG', 'EQT',
           'EFX', 'EQIX', 'EQR', 'ESS',
           'EL', 'ES', 'EXC', 'EXPE',
           'EXPD', 'ESRX', 'XOM', 'FFIV',
           'FB', 'FAST', 'FDX', 'FIS',
           'FITB', 'FSLR', 'FE', 'FSIV',
           'FLIR', 'FLS', 'FLR', 'FMC',
           'FTI', 'F', 'FOSL', 'BEN',
           'FCX', 'FTR', 'GME', 'GPS',
           'GRMN', 'GD', 'GE', 'GGP',
           'GIS', 'GM', 'GPC', 'GNW',
           'GILD', 'GS', 'GT', 'GOOGL',
           'GOOG', 'GWW', 'HAL', 'HBI',
           'HOG', 'HAR', 'HRS', 'HIG',
           'HAS', 'HCA', 'HCP', 'HCN',
           'HP', 'HES', 'HPQ', 'HD',
           'HON', 'HRL', 'HSP', 'HST',
           'HCBK', 'HUM', 'HBAN', 'ITW',
           'IR', 'INTC', 'ICE', 'IBM',
           'IP', 'IPG', 'IFF', 'INTU',
           'ISRG', 'IVZ', 'IRM', 'JEC',
           'JBHT', 'JNJ', 'JCI', 'JOY',
           'JPM', 'JNPR', 'KSU', 'K',
           'KEY', 'GMCR', 'KMB', 'KIM',
           'KMI', 'KLAC', 'KSS', 'KRFT',
           'KR', 'LB', 'LLL', 'LH',
           'LRCX', 'LM', 'LEG', 'LEN',
           'LVLT', 'LUK', 'LLY', 'LNC',
           'LLTC', 'LMT', 'L', 'LOW',
           'LYB', 'MTB', 'MAC', 'M',
           'MNK', 'MRO', 'MPC', 'MAR',
           'MMC', 'MLM', 'MAS', 'MA',
           'MAT', 'MKC', 'MCD', 'MHFI',
           'MCK', 'MJN', 'MMV', 'MDT',
           'MRK', 'MET', 'KORS', 'MCHP',
           'MU', 'MSFT', 'MHK', 'TAP',
           'MDLZ', 'MON', 'MNST', 'MCO',
           'MS', 'MOS', 'MSI', 'MUR',
           'MYL', 'NDAQ', 'NOV', 'NAVI',
           'NTAP', 'NFLX', 'NWL', 'NFX',
           'NEM', 'NWSA', 'NEE', 'NLSN',
           'NKE', 'NI', 'NE', 'NBL',
           'JWN', 'NSC', 'NTRS', 'NOC',
           'NRG', 'NUE', 'NVDA', 'ORLY',
           'OXY', 'OMC', 'OKE', 'ORCL',
           'OI', 'PCAR', 'PLL', 'PH',
           'PDCO', 'PAYX', 'PNR',
           'PBCT', 'POM', 'PEP',
           'PKI', 'PRGO', 'PFE', 'PCG',
           'PM', 'PSX', 'PNW', 'PXD',
           'PBI', 'PCL', 'PNC', 'RL',
           'PPG', 'PPL', 'PX', 'PCP',
           'PCLN', 'PFG', 'PG', 'PGR',
           'PLD', 'PRU', 'PEG', 'PSA', 
           'PHM', 'PVH', 'QRVO', 'PWR', 
           'QCOM', 'DGX', 'RRC', 'RTN', 
           'O', 'RHT', 'REGN', 'RF', 
           'RSG', 'RAI', 'RHI', 'ROK', 
           'COL', 'ROP', 'ROST', 'RLC', 
           'R', 'CRM', 'SNDK', 'SCG', 
           'SLB', 'SNI', 'STX', 'SEE', 
           'SRE', 'SHW', 'SIAL', 'SPG', 
           'SWKS', 'SLG', 'SJM', 'SNA', 
           'SO', 'LUV', 'SWN', 'SE', 
           'STJ', 'SWK', 'SPLS', 'SBUX',
            'HOT', 'STT', 'SRCL', 'SYK', 
            'STI', 'SYMC', 'SYY', 'TROW', 
            'TGT', 'TEL', 'TE', 'TGNA', 
            'THC', 'TDC', 'TSO', 'TXN', 
            'TXT', 'HSY', 'TRV', 'TMO', 
            'TIF', 'TWX', 'TWC', 'TJK', 
            'TMK', 'TSS', 'TSCO', 'RIG', 
            'TRIP', 'FOXA', 'TSN', 'TYC', 
            'UA', 'UNP', 'UNH', 'UPS', 
            'URI', 'UTX', 'UHS', 'UNM', 
            'URBN', 'VFC', 'VLO', 'VAR', 
            'VTR', 'VRSN', 'VZ', 'VRTX', 
            'VIAB', 'V', 'VNO', 'VMC', 
            'WMT', 'WBA', 'DIS', 'WM', 
            'WAT', 'ANTM', 'WFC', 'WDC', 
            'WU', 'WY', 'WHR', 'WFM', 
            'WMB', 'WEC', 'WYN', 'WYNN', 
            'XEL', 'XRX', 'XLNX', 'XL', 
            'XYL', 'YHOO', 'YUM', 'ZBH', 
            'ZION', 'ZTS'
]


def Get_Data_of_Stocks(symbol):
    data = quandl.get('WIKI/{}'.format(symbol),start_date="2012-08-01",end_date="2012-12-01")
    data.to_csv('app/{}.csv'.format(symbol))