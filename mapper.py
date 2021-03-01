def get_url_query(list):
    result = ['KRW-BTC', 'KRW-PCI']
    for i in range(0, len(list)):
        for j in range(0, len(mapper)):
            if mapper[j]['korean_name'] == list[i]:
                if mapper[j]['market'] not in result:
                    result.append(mapper[j]['market'])

    return ','.join(result)


def get_coin_name(market):
    for i in mapper:
        if market == i['market']:
            return i['korean_name']


mapper = [
    {
        "market": "KRW-BTC",
        "korean_name": "비트",
        "english_name": "Bitcoin"
    },
    {
        "market": "KRW-ETH",
        "korean_name": "이더",
        "english_name": "Ethereum"
    },
    {
        "market": "KRW-LTC",
        "korean_name": "라코",
        "english_name": "Litecoin"
    },
    {
        "market": "KRW-XRP",
        "korean_name": "리플",
        "english_name": "Ripple"
    },
    {
        "market": "KRW-ETC",
        "korean_name": "이클",
        "english_name": "Ethereum Classic"
    },
    {
        "market": "KRW-OMG",
        "korean_name": "오미세고",
        "english_name": "OmiseGo"
    },
    {
        "market": "KRW-NEO",
        "korean_name": "네오",
        "english_name": "NEO"
    },
    {
        "market": "KRW-MTL",
        "korean_name": "메탈",
        "english_name": "Metal"
    },
    {
        "market": "KRW-LTC",
        "korean_name": "라이트코인",
        "english_name": "Litecoin"
    },
    {
        "market": "KRW-XRP",
        "korean_name": "리플",
        "english_name": "Ripple"
    },
    {
        "market": "KRW-ETC",
        "korean_name": "이더리움클래식",
        "english_name": "Ethereum Classic"
    },
    {
        "market": "KRW-OMG",
        "korean_name": "오미세고",
        "english_name": "OmiseGo"
    },
    {
        "market": "KRW-SNT",
        "korean_name": "슨트",
        "english_name": "Status Network Token"
    },
    {
        "market": "KRW-WAVES",
        "korean_name": "웨이브",
        "english_name": "Waves"
    },
    {
        "market": "KRW-XEM",
        "korean_name": "넴",
        "english_name": "NEM"
    },
    {
        "market": "KRW-QTUM",
        "korean_name": "퀀텀",
        "english_name": "Qtum"
    },
    {
        "market": "KRW-LSK",
        "korean_name": "리스크",
        "english_name": "Lisk"
    },
    {
        "market": "KRW-STEEM",
        "korean_name": "스팀",
        "english_name": "Steem"
    },
    {
        "market": "KRW-XLM",
        "korean_name": "스텔라루멘",
        "english_name": "Lumen"
    },
    {
        "market": "KRW-ARDR",
        "korean_name": "아더",
        "english_name": "Ardor"
    },
    {
        "market": "KRW-KMD",
        "korean_name": "코모도",
        "english_name": "Komodo"
    },
    {
        "market": "KRW-ARK",
        "korean_name": "아크",
        "english_name": "Ark"
    },
    {
        "market": "KRW-STORJ",
        "korean_name": "스토리지",
        "english_name": "Storj"
    },
    {
        "market": "KRW-GRS",
        "korean_name": "그로스톨코인",
        "english_name": "Groestlcoin"
    },
    {
        "market": "KRW-REP",
        "korean_name": "어거",
        "english_name": "Augur"
    },
    {
        "market": "KRW-EMC2",
        "korean_name": "아인스타이늄",
        "english_name": "Einsteinium"
    },
    {
        "market": "KRW-ADA",
        "korean_name": "에이다",
        "english_name": "Ada"
    },
    {
        "market": "KRW-SBD",
        "korean_name": "스팀달러",
        "english_name": "SteemDollars"
    },
    {
        "market": "KRW-POWR",
        "korean_name": "파워렛저",
        "english_name": "Power ledger"
    },
    {
        "market": "KRW-BTG",
        "korean_name": "비트코인골드",
        "english_name": "Bitcoin Gold"
    },
    {
        "market": "KRW-ICX",
        "korean_name": "아이콘",
        "english_name": "Icon"
    },
    {
        "market": "KRW-EOS",
        "korean_name": "이오스",
        "english_name": "EOS"
    },
    {
        "market": "KRW-TRX",
        "korean_name": "트론",
        "english_name": "TRON"
    },
    {
        "market": "KRW-SC",
        "korean_name": "시아코인",
        "english_name": "Siacoin"
    },
    {
        "market": "KRW-IGNIS",
        "korean_name": "이그니스",
        "english_name": "Ignis"
    },
    {
        "market": "KRW-ONT",
        "korean_name": "온톨로지",
        "english_name": "Ontology"
    },
    {
        "market": "KRW-ZIL",
        "korean_name": "질리카",
        "english_name": "Zilliqa"
    },
    {
        "market": "KRW-POLY",
        "korean_name": "폴리매쓰",
        "english_name": "Polymath"
    },
    {
        "market": "KRW-ZRX",
        "korean_name": "제로엑스",
        "english_name": "0x Protocol"
    },
    {
        "market": "KRW-SRN",
        "korean_name": "시린토큰",
        "english_name": "Sirin Token"
    },
    {
        "market": "KRW-LOOM",
        "korean_name": "룸네트워크",
        "english_name": "Loom Network"
    },
    {
        "market": "KRW-BCH",
        "korean_name": "비트코인캐시",
        "english_name": "Bitcoin Cash"
    },
    {
        "market": "KRW-ADX",
        "korean_name": "애드엑스",
        "english_name": "AdEx"
    },
    {
        "market": "KRW-BAT",
        "korean_name": "베이직어텐션토큰",
        "english_name": "Basic Attention Token"
    },
    {
        "market": "KRW-IOST",
        "korean_name": "아이오에스티",
        "english_name": "IOST"
    },
    {
        "market": "KRW-DMT",
        "korean_name": "디마켓",
        "english_name": "DMarket"
    },
    {
        "market": "KRW-RFR",
        "korean_name": "리퍼리움",
        "english_name": "Refereum"
    },
    {
        "market": "KRW-CVC",
        "korean_name": "시빅",
        "english_name": "Civic"
    },
    {
        "market": "KRW-IQ",
        "korean_name": "에브리피디아",
        "english_name": "Everipedia"
    },
    {
        "market": "KRW-IOTA",
        "korean_name": "아이오타",
        "english_name": "IOTA"
    },
    {
        "market": "KRW-MFT",
        "korean_name": "메인프레임",
        "english_name": "Mainframe"
    },
    {
        "market": "KRW-ONG",
        "korean_name": "온톨로지가스",
        "english_name": "ONG"
    },
    {
        "market": "KRW-GAS",
        "korean_name": "가스",
        "english_name": "GAS"
    },
    {
        "market": "KRW-UPP",
        "korean_name": "센티넬프로토콜",
        "english_name": "Sentinel Protocol"
    },
    {
        "market": "KRW-ELF",
        "korean_name": "엘프",
        "english_name": "aelf"
    },
    {
        "market": "KRW-KNC",
        "korean_name": "카이버네트워크",
        "english_name": "Kyber Network"
    },
    {
        "market": "KRW-BSV",
        "korean_name": "비트코인에스브이",
        "english_name": "Bitcoin SV"
    },
    {
        "market": "KRW-THETA",
        "korean_name": "쎄타토큰",
        "english_name": "Theta Token"
    },
    {
        "market": "KRW-EDR",
        "korean_name": "엔도르",
        "english_name": "Endor"
    },
    {
        "market": "KRW-QKC",
        "korean_name": "쿼크체인",
        "english_name": "QuarkChain"
    },
    {
        "market": "KRW-BTT",
        "korean_name": "비트토렌트",
        "english_name": "BitTorrent"
    },
    {
        "market": "KRW-MOC",
        "korean_name": "모스코인",
        "english_name": "Moss Coin"
    },
    {
        "market": "KRW-ENJ",
        "korean_name": "엔진코인",
        "english_name": "Enjin"
    },
    {
        "market": "KRW-TFUEL",
        "korean_name": "쎄타퓨엘",
        "english_name": "Theta Fuel"
    },
    {
        "market": "KRW-MANA",
        "korean_name": "디센트럴랜드",
        "english_name": "Decentraland"
    },
    {
        "market": "KRW-ANKR",
        "korean_name": "앵커",
        "english_name": "Ankr"
    },
    {
        "market": "KRW-NPXS",
        "korean_name": "펀디엑스",
        "english_name": "Pundi X"
    },
    {
        "market": "KRW-AERGO",
        "korean_name": "아르고",
        "english_name": "Aergo"
    },
    {
        "market": "KRW-ATOM",
        "korean_name": "코스모스",
        "english_name": "Cosmos"
    },
    {
        "market": "KRW-TT",
        "korean_name": "썬더토큰",
        "english_name": "Thunder Token"
    },
    {
        "market": "KRW-CRE",
        "korean_name": "캐리프로토콜",
        "english_name": "Carry Protocol"
    },
    {
        "market": "KRW-SOLVE",
        "korean_name": "솔브케어",
        "english_name": "Solve.Care"
    },
    {
        "market": "KRW-MBL",
        "korean_name": "무비블록",
        "english_name": "MovieBloc"
    },
    {
        "market": "KRW-TSHP",
        "korean_name": "트웰브쉽스",
        "english_name": "12SHIPS"
    },
    {
        "market": "KRW-WAXP",
        "korean_name": "왁스",
        "english_name": "WAX"
    },
    {
        "market": "KRW-HBAR",
        "korean_name": "헤데라해시그래프",
        "english_name": "Hedera Hashgraph"
    },
    {
        "market": "KRW-MED",
        "korean_name": "메디블록",
        "english_name": "MediBloc"
    },
    {
        "market": "KRW-MLK",
        "korean_name": "밀크",
        "english_name": "MiL.k"
    },
    {
        "market": "KRW-STPT",
        "korean_name": "에스티피",
        "english_name": "Standard Tokenization Protocol"
    },
    {
        "market": "KRW-ORBS",
        "korean_name": "오브스",
        "english_name": "Orbs"
    },
    {
        "market": "KRW-VET",
        "korean_name": "비체인",
        "english_name": "VeChain"
    },
    {
        "market": "KRW-CHZ",
        "korean_name": "칠리즈",
        "english_name": "Chiliz"
    },
    {
        "market": "KRW-PXL",
        "korean_name": "픽셀",
        "english_name": "PIXEL"
    },
    {
        "market": "KRW-STMX",
        "korean_name": "스톰엑스",
        "english_name": "StormX"
    },
    {
        "market": "KRW-DKA",
        "korean_name": "디카르고",
        "english_name": "dKargo"
    },
    {
        "market": "KRW-HIVE",
        "korean_name": "하이브",
        "english_name": "Hive"
    },
    {
        "market": "KRW-KAVA",
        "korean_name": "카바",
        "english_name": "Kava"
    },
    {
        "market": "KRW-AHT",
        "korean_name": "아하토큰",
        "english_name": "AhaToken"
    },
    {
        "market": "KRW-SPND",
        "korean_name": "스펜드코인",
        "english_name": "Spendcoin"
    },
    {
        "market": "KRW-LINK",
        "korean_name": "체인링크",
        "english_name": "Chainlink"
    },
    {
        "market": "KRW-XTZ",
        "korean_name": "테조스",
        "english_name": "Tezos"
    },
    {
        "market": "KRW-BORA",
        "korean_name": "보라",
        "english_name": "BORA"
    },
    {
        "market": "KRW-JST",
        "korean_name": "저스트",
        "english_name": "JUST"
    },
    {
        "market": "KRW-CRO",
        "korean_name": "크립토닷컴체인",
        "english_name": "Crypto.com Chain"
    },
    {
        "market": "KRW-TON",
        "korean_name": "톤",
        "english_name": "TON"
    },
    {
        "market": "KRW-SXP",
        "korean_name": "스와이프",
        "english_name": "Swipe"
    },
    {
        "market": "KRW-LAMB",
        "korean_name": "람다",
        "english_name": "Lambda"
    },
    {
        "market": "KRW-HUNT",
        "korean_name": "헌트",
        "english_name": "HUNT"
    },
    {
        "market": "KRW-MARO",
        "korean_name": "마로",
        "english_name": "Maro"
    },
    {
        "market": "KRW-PLA",
        "korean_name": "플레이댑",
        "english_name": "PlayDapp"
    },
    {
        "market": "KRW-DOT",
        "korean_name": "폴카닷",
        "english_name": "Polkadot"
    },
    {
        "market": "KRW-SRM",
        "korean_name": "세럼",
        "english_name": "Serum"
    },
    {
        "market": "KRW-MVL",
        "korean_name": "엠블",
        "english_name": "MVL"
    },
    {
        "market": "KRW-PCI",
        "korean_name": "페이코인",
        "english_name": "PayCoin"
    },
    {
        "market": "KRW-STRAX",
        "korean_name": "스트라티스",
        "english_name": "Stratis"
    },
    {
        "market": "KRW-AQT",
        "korean_name": "알파쿼크",
        "english_name": "Alpha Quark Token"
    },
    {
        "market": "KRW-BCHA",
        "korean_name": "비트코인캐시에이비씨",
        "english_name": "Bitcoin Cash ABC"
    },
    {
        "market": "KRW-GLM",
        "korean_name": "골렘",
        "english_name": "Golem"
    },
    {
        "market": "KRW-QTCON",
        "korean_name": "퀴즈톡",
        "english_name": "Quiztok"
    },
    {
        "market": "KRW-SSX",
        "korean_name": "썸씽",
        "english_name": "SOMESING"
    },
    {
        "market": "KRW-META",
        "korean_name": "메타디움",
        "english_name": "Metadium"
    },
    {
        "market": "KRW-OBSR",
        "korean_name": "옵저버",
        "english_name": "Observer"
    },
    {
        "market": "KRW-FCT2",
        "korean_name": "피르마체인",
        "english_name": "FirmaChain"
    },
    {
        "market": "KRW-LBC",
        "korean_name": "엘비알와이크레딧",
        "english_name": "LBRY Credits"
    },
    {
        "market": "KRW-CBK",
        "korean_name": "코박토큰",
        "english_name": "Cobak Token"
    },
    {
        "market": "KRW-SAND",
        "korean_name": "샌드박스",
        "english_name": "The Sandbox"
    },
    {
        "market": "KRW-HUM",
        "korean_name": "휴먼스케이프",
        "english_name": "Humanscape"
    },
    {
        "market": "KRW-DOGE",
        "korean_name": "도지코인",
        "english_name": "Dogecoin"
    }
]
