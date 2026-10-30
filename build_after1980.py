"""After 1980: what later archaeology, anthropology, and history do to nomadology's claims, the literatures placed,
and neighboring fields. Same family as the five-process grids and the reference sheets.
  after1980_handout.html / after1980.html
Sources: notes/working-file/06_reading_cards.md (method pass, synthesis parts 1-2, cards), work/assessment/
source_assessment_v2.md (placements and field map). Every page number below comes from a card checked against the text.
Markup: **bold**, [[pages]], <i>titles</i>."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_five_processes as g  # noqa: E402

save = g.save


def fmt(s):
    return g.fmt(s).replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")


# (claim, ATP, bears out, complicates, disputes, what it asks)
CLAIMS = [
    ("The nomad holds a space and \"does not move\"", "380-81, 410",
     "Maroons who \"settled right where they were\" (Diouf 4-5), and Haitian cultivators who \"ceased being cultivators\" without leaving the plantation (Casimir 142)",
     "Ancient DNA and isotopes measure displacement, which is migration, not holding (Kristiansen, Furholt). Humphrey and Sneath replace \"nomadism\" with \"mobile pastoralism\" (1)",
     "Sneath attacks the egalitarian nomad as a trope and finds aristocracies on the steppe (<i>The Headless State</i> 3-4, 198-99)",
     "What evidence could register holding a space, as opposed to crossing it?"),
    ("Numbering numbers, which came from the nomads", "387-94",
     "The colonial grading of flight as a numbered number, used to set punishments (Thompson 53)",
     "Qin counties were defined by \"a notional five hundred hearths\" in the century of the first steppe decimal system (Sneath 237 n. 30). The Lupaqa khipu counted households (Murra)",
     "Steppe decimal units belonged to hereditary aristocracies, with \"lords of ten thousand\" in name only (Sneath 3-5, 23)",
     "Keep numbering and numbered as two operations, distributing in space or dividing it, and drop the claim that numbering came first (389)"),
    ("The war machine is exterior, and war does not produce the State", "351, 359",
     "Steppe states formed \"in relation to sedentary states\" such as China (Di Cosmo 171). Lindner treats lineage as recruitment and defection (690, 697)",
     "Kradin's Xiongnu captured outward by raiding and extortion while staying segmentary inside (77, 86)",
     "Munkh-Erdene argues \"for the nomadic origin of the state\" in a warlord's warband (<i>The Nomadic Leviathan</i> 1, 25)",
     "Can command exist without the State-form? (357, 393)"),
    ("Societies ward off the State they anticipate", "357-59, 431-33",
     "Equality \"asserted\" through the ability to leave and weapons held by all (Woodburn 431, 436). Sharing as a test of relations (Peterson). Leach's Kachin oscillate instead of climbing",
     "Resisting extraction pushed Tongan communities to stress women's reproductive roles (Gailey xi). Ritual knowledge founds rank as \"looking after\" (Myers 220-21). People hide food from their own kin (Peterson 864)",
     "Boehm's \"reverse dominance hierarchy\" and Sterelny, both in Protevi (RoV 98), turn the operation into an evolved disposition",
     "Warding off has internal costs. Who bears them?"),
    ("The Urstaat presupposes itself", "427, 448",
     "Early states were \"more aspirational than operational\" yet \"presumptive of an integrated sovereign authority\" (Richardson 2012, 4). Kings co-opted local powers they could not erase (Moreno García and Richardson 6)",
     "State violence was \"rare in fact\" (Garfinkle and Richardson 161), which tells against the despot's terror without touching capture presupposing itself",
     "",
     "Keep presupposition as the operation, and drop the imagery of terror"),
    ("Comparison presupposes appropriation", "444",
     "Uruk scribes booked workers \"just as\" herds (Englund 176-77). A stock is rights converging \"upon a single interest\" (Ingold 553)",
     "Sabi Abyad's many seals recorded a store shared \"probably along egalitarian lines\" (Frangipane 2018, 83). Indus standard weights turn up where wealth differs little (Green 159)",
     "For Protevi, comparison and appropriation are \"analytically separable\" (RoV 176 n. 3)",
     "Is comparison a measure owned by one party and applied to others? Can a town compare without appropriating?"),
    ("The stock follows capture", "428-29, 440",
     "The order of storage and settled life is \"chicken-and-egg\" (Testart 524), and inequality \"cannot be deduced\" from storage (Ingold 553). Storage is one of four responses to risk (Halstead and O'Shea)",
     "Mayshar and colleagues put appropriability before surplus (2022, 1092), though they locate it in the crop and not in a relation",
     "Sterelny's storage threshold (RoV 98)",
     "What capture does this store reveal?"),
    ("Town and State are two thresholds", "432-34",
     "Indus cities had writing, weights, seals, and metallurgy without palaces (Green 154). Cities served as refuges, with nomadism produced by urban flight (Yoffee 60)",
     "Arslantepe had central institutions without a city (Frangipane 2012). Teotihuacan was founded by displaced people and governed corporately (Manzanilla). Fletcher's settlements have \"an almost indefinable edge\" (xxiii)",
     "",
     "What common measure belongs to the town, as distinct from the State's comparison?"),
    ("Four regimes of violence: struggle, war, crime, policing", "447-48",
     "\"State terror\" came before its use by the State's enemies (Richardson 2016)",
     "Sanction by reputation and exclusion did most of the work in Middle Bronze Age Mesopotamia (Garfinkle and Richardson 161). Old Babylonian law treated flight as theft by whoever helped (Richardson 2023, 19-20)",
     "",
     "Is sanction without violence policing, or a fifth regime?"),
    ("Royal science captures nomad science", "362-68",
     "Rice knowledge was captured along with its bearers, with the task measured by the ditch (Carney 99). Caste and royal investiture separated the forge from kingship (Herbert 26, 138). Even the trials that farmers ran on their own fields were taxed, so as to fund the science that would replace them (Richards 160)",
     "Maroon Science, learned through \"testing and evasion,\" is a science whose object is capture itself (Bilby 4). Tracking reasons by hypothesis and deduction, the epistemology ATP gives royal science (Liebenberg 3)",
     "",
     "Extend nomad science to sciences of evasion, and add the routes of capture ATP lacks: caste, the unit of work, the tax"),
    ("The secret and the cipher", "390",
     "Saramaka history is kept restricted and \"told in fragments,\" with experts \"on a single hand\" (Price, <i>First-Time</i> 7-8, 21)",
     "Ritual knowledge escapes demand sharing (Peterson 868) and founds hierarchy without a State (Myers 220-21). Kromanti ceremonies are performed for tourists (Bilby 14)",
     "",
     "Restricted knowledge both founds hierarchy and shields people against capture. Who holds the measure of access?"),
    ("Smooth space will not save us (Protevi's marronage)", "387, 500; RoV 96-120",
     "The campo negro (\"black countryside\"), a formation \"inside slavery and an alternative to it\" (Gomes 282). Three processes in one swamp (Sayers 105-08)",
     "The treaty of 1739 turned Jamaica's Maroons into an instrument of capture (Campbell 130). Grades of flight were a planters' metric (Thompson 53)",
     "Roberts's <i>Freedom as Marronage</i> (2015) enlarges flight into a general model",
     "The colonial word marronage merges the nomad who holds in place with the migrant who flees. Split it"),
    ("The empires vanish when a war machine \"bears down from without\"", "459",
     "Teotihuacan's center was destroyed by \"a premeditated, highly selective\" action against the seats of power (López Luján et al. 13)",
     "\"What it is that is supposed to be collapsing\" (Cowgill). At Arslantepe, new chiefs ruled by \"managing the conflicts\" (Frangipane 2012, 239). States regenerate by emulation (Schwartz 7)",
     "Tainter's return to \"lower complexity\" is evolutionism run backward",
     "How can the end of a capture be named from somewhere other than the State?"),
    ("History is one with the triumph of States", "393-94",
     "The tribe as the settled archive's prey (Lindner). The 1769 map of a quilombo was drawn by the expedition sent to destroy it (Carney and Rosomoff 85). Trouillot's silences in the making of the archive",
     "Regional survey records \"distributions of artifacts in space,\" not only sites (Dunnell and Dancey 267). A Gini coefficient over house sizes is itself a numbered number (Kohler et al.)",
     "",
     "Work from distributions, not absences. An absence of material is not evidence of refusal"),
]
C_INTRO = ('When Deleuze and Guattari wrote the plateaus, they worked from the anthropology and archaeology of the 1970s. Those fields have not stood still in the decades since. '
           'Some of their findings bear out nomadology\'s claims. Others complicate them, and on a few points they dispute the plateaus outright. '
           'What pattern emerges? On the whole, the plateaus are most convincing when we take them as a theory of operations (the forming of a stock or the grading of a flight). '
           'Yet they are at their weakest when they make claims about origins or about which came first, which is why each row ends on what the record asks of a new nomadology.')
C_FOOT = ('ATP pages refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987), RoV to Protevi\'s <i>Regimes of Violence</i> (2025). Every page number comes from a reading card checked against the text '
          '(<i>notes/working-file/06_reading_cards.md</i>). Empty cells mean that no work read for this project disputes the claim.')

# The literatures since 1980, placed: (literature, examples, standpoint, method, landing, gives, misses)
LITS = [
    ("Maroon history and archaeology after 1979", "Gomes, Diouf, Sayers, Weik, Casimir, Bilby, Price's <i>First-Time</i>, Carney and Rosomoff", "Marronage, with capture around it", "Social history, historical archaeology, ethnography under restriction", "fits",
     "A positive account of the outside, in which holding in place counts as much as departure", "Rarely compared with other formations"),
    ("Hunter-gatherer ethnography of sharing and storage", "Woodburn, Peterson, Myers, Ingold 1983, Testart's reply", "Warding off, described in operation", "Ethnography", "another process",
     "Equality asserted, the stock as a relation, knowledge as the stock that warding off does not level", ""),
    ("Indigenous and captured sciences", "Richards, Carney, Herbert, Gladwin, Detienne and Vernant", "Nomad science and its capture", "Field research, history", "fits",
     "Capture by caste, by the unit of work, by the tax, and knowledge that exists only in operation", ""),
    ("Mesopotamian economic history", "Richardson, Garfinkle and Richardson, Steinkeller, Hudson and Van De Mieroop, Englund, Moreno García", "Capture, set against the record's view of itself", "Philology, economic history", "another process",
     "The presumptive State, the uncounted, people booked like herds, violence mostly represented", "Little about life outside the archive"),
    ("Egalitarian urbanism and recording", "Green on the Indus, Frangipane on Sabi Abyad and Arslantepe, Manzanilla on Teotihuacan, Yoffee, Fletcher", "The town, and capture without a city", "Site archaeology, synthesis", "another process",
     "Towns and recording without the State, collapse as redistribution", "The town's own measures, not yet theorized"),
    ("The planters' metric", "Thompson, Campbell", "Capture through and inside marronage", "History", "another process",
     "Grades of flight as a numbered number, the treaty as capture by pact", ""),
    ("Steppe revisionism", "Sneath, Munkh-Erdene, Humphrey and Sneath, Lindner, Frachetti", "Mostly capture (aristocratic order, nomadic statehood), Lindner the war machine", "History, historical anthropology", "material",
     "The decimal institution, with muster set against assessment. The disagreement about concepts is real", "Defines nomadism by movement, which ATP refuses"),
    ("Stage evolutionism, neo-evolutionism, cliodynamics", "Service, Fried, Flannery 1972, Turchin's Seshat, Tainter", "Capture", "Coded variables, types, sequences", "bad fit", "Data only", "Stages, seen from the State"),
    ("Comparative early state, heterarchy, dual processes", "Claessen and Skalník, Khazanov, Blanton, Crumley", "Capture", "Types, interpretive comparison", "drift", "", "Stages and typologies return, and no exteriority"),
    ("Anarchist archaeology and the voluntarist synthesis", "Angelbeck and Grier, Borck and Sanger, Graeber and Wengrow", "Warding off", "Voluntarist", "drift", "", "Prevention without anticipation, choice in place of process"),
    ("The ontological turn and multispecies work", "Viveiros de Castro, Descola, Kohn, Tsing", "Thought of the outside, without process", "Comparison of ontologies, patchiness", "drift", "", "Capture disappears, and comparison is given up"),
    ("Assemblage archaeology", "Harris, Fowler, Hamilakis and Jones, Olsen, Witmore", "None: a flat ontology", "Deleuzian vocabulary by way of DeLanda", "drift", "", "No State-form, no nomad science"),
    ("Mobility science", "Ancient DNA and isotopes (Kristiansen), Demoule's critique", "Movement as population replacement", "Genetics, isotopes", "drift", "Demoule, by contrast, is convergent: the steppe invasion as an artifact of the family tree", "Measures migration, not nomadism"),
]
REL = {
    "Maroon history and archaeology after 1979": (1, "Convergent"),
    "Hunter-gatherer ethnography of sharing and storage": (2, "Complementary on warding off"),
    "Indigenous and captured sciences": (1, "Convergent, in part"),
    "Mesopotamian economic history": (2, "Complementary on capture"),
    "Egalitarian urbanism and recording": (2, "Complementary on the town"),
    "The planters' metric": (2, "Complementary on capture"),
    "Steppe revisionism": (3, "Source of evidence"),
    "Stage evolutionism, neo-evolutionism, cliodynamics": (5, "Antithetical"),
    "Comparative early state, heterarchy, dual processes": (4, "Nominal affinity"),
    "Anarchist archaeology and the voluntarist synthesis": (4, "Nominal affinity"),
    "The ontological turn and multispecies work": (4, "Nominal affinity"),
    "Assemblage archaeology": (4, "Nominal affinity"),
    "Mobility science": (4, "Nominal affinity"),
}
SCALE = [(1, "convergent: works the way nomadology does"), (2, "complementary: a sound account of one process, such as capture"), (3, "source of evidence, with the frame set aside"), (4, "nominal affinity: shares the vocabulary, not the method"), (5, "antithetical")]

LAND = {"fits": "f", "another process": "op", "material": "m", "bad fit": "b", "drift": "af"}
LABEL = {"fits": "works as nomadology does", "another process": "sound on another process", "material": "data only", "drift": "same words, other method", "bad fit": "at odds"}
L_INTRO = ('After stage theory fell out of favor, no whole school in these fields has worked the way nomadology does. '
           'Rather, several smaller areas of research have done so in part, and it is these that we place here. '
           'For each area, the table gives what it studies (which of the five processes it examines, capture for instance) along with its way of working, as some areas follow their material while others impose a model on it. '
           'Its relation to nomadology then appears on a single scale, from nearest to farthest, with each judgment made about a work rather than about its author.')
SCALE_KEY = '<div class="scale">' + "".join(f'<span class="rel{n}"><i class="dot"></i>{s}</span>' for n, s in SCALE) + '</div>'

# Neighboring fields: (field, works, relation)
NEAR = [
    ("History of science and craft", "Pamela Smith, <i>The Body of the Artisan</i> (2004). Detienne and Vernant, <i>Cunning Intelligence</i> (1974). Richards, <i>Indigenous Agricultural Revolution</i> (1985)",
     "Craft knowledge outside the State's division of labor, and mētis (\"cunning intelligence\"), a knowledge that exists only in operation. Candidates for minor science"),
    ("Navigation and tracking", "Gladwin, <i>East Is a Big Bird</i> (1970). Liebenberg, <i>The Art of Tracking</i> (1990). The Shadow Wolves",
     "The Puluwat navigator's vessel holds a place while the world passes (Gladwin 181-83), a local absolute. Once a border agency enlists them, trackers put following in the State's service"),
    ("Prediction and platform labor", "Breiman, \"Statistical Modeling: The Two Cultures\" (2001). Gray and Suri, <i>Ghost Work</i> (2019). Agre, \"Surveillance and Capture\" (1994). Galison on Wiener (1994)",
     "The axiomatic predicting without a model of the process, a \"last mile\" of human tasks that moves with each capture (Gray and Suri xxii), and capture as the reorganization of activity for tracking"),
    ("Military theory", "Brossollet, <i>Essai sur la non-bataille</i> (\"Essay on the Nonbattle,\" 1975). Noyer, \"De la notion de guérilla à la notion de techno-guérilla\" (\"From Guerrilla to Techno-Guerrilla,\" 1990). Lawrence",
     "Brossollet is D&G's own source for the nonbattle and the \"unspecified enemy.\" Noyer shows a State army taking up guerrilla technique. Theorists of the Israeli army have used ATP too (Weizman), which shows how far its vocabulary travels"),
    ("Political economy of the ancient world", "Hudson and Van De Mieroop, <i>Debt and Economic Renewal</i> (2002). Meillassoux, <i>The Anthropology of Slavery</i> (1986). Kohler et al. (2017)",
     "Clean slates that keep dependents dependent on the palace, the sale that confirms a depersonalization already inflicted (capture presupposing itself), and wealth disparities measured as a numbered number"),
    ("Political theory of the State and its outside", "Scott, <i>The Art of Not Being Governed</i> (2009). Simpson and Coulthard on Indigenous refusal. Moten and Harney",
     "Scott's legibility is a sound account of comparison, though his hill peoples are known only through flight. Refusal against settler capture is a sound account of warding off. Fugitivity as ontology flattens geography and capture"),
    ("Archive and history", "Trouillot, <i>Silencing the Past</i> (1995). Stoler. Fuentes. Lindner, \"What Was a Nomadic Tribe?\" (1982)",
     "The archive as made by capture, with a history of what it silenced. Trouillot's new State that killed the leader and took his name for its palace"),
    ("Scholarship on nomadology itself", "See the next page", "The field in which a new nomadology works, set out by strand"),
    ("The crossover canon", "Braidotti's nomadic subject, Tsing, Scott, Graeber and Wengrow",
     "Where adopters of nomadology usually turn instead of doing the disciplinary research the plateaus did. The project keeps these out of its argument by rule, citing them only as cautionary examples"),
]
N_INTRO = ('Nomadology is not confined to the fields it engages most often, which here are anthropology and archaeology, with history beside them. '
           'In their notes, Deleuze and Guattari also draw on mathematics, military theory, political economy and the history of science (Archimedes, Clausewitz, Marx, Husserl), and so must a new nomadology. '
           'Listed below are the neighboring fields that our reading has touched so far, each with what it offers a new nomadology.')

# Scholarship on nomadology, by strand: (strand, [(work, what it does)])
# Titles and dates from general knowledge, not yet checked against copies held by the project (except Protevi and Culp).
SCHOLARSHIP = [
    ("Guides and systematic readings", [
        ("Massumi, <i>A User's Guide to Capitalism and Schizophrenia</i> (1992)", "A guide to both volumes by the translator of <i>A Thousand Plateaus</i>"),
        ("Holland, <i>Deleuze and Guattari's A Thousand Plateaus: A Reader's Guide</i> (2013)", "A plateau-by-plateau guide"),
        ("Bonta and Protevi, <i>Deleuze and Geophilosophy</i> (2004)", "A guide and glossary that takes smooth space toward complexity theory"),
        ("Lampert, <i>Deleuze and Guattari's Philosophy of History</i> (2006)", "Coexistence and simultaneity against succession"),
    ]),
    ("The State, capitalism, and Marx", [
        ("Sibertin-Blanc, <i>State and Politics: Deleuze and Guattari on Marx</i> (2016)", "The two plateaus as a theory of the State and of violence, with a limit for each process"),
        ("Thoburn, <i>Deleuze, Marx and Politics</i> (2003)", "Minor politics and the refusal of work"),
        ("Holland, <i>Nomad Citizenship</i> (2011)", "Markets without capitalism, and a citizenship of the nomadic"),
        ("Lazzarato, <i>Signs and Machines</i> (2014)", "Machinic enslavement and social subjection in today's capitalism"),
        ("Hardt and Negri, <i>Empire</i> (2000)", "Desertion and exodus of a nomadic multitude, closer to the migrant than the nomad"),
    ]),
    ("War, technology, and the military", [
        ("DeLanda, <i>War in the Age of Intelligent Machines</i> (1991)", "Military history along the machinic phylum"),
        ("Alliez and Lazzarato, <i>Wars and Capital</i> (2016)", "The war machine and capital, with wars waged against populations"),
        ("Weizman, \"Lethal Theory\" (2006), <i>Hollow Land</i> (2007)", "How theorists in the Israeli army used <i>A Thousand Plateaus</i> to move through walls"),
    ]),
    ("Political theory and anarchism", [
        ("Patton, <i>Deleuze and the Political</i> (2000)", "Capture and the war machine as concepts of political philosophy"),
        ("Nail, <i>Returning to Revolution</i> (2012), <i>Theory of the Border</i> (2016)", "Nomadology and the Zapatistas, then a theory of borders and movement"),
        ("Colson, <i>Petit lexique philosophique de l'anarchisme</i> (\"A Short Philosophical Lexicon of Anarchism,\" 2001)", "Deleuze and Guattari among the anarchists"),
        ("Culp, <i>Dark Deleuze</i> (2016)", "A darker Deleuze of the outside, against the joyous reading"),
    ]),
    ("Space and geography", [
        ("Antonioli, <i>Géophilosophie de Deleuze et Guattari</i> (\"Deleuze and Guattari's Geophilosophy,\" 2003)", "Territory, the earth, and geophilosophy"),
        ("Saldanha, <i>Space After Deleuze</i> (2017)", "Space and race after Deleuze"),
    ]),
    ("Critiques of nomadology's anthropology", [
        ("Miller, \"The Postidentitarian Predicament in the Footnotes of <i>A Thousand Plateaus</i>\" (1993)", "Traces the plateaus' nomads to the colonial anthropology in their notes, and questions the authority it lends them"),
        ("Kaplan, <i>Questions of Travel</i> (1996)", "The nomad as a romantic figure of theory, at the expense of actual displacement"),
        ("Braidotti, <i>Nomadic Subjects</i> (1994)", "Turns the nomad into a figure of subjectivity, the most widely adopted use of the word"),
    ]),
    ("Back into the partner fields", [
        ("Protevi, <i>Political Affect</i> (2009), <i>Edges of the State</i> (2019), <i>Regimes of Violence</i> (2025)", "The furthest return to anthropology and archaeology, adding a becoming-maroon"),
        ("Badaire", "Deleuze and Guattari's critical uses of the social sciences (title to add)"),
    ]),
]
S_INTRO = ('Nomadology has a scholarship of its own, which runs from the first guides to the plateaus to recent work that takes them back into their partner fields. '
           'Such strands are a beginning and not a census. Jo will add to them. Except for Protevi and Culp, titles and dates are listed from memory and still need to be checked against copies.')


def scholarship_table():
    out = ['<table class="sc"><colgroup><col class="s1"><col class="s2"><col></colgroup><thead><tr><th>Strand</th><th>Work</th><th>What it does with nomadology</th></tr></thead><tbody>']
    for strand, items in SCHOLARSHIP:
        for k, (w, d) in enumerate(items):
            th = f'<th rowspan="{len(items)}">{strand}</th>' if k == 0 else ""
            out.append(f'<tr class="{"row" if k == 0 else "sub"}">{th}<td>{fmt(w)}</td><td>{fmt(d)}</td></tr>')
    out.append("</tbody></table>")
    return "".join(out)


CSS = """
td.bo { background: var(--pair-soft); }
td.co { background: var(--split); }
td.di { background: var(--ext-soft); }
td.as { font-weight: 600; }
td.lo { color: var(--muted); font-style: italic; }
.land { white-space: normal; display: inline-block; }
table.ca tbody th small, table.li tbody th small { display: block; font-weight: 500; color: var(--muted); }
.land { font-family: var(--label); font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; font-size: 0.85em; padding: 0 3px; border: 1px solid; display: inline-block; line-height: 1.2; }
.land.f { color: var(--pair); border-color: var(--pair); background: var(--pair-soft); }
.land.op { color: var(--pair); border-color: var(--pair); }
.land.m { color: var(--muted); border-color: var(--muted); }
.land.af { color: var(--ext); border-color: var(--ext); border-style: dashed; background: var(--ext-soft); }
.land.b { color: var(--fg); border-color: var(--fg); background: var(--split); }
table.nf td.rel { color: var(--fg); }
.dot { display: inline-block; width: 0.75em; height: 0.75em; border-radius: 50%; margin-right: 0.4em; vertical-align: -0.05em; border: 1.5px solid var(--pair); }
.rel1 .dot { background: var(--pair); }
.rel2 .dot { background: var(--pair-soft); }
.rel3 .dot { border-color: var(--muted); background: var(--split); }
.rel4 .dot { border-color: var(--ext); border-style: dashed; background: var(--ext-soft); }
.rel5 .dot { border-color: var(--fg); background: var(--fg); }
td.rel1, td.rel2, td.rel3, td.rel4, td.rel5 { font-family: var(--label); font-weight: 500; }
.scale { display: flex; flex-wrap: wrap; gap: 4px 16px; font-family: var(--label); color: var(--muted); margin: 2px 0 8px; }
table.sc tr.sub td { border-top: 0.5px dotted var(--rule); }
"""
PCSS = """
.ca1 h1, .li1 h1, .nf1 h1 { font-size: 13pt; } .ca1 .intro, .li1 .intro, .nf1 .intro { font-size: 7pt; }
.ca1 table { font-size: 6.75pt; line-height: 1.15; }
.ca1 col.c1 { width: 1.25in; } .ca1 col.c5 { width: 1.55in; }
.ca1 th, .ca1 td { padding: 2.6pt 3.8pt; }
.ca1 thead th { font-size: 8pt; } .ca1 tbody th { font-size: 7pt; } .ca1 tbody th small { font-size: 5.8pt; }
.li1 table { font-size: 6.6pt; line-height: 1.15; }
.li1 col.l1 { width: 1.3in; } .li1 col.l2 { width: 1.6in; } .li1 col.l3 { width: 1.15in; } .li1 col.l4 { width: 1.05in; } .li1 col.l5 { width: 0.95in; } .li1 col.l7 { width: 1.5in; }
.li1 th, .li1 td { padding: 2.4pt 3.6pt; } .li1 thead th { font-size: 7.8pt; } .li1 tbody th { font-size: 6.8pt; }
.nf1 table { font-size: 7.3pt; line-height: 1.18; }
.nf1 col.n1 { width: 1.45in; } .nf1 col.n2 { width: 3.6in; }
.nf1 th, .nf1 td { padding: 3.2pt 4.5pt; } .nf1 thead th { font-size: 8.2pt; } .nf1 tbody th { font-size: 7.3pt; }
.land { border-width: 0.6pt; }
.li1 .scale { font-size: 6.8pt; margin: 0; } .dot { border-width: 0.8pt; }
.sc1 h1 { font-size: 13pt; } .sc1 .intro { font-size: 7pt; }
.sc1 table { font-size: 7.2pt; line-height: 1.16; } .sc1 col.s1 { width: 1.5in; } .sc1 col.s2 { width: 4.2in; }
.sc1 th, .sc1 td { padding: 2.4pt 4.5pt; } .sc1 thead th { font-size: 8.2pt; } .sc1 tbody th { font-size: 7.2pt; }
"""


def claims_table(rows):
    out = ['<table class="ca"><colgroup><col class="c1"><col><col><col><col class="c5"></colgroup><thead><tr>'
           '<th>Claim</th><th>The record bears it out</th><th>The record complicates it</th><th>The record disputes it</th><th>What it asks of a new nomadology</th></tr></thead><tbody>']
    for claim, pp, bo, co, di, asks in rows:
        out.append(f'<tr class="row"><th>{fmt(claim)}<small>{pp}</small></th><td class="bo">{fmt(bo)}</td><td class="co">{fmt(co)}</td>'
                   f'<td class="di">{fmt(di) if di else "·"}</td><td class="as">{fmt(asks)}</td></tr>')
    out.append("</tbody></table>")
    return "".join(out)


def lits_table():
    out = ['<table class="li"><colgroup><col class="l1"><col class="l2"><col class="l3"><col class="l4"><col class="l5"><col><col class="l7"></colgroup><thead><tr>'
           '<th>Area of research</th><th>Representative works</th><th>What it studies</th><th>How it works</th><th>Relation to nomadology</th><th>What to take from it</th><th>What it leaves out</th></tr></thead><tbody>']
    for lit, ex, sees, meth, land, gives, misses in LITS:
        out.append(f'<tr class="row"><th>{fmt(lit)}</th><td>{fmt(ex)}</td><td>{fmt(sees)}</td><td>{fmt(meth)}</td>'
                   f'<td class="rel{REL[lit][0]}"><i class="dot"></i>{REL[lit][1]}</td><td>{fmt(gives) or "·"}</td><td class="lo">{fmt(misses) or "·"}</td></tr>')
    out.append("</tbody></table>")
    return "".join(out)


def near_table():
    out = ['<table class="nf"><colgroup><col class="n1"><col class="n2"><col></colgroup><thead><tr><th>Field</th><th>Works</th><th>What it offers nomadology</th></tr></thead><tbody>']
    for f, w, r in NEAR:
        out.append(f'<tr class="row"><th>{f}</th><td>{fmt(w)}</td><td class="rel">{fmt(r)}</td></tr>')
    out.append("</tbody></table>")
    return "".join(out)


def page(cls, title, side, intro, body, foot):
    return f'<section class="sheet {cls}"><div class="top"><h1>{title}</h1><span class="side">{side}</span></div><p class="intro">{intro}</p>{body}<div class="foot">{foot}</div></section>'


def main():
    half = 7
    pages = [
        page("ca1", "After 1980: what the record does to nomadology's claims", "After 1980 · 1", C_INTRO, claims_table(CLAIMS[:half]), C_FOOT),
        page("ca1", "After 1980, continued", "After 1980 · 2", "Claims 8-14, from the town to the archive.", claims_table(CLAIMS[half:]), C_FOOT),
        page("li1", "The literatures since 1980, placed", "After 1980 · 3", L_INTRO, SCALE_KEY + lits_table(), "Placements from the project's source assessment (<i>work/assessment/source_assessment_v2.md</i>), which Jo may revise."),
        page("nf1", "Neighboring fields", "After 1980 · 4", N_INTRO, near_table(), C_FOOT),
        page("sc1", "Scholarship on nomadology", "After 1980 · 5", S_INTRO, scholarship_table(), "Titles from memory, to be checked against copies (Protevi and Culp excepted)."),
    ]
    save("after1980_handout.html", f'<!doctype html><html><head><meta charset="utf-8"><title>After 1980</title>{g.FONTS}'
         f'<style>{g.TOKENS}{g.SHARED}{g.PRINT}{CSS}{PCSS}</style></head><body>{"".join(pages)}</body></html>')
    web = (f'<meta charset="utf-8"><title>After 1980</title>{g.FONTS}'
           f'<style>{g.TOKENS}{g.DARK}{g.SHARED}{g.WEB}{CSS}.wrap table {{ min-width: 1100px; }} h2.sec {{ font-family: var(--label); font-size: 1.15rem; margin: 30px 0 6px; }} p.secp {{ margin: 0 0 12px; color: var(--muted); max-width: 78ch; }}</style>'
           f'<header><h1>After 1980: what the record does to nomadology\'s claims</h1><p>{C_INTRO}</p></header><div class="wrap">{claims_table(CLAIMS)}</div>'
           f'<h2 class="sec">The literatures since 1980, placed</h2><p class="secp">{L_INTRO}</p>{SCALE_KEY}<div class="wrap">{lits_table()}</div>'
           f'<h2 class="sec">Neighboring fields</h2><p class="secp">{N_INTRO}</p><div class="wrap">{near_table()}</div>'
           f'<h2 class="sec">Scholarship on nomadology</h2><p class="secp">{S_INTRO}</p><div class="wrap">{scholarship_table()}</div><footer><p>{C_FOOT}</p></footer>{g.STICKY}')
    save("after1980.html", web)
    parts = [C_INTRO, L_INTRO, N_INTRO] + [x for c in CLAIMS for x in c[2:] if x] + [x for l in LITS for x in (l[5], l[6]) if x] + [r for _, _, r in NEAR] + [S_INTRO] + [d for _, it in SCHOLARSHIP for _, d in it]
    t = "\n\n".join(parts)
    for a, b in (("**", ""), ("[[", "("), ("]]", ")"), ("<i>", "*"), ("</i>", "*"), ("<b>", ""), ("</b>", "")):
        t = t.replace(a, b)
    open(os.path.join(HERE, "after1980_text.md"), "w").write(t + "\n")
    print(f"wrote after1980 ({len(CLAIMS)} claims, {len(LITS)} literatures, {len(NEAR)} neighboring fields)")


if __name__ == "__main__":
    main()
