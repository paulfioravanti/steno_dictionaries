# pylint: disable=too-many-lines
'''
Test Plover steno chord to romaji transformation
'''

import unittest
from japanese_romaji import lookup


class TestJapaneseRomaji(unittest.TestCase):
    '''
    Test Plover steno chord to romaji transformation
    '''

    __STROKE_LIST = [
        # a
        ("A", "a"),
        ("AD", "aa"),
        ("ADZ", "aa"),
        ("AEU", "ai"),
        ("AFP", "ati"),
        ("AFPL", "a-"),
        ("AO", "ao"),
        ("AOEU", "aoi"),
        ("AOU", "aou"),
        ("APB", "ann"),
        ("ARB", "asi"),
        ("ARBT", "asita"),
        ("AU", "au"),
        ("AZ", "xa"),
        # i
        ("EU", "i"),
        ("EUD", "ii"),
        ("EUDZ", "ii"),
        ("EUFP", "iti"),
        ("EUPB", "inn"),
        ("EUPL", "ima"),
        ("EURB", "isi"),
        ("EUT", "ita"),
        ("EUZ", "xi"),
        # u
        ("U", "u"),
        ("UD", "uu"),
        ("UDZ", "uu"),
        ("UPB", "unn"),
        ("UZ", "xu"),
        # e
        ("E", "e"),
        ("ED", "ee"),
        ("EDZ", "ee"),
        ("EPB", "enn"),
        ("EZ", "xe"),
        # o
        ("O", "o"),
        ("OBG", "oku"),
        ("OD", "oo"),
        ("ODZ", "oo"),
        ("OEU", "oi"),
        ("OPB", "onn"),
        ("OU", "ou"),
        ("OZ", "xo"),
        # ka
        ("KA", "ka"),
        ("KA*D", "kaga"),
        ("KAD", "kaka"),
        ("KADZ", "kaa"),
        ("KAE", "kae"),
        ("KAEU", "kai"),
        ("KAFPL", "ka-"),
        ("KAO", "kao"),
        ("KAOE", "kaoe"),
        ("KAOEU", "kaoi"),
        ("KAOU", "kaou"),
        ("KAPB", "kann"),
        ("KAU", "kau"),
        ("KAZ", "xka"),
        # ki
        ("K*EUD", "kigi"),
        ("KEU", "ki"),
        ("KEUD", "kiki"),
        ("KEUDZ", "kii"),
        ("KEUPB", "kinn"),
        # ku
        ("-BG", "ku"),
        ("-BGD", "kuku"),
        # ("*BGD", "kugu"), ???
        ("K*UD", "kugu"),
        ("KU", "ku"),
        ("KUD", "kuku"),
        ("KUDZ", "kuu"),
        ("KUPB", "kunn"),
        # ke
        ("K*ED", "kege"),
        ("KE", "ke"),
        ("KED", "keke"),
        ("KEDZ", "kee"),
        ("KEPB", "kenn"),
        ("KEZ", "xke"),
        # ko
        ("KO", "ko"),
        ("KO*D", "kogo"),
        ("KOD", "koko"),
        ("KODZ", "koo"),
        ("KOE", "koe"),
        ("KOER", "koeru"),
        ("KOEU", "koi"),
        ("KOFP", "koti"),
        ("KOPB", "konn"),
        ("KORB", "kosi"),
        ("KOU", "kou"),
        ("KOUFP", "kouti"),
        # sa
        ("SA", "sa"),
        ("SAD", "sasa"),
        ("SADZ", "saa"),
        ("SAE", "sae"),
        ("SAEU", "sai"),
        ("SAO", "sao"),
        ("SAOEU", "saoi"),
        ("SAOU", "saou"),
        ("SAPB", "sann"),
        ("SAU", "sau"),
        # shi
        ("-RB", "si"),
        ("-RBDZ", "sii"),
        ("-RBT", "sita"),
        ("SEU", "si"),
        ("SEUD", "sisi"),
        ("SEUDZ", "sii"),
        ("SEUPB", "sinn"),
        ("SEUPL", "sima"),
        ("SEUPLS", "simasu"),
        ("SEUTS", "situ"),
        ("SH*EUD", "shiji"),
        ("SHEU", "shi"),
        ("SHEUD", "shishi"),
        ("SHEUDZ", "shii"),
        ("SHEUPB", "shinn"),
        ("SHEUPL", "shima"),
        ("SHEUPLS", "shimasu"),
        ("SHEUTS", "shitu"),
        # su
        ("-S", "su"),
        ("SHRA", "suhya"),
        ("SKA", "suka"),
        ("SKEU", "suki"),
        ("SKHA", "sucha"),
        ("SKRA", "sukya"),
        ("SPHA", "suma"),
        ("SPHRA", "sumya"),
        ("SPRA", "supya"),
        ("SPWA", "suba"),
        ("SPWRA", "subya"),
        ("STKA", "suda"),
        ("STKPWRA", "sugya"),
        ("STPA", "sufa"),
        ("STPHA", "suna"),
        ("STPHRA", "sunya"),
        ("SU", "su"),
        ("SUD", "susu"),
        ("SUDZ", "suu"),
        ("SUPB", "sunn"),
        ("SUT", "suta"),
        ("SWRA", "surya"),
        # se
        ("SE", "se"),
        ("SED", "sese"),
        ("SEDZ", "see"),
        ("SEPB", "senn"),
        # so
        ("SO", "so"),
        ("SOD", "soso"),
        ("SODZ", "soo"),
        ("SOE", "soe"),
        # ("SOER", "sore"), inverted re?
        ("SOEU", "soi"),
        ("SOPB", "sonn"),
        ("SOU", "sou"),
        # ta
        ("-T", "ta"),
        ("T-T", "tta"),
        ("TA", "ta"),
        ("TA*D", "tada"),
        ("TABG", "taku"),
        ("TAD", "tata"),
        ("TADZ", "taa"),
        ("TAE", "tae"),
        ("TAEU", "tai"),
        ("TAFP", "tati"),
        ("TAO", "tao"),
        ("TAOE", "taoe"),
        ("TAOEU", "taoi"),
        ("TAOU", "taou"),
        ("TAPB", "tann"),
        ("TARB", "tasi"),
        ("TAU", "tau"),
        # chi
        ("-FP", "ti"),
        ("-FPD", "titi"),
        ("-FPDZ", "tii"),
        ("KH*EUD", "chidi"),
        ("KHEU", "chi"),
        ("KHEUD", "chichi"),
        ("KHEUDZ", "chii"),
        ("KHEUPB", "chinn"),
        # tsu
        ("-TS", "tu"),
        ("T*UD", "tudu"),
        ("TU", "tu"),
        ("TUD", "tutu"),
        ("TUDZ", "tuu"),
        ("TUPB", "tunn"),
        ("TUZ", "xtu"),
        # te
        ("T*ED", "tede"),
        ("TE", "te"),
        ("TED", "tete"),
        ("TEDZ", "tee"),
        ("TEPB", "tenn"),
        ("TEU", "ti"),
        ("TEUPB", "tinn"),
        # to
        ("TO", "to"),
        ("TO*D", "todo"),
        ("TOD", "toto"),
        ("TODZ", "too"),
        ("TOE", "toe"),
        ("TOEU", "toi"),
        ("TOPB", "tonn"),
        ("TOU", "tou"),
        # na
        ("TPHA", "na"),
        ("TPHAD", "nana"),
        ("TPHADZ", "naa"),
        ("TPHAE", "nae"),
        ("TPHAEU", "nai"),
        ("TPHAO", "nao"),
        ("TPHAOE", "naoe"),
        ("TPHAOEU", "naoi"),
        ("TPHAOU", "naou"),
        ("TPHAPB", "nann"),
        ("TPHAT", "nata"),
        ("TPHAU", "nau"),
        # ni
        ("TPHEU", "ni"),
        ("TPHEUD", "nini"),
        ("TPHEUDZ", "nii"),
        ("TPHEUFP", "niti"),
        ("TPHEUPB", "ninn"),
        # nu
        ("TPHU", "nu"),
        ("TPHUD", "nunu"),
        ("TPHUDZ", "nuu"),
        ("TPHUPB", "nunn"),
        # ne
        ("TPH*EDZ", "nexe"),
        ("TPHE", "ne"),
        ("TPHED", "nene"),
        ("TPHEDZ", "nee"),
        ("TPHEPB", "nenn"),
        # no
        ("TPHO", "no"),
        ("TPHOD", "nono"),
        ("TPHODZ", "noo"),
        ("TPHOE", "noe"),
        ("TPHOEU", "noi"),
        ("TPHOPB", "nonn"),
        ("TPHORB", "nosi"),
        ("TPHOU", "nou"),
        # ha
        ("HA", "ha"),
        ("HA*D", "haba"),
        ("HAD", "haha"),
        ("HADZ", "haa"),
        ("HAE", "hae"),
        ("HAEU", "hai"),
        ("HAFP", "hati"),
        ("HAO", "hao"),
        ("HAOE", "haoe"),
        ("HAOEU", "haoi"),
        ("HAOU", "haou"),
        ("HAPB", "hann"),
        ("HARB", "hasi"),
        ("HAU", "hau"),
        # hi
        ("H*EUD", "hibi"),
        ("HEU", "hi"),
        ("HEUD", "hihi"),
        ("HEUDZ", "hii"),
        ("HEUPB", "hinn"),
        # fu
        ("TP*UD", "fubu"),
        ("TP*UDZ", "fuxu"),
        ("TPU", "fu"),
        ("TPUD", "fufu"),
        ("TPUDZ", "fuu"),
        ("TPUPB", "funn"),
        # he
        ("H*ED", "hebe"),
        ("H*EDZ", "hexe"),
        ("HE", "he"),
        ("HED", "hehe"),
        ("HEDZ", "hee"),
        ("HEPB", "henn"),
        # ho
        ("HO", "ho"),
        ("HO*D", "hobo"),
        ("HO*DZ", "hoxo"),
        ("HOD", "hoho"),
        ("HODZ", "hoo"),
        ("HOE", "hoe"),
        ("HOEU", "hoi"),
        ("HOPB", "honn"),
        ("HOU", "hou"),
        # ma
        ("-PL", "ma"),
        ("-PLD", "mama"),
        ("-PLS", "masu"),
        ("PHA", "ma"),
        ("PHA*DZ", "maxa"),
        ("PHAD", "mama"),
        ("PHADZ", "maa"),
        ("PHAE", "mae"),
        ("PHAEU", "mai"),
        ("PHAO", "mao"),
        ("PHAOE", "maoe"),
        ("PHAOEU", "maoi"),
        ("PHAOU", "maou"),
        ("PHAPB", "mann"),
        ("PHARBT", "masita"),
        ("PHAU", "mau"),
        # mi
        ("PHEU", "mi"),
        ("PHEUD", "mimi"),
        ("PHEUDZ", "mii"),
        ("PHEUPB", "minn"),
        # mu
        ("PHU", "mu"),
        ("PHUD", "mumu"),
        ("PHUDZ", "muu"),
        ("PHUPB", "munn"),
        # me
        ("PHE", "me"),
        ("PHED", "meme"),
        ("PHEDZ", "mee"),
        ("PHEPB", "menn"),
        ("PHEPL", "mema"),
        # mo
        ("PHO", "mo"),
        ("PHOD", "momo"),
        ("PHODZ", "moo"),
        ("PHOE", "moe"),
        ("PHOEU", "moi"),
        ("PHOPB", "monn"),
        ("PHOU", "mou"),
        # ya
        ("KWRA", "ya"),
        ("KWRA*DZ", "yaxa"),
        ("KWRAD", "yaya"),
        ("KWRADZ", "yaa"),
        ("KWRAE", "yae"),
        ("KWRAEG", "yaegu"),
        ("KWRAEU", "yai"),
        ("KWRAO", "yao"),
        ("KWRAOE", "yaoe"),
        ("KWRAOEU", "yaoi"),
        ("KWRAOU", "yaou"),
        ("KWRAPB", "yann"),
        ("KWRAU", "yau"),
        ("KWRAZ", "xya"),
        # yu
        ("KWRU", "yu"),
        ("KWRUD", "yuyu"),
        ("KWRUDZ", "yuu"),
        ("KWRUPB", "yunn"),
        ("KWRUZ", "xyu"),
        # yo
        ("KWRO", "yo"),
        ("KWRO*DZ", "yoxo"),
        ("KWROD", "yoyo"),
        ("KWRODZ", "yoo"),
        ("KWROE", "yoe"),
        ("KWROEU", "yoi"),
        ("KWROPB", "yonn"),
        ("KWROU", "you"),
        ("KWROZ", "xyo"),
        # ra
        ("RA", "ra"),
        ("RAD", "rara"),
        ("RADZ", "raa"),
        ("RAE", "rae"),
        ("RAEU", "rai"),
        ("RAO", "rao"),
        ("RAOE", "raoe"),
        ("RAOEU", "raoi"),
        ("RAOU", "raou"),
        ("RAPB", "rann"),
        ("RAU", "rau"),
        # ri
        ("REU", "ri"),
        ("REUD", "riri"),
        ("REUDZ", "rii"),
        ("REUPB", "rinn"),
        # ru
        ("RU", "ru"),
        ("RUD", "ruru"),
        ("RUDZ", "ruu"),
        ("RUPB", "runn"),
        # re
        ("RE", "re"),
        ("RED", "rere"),
        ("REDZ", "ree"),
        ("REPB", "renn"),
        # ro
        ("RO", "ro"),
        ("ROD", "roro"),
        ("RODZ", "roo"),
        ("ROE", "roe"),
        ("ROEU", "roi"),
        ("ROPB", "ronn"),
        ("ROU", "rou"),
        # wa
        ("WA", "wa"),
        ("WA*DZ", "waxa"),
        ("WAD", "wawa"),
        ("WADZ", "waa"),
        ("WAE", "wae"),
        ("WAEU", "wai"),
        ("WAO", "wao"),
        ("WAOE", "waoe"),
        ("WAOEU", "waoi"),
        ("WAOU", "waou"),
        ("WAPB", "wann"),
        ("WAT", "wata"),
        ("WAU", "wau"),
        # wo
        ("WO", "wo"),
        # n
        ("-PB", "nn"),
        ("TPH", "nn"),
        # ga
        ("TKPWA", "ga"),
        ("TKPWAD", "gaga"),
        ("TKPWADZ", "gaa"),
        ("TKPWAE", "gae"),
        ("TKPWAEU", "gai"),
        ("TKPWAO", "gao"),
        ("TKPWAOE", "gaoe"),
        ("TKPWAOEU", "gaoi"),
        ("TKPWAOU", "gaou"),
        ("TKPWAPB", "gann"),
        ("TKPWAU", "gau"),
        # gi
        ("TKPWEU", "gi"),
        ("TKPWEUD", "gigi"),
        ("TKPWEUDZ", "gii"),
        ("TKPWEUPB", "ginn"),
        # gu
        ("TKPWU", "gu"),
        ("TKPWUD", "gugu"),
        ("TKPWUDZ", "guu"),
        ("TKPWUPB", "gunn"),
        # ge
        ("TKPWE", "ge"),
        ("TKPWED", "gege"),
        ("TKPWEDZ", "gee"),
        ("TKPWEPB", "genn"),
        # go
        ("TKPWO", "go"),
        ("TKPWOD", "gogo"),
        ("TKPWODZ", "goo"),
        ("TKPWOE", "goe"),
        ("TKPWOEU", "goi"),
        ("TKPWOPB", "gonn"),
        ("TKPWOU", "gou"),
        # za
        ("SA*", "za"),
        ("SA*D", "zaza"),
        ("SA*E", "zae"),
        ("SA*EU", "zai"),
        ("SA*PB", "zann"),
        ("SA*U", "zau"),
        ("SAO*", "zao"),
        ("SAO*E", "zaoe"),
        ("SAO*EU", "zaoi"),
        ("SAO*U", "zaou"),
        ("STKPWA", "za"),
        ("STKPWAD", "zaza"),
        ("STKPWADZ", "zaa"),
        ("STKPWAE", "zae"),
        ("STKPWAEU", "zai"),
        ("STKPWAO", "zao"),
        ("STKPWAOE", "zaoe"),
        ("STKPWAOEU", "zaoi"),
        ("STKPWAOU", "zaou"),
        ("STKPWAPB", "zann"),
        ("STKPWAU", "zau"),
        # ji
        ("SKWR*EUDZ", "jixi"),
        ("SKWREU", "ji"),
        ("SKWREUD", "jiji"),
        ("SKWREUDZ", "jii"),
        ("SKWREUPB", "jinn"),
        ("STKPWEU", "zi"),
        ("STKPWEUD", "zizi"),
        ("STKPWEUDZ", "zii"),
        ("STKPWEUPB", "zinn"),
        # zu
        ("S*U", "zu"),
        ("S*UD", "zuzu"),
        ("S*UDZ", "zuu"),
        ("S*UPB", "zunn"),
        ("STKPWU", "zu"),
        ("STKPWUD", "zuzu"),
        ("STKPWUDZ", "zuu"),
        ("STKPWUPB", "zunn"),
        # ze
        ("S*E", "ze"),
        ("S*ED", "zeze"),
        ("S*EDZ", "zee"),
        ("S*EPB", "zenn"),
        ("STKPWE", "ze"),
        ("STKPWED", "zeze"),
        ("STKPWEDZ", "zee"),
        ("STKPWEPB", "zenn"),
        # zo
        ("SO*", "zo"),
        ("SO*E", "zoe"),
        ("SO*EU", "zoi"),
        ("SO*D", "zozo"),
        ("SO*DZ", "zoo"),
        ("SO*PB", "zonn"),
        ("SO*U", "zou"),
        ("STKPWO", "zo"),
        ("STKPWOE", "zoe"),
        ("STKPWOEU", "zoi"),
        ("STKPWOD", "zozo"),
        ("STKPWODZ", "zoo"),
        ("STKPWOPB", "zonn"),
        ("STKPWOU", "zou"),
        # da
        ("TKA", "da"),
        ("TKAD", "dada"),
        ("TKADZ", "daa"),
        ("TKAE", "dae"),
        ("TKAEU", "dai"),
        ("TKAO", "dao"),
        ("TKAOE", "daoe"),
        ("TKAOEU", "daoi"),
        ("TKAOU", "daou"),
        ("TKAPB", "dann"),
        ("TKAU", "dau"),
        # di
        ("TK*EUDZ", "dixi"),
        ("TKEU", "di"),
        ("TKEUD", "didi"),
        ("TKEUDZ", "dii"),
        ("TKEUPB", "dinn"),
        # du
        ("TK*UDZ", "duxu"),
        ("TKU", "du"),
        ("TKUD", "dudu"),
        ("TKUDZ", "duu"),
        ("TKUPB", "dunn"),
        # de
        ("TKE", "de"),
        ("TKED", "dede"),
        ("TKEDZ", "dee"),
        ("TKEPB", "denn"),
        ("TKERBT", "desita"),
        ("TKET", "deta"),
        # do
        ("TKO", "do"),
        ("TKOD", "dodo"),
        ("TKODZ", "doo"),
        ("TKOE", "doe"),
        ("TKOEU", "doi"),
        ("TKOPB", "donn"),
        ("TKOU", "dou"),
        # ba
        ("PWA", "ba"),
        ("PWA*D", "bapa"),
        ("PWAD", "baba"),
        ("PWADZ", "baa"),
        ("PWAE", "bae"),
        ("PWAEU", "bai"),
        ("PWAO", "bao"),
        ("PWAOE", "baoe"),
        ("PWAOEU", "baoi"),
        ("PWAOU", "baou"),
        ("PWAPB", "bann"),
        ("PWAU", "bau"),
        # bi
        ("PW*EUD", "bipi"),
        ("PWEU", "bi"),
        ("PWEUD", "bibi"),
        ("PWEUDZ", "bii"),
        ("PWEUPB", "binn"),
        # bu
        ("PW*UD", "bupu"),
        ("PWU", "bu"),
        ("PWUD", "bubu"),
        ("PWUDZ", "buu"),
        ("PWUPB", "bunn"),
        # be
        ("PW*ED", "bepe"),
        ("PWE", "be"),
        ("PWED", "bebe"),
        ("PWEDZ", "bee"),
        ("PWEPB", "benn"),
        # bo
        ("PWO", "bo"),
        ("PWO*D", "bopo"),
        ("PWOD", "bobo"),
        ("PWODZ", "boo"),
        ("PWOE", "boe"),
        ("PWOEU", "boi"),
        ("PWOPB", "bonn"),
        ("PWOU", "bou"),
        # pa
        ("PA", "pa"),
        ("PABG", "paku"),
        ("PAD", "papa"),
        ("PADZ", "paa"),
        ("PAE", "pae"),
        ("PAEU", "pai"),
        ("PAO", "pao"),
        ("PAOE", "paoe"),
        ("PAOEU", "paoi"),
        ("PAOU", "paou"),
        ("PAPB", "pann"),
        ("PAU", "pau"),
        # pi
        ("PEU", "pi"),
        ("PEUD", "pipi"),
        ("PEUDZ", "pii"),
        ("PEUPB", "pinn"),
        # pu
        ("PU", "pu"),
        ("PUD", "pupu"),
        ("PUDZ", "puu"),
        ("PUPB", "punn"),
        # pe
        ("PE", "pe"),
        ("PED", "pepe"),
        ("PEDZ", "pee"),
        ("PEPB", "penn"),
        # po
        ("PO", "po"),
        ("POD", "popo"),
        ("PODZ", "poo"),
        ("POE", "poe"),
        ("POEU", "poi"),
        ("POPB", "ponn"),
        ("POU", "pou"),
        # kya
        ("KRA", "kya"),
        ("KRAD", "kyakya"),
        ("KRAE", "kyae"),
        ("KRAEU", "kyai"),
        ("KRAO", "kyao"),
        ("KRAOE", "kyaoe"),
        ("KRAOEU", "kyaoi"),
        ("KRAOU", "kyaou"),
        ("KRAPB", "kyann"),
        ("KRAU", "kyau"),
        # kyu
        ("KRU", "kyu"),
        ("KRUD", "kyukyu"),
        ("KRUDZ", "kyuu"),
        ("KRUPB", "kyunn"),
        # kyo
        ("KRO", "kyo"),
        ("KROD", "kyokyo"),
        ("KRODZ", "kyoo"),
        ("KROE", "kyoe"),
        ("KROEU", "kyoi"),
        ("KROPB", "kyonn"),
        ("KROU", "kyou"),
        # gya
        ("TKPWRA", "gya"),
        ("TKPWRAD", "gyagya"),
        ("TKPWRADZ", "gyaa"),
        ("TKPWRAE", "gyae"),
        ("TKPWRAEU", "gyai"),
        ("TKPWRAO", "gyao"),
        ("TKPWRAOE", "gyaoe"),
        ("TKPWRAOEU", "gyaoi"),
        ("TKPWRAOU", "gyaou"),
        ("TKPWRAPB", "gyann"),
        ("TKPWRAU", "gyau"),
        # gyu
        ("TKPWRU", "gyu"),
        ("TKPWRUD", "gyugyu"),
        ("TKPWRUDZ", "gyuu"),
        ("TKPWRUPB", "gyunn"),
        # gyo
        ("TKPWRO", "gyo"),
        ("TKPWROD", "gyogyo"),
        ("TKPWRODZ", "gyoo"),
        ("TKPWROE", "gyoe"),
        ("TKPWROEU", "gyoi"),
        ("TKPWROPB", "gyonn"),
        ("TKPWROU", "gyou"),
        # nya
        ("TPHRA", "nya"),
        ("TPHRAD", "nyanya"),
        ("TPHRADZ", "nyaa"),
        ("TPHRAE", "nyae"),
        ("TPHRAEU", "nyai"),
        ("TPHRAO", "nyao"),
        ("TPHRAOE", "nyaoe"),
        ("TPHRAOEU", "nyaoi"),
        ("TPHRAOU", "nyaou"),
        ("TPHRAPB", "nyann"),
        ("TPHRAU", "nyau"),
        # nyu
        ("TPHRU", "nyu"),
        ("TPHRUD", "nyunyu"),
        ("TPHRUDZ", "nyuu"),
        ("TPHRUPB", "nyunn"),
        # nyo
        ("TPHRO", "nyo"),
        ("TPHROD", "nyonyo"),
        ("TPHRODZ", "nyoo"),
        ("TPHROE", "nyoe"),
        ("TPHROEU", "nyoi"),
        ("TPHROPB", "nyonn"),
        ("TPHROU", "nyou"),
        # hya
        ("HRA", "hya"),
        ("HRA*D", "hyabya"),
        ("HRAD", "hyahya"),
        ("HRADZ", "hyaa"),
        ("HRAE", "hyae"),
        ("HRAEU", "hyai"),
        ("HRAO", "hyao"),
        ("HRAOE", "hyaoe"),
        ("HRAOEU", "hyaoi"),
        ("HRAOU", "hyaou"),
        ("HRAPB", "hyann"),
        ("HRAU", "hyau"),
        # hyu
        ("HR*UD", "hyubyu"),
        ("HRU", "hyu"),
        ("HRUD", "hyuhyu"),
        ("HRUDZ", "hyuu"),
        ("HRUPB", "hyunn"),
        # hyo
        ("HRO", "hyo"),
        ("HRO*D", "hyobyo"),
        ("HROD", "hyohyo"),
        ("HRODZ", "hyoo"),
        ("HROE", "hyoe"),
        ("HROEU", "hyoi"),
        ("HROPB", "hyonn"),
        ("HROU", "hyou"),
        # bya
        ("PWRA", "bya"),
        ("PWRAD", "byabya"),
        ("PWRADZ", "byaa"),
        ("PWRAE", "byae"),
        ("PWRAEU", "byai"),
        ("PWRAO", "byao"),
        ("PWRAOE", "byaoe"),
        ("PWRAOEU", "byaoi"),
        ("PWRAOU", "byaou"),
        ("PWRAPB", "byann"),
        ("PWRAU", "byau"),
        # byu
        ("PWRU", "byu"),
        ("PWRUD", "byubyu"),
        ("PWRUDZ", "byuu"),
        ("PWRUPB", "byunn"),
        # byo
        ("PWRO", "byo"),
        ("PWROD", "byobyo"),
        ("PWRODZ", "byoo"),
        ("PWROE", "byoe"),
        ("PWROEU", "byoi"),
        ("PWROPB", "byonn"),
        ("PWROU", "byou"),
        # pya
        ("PRA", "pya"),
        ("PRAD", "pyapya"),
        ("PRADZ", "pyaa"),
        ("PRAE", "pyae"),
        ("PRAEU", "pyai"),
        ("PRAO", "pyao"),
        ("PRAOE", "pyaoe"),
        ("PRAOEU", "pyaoi"),
        ("PRAOU", "pyaou"),
        ("PRAPB", "pyann"),
        ("PRAU", "pyau"),
        # pyu
        ("PRU", "pyu"),
        ("PRUD", "pyupyu"),
        ("PRUDZ", "pyuu"),
        ("PRUPB", "pyunn"),
        # pyo
        ("PRO", "pyo"),
        ("PROD", "pyopyo"),
        ("PRODZ", "pyoo"),
        ("PROE", "pyoe"),
        ("PROEU", "pyoi"),
        ("PROPB", "pyonn"),
        ("PROU", "pyou"),
        # mya
        ("PHRA", "mya"),
        ("PHRAD", "myamya"),
        ("PHRADZ", "myaa"),
        ("PHRAE", "myae"),
        ("PHRAEU", "myai"),
        ("PHRAO", "myao"),
        ("PHRAOE", "myaoe"),
        ("PHRAOEU", "myaoi"),
        ("PHRAOU", "myaou"),
        ("PHRAPB", "myann"),
        ("PHRAU", "myau"),
        # myu
        ("PHRU", "myu"),
        ("PHRUD", "myumyu"),
        ("PHRUDZ", "myuu"),
        ("PHRUPB", "myunn"),
        # myo
        ("PHRO", "myo"),
        ("PHROD", "myomyo"),
        ("PHRODZ", "myoo"),
        ("PHROE", "myoe"),
        ("PHROEU", "myoi"),
        ("PHROPB", "myonn"),
        ("PHROU", "myou"),
        # rya
        ("WRA", "rya"),
        ("WRAD", "ryarya"),
        ("WRADZ", "ryaa"),
        ("WRAE", "ryae"),
        ("WRAEU", "ryai"),
        ("WRAO", "ryao"),
        ("WRAOE", "ryaoe"),
        ("WRAOEU", "ryaoi"),
        ("WRAOU", "ryaou"),
        ("WRAPB", "ryann"),
        ("WRAU", "ryau"),
        # ryu
        ("WRU", "ryu"),
        ("WRUD", "ryuryu"),
        ("WRUDZ", "ryuu"),
        ("WRUPB", "ryunn"),
        # ryo
        ("WRO", "ryo"),
        ("WROD", "ryoryo"),
        ("WRODZ", "ryoo"),
        ("WROE", "ryoe"),
        ("WROEU", "ryoi"),
        ("WROPB", "ryonn"),
        ("WROU", "ryou"),
        # ja
        ("SKWRA", "ja"),
        ("SKWRAD", "jaja"),
        ("SKWRADZ", "jaa"),
        ("SKWRAE", "jae"),
        ("SKWRAEU", "jai"),
        ("SKWRAO", "jao"),
        ("SKWRAOE", "jaoe"),
        ("SKWRAOEU", "jaoi"),
        ("SKWRAOU", "jaou"),
        ("SKWRAPB", "jann"),
        ("SKWRAU", "jau"),
        # ju
        ("SKWRU", "ju"),
        ("SKWRUD", "juju"),
        ("SKWRUDZ", "juu"),
        ("SKWRUPB", "junn"),
        # je
        ("SKWRE", "je"),
        ("SKWRED", "jeje"),
        ("SKWREDZ", "jee"),
        ("SKWREPB", "jenn"),
        # jo
        ("SKWRO", "jo"),
        ("SKWROD", "jojo"),
        ("SKWRODZ", "joo"),
        ("SKWROE", "joe"),
        ("SKWROEU", "joi"),
        ("SKWROPB", "jonn"),
        ("SKWROU", "jou"),
        # cha
        ("KHA", "cha"),
        ("KHA*D", "chadya"),
        ("KHAD", "chacha"),
        ("KHADZ", "chaa"),
        ("KHAE", "chae"),
        ("KHAEU", "chai"),
        ("KHAO", "chao"),
        ("KHAOE", "chaoe"),
        ("KHAOEU", "chaoi"),
        ("KHAOU", "chaou"),
        ("KHAPB", "chann"),
        ("KHAU", "chau"),
        # chu
        ("KH*UD", "chudyu"),
        ("KHU", "chu"),
        ("KHUD", "chuchu"),
        ("KHUDZ", "chuu"),
        ("KHUPB", "chunn"),
        # che
        ("KH*ED", "chedye"),
        ("KHE", "che"),
        ("KHED", "cheche"),
        ("KHEDZ", "chee"),
        ("KHEPB", "chenn"),
        # cho
        ("KHO", "cho"),
        ("KHO*D", "chodyo"),
        ("KHOD", "chocho"),
        ("KHODZ", "choo"),
        ("KHOE", "choe"),
        ("KHOEU", "choi"),
        ("KHOPB", "chonn"),
        ("KHOU", "chou"),
        # sha
        ("SHA", "sha"),
        ("SHA*D", "shaja"),
        ("SHAD", "shasha"),
        ("SHADZ", "shaa"),
        ("SHAE", "shae"),
        ("SHAEU", "shai"),
        ("SHAEUPB", "shainn"),
        ("SHAO", "shao"),
        ("SHAOE", "shaoe"),
        ("SHAOEU", "shaoi"),
        ("SHAOU", "shaou"),
        ("SHAPB", "shann"),
        ("SHAU", "shau"),
        # shu
        ("SH*UD", "shuju"),
        ("SHU", "shu"),
        ("SHUD", "shushu"),
        ("SHUDZ", "shuu"),
        ("SHUPB", "shunn"),
        # she
        ("SH*ED", "sheje"),
        ("SHE", "she"),
        ("SHED", "sheshe"),
        ("SHEDZ", "shee"),
        ("SHEPB", "shenn"),
        # sho
        ("SHO", "sho"),
        ("SHO*D", "shojo"),
        ("SHOD", "shosho"),
        ("SHODZ", "shoo"),
        ("SHOE", "shoe"),
        ("SHOEU", "shoi"),
        ("SHOPB", "shonn"),
        ("SHOU", "shou"),
        # ye
        ("W*E", "wye"),
        # yi
        ("W*EU", "wyi"),
        # we
        ("WE", "we"),
        # wi
        ("WEU", "wi"),
        # va
        ("SRA", "va"),
        ("SRAPB", "vann"),
        # fi
        ("TPEU", "fi"),
        ("TPEUD", "fifi"),
        ("TPEUPB", "finn")
    ]

    def test_converting_steno_to_romaji(self):
        '''
        Test steno to romaji conversion
        '''
        for key, expected in self.__STROKE_LIST:
            with self.subTest():
                actual = lookup([key])
                self.assertEqual(actual, f"{{^{expected}^}}")

    def test_asterisk_stroke(self):
        '''
        * -> Backspace
        '''
        key = ["*"]
        expected = "{#BACKSPACE}{^}"
        actual = lookup(key)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
