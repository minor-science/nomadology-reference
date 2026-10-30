"""Build the five-process grids from one data source:
  five_processes_grid.html      web page, five processes
  five_processes_grid_v2.html   web page, with Protevi's marronage column
  grid_handout.html             two-page letter handout (render to PDF with headless Chrome)
Column order follows ATP's Axiom I (outside to inside to across): warding off, war machine,
(marronage), capture, polarization, encompassment."""
import html, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
COLS5 = ["wo", "wm", "state", "town", "ecu"]
COLS6 = ["wo", "wm", "mar", "state", "town", "ecu"]
HEAD = {
    "wo": ("Warding off", "primitive societies"),
    "wm": ("War machine", "nomads"),
    "mar": ("Marronage", "maroon societies · tentative"),
    "state": ("Capture", "States"),
    "town": ("Polarization", "towns"),
    "ecu": ("Encompassment", "ecumenical organizations"),
}
MIX = {"wo": "In maroon societies (Protevi)", "wm": "In maroon societies (Protevi)", "ecu": "“Perhaps” in them (Protevi)"}

# Markup in cell text: **bold**, [[pages]]. A value starting "EXT:" is an open cell.
# Marronage cells are (Protevi's text, essay extension or None).
# Split cells (first row) are ("SPLIT", [part, part], note or None[, essay]).
ROWS = [
    ("What are its poles and forms?", {
        "wo": ("SPLIT", ["**Segmentary, egalitarian**: anticipates the town (e.g., village halves of equal standing)",
                         "**Encompassing, hierarchized**: anticipates the State (e.g., one lineage on top) [[433, cf. Lévi-Strauss]]"],
               "Moves into towns and States, and even into capitalism (e.g., bands with “their own towns”) [[437]]"),
        "wm": ("SPLIT", ["**Creative**: “a creative line of flight” (guerrilla, popular war)",
                         "**Destructive**: war as its object (total war, fascism) [[422-23, cf. Clausewitz, 420]]"],
               "Captured by “encastment” (Rome’s federated barbarians) or “appropriation proper” (a citizen army) as an army [[419, 425]], or a “worldwide war machine” of “military-industrial” complexes [[387, cf. Virilio]]"),
        "mar": ("SPLIT", ["**Wild**: outside the plantation but near enough to trade and raid (e.g., Jamaica’s mountains)",
                          "**Urban**: “hiding in plain sight” (forged papers in a city) [[RoV 109]]"],
                "State-establishing maroons or Haiti’s counter-plantation [[RoV 104]], as “tendencies,” not types [[RoV 109]]",
                "Three operations: putting the plantation to flight in place, leaving it, and occupying a space without leaving"),
        "state": ("SPLIT", ["**Binder** (Varuna, Romulus): “capture, bonds, knots, and nets”",
                            "**Jurist** (Mitra, Numa): “treaties, pacts, contracts” [[351, 424, cf. Dumézil]]"],
                  "Three forms: the archaic empire, Marx’s “Asiatic formation” (pharaonic Egypt, the Inka), evolved States (Rome’s empire, feudal kingdoms, city-states), and nation-States (19th-century France) [[427, 451, 459]]"),
        "town": ("SPLIT", ["**Capital**: the town grows from the palace (Egypt)",
                           "**Metropolis**: the palace grows from the town (Sumer, and later Athens) [[432]]"],
                 "Commercial towns freed (e.g., the Hanse, Venice), then resubjugated [[434]]"),
        "ecu": ("SPLIT", ["**Between** formations: trade, metallurgy, religion (e.g., Christianity), art",
                          "**Axiomatic**: one world market, “isomorphy” (today) [[435-37, cf. Samir Amin]]"],
                "Two poles of the capitalist State: “social democracy” adds axioms, “totalitarianism” subtracts them (Chile) [[462-63]]"),
    }, [dict(a="wo", z="wm", text="Primitive mechanisms of war become a nomad war machine “when they gain autonomy” [[430]]", kind="pair")]),
    ("How is a collective composed?", {
        "wo": "**Lineal**: by descent, in clan segments that “meld and divide” [[388]]",
        "wm": "**Numerical**: tens, hundreds, thousands (the Mongol army, Moses’s census in Numbers), with a special body [[387-93]]",
        "mar": ("Initiation for “multiple African origins,” with deserters executed [[RoV 117]]", "Brazil’s campo negro: networks tying runaway camps to slave quarters and markets (Gomes)"),
        "state": "**Territorial** (“geometric”): by place, through census, taxation, and election (the voter roll) [[388-89]]",
        "town": "“Physical organization”: by entry into circuits (burghers, guilds), under a magistrate [[433, 435]]",
        "ecu": "EXT:Affiliation across formations (pilgrims, merchant diasporas, converts), for which ATP names no type",
    }, [dict(a="wo", z="wm", text="The numerical composition is “superposed upon the primitive lineal organization” [[435]]", kind="pair"),
        dict(a="wm", z="state", text="**Numbering and numbered**: one composes a body that moves, the other measures a divided space [[387-89]]", kind="pair")]),
    ("How is space occupied?", {
        "wo": "Territory: the earth inscribed by lineages (clan lands), with **itinerancy** from one territory to the next [[388, 440]]",
        "wm": "**Smooth**: occupied without being counted (steppe, desert, sea), where points serve paths, and holey with the smiths, for a **nomad** who “does not move” [[362 cf. Boulez, 380-81, 413-15]]",
        "mar": ("“Neither ‘smooth’ nor ‘striated’” but “secluded or marginal,” with ambush points and hidden defenses [[RoV 104, 120]]", "Holey space: a 1769 map of a Brazilian runaway settlement, with smithies and “holes for escape” (Carney and Rosomoff)"),
        "state": "**Striated**: counted in order to be occupied (survey grids, the land register), with the center “on top,” and **migrants** controlled [[362, 385, 433]]",
        "town": "Roads and circuits with their entries and exits (market towns, ports), “melodic lines,” and the rotation of **transhumance** (“even the merchant”) [[410, 432, 434]]",
        "ecu": "Between formations, as “an intermediate milieu” (trade and pilgrimage routes) [[435]]",
    }, [dict(a="wm", z="state", text="**Smooth and striated** “exist only in mixture” [[474]]", kind="pair", solid=["mar"]),
        dict(a="state", z="town", text="Melodic lines and harmonic cross sections together striate space [[434]]", kind="pair")]),
    ("How is power exercised?", {
        "wo": "Chiefs without command (cf. Clastres’s Amazonian chiefs), in circles “not concentric” [[357, 433]]",
        "wm": "A chief with limited power, and a special body (Genghis Khan’s guard) [[392]]",
        "mar": ("Palmares, a 17th-century Brazilian runaway polity, as “kingdom” or “republic,” and Haiti’s counter-plantation, “without an apparatus of capture” [[RoV 104, 118]]", None),
        "state": "Power “on top”: hierarchy, a civil service (scribes, ministries), resonance, global integration [[433]]",
        "town": "Power “of the middle”: forced coordination (councils, magistrates), “egalitarian pretensions” [[432-33]]",
        "ecu": "“The consolidation of the diverse as such” (one church across many kingdoms) [[436]]",
    }, [dict(a="wo", z="town", text="Warding off holds off **both** thresholds, State and town [[431-33]]", kind="pair", solid=["state"]),
        dict(a="mar", z="state", text="“A capture of the apparatus of capture itself” [[RoV 104]]", kind="mar"),
        dict(a="state", z="town", text="**State and town**: two thresholds, “two runners” [[432-34, cf. Braudel]]", kind="pair")]),
    ("How is exchange made?", {
        "wo": "The **last receivable**, “the law of demand” (ATP’s seeds for axes), with depletion warding off the stock [[437-40, cf. Jevons]]",
        "wm": "",
        "mar": ("“Trade, raid, tribute, and treaty” [[RoV 103]]", None),
        "state": "**Comparison and appropriation**: rent, profit, tax on land, tools, money (landowner, entrepreneur, banker) [[443-44, cf. Marx’s “trinity formula”]]",
        "town": "Commerce, “also spiritual” (merchant leagues, monasteries), recoding decoded flows [[432, 434]]",
        "ecu": "Long-distance trade (metals since the Neolithic), and one world market under capitalism [[435-36]]",
    }, [dict(a="wo", z="state", text="**Limit and threshold**: past the threshold, “stockpiling begins” [[438-40]]", kind="pair"),
        dict(a="mar", z="state", text="Flight is “co-constitutive of states” [[RoV 115]]", kind="mar"),
        dict(a="state", z="town", text="Proposed: a measure kept in common is not yet capture (RoV 176 n. 3)", kind="ext")]),
    ("How are activity and matter handled?", {
        "wo": "",
        "wm": "**Free action** and the weapon (bow, lance), **following** the phylum (the smith, cf. Childe) [[394-411]]",
        "mar": ("Hunting and swidden “adapted to … the risk of attack” [[RoV 117]]", "Maroon farming and smithing in Brazilian runaway settlements (Carney and Rosomoff)"),
        "state": "**Work** and the tool (the plow, the daily quota), and **hylomorphism**, form imposed on matter (the mold, cf. Simondon) [[369, 397-98, 408]]",
        "town": "Makes the phylum “pass through specific places” (markets, workshops) [[432]]",
        "ecu": "Metallurgy cuts across formations (bronze, iron) [[435]]",
    }, [dict(a="wm", z="state", text="**Free action and work**: work is free action captured, measured, stocked [[441-42]]", kind="pair")]),
    ("How is knowledge made?", {
        "wo": "Territorial codes (kin rules, ritual)",
        "wm": "**Nomad science**: problematic and following (Gothic builders, smiths, navigators), with the cipher and the secret [[361-74, 390]]",
        "mar": ("Marronage as a “figure” in Glissant and other Caribbean writers [[RoV 121]]", "Knowledge kept by restriction, as in Saramaka history told in fragments (Richard Price) or Jamaican “Maroon Science” (Bilby)"),
        "state": "**Royal science**: theorematic and reproducing (Euclid, State engineering), with the State form of thought [[361-76]]",
        "town": "Frequency, “melodic lines” [[434]]",
        "ecu": "Translation, religions, art (scripture carried across languages) [[430, 436]]",
    }, [dict(a="wm", z="state", text="One field of interaction: royal science appropriates, nomad science cuts loose, through “vague essences” [[367, cf. Husserl]]", kind="pair")]),
    ("How is violence exercised?", {
        "wo": "**Struggle**: blow for blow, coded (the feud) [[447]]",
        "wm": "**War**, against the State (raids), yet not its object [[416-18]]",
        "mar": ("“Its own regime of violence”: raiding, defensive war, return of runaways [[RoV 117]]", None),
        "state": "**Policing**, capturing while “constituting a right to capture” (police, courts, prisons), against **crime**, capturing what one has no “right” to capture (theft) [[447-48, cf. Marx on primitive accumulation]]",
        "town": "EXT:Civil violence (“Who can say …?” [[433]])",
        "ecu": "EXT:Violence carried across societies, as in West African slave-raiding (Meillassoux)",
    }, [dict(a="wm", z="state", text="The State “has no war machine of its own” [[355]]", kind="pair"),
        dict(a="mar", z="state", text="**Mastery** and **marronage**: Protevi’s added regimes [[RoV 115-17]]", kind="mar")]),
    ("How are persons captured or freed?", {
        "wo": "",
        "wm": "The special body: slaves who become soldiers (Mamluks, Janissaries) [[393]]",
        "mar": ("Captives held “to ensure acculturation,” and marginality as “becoming free” [[RoV 109, 117]]", None),
        "state": "Machinic **enslavement** (galley rowers, app-directed work) and social **subjection** (worker, citizen), the “megamachine” [[428 cf. Mumford, 456-59]]",
        "town": "EXT:The town as refuge, from early cities of the displaced (Yoffee) to Teotihuacan in Mexico (Manzanilla)",
        "ecu": "EXT:Enslavement across societies: the Atlantic slave system",
    }, [dict(a="mar", z="state", text="Treaty maroons “assist in pursuit, capture, and return” [[RoV 117]]", kind="mar")]),
    ("What does it prevent, and what escapes it?", {
        "wo": "Wards off the State and the town (dispersal, sharing) [[431-33]]",
        "wm": "Wards off lineal aristocracy, imperial functionaries [[393]]",
        "mar": ("“Not anti-State; they seek to be autonomous” [[RoV 104]]", None),
        "state": "Decoded flows (private debt, runaways) and minorities [[448, 469-73]]",
        "town": "Wards off the State-form and capitalism (medieval Italian and Hanseatic towns), then resubjugated [[434]]",
        "ecu": "Its own “bands, deserts, war machines” (Christianity’s desert monks) [[436]]",
    }, [dict(a="state", z="ecu", text="**The axiomatic**: capitalism wins “through the State-form,” works “like a single City,” and worldwide organization “becomes the capitalist axiomatic” [[434-36]]", kind="pair", solid=["town"])]),
    ("What is its limit?", {
        "wo": "The **last**, limit of an ordinal series (the last ax), keeping the threshold “at a distance” [[438-40]]",
        "wm": "EXT:Open: ATP names none",
        "mar": ("", None),
        "state": "The **threshold**, “the lowest element in a cardinal set” (the least fertile land) [[441]]",
        "town": "EXT:Open: ATP names none",
        "ecu": "**Its own limits**, which capitalism confronts and “displaces” at once (oil, nuclear power) [[463]]",
    }, [dict(a="wo", z="ecu", text="Each process has a limit of its own (cf. Sibertin-Blanc, 55)", kind="ext", solid=["wm", "mar", "state", "town"])]),
]
# Findings from the specialist record that complicate or dispute a cell (shown as "Record:" notes).
NOTES = {
    ("What are its poles and forms?", "wo"): 'Ethnography complicates warding off, since among the Pintupi of Australia’s Western Desert, control of ritual knowledge founds rank as “looking after” (Myers), while in Tonga the communities that resisted their chiefs’ extraction came to stress women’s reproductive roles, which lowered women’s standing (Gailey).',
    ("What are its poles and forms?", "wm"): 'Can a war machine found a State? Historians of the Mongol steppe disagree. For Munkh-Erdene the warband of a charismatic warlord is the “nomadic origin of the state,” whereas for Di Cosmo steppe states formed “in relation to sedentary states” such as China, which leaves the question open.',
    ("How is space occupied?", "wm"): 'Anthropologists of Inner Asia have dropped “nomadism” in favor of “mobile pastoralism” (Humphrey and Sneath), much as ancient DNA studies measure migration. Yet for Deleuze and Guattari it is “false to define the nomad by movement” (381), so the specialists and the plateaus are not arguing about the same thing.',
    ("How is power exercised?", "town"): 'Archaeology reopens the question of which threshold comes first. Sumer’s city-states are ATP’s own “town solution” (432), the Indus cities had writing and standard weights but no palaces (Green), and every place name recorded in Uruk-period Mesopotamia is the name of a city (Moreno García and Richardson).',
    ("How is exchange made?", "state"): 'Studies of hunter-gatherers suggest that setting food aside does not yet make a stock, which requires rights converging “upon a single interest” (Ingold). Indeed, Testart calls the order of storage and settled life “chicken-and-egg.” Both tell against the storage-first account Protevi takes up (RoV 98).',
    ("How is knowledge made?", "state"): 'In ancient Egypt and Babylonia, fields were measured by a dozen kinds of officer with no fixed competence, which is to say royal measure without a royal science (Moreno García and Richardson).',
    ("How is violence exercised?", "state"): 'In Middle Bronze Age Mesopotamia, violence by State and community was “rare in fact,” as people were sanctioned instead through reputation and exclusion, a regime missing from Deleuze and Guattari’s four (Garfinkle and Richardson).',
    ("How are persons captured or freed?", "mar"): 'Old Babylonian law (about 1900-1600 BCE) treated a slave’s flight as theft by whoever helped, not as the fugitive’s own act (Richardson). Even whether flight counts as the fugitive’s act, then, depends on the regime.',
}
NOTE_ID = {k: i for i, k in enumerate(NOTES, 1)}

# Who and what is named on the charts, for readers who do not know the sources.
KEY = [
    ('Amin, Samir', 'Deleuze and Guattari side with the economist Samir Amin, a theorist of world-systems and unequal development, in holding that “there can be no economic theory of international relations,” which is the ground of the ecumenical (435-36).'),
    ('Bilby, Kenneth', 'For the anthropologist Kenneth Bilby, in <i>True-Born Maroons</i> (2005), the Jamaican Maroons keep a knowledge they call “Maroon Science,” learned through “testing and evasion.”'),
    ('Boulez, Pierre', 'Smooth and striated space come from the composer Pierre Boulez, who distinguished musical time counted in advance from time occupied without being counted (362, 477-78).'),
    ('Braudel, Fernand', 'Fernand Braudel describes the State and the town as “two runners” in the history of European capitalism, an image Deleuze and Guattari quote (434).'),
    ('Carney, Judith, and Richard Rosomoff', 'In <i>In the Shadow of Slavery</i> (2009), the geographers Judith Carney and Richard Rosomoff reproduce a 1769 militia map of a runaway settlement in Minas Gerais, Brazil, marking its smithies, gardens, hidden defenses, and “holes for escape” (85).'),
    ('Casimir, Jean', 'The Haitian historian Jean Casimir shows in <i>The Haitians</i> (2020) how cultivators after the revolution built a “counter-plantation” of family farms and, “without moving from the plantations,” stopped being the plantation’s workers (142), a book Protevi also cites (RoV 104).'),
    ('Childe, V. Gordon', 'Deleuze and Guattari take the itinerant smith, who follows metal, from V. Gordon Childe, an archaeologist of prehistoric Europe who also dug in the Near East (412, 415).'),
    ('Clastres, Pierre', 'Warding off begins with the anthropologist Pierre Clastres, whose <i>Society against the State</i> (1974) describes Amazonian chiefs who speak but cannot command (357-59).'),
    ('Clausewitz, Carl von', 'The war machine’s two poles rework the distinction that the Prussian theorist Carl von Clausewitz draws between absolute war as an Idea and the real wars that States fight (420-23).'),
    ('Di Cosmo, Nicola', 'In <i>Ancient China and Its Enemies</i> (2002), the historian Nicola Di Cosmo has the Xiongnu state form in reaction to China, adopting forms of sedentary states as it did so (171).'),
    ('Dumézil, Georges', 'Sovereignty’s two heads (Varuna the binder against Mitra the jurist) come from Georges Dumézil’s comparative history of Indo-European religion (351, 424).'),
    ('Gailey, Christine Ward', 'Christine Ward Gailey’s <i>Kinship to Kingship</i> (1987) treats state formation in Tonga as a process, one in which communities resisting the chiefs’ extraction came to stress women’s reproductive roles, so that women’s status fell (xi).'),
    ('Garfinkle, Steven, and Seth Richardson', 'For Middle Bronze Age Mesopotamia (about 2000-1600 BCE), the historians Steven Garfinkle and Seth Richardson find State and community violence “rare in fact,” with sanction running instead through reputation and exclusion (161).'),
    ('Glissant, Édouard', 'The Martinican writer Édouard Glissant, among the Caribbean writers Protevi cites, takes the maroon as a figure of resistance (RoV 121).'),
    ('Gomes, Flávio dos Santos', 'Quilombos are Brazil’s runaway settlements. The historian Flávio dos Santos Gomes calls the networks tying them to slave quarters, the free poor, and traders a <i>campo negro</i>, a formation “inside slavery and an alternative to it.”'),
    ('Green, Adam', 'In “Killing the Priest-King” (2021), the archaeologist Adam Green describes Indus cities (about 2600-1900 BCE) with writing, standard weights, seals, and metalwork, yet no palaces or royal tombs.'),
    ('Humphrey, Caroline, and David Sneath', 'Writing on Mongolia and Inner Asia in <i>The End of Nomadism?</i> (1999), the anthropologists Caroline Humphrey and David Sneath call nomadism “a category imagined by outsiders” and prefer “mobile pastoralism” (1).'),
    ('Husserl, Edmund', 'Nomad science takes its anexact rigor from Edmund Husserl’s “vague essences,” roundness as opposed to the circle (367).'),
    ('Indus, Sumer, Uruk', 'The Indus civilization flourished in present-day Pakistan and northwest India (about 2600-1900 BCE). Sumer names the city-states of southern Mesopotamia (from about 2900 BCE), while the period of Uruk, a Mesopotamian city (about 4000-3100 BCE), gives the earliest writing, kept as accounts.'),
    ('Ingold, Tim', 'For the anthropologist Tim Ingold, setting food aside is not yet a stock, since a stock is rights converging “upon a single interest” (1983, 553).'),
    ('Jevons, W. Stanley', 'The limit and threshold of warding off borrow “the last” unit from the marginalist economist Jevons, whom Deleuze and Guattari dub “a kind of Lewis Carroll of economics” (437).'),
    ('Three operations of marronage', 'The sheet proposes three operations of marronage, namely putting a system to flight in place, leaving it, and holding a space without leaving it.'),
    ('Lévi-Strauss, Claude', 'Claude Lévi-Strauss showed that the same village can present itself as segmentary and egalitarian or as encompassing and hierarchized, two potentials that Deleuze and Guattari treat as anticipations of town and State (433).'),
    ('Manzanilla, Linda', 'The archaeologist Linda Manzanilla studies Teotihuacan, a city of central Mexico (about 100 BCE-550 CE) founded largely by people displaced by a volcanic eruption, governed corporately, and burned at its center around 550 CE.'),
    ('Marx, Karl', 'From Karl Marx come ATP’s archaic State, his “Asiatic formation” (427), the “trinity formula” behind rent and profit as well as tax (443), and the primitive accumulation behind State violence (447).'),
    ('Meillassoux, Claude', 'In <i>The Anthropology of Slavery</i> (1986), the French anthropologist Claude Meillassoux shows a West African slave system joining the societies raided for captives, the aristocracies that raid them, and the merchants who sell the captives (74).'),
    ('Moreno García, Juan Carlos, and Seth Richardson', 'In <i>Monarchies and the Organization of Power</i> (2025), the historians Juan Carlos Moreno García and Seth Richardson find Egyptian and Babylonian kings co-opting local powers they could not erase (6), with fields measured by many kinds of officer (16).'),
    ('Mumford, Lewis', 'Machinic enslavement takes its image from the historian Lewis Mumford’s “megamachine,” the archaic empire as a machine made of people (428, 457).'),
    ('Munkh-Erdene, Lhamsuren', 'In <i>The Nomadic Leviathan</i> (2023), the Mongolian historian Lhamsuren Munkh-Erdene argues “for the nomadic origin of the state” in the warband of a charismatic warlord (1, 25).'),
    ('Myers, Fred', 'Among the Pintupi of Australia’s Western Desert, as the anthropologist Fred Myers describes them in <i>Pintupi Country, Pintupi Self</i> (1986), authority rests in the Law, outside any living person, even as elders’ ritual knowledge founds rank as “looking after” (220-21).'),
    ('Palmares', 'Palmares was a large runaway polity in 17th-century Brazil, which historians have described either as a kingdom or as a “republic” (RoV 118).'),
    ('Price, Richard', 'In <i>First-Time</i> (1983), the anthropologist Richard Price records how the Saramaka of Suriname keep the history of their ancestors’ war against the planters restricted, telling it only in fragments.'),
    ('Richardson, Seth', 'The historian of Mesopotamia Seth Richardson shows that Old Babylonian law treated flight as theft by whoever helped the slave (2023, 19-20).'),
    ('Sibertin-Blanc, Guillaume', 'In <i>State and Politics: Deleuze and Guattari on Marx</i> (2016), the philosopher Guillaume Sibertin-Blanc treats plateaus 12-13 as a theory of violence. For him each process meets a limit of its own, so that warding off, polarization, capture, and deployment in smooth space each reach a point past which they fail (55).'),
    ('Simondon, Gilbert', 'Following matter, as opposed to imposing form, draws on the philosopher Gilbert Simondon’s critique of the form-matter, or hylomorphic, model (408).'),
    ('Testart, Alain', 'For the French anthropologist Alain Testart, the order of storage and settled life among hunter-gatherers is “a chicken-and-egg question” (1982, 524).'),
    ('Virilio, Paul', 'The “worldwide war machine” draws on Paul Virilio, a theorist of speed and war, and his “fleet in being,” which holds the sea from any point (387).'),
    ('Yoffee, Norman', 'In <i>Myths of the Archaic State</i> (2005), the archaeologist Norman Yoffee treats early cities as refuges and nomadism as something urban life produces (60).'),
]

TRANSFER = "“Each process can also function at a ‘power’ other than its own”: the State appropriates the war machine, the instruments of polarization, and warding off, which in turn moves into towns, States, and capitalism [[437]]"
TRANSFER_MAR = "Protevi: “state-establishing maroons” can “partake in the machinic process of overcoding” [[RoV 103]]"


def fmt(s):
    s = html.escape(s, quote=False)
    parts = s.split("**")
    s = "".join(p if i % 2 == 0 else f"<b>{p}</b>" for i, p in enumerate(parts))
    return s.replace("[[", '<span class="pg">').replace("]]", "</span>")


MODE = {"print": False, "seen": []}


def rec(q, key):
    n = NOTES.get((q, key))
    if not n:
        return ""
    i = NOTE_ID[(q, key)]
    if MODE["print"]:
        return f'<sup class="rmark">R{i}</sup>'
    return f'<span class="rec"><b class="rid">R{i}</b> {fmt(n)}</span>'


def cell(key, val, q=""):
    r = rec(q, key)
    m = ' m' if key == "mar" else ''
    if isinstance(val, tuple) and val and val[0] == "SPLIT":
        parts, note = val[1], val[2]
        essay = val[3] if len(val) > 3 else None
        s = '<div class="split">' + "".join(f"<div>{fmt(p)}</div>" for p in parts) + "</div>"
        if note:
            s += f'<div class="mut">{fmt(note)}</div>'
        if essay:
            s += f'<span class="essay">{fmt(essay)}</span>'
        return f'<td class="poles{m}">{s}{r}</td>'
    if key == "mar":
        prot, ext = val
        if not prot and not ext:
            return '<td class="m none">·</td>'
        s = fmt(prot) + (f'<span class="essay">{fmt(ext)}</span>' if ext else "")
        return f'<td class="m">{s}{r}</td>'
    if not val:
        return '<td class="none">·</td>'
    if val.startswith("EXT:"):
        return f'<td class="ext">{fmt(val[4:])}</td>'
    return f"<td>{fmt(val)}{r}</td>"


def band(b, cols):
    a, z, kind = b["a"], b["z"], b["kind"]
    if (a not in cols) or (z not in cols):
        return ""
    i, j = cols.index(a), cols.index(z)
    segs = []
    for k in range(i, j + 1):
        c = []
        if k == i: c.append("l")
        if k == j: c.append("r")
        if i < k < j and cols[k] not in b.get("solid", []):
            c.append("skip")
        segs.append(f'<i class="{" ".join(c)}"></i>')
    klass = {"pair": "", "ext": " ext", "mar": " mk", "rec": " ext rc"}[kind]
    tds = ["<td></td>"]
    k = 0
    while k < len(cols):
        if k == i:
            tds.append(f'<td colspan="{j - i + 1}" class="bandcell"><div class="seg{klass}">{"".join(segs)}</div><p class="bt{klass}">{fmt(b["text"])}</p></td>')
            k = j + 1
        else:
            tds.append(f'<td class="{"m" if cols[k] == "mar" else ""}"></td>')
            k += 1
    return '<tr class="band">' + "".join(tds) + "</tr>"


def table(cols):
    out = ['<table><colgroup><col class="q">' + "".join('<col class="mc">' if c == "mar" else "<col>" for c in cols) + "</colgroup><thead><tr><th>Question</th>"]
    for c in cols:
        t, s = HEAD[c]
        tag = f'<span class="tag">{MIX[c]}</span>' if ("mar" in cols and c in MIX) else ""
        cls = ' class="m"' if c == "mar" else ""
        out.append(f"<th{cls}>{t}<small>{s}</small>{tag}</th>")
    out.append("</tr></thead><tbody>")
    for q, vals, bands in ROWS:
        out.append(f'<tr class="row"><th>{q}</th>' + "".join(cell(c, vals.get(c, ""), q) for c in cols) + "</tr>")
        for b in bands:
            if MODE["print"] and "mar" in cols and b["kind"] != "mar":
                continue
            out.append(band(b, cols))
    t = fmt(TRANSFER) + (f'<span class="tm">{fmt(TRANSFER_MAR)}</span>' if "mar" in cols else "")
    out.append(f'<tr class="transfer"><th>How does it pass into the others?</th><td colspan="{len(cols)}">{t}</td></tr></tbody></table>')
    return "".join(out)


TOKENS = """
:root { --bg:#F5F6F3; --surface:#FFFFFF; --fg:#1D2224; --muted:#5B6468; --rule:#D5D9D6; --pair:#1F6B66; --pair-soft:#E3EFED;
  --ext:#7A4E7E; --ext-soft:#F3ECF4; --mar:#8A5A1F; --mar-soft:#F6EEE2; --split:#EEF1EF;
  --serif:"Source Serif 4", Georgia, "Times New Roman", serif; --label:"IBM Plex Sans Condensed", "Arial Narrow", Arial, sans-serif; }
"""
DARK = """
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#141819; --surface:#1B2022; --fg:#E3E7E5; --muted:#9AA4A7; --rule:#2E3538; --pair:#63B9B1; --pair-soft:#1C2C2B; --ext:#C79BCB; --ext-soft:#2A2030; --mar:#D9A55C; --mar-soft:#2A2218; --split:#222829; color-scheme: dark; } }
:root[data-theme="dark"] { --bg:#141819; --surface:#1B2022; --fg:#E3E7E5; --muted:#9AA4A7; --rule:#2E3538; --pair:#63B9B1; --pair-soft:#1C2C2B; --ext:#C79BCB; --ext-soft:#2A2030; --mar:#D9A55C; --mar-soft:#2A2218; --split:#222829; color-scheme: dark; }
"""
SHARED = """
table { border-collapse: collapse; width: 100%; table-layout: fixed; }
th, td { text-align: left; vertical-align: top; }
thead th { font-family: var(--label); font-weight: 600; letter-spacing: 0.02em; background: var(--surface); position: relative; z-index: 2; box-shadow: inset 0 -2px 0 var(--fg); }
thead th small { display: block; font-weight: 500; color: var(--muted); letter-spacing: 0.05em; text-transform: uppercase; }
thead th.m { background: var(--mar-soft); color: var(--mar); box-shadow: inset 0 -2px 0 var(--mar); }
.tag { display: inline-block; font-family: var(--label); font-weight: 500; color: var(--mar); border: 1px solid var(--mar); text-transform: uppercase; letter-spacing: 0.04em; }
tbody th { font-family: var(--label); font-weight: 600; color: var(--muted); }
tr.row > * { border-top: 1px solid var(--rule); }
col.mc, td.m { background: var(--mar-soft); }
td b { font-weight: 600; }
.pg { color: var(--muted); font-size: 0.88em; }
td.ext { background: var(--ext-soft); outline: 1.2px dashed var(--ext); font-style: italic; }
td.none { color: var(--rule); }
.essay { display: block; font-style: italic; background: var(--ext-soft); outline: 1px dashed var(--ext); }
.essay::before { content: "Proposed: "; font-style: normal; color: var(--ext); }
.rec { display: block; font-style: italic; color: var(--fg); background: var(--ext-soft); outline: 1px dashed var(--ext); }
.rec::before { content: "Record "; font-style: normal; color: var(--ext); }
.rid { font-family: var(--label); font-style: normal; color: var(--ext); }
dl.key { margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 8px 22px; }
dl.key dt { font-family: var(--label); font-weight: 600; }
dl.key dd { margin: 0; color: var(--muted); }
.split { display: grid; grid-template-columns: 1fr 1fr; border: 1px solid var(--rule); background: var(--split); }
.split > div { min-width: 0; }
.split > div + div { border-left: 1px solid var(--rule); }
.mut { color: var(--muted); font-style: italic; }
.seg { display: flex; }
.seg i { flex: 1; border-top: 2px solid var(--pair); }
.seg i.l { border-left: 2px solid var(--pair); }
.seg i.r { border-right: 2px solid var(--pair); }
.seg i.skip { border-top: 2px dotted var(--pair); opacity: 0.55; }
.seg.ext i { border-color: var(--ext); border-top-style: dashed; }
.seg.mk i { border-color: var(--mar); }
p.bt { color: var(--pair); }
p.bt.ext { color: var(--ext); }
p.bt.mk { color: var(--mar); }
tr.transfer > * { border-top: 2px solid var(--fg); background: var(--pair-soft); }
.tm { display: block; color: var(--mar); }
"""
WEB = """
body { background: var(--bg); color: var(--fg); font-family: var(--serif); font-size: 15px; line-height: 1.45;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 40px; }
header { max-width: 78ch; display: grid; gap: 10px; margin-bottom: 16px; }
h1 { font-size: 1.7rem; font-weight: 600; margin: 0; text-wrap: balance; }
header p { margin: 0; color: var(--muted); }
header p b { color: var(--fg); }
header p.mnote { color: var(--fg); border-left: 3px solid var(--mar); padding-left: 12px; }
.legend { display: flex; flex-wrap: wrap; gap: 8px 20px; font-family: var(--label); font-size: 0.85rem; color: var(--muted); margin: 4px 0 16px; }
.legend span { display: inline-flex; align-items: center; gap: 8px; }
.sw { display: inline-block; }
.sw-p { width: 26px; height: 9px; border: 2px solid var(--pair); border-bottom: 0; }
.sw-m { width: 26px; height: 9px; border: 2px solid var(--mar); border-bottom: 0; }
.sw-e { width: 18px; height: 14px; border: 1.5px dashed var(--ext); background: var(--ext-soft); }
.sw-s { width: 26px; height: 14px; border: 1px solid var(--rule); background: linear-gradient(90deg, var(--split) 0 48%, var(--rule) 48% 52%, var(--split) 52%); }
.wrap { overflow-x: auto; border: 1px solid var(--rule); background: var(--surface); }
table { min-width: 1180px; }
.six table { min-width: 1360px; }
col.q { width: 140px; }
th, td { padding: 10px 12px; }
thead th { font-size: 0.95rem; }
thead th small { font-size: 0.72rem; margin-top: 2px; }
.tag { margin-top: 6px; font-size: 0.68rem; padding: 1px 6px; }
tbody th { font-size: 0.85rem; }
td.ext { outline-offset: -5px; }
.essay, .rec { margin-top: 8px; padding: 6px 8px; }
.split > div { padding: 6px 8px; font-size: 0.93rem; }
.mut { margin-top: 6px; font-size: 0.9rem; }
tr.band td { padding: 0 12px 10px; }
.seg { height: 9px; margin: 0 4px; }
p.bt { margin: 4px 4px 0; font-size: 0.88rem; }
tr.transfer > * { padding: 12px; }
.tm { margin-top: 6px; }
.keysec { margin-top: 26px; max-width: 1200px; }
.keysec h2 { font-family: var(--label); font-size: 1.05rem; margin: 0 0 4px; }
.keysec p { margin: 0 0 12px; color: var(--muted); }
.webnotes li { margin: 0 0 8px; }
.webnotes li b { color: var(--ext); font-family: var(--label); margin-right: 6px; }
dl.key dd { font-size: 0.92rem; }
footer { max-width: 78ch; margin-top: 18px; color: var(--muted); font-size: 0.88rem; display: grid; gap: 8px; }
footer p { margin: 0; }
"""
PRINT = """
@page { size: letter landscape; margin: 0.2in; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
html, body { margin: 0; background: #fff; color: var(--fg); font-family: var(--serif); }
.sheet { width: 10.6in; height: 8.1in; display: flex; flex-direction: column; gap: 0.05in; break-after: page; page-break-after: always; overflow: hidden; }
.sheet:last-child { break-after: auto; page-break-after: auto; }
.top { display: flex; justify-content: space-between; align-items: baseline; gap: 0.2in; }
h1 { margin: 0; font-weight: 600; }
.side { font-family: var(--label); font-size: 6.4pt; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; white-space: nowrap; }
.intro { margin: 0; color: var(--muted); line-height: 1.28; }
.intro b { color: var(--fg); }
.intro.m { color: var(--fg); border-left: 2pt solid var(--mar); padding-left: 6pt; }
.legend { display: flex; flex-wrap: wrap; gap: 3pt 12pt; font-family: var(--label); font-size: 6pt; color: var(--muted); }
.legend span { display: inline-flex; align-items: center; gap: 4pt; }
.sw { display: inline-block; }
.sw-p { width: 16pt; height: 5pt; border: 1.2pt solid var(--pair); border-bottom: 0; }
.sw-m { width: 16pt; height: 5pt; border: 1.2pt solid var(--mar); border-bottom: 0; }
.sw-e { width: 11pt; height: 8pt; border: 1pt dashed var(--ext); background: var(--ext-soft); }
.sw-s { width: 16pt; height: 8pt; border: 0.6pt solid var(--rule); background: linear-gradient(90deg, var(--split) 0 47%, var(--rule) 47% 53%, var(--split) 53%); }
table { border: 0.6pt solid var(--rule); }
thead th { box-shadow: inset 0 -1.2pt 0 var(--fg); }
thead th.m { box-shadow: inset 0 -1.2pt 0 var(--mar); }
tr.row > * { border-top-width: 0.5pt; }
td.ext { outline-width: 0.8pt; outline-offset: -2.5pt; }
.essay, .rec { outline-width: 0.8pt; outline-offset: -1pt; }
.s1 .rec { margin-top: 1.5pt; padding: 0.6pt 2.6pt; }
.split { border-width: 0.5pt; }
.split > div + div { border-left-width: 0.5pt; }
.seg i, .seg i.l, .seg i.r { border-width: 1.1pt; }
.seg i.skip { border-top-width: 1.2pt; }
tr.transfer > * { border-top-width: 1pt; }
.foot { font-size: 5.3pt; color: var(--muted); margin-top: auto; }
.rmark { font-family: var(--label); font-size: 0.8em; font-weight: 600; color: var(--ext); border: 0.6pt dashed var(--ext); background: var(--ext-soft); padding: 0 1.5pt; margin-left: 2pt; vertical-align: 0.3em; line-height: 1; }
.s3 { gap: 0.08in; height: auto; overflow: visible; }
.s3 dl.key div { break-inside: avoid; }
.s3 h1 { font-size: 13pt; } .s3 .intro { font-size: 7.2pt; max-width: 9in; }
.s3 h2 { font-family: var(--label); font-size: 9pt; margin: 0.06in 0 0; }
.rnotes { list-style: none; margin: 0; padding: 5pt 7pt; columns: 2; column-gap: 16pt; font-size: 6.5pt; line-height: 1.2; background: var(--ext-soft); outline: 0.8pt dashed var(--ext); outline-offset: -1pt; }
.rnotes li { break-inside: avoid; margin-bottom: 3pt; }
.rnotes li b { color: var(--ext); font-family: var(--label); margin-right: 3pt; }
.rwhere { font-family: var(--label); font-size: 0.9em; color: var(--muted); margin-right: 3pt; }
.s3 dl.key { display: block; columns: 5; column-gap: 11pt; font-size: 5.65pt; line-height: 1.16; }
.s3 dl.key div { break-inside: avoid; margin-bottom: 3pt; }
.s3 dl.key dt { font-size: 6.4pt; }
.s1 h1 { font-size: 13pt; } .s1 .intro { font-size: 6.3pt; }
.s1 table { font-size: 5.4pt; line-height: 1.08; }
.s1 col.q { width: 0.92in; }
.s1 th, .s1 td { padding: 1.6pt 3.4pt; }
.s1 thead th { font-size: 7.8pt; } .s1 thead th small { font-size: 5.4pt; }
.s1 tbody th { font-size: 6.3pt; }
.s1 .split > div { padding: 1.2pt 2.6pt; } .s1 .mut { margin-top: 1.5pt; }
.s1 tr.band td { padding: 0 3.6pt 1.2pt; } .s1 .seg { height: 3pt; margin: 0 2pt; } .s1 p.bt { font-size: 5.6pt; margin: 0.5pt 2pt 0; line-height: 1.12; }
.s1 tr.transfer > * { padding: 3pt 4pt; }
.s2 h1 { font-size: 12.5pt; } .s2 .intro { font-size: 6.7pt; }
.s2 table { font-size: 5.45pt; line-height: 1.1; }
.s2 col.q { width: 0.8in; }
.s2 th, .s2 td { padding: 1.8pt 3pt; }
.s2 thead th { font-size: 6.9pt; } .s2 thead th small { font-size: 4.9pt; }
.s2 .tag { font-size: 4.6pt; padding: 0 2.5pt; margin-top: 1pt; }
.s2 tbody th { font-size: 5.6pt; }
.s2 .split > div { padding: 1pt 2.4pt; } .s2 .mut { margin-top: 1pt; }
.s2 .essay, .s2 .rec { margin-top: 1pt; padding: 0.4pt 2.4pt; }
.s2 tr.band td { padding: 0 2.6pt 0.8pt; } .s2 .seg { height: 2.5pt; margin: 0 1.5pt; } .s2 p.bt { font-size: 5.1pt; margin: 0.3pt 1.5pt 0; line-height: 1.1; }
.s2 tr.transfer > * { padding: 2pt 2.8pt; } .s2 .tm { margin-top: 0.6pt; }
"""

LEG5 = '<div class="legend"><span><i class="sw sw-s"></i>Split cell: a process’s own poles or forms</span><span><i class="sw sw-p"></i>Bracket: a relation joining columns (dotted where it passes over one)</span><span><i class="sw sw-e"></i>Dashed: either a proposed extension (not a claim of ATP) or a finding from the record that complicates a cell</span></div>'
LEG6 = '<div class="legend"><span><i class="sw sw-s"></i>Split cell: poles or forms</span><span><i class="sw sw-p"></i>ATP’s relations between columns (on paper, see the front)</span><span><i class="sw sw-m"></i>Protevi’s relations between marronage and capture</span><span><i class="sw sw-e"></i>Dashed: a proposed extension, or a finding from the record</span><span><span class="tag">In maroon societies</span> processes Protevi finds in them (RoV 119)</span></div>'
ORDER = "Columns run from the outside, to the inside, to what crosses all of them (ATP’s Axiom I, 351)."
INTRO5_TEXT = 'Deleuze and Guattari “define social formations by machinic processes and not by modes of production” (435), which is to say that each column below names a process, not a kind of society. In fact, every society has all five “in perpetual interaction” (430), though usually one of them dominates and gives the society its character. They coexist “extrinsically and intrinsically” (435-37), which is to say between societies, as the brackets show, and within each one, as when warding off moves into towns (the bottom row). Each row puts the same question to all five, while the columns run from the outside, through the inside, to what crosses all of them (Axiom I, 351).'
INTRO6_WEB = 'Protevi’s marronage column is tentative, and deliberately so. In <i>Regimes of Violence</i> he announces “a becoming-maroon” beside the other becomings (RoV 96), sets out to supplement Deleuze and Guattari’s topology with maroons (102-03), and describes marronage as “a set of interlinking processes” whose focus is “marginality” (108). Later, however, he speculates that maroon societies combine prevention-anticipation, war machines, “and perhaps ecumenical” processes (119). Is marronage a process of its own, or a mix of the others? The column is meant to pose that question. The column sits between the war machine and capture because Protevi places the maroon zone “neither ‘smooth’ nor ‘striated’” (104).'
INTRO6_PRINT = 'Protevi’s marronage column is tentative. He announces “a becoming-maroon” (RoV 96), describes marronage as “a set of interlinking processes” (108), and later treats maroon societies as a mix of prevention-anticipation, war machines, “and perhaps ecumenical” processes (119). Is marronage a process of its own, or a mix of the others? The column sits between the war machine and capture because, for Protevi, the maroon zone is “neither ‘smooth’ nor ‘striated’” (104).'
FOOT_PRINT = 'Page numbers without a prefix refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987), and those marked RoV to Protevi’s <i>Regimes of Violence</i> (Minnesota, 2025), while bold type marks the two terms of a double. Dashed cells are proposed extensions, not claims made in ATP. The markers R1-R8 point to findings from the record, spelled out on the notes page along with a key to every name. To print, use both sides of the sheet and flip on the short edge. The processes were first sorted aloud in the seminar of 20 November 1979 (anticipation-warding off, capture, polarization, the ecumenical); passages in <i>work/context/</i>.'
FOOT_WEB = 'Page numbers without a prefix refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987), and those marked RoV to Protevi’s <i>Regimes of Violence</i> (Minnesota, 2025), while bold type marks the two terms of a double. Capture is the State’s process, since “State societies are defined by apparatuses of capture” (435), yet capture also works outside States, which is why each column names the process before the formation. The processes were first sorted aloud in the seminar of 20 November 1979 (anticipation-warding off, capture, polarization, the ecumenical); passages in <i>work/context/</i>.'
FOOT = 'Page numbers without a prefix refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987), and those marked RoV to Protevi’s <i>Regimes of Violence</i> (Minnesota, 2025), while bold type marks the two terms of a double.'
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Sans+Condensed:wght@500;600&display=swap">'
STICKY = """<script>
/* Keep each table's title row at the top of the window while that table is on screen; a sideways-scrolling box stops CSS sticky. */
(function () {
  var heads = Array.prototype.slice.call(document.querySelectorAll('table > thead'));
  if (!heads.length) return;
  var items = heads.map(function (h) {
    var t = h.parentNode;
    return { box: t.closest('.wrap') || t, head: h, cells: Array.prototype.slice.call(h.querySelectorAll('th')) };
  });
  var ticking = false;
  function place() {
    ticking = false;
    items.forEach(function (it) {
      var r = it.box.getBoundingClientRect();
      var y = Math.min(Math.max(0, -r.top), Math.max(0, r.height - it.head.offsetHeight));
      for (var i = 0; i < it.cells.length; i++) it.cells[i].style.transform = y ? 'translateY(' + y + 'px)' : '';
    });
  }
  function ask() { if (!ticking) { ticking = true; requestAnimationFrame(place); } }
  window.addEventListener('scroll', ask, { passive: true });
  window.addEventListener('resize', ask);
  place();
})();
</script>"""

V1 = "five_processes.html"
V2 = "five_processes_marronage.html"


# The findings from the record (R1-R8), as on the handout's notes page
WEBNOTES = ('<section class="keysec"><h2>Findings from the record</h2><p>The markers R1-R8 on the chart point to findings from anthropology, archaeology, and history that complicate a cell or dispute it outright.</p>'
            '<ol class="webnotes" style="list-style:none;padding:0;margin:0;max-width:1200px">{notes}</ol></section>')


def web(cols, title, h1, intro_html, legend, other):
    six = " six" if "mar" in cols else ""
    return f'''<meta charset="utf-8">
<title>{title}</title>
{FONTS}
<style>{TOKENS}{DARK}{SHARED}{WEB}</style>
<header><h1>{h1}</h1>{intro_html}</header>
{legend}
<div class="wrap{six}">{table(cols)}</div>
{WEBNOTES.format(notes=notes_list())}
<section class="keysec"><h2>Who and what is named</h2><p>For readers who do not know the literature: each scholar and place on the chart, in a line.</p><dl class="key">{key_list()}</dl></section>
<footer><p>{FOOT_WEB}</p><p>{other}</p></footer>
{STICKY}
'''


def sheet(cols, title, side, intro_html, legend, cls):
    MODE["print"] = True
    tb = table(cols)
    MODE["print"] = False
    return f'<section class="sheet {cls}"><div class="top"><h1>{title}</h1><span class="side">{side}</span></div>{intro_html}{legend}{tb}<div class="foot">{FOOT_PRINT}</div></section>'


def notes_list():
    return "".join(f"<li><b>R{NOTE_ID[k]}</b> <span class=\"rwhere\">{k[0]} · {HEAD[k[1]][0]}</span> {fmt(n)}</li>" for k, n in NOTES.items())


def key_list():
    return "".join(f"<div><dt>{name}</dt><dd>{desc}</dd></div>" for name, desc in sorted(KEY, key=lambda x: x[0].lower().replace("é", "e")))


def notes_sheet():
    return f'''<section class="sheet s3"><div class="top"><h1>Notes and sources</h1><span class="side">Five processes · notes</span></div>
<p class="intro">The markers R1-R8 on the two charts point to findings from anthropology, archaeology, and history that complicate a cell or dispute it outright. Below them is a key to every scholar and place named on the charts, including the thinkers whose concepts Deleuze and Guattari borrow (marked “cf.”), so that readers new to these literatures can follow along without a library.</p>
<h2>Findings from the record</h2><ol class="rnotes">{notes_list()}</ol>
<h2>Who and what is named</h2><dl class="key">{key_list()}</dl>
<div class="foot">{FOOT}</div></section>'''


def save(name, text):
    # ASCII only, with character references, so curly quotes and accents survive any viewer's encoding guess.
    open(os.path.join(HERE, name), "wb").write(text.encode("ascii", "xmlcharrefreplace"))


def text_dump():
    """Plain text of every cell, intro, note, and key entry, for the voice and quotation checks."""
    out = [INTRO5_TEXT, INTRO6_WEB, TRANSFER, TRANSFER_MAR, FOOT_WEB]

    def walk(x):
        if isinstance(x, str):
            if x not in ("SPLIT",) and x.strip():
                out.append(x.replace("EXT:", "").strip())
        elif isinstance(x, dict):
            if "text" in x:
                walk(x["text"])
            else:
                for v in x.values():
                    walk(v)
        elif isinstance(x, (list, tuple)):
            for v in x:
                walk(v)
    for row in ROWS:
        walk(row[1:])
    out += list(NOTES.values()) + [d for _, d in KEY]
    t = "\n\n".join(o for o in out if o)
    for a, b in (("**", ""), ("[[", "("), ("]]", ")"), ("<i>", "*"), ("</i>", "*"), ("<b>", ""), ("</b>", "")):
        t = t.replace(a, b)
    return re.sub(r"<[^>]+>", "", t)


def main():
    w1 = web(COLS5, "Five Machinic Processes", "The five machinic processes", f"<p>{INTRO5_TEXT}</p>", LEG5,
             f'With Protevi’s marronage column: <a href="{V2}">The five machinic processes, with marronage</a>.')
    w2 = web(COLS6, "Machinic Processes and Marronage", "The five machinic processes, with marronage",
             f'<p>{INTRO5_TEXT}</p><p class="mnote">{INTRO6_WEB}</p>', LEG6,
             f'Without the marronage column: <a href="{V1}">The five machinic processes</a>.')
    save("five_processes.html", w1)
    save("five_processes_marronage.html", w2)
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Five Machinic Processes</title>{FONTS}
<style>{TOKENS}{SHARED}{PRINT}</style></head><body>
{sheet(COLS5, "The five machinic processes", "Five processes · front", f'<p class="intro">{INTRO5_TEXT}</p>', LEG5, "s1")}
{sheet(COLS6, "The five machinic processes, with marronage", "With marronage, after Protevi · back", f'<p class="intro m">{INTRO6_PRINT}</p>', LEG6, "s2")}
{notes_sheet()}
</body></html>'''
    save("five_processes_handout.html", doc)
    open(os.path.join(HERE, "five_processes_text.md"), "w").write(text_dump() + "\n")
    print("wrote five_processes.html, five_processes_marronage.html, five_processes_handout.html, five_processes_text.md")


if __name__ == "__main__":
    main()
