"""Three more sheets in the family of the five-process grids and the two-sciences sheet:
  concordance_handout.html / concordance.html      the concepts: plain sense, home field, workshop, drift
  state_forms_handout.html / state_forms.html      the State's three forms, and the axiomatic's seven givens
  library_handout.html / library.html              the plateaus' own sources, by field
Sources: kit/concept_ledger.tsv (concordance), the plateau 13 inventory (state forms), ATP 552-71, notes to
plateaus 12-13 (library). Markup: **bold**, [[pages]], <i>titles</i>. Render to PDF with headless Chrome."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_five_processes as g  # noqa: E402

save = g.save


def fmt(s):
    return g.fmt(s).replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")


# ---------------------------------------------------------------- 1. Concordance
# (concept, ATP pages, plain sense, came from, worked out, drift)
CONCEPTS = [
    ("The five machinic processes", "435, 437",
     "Five coexisting processes (warding off, the war machine, capture, polarization, encompassment) that define social formations in place of modes of production",
     "Two libraries: historians and urbanists (Braudel, Childe, Wittfogel, Mumford, Amin, Jacobs) for town, State, and ecumenical, and anthropologists (Clastres, Lévi-Strauss, Dumézil) for warding off, capture, and war machine",
     "Guattari in 1973 on a Neolithic organization that survives \"in Oriental despotism ... even in capitalism\" [[R13 129]]. Deleuze in 1979: projecting one form onto another without precaution is \"a catastrophe\" [[seminar, 20 Nov 1979]]",
     "Taken for a typology of societies, or flattened into capture against escape, which drops the town and the ecumenical (Protevi's table has neither, RoV xx-xxi)"),
    ("Warding off (anticipation-prevention)", "357-59, 429-33, 437-40",
     "The ways in which a society anticipates a power it has never seen, so as to prevent it",
     "Clastres's chief without command (<i>Society against the State</i>), Lévi-Strauss's two village plans (<i>Structural Anthropology</i> 149-51), and Mauss on the destruction of wealth",
     "Deleuze names Mauss as the source that Clastres \"took up and renewed\" [[seminar, 20 Nov 1979]]. Guattari on the potlatch: \"above all no reciprocity, even when there is reciprocity\" [[R13 142]]",
     "An evolved disposition (Boehm's reverse dominance hierarchy, RoV 98), a damping mechanism (Protevi's \"thick threshold\"), or a costless equality"),
    ("Limit and threshold", "437-41",
     "The limit is the next-to-last, marking a fresh start for an assemblage. The threshold is the last, marking a change of assemblage",
     "Jevons's \"final degree of utility\" (1871) and the marginalists Pirou and Pareto [[566-67 nn. 24-26]]",
     "Deleuze: \"The marginal object is the penultimate or the limit\" [[seminar, 27 Nov 1979]]",
     "Lost. Bonta and Protevi's glossary keeps the distinction but not its marginalist content"),
    ("Apparatus of capture", "424-27, 444, 459-60",
     "Direct comparison and monopolistic appropriation together, as in rent, profit, and tax",
     "Dumézil's two-headed sovereignty (Varuna the binder, Mitra the jurist) in <i>Mitra-Varuna</i> (1948), together with the Roman debt bond called the nexum",
     "Deleuze: \"magic\" was \"a convenient and temporary word ... there is a war capture, but it is not at all the same as a State capture\" [[seminar, 22 Jan 1980]]. Fourquet in 1972: \"the first form of writing is accounting\" [[R13 28]]",
     "Co-optation (\"the system captures resistance\"), or simply everything a State does"),
    ("Urstaat", "359, 427, 460",
     "The State presupposed by every account of its origin, which \"comes into the world fully formed\"",
     "Marx's Asiatic mode (<i>Grundrisse</i>), Wittfogel, Childe, and Nietzsche's founders who come \"like lightning\" (<i>Genealogy</i> II.17)",
     "Against it, in 1973: \"we will have learned nothing from knowing that this State was already in germ in Sumer or in Egypt\" [[R13 116]]",
     "Taken for a historical despotism, or for an origin"),
    ("Polarization (the town)", "432-35",
     "The town as a point on circuits of roads, a power \"of the middle\" that coordinates by force",
     "Fourquet and Murard's 1976 <i>Les équipements du pouvoir</i> (\"The Facilities of Power\"), along with Braudel's \"two runners, the state and the town\" and Lévi-Strauss's village plans",
     "Towns \"always emerge as a network\" before any territorial State, as with the Hanse [[R13 70-71, 89-92]]. Deleuze: \"a bureaucracy of networks\" [[seminar, 20 Nov 1979]]",
     "Almost absent from the reception, and near zero in Protevi"),
    ("Encompassment (the ecumenical)", "435-36, 454",
     "Organizations that pass through heterogeneous formations at once (trade, religions, art)",
     "Samir Amin's <i>Unequal Development</i> (146, 295), Braudel's world-economy, and Lacarrière on the desert fathers",
     "Islam as \"an immense network,\" whose first public facilities were \"language, money ... and religion\" [[R13 77-79]]",
     "Almost absent, with world-systems theory taken up in its place"),
    ("Code, overcoding, axiomatic", "427, 448-54, 461-62",
     "A code relates qualified elements within a domain, overcoding subordinates codes to a higher unity, and an axiomatic treats unqualified flows directly",
     "Lévi-Strauss's codes of exchange, the genetic code (Jacob and Monod), Hjelmslev, and set theory",
     "Guattari in 1973: \"public facilities are the axioms of capital ... no intrinsic coding\" [[R13 131]]",
     "Code heard as computer code, though most of what now goes by that name is axiomatic"),
    ("Adding axioms", "462-63, 470",
     "Capitalism's answer to whatever escapes it, which is to add an axiom for it",
     "Set theory and Marxist accounts of co-optation",
     "Guattari in 1973: capital is \"obliged to enlarge its own axiomatic without stopping\" and \"the first axiom of capital is recuperation\" [[R13 133, 140]]",
     "Folded into capture as co-optation, with recuperation as fate, though ATP calls recuperation a \"disenchanted concept\" (463)"),
    ("The stock", "440-44",
     "What begins when exchange stops being of interest, with land, tools, and money as stockpiled territory, activity, and exchange",
     "Ingold on social storage (1983), Testart (1982), and Jacobs and Mellaart on Çatal Hüyük",
     "The State as \"a social machine ... for putting flows in reserve\" [[R13 72]]",
     "Storage as a threshold toward the State (Sterelny, in RoV 98)"),
    ("Nomad and nomos", "380-85, 422",
     "The nomad occupies a space without dividing it. The nomos is a distribution \"without division into shares\"",
     "Toynbee's nomads who \"stood their ground,\" Laroche on the root <i>nem-</i> [[557 n. 51]] against Schmitt's nomos as land seizure, and Ibn Khaldun",
     "Deleuze: there are \"nomades sur place\" (\"nomads on the spot\") [[seminar, 25 Mar 1980]]",
     "A people of the steppe, mobility, flight, the digital nomad, Braidotti's nomadic subject"),
    ("Smooth and striated", "362, 474-500",
     "Space occupied without being counted, against space counted in order to be occupied",
     "Boulez's smooth and pulsed time (<i>Penser la musique aujourd'hui</i>, 1963)",
     "Deleuze in 1973: \"The highway today is channeled nomadism ... while public service implies a general nomadism\" [[R13 186]]. In 1980, no space is \"better than the other\" [[seminar, 25 Mar 1980]]",
     "Smooth taken as good or free, as nature or complexity, or as an architectural look. For Protevi, \"too abstract\" for marronage (RoV 120)"),
    ("Holey space", "413-15",
     "Space bored through mountain and subsoil by the smith, communicating with both smooth and striated space",
     "Élie Faure on the rock-cut temples of India, Eisenstein's <i>Strike</i>, and Childe and Griaule on smiths",
     "The vacant lot, or terrain vague (\"waste ground\"), as a modern holey remainder [[R13 173-74]]",
     "Ignored, Protevi included"),
    ("Line of flight (the leak)", "204, 216, 229",
     "From the French fuite, which is also a leak: to put a system to flight is to make it leak",
     "French fuite (\"leak,\" \"flight\") and painting's point de fuite (\"vanishing point\"), Anglo-American literature, George Jackson",
     "\"To put a system to flight as one bursts a tube\" [[<i>Dialogues</i> 36]]. In 1973: \"it leaks on all sides\" [[R13 118-19]]",
     "Flight as leaving, exodus, or refuge (Protevi's \"autonomy-seeking flight / refuge\")"),
    ("War machine", "351-423",
     "A process whose positive object is to compose a smooth space and its people, with war only as its supplement",
     "Dumézil on the warrior's exteriority, Clausewitz, Ibn Khaldun, Clastres, de Heusch, Brossollet, Virilio, Kleist",
     "Guattari in 1972: \"The ideal of despotism is Genghis Khan: destroy everything (except the artisans)\" [[R13 29]], and in 1973 \"nomadic State power\" [[R13 135]]",
     "Militarism, \"the nomads\" (Sneath, Munkh-Erdene), creativity in general, or any subversive collective"),
    ("Numbering number", "387-94",
     "A number that distributes people in space and moves with them, articulated and doubled by a special body",
     "Kristeva's <i>Semeiotike</i> (293-97), Aristotle's counting number (<i>Physics</i> IV.11), the muster of Numbers 1, and Jethro's judges in Exodus 18",
     "Deleuze on Boulez: \"cipher, numbering number, nomad or Mallarmean number\"",
     "Little used, and taken by the specialists for sovereignty"),
    ("Esprit de corps", "366",
     "A solidarity that makes the family \"a band vector instead of a fundamental cell\"",
     "Ibn Khaldun's asabiyya (<i>The Muqaddimah</i>)",
     "",
     "Team spirit (Protevi's chapter on team sports, RoV 73-88)"),
    ("The secret, the cipher", "390, 286-90",
     "The cipher \"invents the secret and its outgrowths,\" against the public knowledge of the State",
     "Simmel on secret societies, de Heusch's man of war, and for today the anthropology of restricted knowledge (Price, Bilby, Peterson, Myers)",
     "Deleuze in 1972: codes work by \"zones of secrecy,\" an axiomatic by \"objective concealment\" [[seminar, 7 Mar 1972]]",
     "Knowledge treated as one more stock for capture"),
    ("Nomad and royal science", "361-74, 461",
     "Two conceptions of science in one field, the one following a material and the other reproducing a form",
     "Serres on Lucretius, Husserl's vague essences (<i>Ideas</i> I §74), Bachelard, Simondon, Vergez on the compagnonnages, Lautman",
     "Querrien's <i>Devenir fonctionnaire</i> (1977). Guattari in 1973: \"Bourbaki is a capitalist theorist\" [[R13 145]]",
     "Unused by Protevi, and otherwise taken as complexity theory (Bonta and Protevi) or as Indigenous or alternative knowledge"),
    ("Minority, the nondenumerable", "469-71",
     "A set defined by the relations internal to its number, which no axiom can count",
     "Cantor's set theory and Yann Moulier-Boutang",
     "Guattari in 1973: \"a special axiom ... for the Katangans, as long as it does not leak anywhere\" [[R13 138]]",
     "Minor as small or marginal"),
    ("Machinic enslavement and social subjection", "456-60",
     "People as parts of a machine, against people as subjects who use a machine",
     "Mumford's megamachine, Reuleaux, Marx on constant and variable capital, and cybernetics",
     "The city as \"the social cybernetic machine of industrial capitalism\" (1971) [[R13 20 n. 1]]",
     "Taken up for digital capitalism (Lazzarato), rarely for slavery"),
    ("Machinic phylum", "404-15",
     "Matter in movement and variation, carrying singularities and traits of expression, which can only be followed",
     "Simondon, Childe on metallurgy, and Hjelmslev",
     "Guattari in 1973: the phylum as \"the most deterritorialized point\" [[R13 131]]",
     ""),
    ("Public facilities", "behind 454, 461-62",
     "Schools, hospitals, roads, and other such facilities, which Guattari called \"the axioms of capital\" (not an ATP term)",
     "French postwar planning, where équipements collectifs (\"public facilities\") enters the Fourth Plan in 1962",
     "Facilities as \"instruments of domination and territorial fixing of flows\" [[R13 127]]",
     "Translated \"collective equipment,\" and confused with infrastructure"),
    ("Channeled nomadism, the right of use", "not in ATP, cf. 386",
     "The highway channels nomadism, while public service implies a general nomadism, so that \"the right of use is the community\"",
     "French public service law, with its usager (\"user\") and droit d'usage (\"right of use\")",
     "Deleuze in the CERFI discussion of public facilities [[R13 186]]",
     "Unknown to the reception"),
]
CONC_INTRO = ('A concept, as Deleuze often put it, is the movement behind its name. Indeed, these names have moved a great deal. Each row gives a concept of the two plateaus in plain words, the field from which it came, '
              'where it was worked out before 1980 (CERFI\'s journal <i>Recherches</i> in 1972-73, Deleuze\'s seminars at Vincennes in 1979-80), and how it has been taken up since. '
              'R13 is <i>Recherches</i> 13 (December 1973), cited by its printed pages.')
CONC_FOOT = ('ATP page numbers refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987), RoV to Protevi\'s <i>Regimes of Violence</i> (2025). '
             'Seminar dates refer to the Purdue transcripts of Deleuze\'s lectures. Translations from the French are the project\'s own. Source: <i>kit/concept_ledger.tsv</i>.')


def conc_table(rows=None):
    out = ['<table class="cc"><colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"><col class="c5"></colgroup><thead><tr>'
           '<th>Concept</th><th>In plain words</th><th>Where it came from</th><th>Where it was worked out</th><th>How it has been taken up since</th></tr></thead><tbody>']
    for name, pp, plain, home, work, drift in (rows or CONCEPTS):
        out.append(f'<tr class="row"><th>{fmt(name)}<small>{pp}</small></th><td>{fmt(plain)}</td><td>{fmt(home)}</td>'
                   f'<td class="wk">{fmt(work) if work else "·"}</td><td class="dr">{fmt(drift) if drift else "·"}</td></tr>')
    out.append("</tbody></table>")
    return "".join(out)


# ---------------------------------------------------------------- 2. The State's forms
SCOLS = ["arch", "evol", "nat"]
SHEAD = {"arch": ("The archaic empire", "Marx's \"Asiatic formation\""),
         "evol": ("Evolved States", "empires, cities, feudal systems, monarchies"),
         "nat": ("Nation-States", "models of realization of the axiomatic")}
SROWS = [
    ("Where is it found?", {
        "arch": "Egypt, Mesopotamia, the Indus valley, China, and \"not only in Asia, but also in Africa, America, Greece, Rome\" [[427, 450]]",
        "evol": "Rome's empire (with its consilium and fiscus), the Aegean cities, feudal systems, and absolute monarchy [[451-52, 459]]",
        "nat": "Modern nation-States of every kind (democratic, totalitarian, liberal, tyrannical), as well as the bureaucratic socialist States [[455-56, 459]]"}, []),
    ("What does it do with flows?", {
        "arch": "It **overcodes** flows already coded by the communities it rules [[427-28, 459]]",
        "evol": "It organizes \"qualified or topical conjunctions of decoded flows\" [[451, 459]]",
        "nat": "It realizes \"a general conjugation of flows,\" the capitalist axiomatic [[454-55, 459]]"}, []),
    ("What is its regime of signs?", {
        "arch": "Overcoding, \"or the Signifier\" [[428]]",
        "evol": "Processes of **subjectification** [[451]]",
        "nat": "The **axiomatic**, which deals \"directly with purely functional elements and relations\" [[454]]"}, []),
    ("What binds people?", {
        "arch": "The nexum, \"the objective, imperial collective bond\" [[428, 460]]",
        "evol": "Personal bonds, from contracts between owners to the conventions that tie the owned to their owners [[451]]",
        "nat": "\"The Subject that binds itself,\" a contract \"between self and self\" [[460]]"},
     [dict(a="arch", z="nat", text="**One moment** of the State through all its forms: \"capture, bond, knot, nexum, magical capture\" [[460]]", kind="pair")]),
    ("What becomes of property?", {
        "arch": "Everything is public, with the despot as \"the sole and transcendent public-property owner\" and land that cannot be sold [[428]]",
        "evol": "The public sphere becomes \"the shared means for a now private appropriation\" [[451]]",
        "nat": "Property is in \"convertible abstract rights,\" and capital is itself \"a right\" [[453-54]]"}, []),
    ("What is the form of its law?", {
        "arch": "\"The overcoding of customs\" [[453]]",
        "evol": "\"A set of topics,\" subjective and conjunctive (Roman law, cf. Veyne) [[451, 453]]",
        "nat": "The form of an axiomatic, as in the French civil code (cf. Ray) [[453]]"}, []),
    ("How are persons captured?", {
        "arch": "Machinic **enslavement**, \"generalized slavery\" in the megamachine (cf. Mumford) [[428, 457]]",
        "evol": "**Subjection**: ancient slavery and feudal serfdom were already \"procedures of subjection\" [[457]]",
        "nat": "Social subjection of the \"naked\" or \"free\" worker, joined by a new enslavement in cybernetic \"humans-machines systems\" [[457-58]]"},
     [dict(a="arch", z="nat", text="\"A small amount of subjectification took us away from machinic enslavement, but a large amount brings us back to it\" [[458]]", kind="pair", solid=["evol"])]),
    ("What kind of surplus value?", {
        "arch": "Surplus value \"of code\" [[451]]",
        "evol": "Surplus value \"of flow,\" first among the Aegean merchants and smiths [[450-51]]",
        "nat": "Surplus value that \"becomes machinic\" with automation [[458]]"}, []),
    ("What does it do with the war machine?", {
        "arch": "It has none of its own, working instead through police and prisons while encasting warriors captured from outside [[418, 425]]",
        "evol": "Appropriation proper, as in the hoplite reform's army of citizen-soldiers [[419, 426]]",
        "nat": "Total war, then a worldwide war machine \"of which they are no longer anything more than the opposable or apposed parts\" [[421, 466-67]]"}, []),
    ("How diverse is it?", {
        "arch": "\"Little diversity, due to a certain formal immutability\" [[459]]",
        "evol": "\"Extremely diverse\" [[459]]",
        "nat": "A diversity that is \"a function of isomorphy,\" and of heteromorphy or polymorphy [[459, 464-66]]"}, []),
    ("What escapes it?", {
        "arch": "Decoded flows of labor and money, and private property \"slipping through the net,\" carried by \"the collective figure of the Outsider\" (freed slaves, cf. Tökei) [[449]]",
        "evol": "Decoded flows that \"draw capitalism in negative outline\" but are not let \"stream together\" [[452]]",
        "nat": "Minorities as nondenumerable sets, and \"undecidable propositions\" [[470-73]]"},
     [dict(a="arch", z="evol", text="The Aegean \"presuppose[s]\" the oriental stock, and \"there is always an empire on the horizon\" [[459-60]]", kind="pair"),
      dict(a="evol", z="nat", text="\"Capitalism was continually being born, disappearing and reviving at every crossroads of history\" [[460]]", kind="pair")]),
]
S_MEET = "\"Capitalism has reawakened the Urstaat, and given it new strength.\" The modern States \"restore the most absolute of empires, a new 'megamachine,' whatever the novelty or timeliness of its now immanent form\" [[460]]"
S_INTRO = ('Deleuze and Guattari distinguish \"three major forms\" of the State (459). In fact, they are not stages, since each form is in \"resonance\" with the others, and all of them \"exhibit a unity of composition in spite of their differences in organization and development\" (459). '
           'The sheet opens the single column that <i>The five machinic processes</i> gives to capture. Brackets join the forms where Deleuze and Guattari set out a relation between them.')
GIVENS = [
    ("1. Addition, subtraction", "461-63",
     "Axioms are \"operative statements.\" Social democracy adds them (Keynes and the New Deal as \"axiom laboratories\"), totalitarianism subtracts them, as in \"the minimum State of anarcho-capitalism (cf. Chile)\"",
     "\"It would be an error to take a disinterested stance toward struggle on the level of the axioms\" [[463]]"),
    ("2. Saturation", "463-64",
     "Capitalism \"has no laws but immanent ones.\" It confronts its own limits and displaces them at once (oil, nuclear power)",
     "Local struggles must \"directly target national and international axioms, at the precise point of their insertion\" [[464]]"),
    ("3. Models, isomorphy", "464-66",
     "All States are models of realization: isomorphic at the center, heteromorphic in the socialist East, polymorphic at the periphery",
     "It \"would be absurd\" to think popular movements condemned in advance, or all States \"equivalent and homogeneous\" [[466]]"),
    ("4. Power", "466-67",
     "A \"power of the continuum\" in the military-industrial complexes, where \"peace ... technologically frees the unlimited material process of total war\"",
     "The same capital \"continually recreate[s] unexpected possibilities for counterattack\" [[422]]"),
    ("5. The included middle", "468-69",
     "The center needs a periphery, and \"internal Third Worlds\" rise inside the center, with labor split between intensive surplus labor and \"erratic\" work",
     "Negri's \"internal margin,\" which \"tends increasingly to merge the students with the emarginati\" [[469]]"),
    ("6. Minorities", "469-71",
     "Minorities are nondenumerable sets, which States answer by \"translating the minorities into denumerable sets or subsets\"",
     "The demand \"to formulate their problems themselves\" is what the axiomatic \"cannot tolerate\" [[471]]"),
    ("7. Undecidable propositions", "471-73",
     "Not \"the uncertainty of the results\" but \"the coexistence and inseparability\" of what the system conjugates and what escapes it",
     "\"The germ and locus par excellence of revolutionary decisions\" [[473]]"),
]
POLES = [("Social democracy", "Adds axioms by organizing a domestic market and multiplying \"directing axioms\" [[462]]"),
         ("Totalitarianism", "Subtracts axioms and promotes the foreign sector, \"the minimum State,\" with the population \"a consequence\" [[462]]"),
         ("Fascism", "A war economy and \"a multiplication by subtraction,\" a \"suicidal\" State more than a totalitarian one (cf. Virilio) [[462-63, 467]]")]
G_INTRO = ('In the present, as D&G see it, \"capitalism and present-day politics are an axiomatic in the literal sense,\" which is why \"nothing is played out in advance\" (461). '
           'They set out \"a summary sketch of the \'givens\'\" in seven parts. The last column records where, by their own account, struggle enters.')
S_FOOT = 'Page numbers refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987). Bold type marks the two terms of a contrast. Brackets mark relations between the forms, dotted where they pass over a column. The three forms are worked out at length in the 1979-80 seminar, sessions 2 and 6-8, and the axiomatic in sessions 8-13 (listed on the back page of the library sheet).'


def scell(v):
    return f"<td>{fmt(v)}</td>"


def state_table():
    out = ['<table class="sf"><colgroup><col class="q"><col><col><col></colgroup><thead><tr><th>Question</th>']
    for c in SCOLS:
        t, s = SHEAD[c]
        out.append(f"<th>{t}<small>{s}</small></th>")
    out.append("</tr></thead><tbody>")
    for q, vals, bands in SROWS:
        out.append(f'<tr class="row"><th>{q}</th>' + "".join(scell(vals[c]) for c in SCOLS) + "</tr>")
        for b in bands:
            out.append(sband(b))
    out.append(f'<tr class="transfer"><th>How do the forms meet?</th><td colspan="3">{fmt(S_MEET)}</td></tr></tbody></table>')
    return "".join(out)


def sband(b):
    i, j = SCOLS.index(b["a"]), SCOLS.index(b["z"])
    segs = []
    for k in range(i, j + 1):
        c = (["l"] if k == i else []) + (["r"] if k == j else []) + (["skip"] if i < k < j and SCOLS[k] not in b.get("solid", []) else [])
        segs.append(f'<i class="{" ".join(c)}"></i>')
    tds = ["<td></td>"]
    k = 0
    while k < len(SCOLS):
        if k == i:
            tds.append(f'<td colspan="{j - i + 1}" class="bandcell"><div class="seg">{"".join(segs)}</div><p class="bt">{fmt(b["text"])}</p></td>')
            k = j + 1
        else:
            tds.append("<td></td>")
            k += 1
    return '<tr class="band">' + "".join(tds) + "</tr>"


def givens_table():
    out = ['<table class="gv"><colgroup><col class="g1"><col class="g2"><col class="g3"><col class="g4"></colgroup>'
           '<thead><tr><th>Given</th><th>ATP</th><th>What Deleuze and Guattari say</th><th>Where struggle enters</th></tr></thead><tbody>']
    for name, pp, say, strug in GIVENS:
        out.append(f'<tr class="row"><th>{name}</th><td class="pp">{pp}</td><td>{fmt(say)}</td><td class="st">{fmt(strug)}</td></tr>')
    out.append("</tbody></table>")
    poles = "".join(f'<div><b>{n}</b> {fmt(d)}</div>' for n, d in POLES)
    return "".join(out) + f'<div class="poles3"><span class="plab">Poles of the capitalist State</span>{poles}</div>'


# ---------------------------------------------------------------- 3. Nomadology bibliography
# (field, [(source, what it contributed, ATP pages, against?)]); "against" marks a source Deleuze and Guattari dispute or correct.
LIBRARY = [
    ("Myth, religion, and ancient thought", [
        ("Dumézil, <i>Mitra-Varuna</i> (1948), <i>The Destiny of the Warrior</i>, <i>Mythe et épopée</i>", "The two heads of sovereignty (the binder and the jurist), the warrior's three sins, the nexum", "351-55, 424-26", False),
        ("de Heusch, <i>Le roi ivre</i> (1972)", "The Bantu myth of Nkongolo and Mbidi, with the secret of the man of war", "353", False),
        ("Detienne, <i>Les maîtres de vérité</i> (1973), and on the phalanx", "Two poles of Greek thought, the warriors between them, isonomy, the hoplite reform", "375, 399, 426", False),
        ("Vernant, <i>Mythe et pensée chez les Grecs</i>", "The city-state's homogeneous geometrical extension", "388", False),
        ("Eliade, <i>Images and Symbols</i> (1961)", "The binder-god, studied by a \"syncretic and archetypal\" method that D&G set against Dumézil's differential one", "424", True),
        ("Hélène Clastres, <i>La terre sans mal</i> (1975)", "Tupi-Guarani prophets against the chiefs", "357, 384", False),
        ("Alphandéry, <i>La chrétienté et l'idée de croisade</i>", "The Crusade's changes of course as part of its idea", "384", False),
        ("Lacarrière, <i>Les hommes ivres de Dieu</i> (1975)", "The desert fathers, Christianity's own bands and deserts", "436", False),
    ]),
    ("Anthropology and ethnography", [
        ("Pierre Clastres, <i>Society against the State</i> (1977), \"Archéologie de la violence\" (1980)", "Warding off the State, war against the State, the chief without command", "357-59, 429", False),
        ("Mauss (by way of Clastres)", "The potlatch as a check on the concentration of wealth", "357", False),
        ("Lévi-Strauss, <i>Structural Anthropology</i> (149-51)", "One village, two plans, segmentary or hierarchized", "433", False),
        ("Berthe, \"Aînés et cadets\" (1965)", "The \"third village\" that keeps the circuit from closing", "433", False),
        ("Meunier, <i>Les gamins de Bogota</i> (1977)", "Street gangs that keep their leader from gaining stable power", "358", False),
        ("Griaule and Dieterlen, <i>Le renard pâle</i> (1965)", "Dogon smiths, \"mixed\" rather than impure", "415", False),
        ("Pottier on Tuareg smiths (1945), Bloch, <i>Les Tziganes</i> (1969)", "Smiths as a special body, and cave dwelling beyond nomad and sedentary", "393, 413", False),
        ("Cline (1937) and Clément (1948) on African smiths", "Studies of how others regard the smith, which D&G find \"hardly conclusive\"", "413", True),
        ("Gluckman, <i>Custom and Conflict in Africa</i> (1959)", "Immutable form with constant rebellion", "385", False),
        ("Thesiger, <i>Arabian Sands</i> (1959), Carpenter, <i>Eskimo</i> (1964), Emperaire, <i>Les nomades de la mer</i> (1954)", "Deserts of sand and ice as haptic, sonorous space, and the itineraries of sea nomads", "382", False),
        ("Milovanoff on the nomad's tent (1978)", "A dwelling tied to an itinerary, not a territory", "380", False),
        ("Bernstein on primate dominance (1978)", "Leadership that inhibits stable power", "358", False),
    ]),
    ("Archaeology and prehistory", [
        ("Childe, <i>The Prehistory of European Society</i>, <i>The Most Ancient East</i>", "The itinerant smith, the agricultural surplus, the Aegean's freer artisans", "412, 415, 428, 450-51", False),
        ("Mellaart, <i>Çatal Hüyük</i> (1967), and Jane Jacobs's \"New Obsidian\"", "A stock before agriculture, with the town creating the country", "428-29, 440", False),
        ("Griaznov, <i>The Ancient Civilization of Southern Siberia</i> (1969)", "Nomadism begun by farmers who left the town", "430", False),
        ("Leroi-Gourhan, <i>Milieu et techniques</i> (1945)", "Types of percussion, and a technological vitalism", "395, 407", False),
        ("Forbes, <i>Metallurgy in Antiquity</i> (1950), Limet on Sumerian metal (1960)", "The miner, smelter, smith, and metalworker, and twelve varieties of copper", "405, 415", False),
        ("Harmand, <i>La guerre antique</i> (1973)", "An archaic State that works through jailers before warriors", "427", False),
    ]),
    ("History", [
        ("Braudel, <i>Capitalism and Material Life</i> (1967)", "\"Two runners, the state and the town,\" East and West, the tool as result", "385, 399, 434, 468", False),
        ("Toynbee, <i>A Study of History</i>", "The nomad who \"does not move\"", "381", False),
        ("Hubac, <i>Les nomades</i> (1948)", "Local climates, though he \"tends to confuse nomads and migrants\"", "382", True),
        ("Ibn Khaldun, <i>The Muqaddimah</i>", "Esprit de corps, with the countryside as nomos", "366, 380", False),
        ("Vladimirtsov, <i>Le régime social des Mongols</i> (1948)", "Genghis Khan's guard of \"antrustions,\" and a feudal account of the steppe that D&G reject", "392, 394", True),
        ("Grousset, <i>The Empire of the Steppes</i>", "Tamerlane against Genghis Khan", "419", False),
        ("Ssu-ma Ch'ien, \"The Account of the Hsiung-nu\"", "Number and direction in the war machine", "390", False),
        ("Lynn White Jr., <i>Medieval Technology and Social Change</i> (1962)", "The stirrup, the heavy plow, long technological lineages", "399, 404", False),
        ("Mazaheri, \"Le sabre contre l'épée\" (1958)", "Saber and sword as two technological lineages", "404-06", False),
        ("Will, <i>Korinthiaka</i> (1955), Ardant, <i>Histoire financière</i> (1976)", "Money derived from taxation, not trade", "442-43", False),
        ("Tökei on Chinese landed property (1958) and the Asiatic mode", "Freed slaves as the seeds of private property", "449", False),
        ("Veyne, <i>Le pain et le cirque</i> (1976), Boulvert (1974)", "Roman subjective law as \"topics,\" freedmen in the imperial service", "451", False),
        ("Lombard, Chaunu, Musset, Gautier, Watt, Chevalier", "East and West, the invasions, North Africa, Medina, Paris's \"nomads\"", "380, 383, 385", False),
        ("Charrière, <i>Scythian Art</i>, Musset on runes, Pelliot on Mongol scripts", "Jewelry, runic writing, borrowed scripts", "401-02", False),
    ]),
    ("Mathematics, physics, and philosophy of science", [
        ("Serres, <i>La naissance de la physique</i> (1977)", "The first three traits of nomad science, the clinamen, \"rigorous, anexact\"", "361-62, 367, 372", False),
        ("Boulez, <i>Boulez on Music Today</i>", "Smooth and striated space-time", "362, 477-78", False),
        ("Proclus, and Bouligand, <i>Le déclin des absolus</i> (1949)", "The theorematic against the problematic, problems against the global synthesis", "362, 374", False),
        ("Husserl, <i>Ideas</i> I §74, <i>Origin of Geometry</i> (with Derrida)", "Vague essences, protogeometry", "367", False),
        ("Bachelard, <i>Essai sur la connaissance approchée</i> (1927)", "The rigor of the anexact", "367", False),
        ("Simondon, <i>L'individu</i> (1964), <i>Du mode d'existence</i> (1969)", "The critique of hylomorphism, from the mold to modulation and metallurgy", "369, 408-10", False),
        ("Lautman, <i>Les schémas de structure</i> (1938)", "Riemann spaces immersed in a Euclidean one", "373", False),
        ("Brunschvicg, Chasles, Desargues's <i>Oeuvres</i>", "The line from Desargues to Monge and Poncelet, \"founders of a modern geometry\"", "363, 365", False),
        ("Kristeva, <i>Semeiotike</i> (1969)", "The traits of the numbering number", "390", False),
        ("Guéroult on Leibniz (1934)", "Work against free action", "397", False),
        ("Benveniste on rhythm (1971)", "Rhythm as form, \"ambiguous\" to D&G for leaving out hydraulics", "363", True),
        ("Blanché, <i>L'axiomatique</i> (1959), the intuitionists (Brouwer, Heyting)", "Saturation, models, undecidable propositions, a calculus of problems", "455, 461", False),
        ("Worringer, <i>Form in Gothic</i> (1927)", "The Gothic line and nonorganic life", "411", False),
        ("Querrien, <i>Devenir fonctionnaire</i> (CERFI), Vergez on the compagnonnages (1976)", "Gothic builders, State engineers, the cutting line", "364-66", False),
        ("de Montmollin, <i>Les systèmes hommes-machines</i> (1967)", "\"Humans-machines\" systems", "458", False),
    ]),
    ("War and strategy", [
        ("Clausewitz, <i>On War</i>, with Aron, <i>Penser la guerre</i> (1976)", "Absolute war as Idea, real wars between two poles", "389, 419-21", False),
        ("Lawrence, <i>Seven Pillars of Wisdom</i>, \"The Science of Guerrilla War\"", "The nonbattle", "416", False),
        ("Brossollet, <i>Essai sur la non-bataille</i> (1975)", "The nonbattle and the \"unspecified enemy\"", "416, 422", False),
        ("Virilio, <i>Speed and Politics</i>, <i>L'insécurité du territoire</i>", "Polis as police, the fleet in being, dromocracy, the inversion of Clausewitz, though he \"tends to equate\" three kinds of speed", "386-87, 395-96, 421, 467", True),
        ("Fuller, <i>Armament and History</i> (1945)", "Weapons and tools identical for ages, the tank as a land ship", "395, 397", False),
        ("Ludendorff, <i>Der totale Krieg</i> (1935), Nef, <i>War and Human Progress</i>", "Total war and its economy", "421", False),
        ("Jünger, <i>Traité du rebelle</i>, <i>The Glass Bees</i>", "The Rebel between Worker and Soldier, and mutilation", "403, 426", False),
    ]),
    ("Political economy", [
        ("Marx, <i>Grundrisse</i>, <i>Capital</i>", "The Asiatic formation, rent, the trinity formula, primitive accumulation", "427, 441-47, 452", False),
        ("Wittfogel, <i>Oriental Despotism</i> (1957)", "Waterworks and empire", "363, 427", False),
        ("Jevons, Pirou, Pareto, Fradin", "The marginal \"last,\" ophelimity, groping evaluation", "437-39", False),
        ("Ricardo, <i>Principles</i>", "Differential rent", "441", False),
        ("Bernard Schmitt, <i>Monnaie, salaires et profits</i> (1980)", "The model of capture in four steps", "442, 445-46", False),
        ("Samir Amin, <i>Unequal Development</i>, <i>Accumulation on a World Scale</i>", "No economic theory of international relations, the axioms of the periphery", "436, 465, 469", False),
        ("Emmanuel, <i>Unequal Exchange</i>, Sweezy, Dobb", "Indirect tax, capital as a homogeneous fund, rights to wealth", "443, 453", False),
        ("Mumford, \"The First Megamachine\" (1966), <i>The Pentagon of Power</i>", "The archaic empire as a machine made of people", "428, 457, 460", False),
        ("Fourquet and Murard, <i>Les équipements du pouvoir</i> (1976), Jean Robert, Balazs, Châtelet", "Towns as networks, the inversion of signs, the doubtful city-state", "431-33, 447", False),
        ("Ray on the civil code (1926)", "Modern law as an axiomatic", "453", False),
        ("Faye, <i>Langages totalitaires</i> (1972)", "The Nazi economy", "463", False),
        ("Tronti, Negri, and Italian autonomia, Moulier", "The refusal of work, the internal margin", "469, 472", False),
        ("Engels, <i>The Origin of the Family</i>", "Three theses on the State's origin, all of which \"beg the question\"", "427", True),
    ]),
    ("Literature, art, and philosophy", [
        ("Kleist, <i>Penthesilea</i>, \"On the Gradual Formation of Ideas in Speech\", \"On the Marionette Theater\"", "Secrecy, speed, affect, thought as a war machine", "355-56, 378, 400", False),
        ("Nietzsche, <i>Schopenhauer as Educator</i>, <i>Genealogy</i> II.17", "The private thinker, founders who come like lightning", "353, 376-77", False),
        ("Artaud's letters to Rivière, Rimbaud, Kenneth White", "Thought without image, the inferior race, intellectual nomadism", "378-79", False),
        ("Foucault, \"La pensée du dehors\" (1966)", "The form of exteriority of thought", "377", False),
        ("Kojève, Weil, and Jaspers", "A Hegelianism of the right that \"weds the destiny of thought to the State\"", "375-79", True),
        ("Élie Faure, <i>History of Art</i>, Eisenstein, <i>Strike</i>", "Holey space", "413-14", False),
        ("Castaneda, <i>The Teachings of Don Juan</i>, Herbert, <i>Children of Dune</i>", "Following the devil's weed, a walk without measure", "372, 390", False),
        ("Starobinski, <i>Trois fureurs</i> (1974), Shakespeare, Kafka", "Ajax, Richard III, the nomads in the capital", "353-55", False),
    ]),
]
L_INTRO = ('Deleuze and Guattari built nomadology out of other people\'s research: myth, anthropology, archaeology, history, mathematics, military theory, and political economy, with literature throughout. '
           'Their notes to the two plateaus (ATP 552-71) cite about a hundred works, grouped here by field, each with what it contributed to the plateaus. '
           'Sources marked <b class="ag">against</b> are ones they dispute or correct, which is part of the method too. Yet every field here has moved in the fifty years since.')
L_FOOT = 'Pages are those of the text where a source enters, with the notes to those pages, in the Minnesota translation of <i>A Thousand Plateaus</i> (1987). Titles and dates as given in the notes.'


# ---------------------------------------------------------------- 3b. The workshop around the plateaus (library, back)
# The texts where the plateaus' ideas are worked out outside the book. Detail and verified quotations: work/context/.
SESSIONS = [  # 1979-80 seminar, "Apparatuses of Capture and War Machines" (Purdue edition, PDF page of each session)
    ("1", "6 Nov 1979", "The year's five oppositions: space, number, work against free action, weapons and jewels against tools and signs, and affects against sentiments. Also police before army, the phylum; Engels's three theses; the three heads of capture", "351-403, 424-48"),
    ("2", "13 Nov 1979", "Civil capture; the Asiatic mode; code and overcoding; the megamachine; machinic enslavement and social subjection; Jacobs's stock before agriculture", "424-29, 449-58"),
    ("3", "20 Nov 1979", "Clastres and Mauss; anticipation-warding off; the two waves; town and State (Braudel); the ecumenical; \"the last glass\"", "357-60, 429-39"),
    ("4", "27 Nov 1979", "The marginal shepherd; limit and threshold; seeds against obsidian axes", "435-39"),
    ("5", "15 Jan 1980", "Personal dependency; the man of the lament (Tökei)", "449-51"),
    ("6", "22 Jan 1980", "Territory and land; comparison and appropriation; the despotic face; \"magic\"; Kafka's two bureaucracies; the freed slave", "424, 440-51"),
    ("7", "29 Jan 1980", "Alliez on mercantilism; overcoding's decoded flows; Childe's East and West; topical conjunctions", "428-29, 443-53"),
    ("8", "5 Feb 1980", "Capital's nominal and real definitions; land rent; the minimum State; NASA; the nation; what an axiomatic is", "452-73"),
    ("9", "26 Feb 1980", "Minor science (Euclid and Archimedes, Desargues, Monge, Poncelet); formalization and axiomatic", "361-74, 454-61"),
    ("10", "4 Mar 1980", "The police at Vincennes; the \"unspecified enemy\"", "422, 467"),
    ("11", "11 Mar 1980", "Adding and subtracting axioms; totalitarian, social-democratic, fascist; saturation", "461-63"),
    ("12", "18 Mar 1980", "Aim and objective; the immanent limit; Linhart's \"modern hunger\"; isomorphy; the periphery", "420-21, 463-69"),
    ("13", "25 Mar 1980", "Metallurgical peoples and holey space; nomads in place; power and total war; undecidables; minorities", "380-82, 411-15, 420-22, 466-73"),
]
WORKSHOP = [
    ("Deleuze's other seminars", [
        ("27 Feb 1979, \"Metal, Metallurgy, Music, Husserl, Simondon\"", "Vague essences, molding against modulation, metal as continuous variation, the smith beside the musician", "367-69, 404-15"),
        ("1977 (A Thousand Plateaus II)", "Kleist against Goethe, haecceities, the two planes", "355-56, 368-69"),
        ("1971-72 (Anti-Oedipus I)", "The Asiatic State \"in one blow\", code and axiomatic, finite and infinite debt", "427, 449-55"),
        ("1981 (Painting)", "Worringer's Gothic line, Riegl's haptic", "382, 411"),
    ]),
    ("With Parnet, with Guattari", [
        ("<i>Dialogues</i> (1977), \"Many Politics\"", "Propositions I-III in a paragraph; lines of flight turned to abolition; absolute peace", "351-61, 421-23"),
        ("Interview, early 1970s (<i>Chaosophy</i>)", "\"a revolution requires a war machine, but this is not a state apparatus\"", "422-23"),
        ("Guattari, on machinic enslavement (<i>Soft Subversions</i>)", "Enslavement and subjection, from Guattari's side", "456-58"),
        ("Guattari's seminars, 1980-88", "The war machine as a position in schizoanalytic cartography (1982)", "351"),
    ]),
    ("The CERFI", [
        ("<i>Recherches</i> 13 (Dec 1973), \"Les équipements du pouvoir\"", "The Plan, collective equipment, town and State, with Deleuze, Guattari, Foucault in conversation", "364-68, 431-33"),
        ("Querrien, <i>Devenir fonctionnaire</i> (1978)", "Nomad masons, cutting by templates, Trudaine's assemblies, the commoner corps", "364-68"),
    ]),
]
W_INTRO = ('Much of the two plateaus was worked out aloud first, in the 1979-80 seminar at Vincennes on \"Apparatuses of Capture and War Machines\", thirteen sessions between November and March, with students (Éric Alliez, Georges Comtesse, Richard Pinhas, Claire Parnet) intervening. '
           'The table matches each session to the pages it develops; the list below names the other places the ideas live. '
           'Every passage, with verified quotations, is in <i>work/context/context_12_13.md</i> and under \"Elsewhere\" on the web reference.')
W_FOOT = ('Seminar transcripts and translations: The Deleuze Seminars (Purdue), 1979-80 trans. Kerslake and Stivale. A revised edition of the 1979-80 seminar is Lapoujade, ed., <i>Sur l\'appareil d\'État et la machine de guerre</i> (Minuit, 2025). Pages are those of the Minnesota translation of ATP.')


def workshop_html(web=False):
    rows = "".join(f'<tr><th>{n}</th><td class="pp">{d}</td><td>{fmt(t)}</td><td class="pp">{pp}</td></tr>' for n, d, t, pp in SESSIONS)
    table = f'<table class="ws"><colgroup><col class="w1"><col class="w2"><col class="w3"><col class="w4"></colgroup><thead><tr><th>Session</th><th>Date</th><th>What it works out</th><th>ATP</th></tr></thead><tbody>{rows}</tbody></table>'
    out = []
    for field, items in WORKSHOP:
        lis = "".join(f'<li><span class="src">{s}</span> {fmt(w)} <span class="pg">{pp}</span></li>' for s, w, pp in items)
        out.append(f'<section class="fld"><h2>{field} <small>{len(items)}</small></h2><ul>{lis}</ul></section>')
    if web:  # on screen the session table scrolls in its own box instead of widening the page
        table = f'<div class="wrap">{table}</div>'
    return table + f'<div class="lib ws2">{"".join(out)}</div>'


def library_html():
    out = []
    for field, items in LIBRARY:
        lis = "".join(f'<li>{"<b class=ag>against</b> " if ag else ""}<span class="src">{fmt(s)}</span> {fmt(w)} <span class="pg">{pp}</span></li>' for s, w, pp, ag in items)
        out.append(f'<section class="fld"><h2>{field} <small>{len(items)}</small></h2><ul>{lis}</ul></section>')
    return f'<div class="lib">{"".join(out)}</div>'


# ---------------------------------------------------------------- styles and pages
CSS = """
table.cc tbody th small, table.sf thead th small { display: block; }
table.cc tbody th small { font-weight: 500; color: var(--muted); }
td.wk { background: var(--pair-soft); }
td.dr { background: var(--ext-soft); font-style: italic; }
table.gv td.st { background: var(--pair-soft); }
table.gv td.pp { font-family: var(--label); color: var(--muted); }
.poles3 { display: grid; grid-template-columns: auto 1fr 1fr 1fr; border: 1px solid var(--rule); background: var(--split); }
.poles3 > * { padding: 4px 8px; }
.poles3 > * + * { border-left: 1px solid var(--rule); }
.plab { font-family: var(--label); font-weight: 600; color: var(--muted); }
.lib { columns: 3; column-gap: 22px; }
.fld { break-inside: avoid-column; margin-bottom: 10px; }
.fld h2 { font-family: var(--label); font-weight: 600; margin: 0 0 3px; color: var(--pair); border-bottom: 1px solid var(--pair); }
.fld h2 small { color: var(--muted); font-weight: 500; }
.fld ul { list-style: none; margin: 0; padding: 0; }
.fld li { margin-bottom: 3px; }
.src { font-weight: 600; }
table.ws { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
table.ws th, table.ws td { border: 1px solid var(--rule); padding: 3px 6px; text-align: left; vertical-align: top; }
table.ws thead th { font-family: var(--label); background: var(--surface); }
table.ws td.pp { font-family: var(--label); color: var(--muted); white-space: nowrap; }
b.ag, .ag { font-family: var(--label); font-weight: 600; color: var(--ext); border: 1px dashed var(--ext); background: var(--ext-soft); padding: 0 3px; text-transform: uppercase; font-size: 0.8em; letter-spacing: 0.03em; }
"""
PCSS = """
.cc1 h1, .sf1 h1, .gv1 h1, .lb1 h1 { font-size: 13pt; }
.cc1 .intro, .sf1 .intro, .gv1 .intro, .lb1 .intro { font-size: 7pt; }
.cc1 table { font-size: 6.75pt; line-height: 1.16; }
.cc1 col.c1 { width: 1.05in; } .cc1 col.c2 { width: 1.95in; } .cc1 col.c3 { width: 2.3in; } .cc1 col.c4 { width: 2.65in; }
.cc1 th, .cc1 td { padding: 2.6pt 3.6pt; }
.cc1 thead th { font-size: 8pt; } .cc1 tbody th { font-size: 7pt; } .cc1 tbody th small { font-size: 5.8pt; }
.sf1 table { font-size: 6.9pt; line-height: 1.14; }
.sf1 col.q { width: 1.15in; }
.sf1 th, .sf1 td { padding: 2.2pt 4pt; }
.sf1 thead th { font-size: 8.4pt; } .sf1 thead th small { font-size: 5.8pt; } .sf1 tbody th { font-size: 6.8pt; }
.sf1 tr.band td { padding: 0 4pt 1.5pt; } .sf1 .seg { height: 3pt; margin: 0 2pt; } .sf1 p.bt { font-size: 6.2pt; margin: 0.6pt 2pt 0; line-height: 1.12; }
.sf1 tr.transfer > * { padding: 3pt 4pt; }
.gv1 table { font-size: 8pt; line-height: 1.2; }
.gv1 col.g1 { width: 1.5in; } .gv1 col.g2 { width: 0.6in; } .gv1 col.g3 { width: 4.7in; }
.gv1 th, .gv1 td { padding: 4pt 5pt; } .gv1 thead th { font-size: 8.6pt; } .gv1 tbody th { font-size: 7.8pt; }
.gv1 .poles3 { font-size: 7.6pt; line-height: 1.2; margin-top: 0.08in; border-width: 0.6pt; } .gv1 .poles3 > * { padding: 3pt 5pt; }
.lb1 .lib { font-size: 6.1pt; line-height: 1.15; column-gap: 12pt; }
.lb1 .fld h2 { font-size: 7.6pt; border-bottom-width: 0.6pt; } .lb1 .fld { margin-bottom: 4pt; } .lb1 .fld li { margin-bottom: 1.6pt; }
.lb1 b.ag, .lb1 .ag { border-width: 0.6pt; padding: 0 1.5pt; }
.lb1 table.ws { font-size: 7.8pt; line-height: 1.15; table-layout: fixed; } .lb1 col.w1 { width: 0.5in; } .lb1 col.w2 { width: 0.8in; } .lb1 col.w3 { width: 6.2in; } .lb1 col.w4 { width: 1.6in; } .lb1 table.ws th, .lb1 table.ws td { padding: 1.8pt 4pt; } .lb1 .ws2 { font-size: 7.6pt; columns: 3; margin-top: 8pt; }
"""
WCSS = """
.wrap table { min-width: 1100px; }
col.q { width: 150px; }
table.cc col.c1 { width: 170px; }
.poles3 { margin-top: 12px; font-size: 0.92rem; }
.lib { font-size: 0.92rem; }
@media (max-width: 900px) { .lib { columns: 1; } }
h2.sec { font-family: var(--label); font-size: 1.15rem; margin: 30px 0 6px; }
p.secp { margin: 0 0 12px; color: var(--muted); max-width: 78ch; }
"""


def page(cls, title, side, intro, body, foot):
    return f'<section class="sheet {cls}"><div class="top"><h1>{title}</h1><span class="side">{side}</span></div><p class="intro">{intro}</p>{body}<div class="foot">{foot}</div></section>'


def handout(title, pages):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>{g.FONTS}'
            f'<style>{g.TOKENS}{g.SHARED}{g.PRINT}{CSS}{PCSS}</style></head><body>{"".join(pages)}</body></html>')


def web(title, h1, parts, foot):
    body = "".join(f'<h2 class="sec">{h}</h2><p class="secp">{p}</p>{b}' if h else f'<header><h1>{h1}</h1><p>{p}</p></header>{b}' for h, p, b in parts)
    return (f'<meta charset="utf-8"><title>{title}</title>{g.FONTS}'
            f'<style>{g.TOKENS}{g.DARK}{g.SHARED}{g.WEB}{CSS}{WCSS}</style>{body}<footer><p>{foot}</p></footer>{g.STICKY}')


def text_dump():
    parts = [CONC_INTRO, S_INTRO, G_INTRO, L_INTRO, S_MEET, W_INTRO] + [t for _, _, t, _ in SESSIONS] + [w for _, its in WORKSHOP for _, w, _ in its]
    for c in CONCEPTS:
        parts += list(c[2:])
    for _, vals, bands in SROWS:
        parts += list(vals.values()) + [b["text"] for b in bands]
    for gv in GIVENS:
        parts += [gv[2], gv[3]]
    parts += [d for _, d in POLES]
    for _, items in LIBRARY:
        parts += [w for _, w, _, _ in items]
    t = "\n\n".join(p for p in parts if p)
    for a, b in (("**", ""), ("[[", "("), ("]]", ")"), ("<i>", "*"), ("</i>", "*"), ("<b>", ""), ("</b>", "")):
        t = t.replace(a, b)
    return t


def main():
    wrap = lambda t: f'<div class="wrap">{t}</div>'
    save("concordance_handout.html", handout("Nomadology's Concepts", [
        page("cc1", "Nomadology's concepts, and how they have moved", "Concordance · front", CONC_INTRO, conc_table(CONCEPTS[:12]), CONC_FOOT),
        page("cc1", "Nomadology's concepts, continued", "Concordance · back", "Concepts 13-24, from nomad and nomos to the right of use.", conc_table(CONCEPTS[12:]), CONC_FOOT)]))
    save("concordance.html", web("Nomadology's Concepts", "Nomadology's concepts, and how they have moved", [("", CONC_INTRO, wrap(conc_table()))], CONC_FOOT))
    save("state_forms_handout.html", handout("The State's Forms", [
        page("sf1", "The State's three forms", "State forms · front", S_INTRO, state_table(), S_FOOT),
        page("gv1", "The axiomatic today: seven givens", "State forms · back", G_INTRO, givens_table(), S_FOOT)]))
    save("state_forms.html", web("The State's Forms", "The State's three forms", [
        ("", S_INTRO, wrap(state_table())), ("The axiomatic today: seven givens", G_INTRO, wrap(givens_table()))], S_FOOT))
    save("library_handout.html", handout("Nomadology Bibliography", [
        page("lb1", "Nomadology bibliography", "Sources of plateaus 12-13 · front", L_INTRO, library_html(), L_FOOT),
        page("lb1", "The workshop around the plateaus", "Library · back", W_INTRO, workshop_html(), W_FOOT)]))
    save("library.html", web("Nomadology Bibliography", "Nomadology bibliography", [("", L_INTRO, library_html()), ("The workshop around the plateaus", W_INTRO, workshop_html(web=True))], L_FOOT + " " + W_FOOT))
    open(os.path.join(HERE, "reference_sheets_text.md"), "w").write(text_dump() + "\n")
    n = sum(len(i) for _, i in LIBRARY)
    print(f"wrote concordance, state forms, library ({n} library entries, {len(CONCEPTS)} concepts)")


if __name__ == "__main__":
    main()
