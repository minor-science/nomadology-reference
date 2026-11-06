"""Build the reference packet: one PDF of every handout, in the order of the web index.

  nomadology_reference_packet.pdf

Cover, guide and contents first, then the eight handouts, then a page about the project.
Each handout starts on a right-hand page (blank pages are added after sheets with an odd
number of pages), packet page numbers are stamped in the outer bottom corner, and the PDF
gets bookmarks for every sheet.

Run after the handout PDFs are regenerated and before seo.py (which sets the PDF Author):
  ../.venv/bin/python build_packet.py
Needs pypdf (in ../.venv) and Google Chrome.
"""
import datetime
import html
import io
import os
import subprocess
import tempfile

from pypdf import PdfReader, PdfWriter, PageObject

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = os.path.join(HERE, "nomadology_reference_packet.pdf")
W, H = 792, 612  # letter landscape, in points, as every handout
URL = "https://minor-science.github.io/nomadology-reference/"
TPS = "https://www.instagram.com/thepublicschoolla/"
BYLINE = "Andrew Culp and the A Thousand Plateaus research group of The Public School Los Angeles"

# (numeral, title, handout, what it gives), in the order of index.html
SHEETS = [
    ("I", "Where the name nomadology came from, and what else it could be called", "name_handout.pdf",
     "How Deleuze and Guattari built the word, from the Greek root <i>nem-</i> and Leibniz's <i>Monadology</i>, with names already in use and new ones to weigh"),
    ("II", "Plateaus 12 and 13, entry by entry", "plateaus_beat_sheet.pdf",
     "Every axiom, proposition and problem of the two plateaus by page. The web version can be searched and shows the quotations"),
    ("III", "The five machinic processes", "five_processes_handout.pdf",
     "Warding off, the war machine, capture, polarization and encompassment in coexistence (430-37), with Protevi's marronage on the web"),
    ("IV", "Royal science and nomad science", "sciences_handout.pdf",
     "The two sciences and their shifting borderline (361-74). On the back, questions the partner fields ask from the side of the State, turned into questions for a nomadology"),
    ("V", "The State's three forms", "state_forms_handout.pdf",
     "From the archaic imperial State to the modern nation-States, question by question (459)"),
    ("VI", "Nomadology concepts: where they came from and how they were taken up", "concordance_handout.pdf",
     "Each concept in plain words, with the field it began in, where it was worked out before 1980, and how it has been taken up since"),
    ("VII", "After 1980: what later research says about nomadology", "after1980_handout.pdf",
     "Claim by claim, the research since the plateaus that bears them out, complicates them or disputes them"),
    ("VIII", "Nomadology bibliography", "library_handout.pdf",
     "The works cited in the notes to the two plateaus (552-71), by field, with what each contributed"),
]

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;'
         '0,8..60,600;1,8..60,400&family=IBM+Plex+Sans+Condensed:wght@500;600&display=swap">')
CSS = """
@page { size: letter landscape; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #fff; color: #1D2224; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font: 400 10pt/1.42 "Source Serif 4", Georgia, serif; }
.pg { width: 11in; height: 8.5in; padding: 0.6in 0.75in; page-break-after: always; position: relative; overflow: hidden; }
.pg:last-child { page-break-after: auto; }
.lab { font: 600 7.5pt/1.3 "IBM Plex Sans Condensed", Arial Narrow, sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #5B6468; }
a { color: inherit; }
/* cover */
.cover { display: flex; flex-direction: column; justify-content: space-between; border-left: 10pt solid #1F6B66; }
.cover h1 { margin: 0.9in 0 0; font: 600 76pt/.86 "IBM Plex Sans Condensed", Arial Narrow, sans-serif; text-transform: uppercase; letter-spacing: -.01em; }
.cover .sub { margin: 16pt 0 0; font-size: 20pt; line-height: 1.25; max-width: 7.6in; }
.cover .plat { margin: 10pt 0 0; font-size: 12pt; color: #5B6468; }
.cover .by { font-size: 12pt; max-width: 9in; }
.cover .meta { margin-top: 8pt; }
/* guide */
.guide { display: grid; grid-template-columns: 1fr 1fr; column-gap: 0.45in; }
.guide h2 { margin: 0 0 6pt; font: 600 15pt/1.2 "IBM Plex Sans Condensed", Arial Narrow, sans-serif; }
.guide h3 { margin: 10pt 0 3pt; }
.guide p { margin: 0 0 6pt; }
.guide ul { margin: 0 0 4pt; padding-left: 12pt; }
.guide li { margin: 0 0 3pt; }
ol.toc { list-style: none; margin: 0; padding: 0; }
ol.toc li { display: grid; grid-template-columns: 0.42in 1fr 0.35in; column-gap: 6pt; padding: 4.5pt 0; border-top: 0.6pt solid #D5D9D6; }
ol.toc .n { font: 600 12pt/1.1 "IBM Plex Sans Condensed", sans-serif; text-align: right; }
ol.toc .t { font-weight: 600; }
ol.toc .d { display: block; font-weight: 400; font-size: 8.6pt; line-height: 1.32; color: #3b4447; margin-top: 1pt; }
ol.toc .p { text-align: right; font: 500 10pt/1.2 "IBM Plex Sans Condensed", sans-serif; }
/* about */
.about { display: grid; grid-template-columns: 1fr 1fr; column-gap: 0.45in; }
.about h2 { margin: 0 0 6pt; font: 600 15pt/1.2 "IBM Plex Sans Condensed", Arial Narrow, sans-serif; }
.about h3 { margin: 12pt 0 3pt; }
.about p { margin: 0 0 6pt; }
.ask { font-size: 12pt; line-height: 1.35; font-style: italic; }
dl { margin: 0; } dt { margin-top: 6pt; } dd { margin: 0; }
"""


def chrome_pdf(body, path):
    doc = f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>'
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(doc)
        src = f.name
    try:
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                        f"--print-to-pdf={path}", "file://" + src], check=True, capture_output=True)
    finally:
        os.unlink(src)


def front(date, starts):
    rows = "".join(f'<li><span class="n">{n}</span><span class="t">{html.escape(t)}<span class="d">{d}</span></span>'
                   f'<span class="p">{starts[n]}</span></li>' for n, t, _, d in SHEETS)
    cover = f"""<section class="pg cover"><div>
<p class="lab">Minor science</p>
<h1>Nomadology<br>reference</h1>
<p class="sub">Reference sheets for <i>A Thousand Plateaus</i>, plateaus 12 and 13</p>
<p class="plat">"1227: Treatise on Nomadology&#8212;The War Machine" and "7000 B.C.: Apparatus of Capture"</p></div>
<div><p class="by">By Andrew Culp and the <i>A Thousand Plateaus</i> research group of The Public School Los Angeles</p>
<p class="lab meta">Packet of {date} &#183; current versions at minor-science.github.io/nomadology-reference</p></div></section>"""
    guide = f"""<section class="pg guide"><div>
<h2>How to use this packet</h2>
<p>These are working references for the two plateaus in which Deleuze and Guattari set out nomadology. They were made while writing a response to John Protevi's <i>Regimes of Violence: Toward a Political Anthropology</i> (Minnesota, 2025). Each sheet stands on its own, and each has a web version at the address on the cover, often with more detail.</p>
<p>The sheets run in the order of the web index. The name comes first, then the two plateaus entry by entry, then four sheets of concepts, and last two sheets of sources.</p>
<h3 class="lab">Reading a sheet</h3>
<ul>
<li>Page numbers without a prefix refer to Brian Massumi's translation (Minnesota, 1987). <i>Mille plateaux</i> (Minuit, 1980) is cited where the French wording counts, and RoV marks Protevi's book.</li>
<li>Bold type marks the two terms of a contrast.</li>
<li>Dashed cells are proposed extensions, not claims made in <i>A Thousand Plateaus</i>.</li>
<li>Markers such as R1 point to findings from the record, spelled out on the sheet's notes page.</li>
</ul>
<h3 class="lab">How the sheets connect</h3>
<p>The five machinic processes (III) and the two sciences (IV) are companions, the first for the plateaus' social formations and the second for their kinds of knowledge. The State's three forms (V) takes one proposition of capture in detail. After 1980 (VII) tests the plateaus' claims against later research, while the concordance (VI) and the bibliography (VIII) follow the concepts and the works cited back to their sources.</p>
<h3 class="lab">Printing</h3>
<p>Print on both sides and flip on the short edge. Each sheet begins on a right-hand page, so a few pages are left blank.</p>
</div><div><h2>Contents</h2><ol class="toc">{rows}</ol></div></section>"""
    return cover + guide


def about(date):
    return f"""<section class="pg about"><div>
<h2>About</h2>
<p>The sheets are by Andrew Culp (California Institute of the Arts) and the <i>A Thousand Plateaus</i> research group of The Public School Los Angeles (<a href="{TPS}">instagram.com/thepublicschoolla</a>), a weekly reading group begun in 2024 that works through the plateau line by line. Its question:</p>
<p class="ask">What do we still have to learn from the Treatise on Nomadology after devastating decades of neoliberal austerity and reactionary neofascisms?</p>
<p>It reads with two aims in particular, a philosophical definition of the State, including state thought, and new paths for the war machine.</p>
<h3 class="lab">To cite this packet</h3>
<p>{BYLINE}. <i>Nomadology Reference: Reference Sheets for A Thousand Plateaus, Plateaus 12 and 13</i>. Packet of {date}. {URL}</p>
</div><div>
<h3 class="lab" style="margin-top:0">Companions on the web</h3>
<dl>
<dt><b>Minor science</b></dt><dd>All the projects. minor-science.github.io</dd>
<dt><b>Nomadology visualizer</b></dt><dd>Simulations that set capture, warding off and the war machine in motion in four materials. nomad-viz.vercel.app</dd>
<dt><b><i>A Thousand Plateaus</i> reader</b></dt><dd>The French and Massumi's English, sentence by sentence. minor-science.github.io/thousand-plateaus-reader</dd>
<dt><b>Source files</b></dt><dd>github.com/minor-science/nomadology-reference</dd>
</dl>
<h3 class="lab">Still to come</h3>
<p>A short account of nomadology: a short essay on what the two plateaus argue, as a study of how the State converts what lies outside it.</p>
</div></section>"""


def numbers(total, skip):
    """A PDF of page numbers, one per packet page, in the outer bottom corner."""
    pages = []
    for i in range(1, total + 1):
        side = "right" if i % 2 else "left"
        txt = "" if i in skip else str(i)
        pages.append(f'<section class="pg" style="padding:0"><span style="position:absolute;bottom:0.07in;{side}:0.32in;'
                     f'font:500 6.5pt/1 \'IBM Plex Sans Condensed\',sans-serif;color:#5B6468">{txt}</span></section>')
    path = os.path.join(tempfile.mkdtemp(), "numbers.pdf")
    clear = "<style>html,body{background:transparent!important;-webkit-print-color-adjust:economy;print-color-adjust:economy}</style>"
    chrome_pdf(clear + "".join(pages), path)
    return path


def main():
    date = datetime.date.today().strftime("%B %Y")
    readers = {f: PdfReader(os.path.join(HERE, f)) for _, _, f, _ in SHEETS}
    # lay out the pages: cover 1, guide 2, then each sheet from a right-hand (odd) page
    plan, starts, page = [], {}, 3
    for n, t, f, _ in SHEETS:
        starts[n] = page
        k = len(readers[f].pages)
        plan.append((n, t, f, k))
        page += k + (k % 2)
    about_page = page
    total = about_page + 1  # the about page, then a blank back
    tmp = tempfile.mkdtemp()
    fm, bm = os.path.join(tmp, "front.pdf"), os.path.join(tmp, "about.pdf")
    chrome_pdf(front(date, starts), fm)
    chrome_pdf(about(date), bm)
    w = PdfWriter()
    blanks = set()
    for p in PdfReader(fm).pages:
        w.add_page(p)
    marks = []
    for n, t, f, k in plan:
        marks.append((f"{n}. {t}", len(w.pages)))
        for p in readers[f].pages:
            w.add_page(p)
        if k % 2:
            w.add_blank_page(W, H)
            blanks.add(len(w.pages))
    marks.append(("About", len(w.pages)))
    w.add_page(PdfReader(bm).pages[0])
    w.add_blank_page(W, H)
    blanks.add(len(w.pages))
    assert len(w.pages) == total, (len(w.pages), total)
    nums = PdfReader(numbers(total, blanks | {1}))
    for i, p in enumerate(w.pages):
        if (i + 1) not in blanks and i:
            p.merge_page(nums.pages[i])
    w.add_outline_item("Cover", 0)
    w.add_outline_item("How to use this packet; contents", 1)
    for title, idx in marks:
        w.add_outline_item(title, idx)
    w.add_metadata({"/Title": "Nomadology reference: the packet", "/Author": BYLINE,
                    "/Subject": "Reference sheets for A Thousand Plateaus, plateaus 12 and 13"})
    w.page_mode = "/UseOutlines"
    with open(OUT, "wb") as f:
        w.write(f)
    print(f"{OUT}: {total} pages, sheets start at", ", ".join(f"{n} {s}" for n, s in starts.items()))


if __name__ == "__main__":
    main()
