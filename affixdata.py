stripped_affix = set([
    'TV-kanava',
    'ajopelisarja',
    'albumi',
    'alus',
    'alusta',
    'alustalla',
    'ammattilaisliiga',
    'ammattilaisliitto',
    'ammattiliitto',
    'ananasmehu',
    'animaatio',
    'animaatioelokuva',
    'animaatiosarja',
    'animesarja',
    'asejärjestelmä',
    'asiakasohjelma',
    'autokilpailu',
    'autolehti',
    'automalli',
    'autoyhtiö',
    'avaruusalus',
    'avaruusasema',
    'avaruuskapseli',
    'avaruusluotain',
    'avaruusohjelma',
    'avaruussukkula',
    'avaruusteknologiayhtiö',
    'avoauto',
    'baletti',
    'blogi',
    'brändi',
    'bussi',
    'debyyttialbumi',
    'debyyttisingle',
    'demoni',
    'demotapahtuma',
    'divisioona',
    'draamaelokuva',
    'draamasarja',
    'eduskuntaryhmä',
    'elintarvikekonserni',
    'elokuva',
    'elokuvasarja',
    'elokuvatrilogia',
    'elokuvayhtiö',
    'emoyhtiö',
    'energiajuoma',
    'ep',
    'erikoismalli',
    'erikoisyksikkö',
    'esikoisalbumi',
    'fantasiakirjasarja',
    'fantasiasarja',
    'farssi',
    'festivaalitapahtuma',
    'firma',
    'fuusioyhtye',
    'gaala',
    'gospelyhtye',
    'grafiikkasuoritin',
    'hakukone',
    'hampurilaisketju',
    'henkilöauto',
    'herra',
    'herttua',
    'hevonen',
    'hirviö',
    'hitti',
    'hittisingle',
    'hotelliketju',
    'huoltoalus',
    'hyväntekeväisyyssingle',
    'hyötyajoneuvo',
    'hävittäjä',
    'hävittäjäkone',
    'ikkunointijärjestelmä',
    'iltapäivälehti',
    'installaatio',
    'investointipankki',
    'jalkapalloseura',
    'jengi',
    'julkaisu',
    'jumala',
    'jumalatar',
    'juna',
    'junioriliiga',
    'juoma',
    'juusto',
    'järjestelmä',
    'järjestö',
    'jääkiekkoseura',
    'jäätikkö',
    'kaapelikanava',
    'kaapelitelevisiokanava',
    'kaivosyhtiö',
    'kampanja',
    'kanava',
    'kanavalta',
    'kanavapaketti',
    'kanavasta',
    'kantoraketti',
    'kantriyhtye',
    'kapinaliike',
    'karkki',
    'katumaasturi',
    'kauhuelokuva',
    'kauhuelokuvasarja',
    'kauhusarja',
    'kauppaketju',
    'kaupunkilehti',
    'keiju',
    'keksi',
    'keskusteluohjelma',
    'ketju',
    'kiinteistöyhtiö',
    'kilpa-auto',
    'kirja',
    'kirjasarja',
    'kissa',
    'kitarayhtiö',
    'kivääri',
    'klooni',
    'koira',
    'kokoelma-albumi',
    'kokoelmalevysarja',
    'kokoelmapaketti',
    'kolikkopeli',
    'komediaelokuva',
    'komediasarja',
    'kone',
    'konekivääri',
    'konseptialbumi',
    'konserni',
    'konserttikiertue',
    'konsoli',
    'koomikkoryhmä',
    'kotitietokone',
    'kuljetuslentokone',
    'kuningas',
    'kunniamitali',
    'kuorma-auto',
    'kustannusyhtiö',
    'kuu',
    'kuunnelmasarja',
    'kuvankäsittelyohjelma',
    'kykyjenetsintäohjelma',
    'käsikonsoli',
    'käsipelikonsoli',
    'käyttöjärjestelmä',
    'käyttöliittymä',
    'käyttöliittymäkirjasto',
    'kääpiö',
    'kääpiöauto',
    'laboratorio',
    'laite',
    'laitteisto',
    'lajike',
    'lammas',
    'lasisarja',
    'laskeutumisjärjestelmä',
    'lastenohjelma',
    'latauspalvelu',
    'laukaisualusta',
    'lautapeli',
    'lehti',
    'lennokki',
    'lentokone',
    'lentotukialus',
    'lentoyhtiö',
    'levy',
    'levy-yhtiö',
    'liiga',
    'liiketoimintaryhmä',
    'likööri',
    'linja-auto',
    'lista',
    'listaohjelma',
    'lisälaite',
    'livealbumi',
    'lohikäärme',
    'lukulaite',
    'luotain',
    'luotijuna',
    'lyhytelokuva',
    'lännensarja',
    'maastoauto',
    'mainostoimisto',
    'makeisyritys',
    'maksukanava',
    'mallisarja',
    'mallisto',
    'mallitoimisto',
    'manga',
    'matkapuhelin',
    'mediakonserni',
    'mediasoitin',
    'menestyselokuva',
    'merimaaliohjus',
    'merkkinen',
    'metalliyhtye',
    'metalyhtye',
    'miehistökapseli',
    'mieskuoro',
    'mikrosiru',
    'minialbumi',
    'minipeli',
    'minisarja',
    'mobiilialusta',
    'moottorivaunu',
    'mopo',
    'muistikortti',
    'mummo',
    'musiikkifestivaali',
    'musiikkikanava',
    'musiikkiohjelmisto',
    'musiikkiopisto',
    'musiikkisoitin',
    'musiikkivideo',
    'musiikkiyhtye',
    'musikaali',
    'nauhuri',
    'neiti',
    'nettiselain',
    'nimi',
    'noita',
    'novelli',
    'novellikokoelma',
    'nuorisoliike',
    'nuortenkirjasarja',
    'nyrkkeilyliitto',
    'näytelmä',
    'oheislaite',
    'oheistuote',
    'ohjain',
    'ohjelma',
    'ohjelmasarja',
    'ohjelmisto',
    'ohjelmointikieli',
    'ohjelmointirajapinta',
    'ohjus',
    'ohjustorjuntajärjestelmä',
    'olento',
    'olut',
    'ooppera',
    'operetti',
    'oppositioliike',
    'organisaatio',
    'orkesteri',
    'paikallislehti',
    'pakettiauto',
    'palkinto',
    'paluukiertue',
    'palvelin',
    'palvelinohjelmisto',
    'palvelu',
    'pankki',
    'pankkikonserni',
    'panssarivaunu',
    'papukaija',
    'peikko',
    'peli',
    'pelikokoelma',
    'pelikonsoli',
    'pelimoottori',
    'pelisarja',
    'pelitalo',
    'pelitapahtuma',
    'pienoismalli',
    'pienoisromaani',
    'piirisarja',
    'piirroselokuva',
    'piirrossarja',
    'pikaruokaketju',
    'pikkuauto',
    'pilvipalvelu',
    'pistooli',
    'pitkäsoitto',
    'planeetta',
    'poika',
    'pokeriohjelma',
    'poni',
    'popyhtye',
    'potkuriturbiinikone',
    'protokolla',
    'puhelin',
    'puhelinoperaattori',
    'puolue',
    'purjehdusseura',
    'purjevene',
    'päivitys',
    'päivälehti',
    'pääomasijoitusyhtiö',
    'pörssiyhtiö',
    'radio-ohjelma',
    'radiokanava',
    'radiopuhelin',
    'radioverkko',
    'rahasto',
    'rahtivarustamo',
    'raitiovaunu',
    'rakennusliike',
    'raketti',
    'ravintola',
    'ravintolaketju',
    'rikossarja',
    'risteilyohjus',
    'robotti',
    'rockfestivaali',
    'rockyhtye',
    'romaani',
    'roolipelisarja',
    'rouva',
    'runo',
    'runokokoelma',
    'saari',
    'saippuaooppera',
    'saippuasarja',
    'sarja',
    'sarjakuva',
    'sarjakuva-albumi',
    'sarjakuvaromaani',
    'satelliitti',
    'savuke',
    'selain',
    'selainmoottori',
    'selviytymiskauhupelisarja',
    'serkku',
    'setä',
    'sijoitusyhtiö',
    'sinfonia',
    'single',
    'sisko',
    'sissiliike',
    'sivusta',
    'sivusto',
    'sketsisarja',
    'skootteri',
    'sonni',
    'sovelluskauppa',
    'standardointiorganisaatio',
    'studioalbumi',
    'suihkuhävittäjä',
    'suihkukone',
    'sukellusvene',
    'sukkula',
    'sulatejuusto',
    'suoritin',
    'superyhtye',
    'suurnopeusjuna',
    'sähköpostiohjelma',
    'taistelupanssarivaunu',
    'talli',
    'talouslehti',
    'tanssiohjelma',
    'tanssiryhmä',
    'tanssisali',
    'tapahtuma',
    'tappelupelisarja',
    'tasohyppelypelisarja',
    'taulutietokone',
    'tavaramerkki',
    'teemakappale',
    'teknologia',
    'tekstinkäsittelyohjelma',
    'televisio',
    'televisio-ohjelma',
    'televisioelokuva',
    'televisiokanava',
    'televisiosarja',
    'televisioyhtiö',
    'teos',
    'terroristijärjestö',
    'tetralogia',
    'tieteiselokuva',
    'tieteissarja',
    'tietokirja',
    'tietokone',
    'tietoliikennesatelliitti',
    'tietosanakirja',
    'tilannekomediasarja',
    'toimintaelokuva',
    'toimintaroolipelisarja',
    'toimintaseikkailupelisarja',
    'toimisto',
    'toimisto-ohjelmisto',
    'tonttu',
    'torjuntahävittäjä',
    'tositelevisiosarja',
    'trilogia',
    'tuotantoyhtiö',
    'tuote',
    'tuoteperhe',
    'tuotesarja',
    'tupla-albumi',
    'tuplaydinsuoritin',
    'turnaus',
    'tutkimusseura',
    'täti',
    'ukki',
    'urheiluauto',
    'uutiskanava',
    'uutistoimisto',
    'vaari',
    'vaateketju',
    'vakioautosarja',
    'vakoilusatelliitti',
    'vakuutusyhtiö',
    'varustamo',
    'vastarintaliike',
    'vaunu',
    'velho',
    'veli',
    'vene',
    'verkko',
    'verkkokauppa',
    'veturi',
    'video',
    'videopalvelu',
    'videopeli',
    'viihdeohjelma',
    'viihdesarja',
    'viikkolehti',
    'visailuohjelma',
    'vuono',
    'ydinohjus',
    'yhteisyritys',
    'yhtye',
    'yhtymä',
    'yksikkö',
    'ylijumala',
    'ympäristö',
    'yritys',
    'yritysryhmä',
    'yrttilikööri',
    'yökerho',
    'älypuhelin',
    'öljy-yhtiö',
])


not_split = set([
    ('SM', 'liiga'),
    ('Suomi', 'liiga'),
    ('Eurooppa', 'liiga'),
    ('Suomi', 'sarja'),
    ('Renault', 'sarja'),
    ('CD', 'levy'),
    ('Jussi', 'palkinto'),
    ('Finlandia', 'palkinto'),
    ('Suomi', 'palkinto'),
    ('Runeberg', 'palkinto'),
    ('Annie', 'palkinto'),
    ('Venla', 'palkinto'),
    ('Annie', 'gaala'),
    ('Emma', 'gaala'),
    ('Oscar', 'gaala'),
    ('Grammy', 'gaala'),
    ('Karjala', 'turnaus'),
    ('', ''),
    ('', ''),
    ('', ''),
])
