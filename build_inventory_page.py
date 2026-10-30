"""The plateau 12-13 inventory (work/atp_12_13_inventory.md) as a reference:
  plateaus_reference.html          searchable web page: every entry by heading, with filters, plus the by-kind tables
  plateaus_beat_sheet.html / .pdf  print beat sheet: every entry as page and label, in columns, an index to the plateaus
Same family as the five-process sheet (tokens and fonts from build_five_processes.py)."""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_five_processes as g  # noqa: E402

SRC = os.path.join(HERE, "..", "atp_12_13_inventory.md")


# ------------------------------------------------------------------ a small markdown converter

# ------------------------------------------------------------------ background index (work/context/)
import csv as _csv
CTX_TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "context", "context_12_13.tsv")


def md_inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def short_tag(src, loc):
    m = re.search(r"session (\d+)", loc)
    if "ATP-V-79-80" in src and m: return f"Seminar 79-80 s.{m.group(1)}"
    for key, tag in (("ATP-IV", "Seminar 27.2.79"), ("ATP-II", "Seminar 1977"), ("Anti-Oedipus", "Seminar AO 71-72"),
                     ("Painting", "Seminar Painting 1981"), ("dialogues", "Dialogues"), ("guattari-seminars", "Guattari seminar"),
                     ("querrien", "Querrien"), ("recherches13", "Recherches 13"), ("chaosophy", "Chaosophy"), ("soft-subversions", "Guattari"),
                     ("dumezil", "Dumézil"), ("braudel", "Braudel"), ("amin", "Amin"), ("clastres", "Clastres"), ("jevons", "Jevons"),
                     ("kjv", "Numbers"), ("difference_repetition", "Difference and Repetition")):
        if key in src: return tag
    return src.split("/")[-1]


def load_context():
    if not os.path.exists(CTX_TSV):
        return []
    with open(CTX_TSV) as fh:
        rows = list(_csv.DictReader(fh, delimiter="\t"))
    for r in rows:
        r["a"], r["b"] = int(r["atp_first"]), int(r["atp_last"])
        r["html"] = md_inline(r["rendered"])
        r["tag"] = short_tag(r["src"], r["loc"])
    return rows


def attach_context(sections, ctx):
    """Give each headed statement the background entries overlapping its page range."""
    for i, s in enumerate(sections):
        a = int(re.match(r"\d+", s["page"]).group(0))
        nxt = [int(re.match(r"\d+", t["page"]).group(0)) for t in sections[i + 1:] if t["plateau"] == s["plateau"]]
        b = (nxt[0] if nxt else (423 if s["plateau"] == "12" else 473))
        b = max(a, b - 1) if nxt and nxt[0] > a else max(a, b)
        hits = [r for r in ctx if not (r["b"] < a or r["a"] > b)]
        s["ctx"] = [f'<li><span class="ctag">{html.escape(r["tag"])}</span> {r["html"]}</li>' for r in hits]
        s["ctags"] = sorted({r["tag"] for r in hits}, key=lambda t: (not t.startswith("Seminar 79"), t))


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    return s


def blocks(lines):
    """Convert a list of markdown lines (lists, tables, paragraphs) to HTML."""
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.strip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows if not re.match(r"^\|[\s|:-]+\|$", r)]
            head, body = cells[0], cells[1:]
            out.append('<table class="md"><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table>")
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+", ln)
        if m:
            ordered = m.group(2)[0].isdigit()
            base = len(m.group(1))
            items = []
            while i < len(lines):
                mm = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", lines[i])
                if mm and len(mm.group(1)) == base:
                    items.append([mm.group(3)])
                    i += 1
                elif lines[i].strip() and (len(lines[i]) - len(lines[i].lstrip())) > base and items:
                    items[-1].append(lines[i][base + 2:] if len(lines[i]) > base + 2 else lines[i].strip())
                    i += 1
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it[0])}{blocks(it[1:]) if len(it) > 1 else ''}</li>" for it in items) + f"</{tag}>")
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("|") and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "".join(out)


# ------------------------------------------------------------------ parse the inventory
NUMWORDS = r"(?:Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve)"


def kinds(label, body):
    k = []
    lab = label.lower()
    if re.search(r"\bdefin", lab) or body.lstrip().lower().startswith(("definition", '"definition')):
        k.append("definition")
    if re.match(NUMWORDS + r"\b", label) or re.search(r"\b" + NUMWORDS.lower()[3:-1] + r"\b", lab) or "|" in body or re.search(r"^\s*\d+\.\s", body, re.M):
        k.append("list")
    if re.search(r"\band\b|\bagainst\b|, not\b|\bnot\b.*\bbut\b", lab):
        k.append("contrast")
    if "?" in label or re.match(r'^"[^"]*\?"', body.strip()):
        k.append("question")
    return k or ["thesis"]


def parse():
    text = open(SRC).read()
    main, part3 = text.split("# Part 3. The same material by kind", 1)
    entries, sections = [], []
    plateau = sec = sub = None
    cur = None
    for ln in main.split("\n"):
        if ln.startswith("# Part 1."):
            plateau = "12"
            continue
        if ln.startswith("# Part 2."):
            plateau = "13"
            continue
        if plateau is None:
            continue
        mh = re.match(r"^## (Axiom|Proposition|Problem) ([IVX]+) \(([\d-]+)\)\. (.*)$", ln)
        if mh:
            cur = None
            kind, num, pp, stmt = mh.groups()
            sec = f"{kind} {num}"
            sub = None
            sections.append(dict(id=f"s{len(sections)}", plateau=plateau, kind=kind.lower(), num=num, page=pp, statement=stmt.strip('"')))
            continue
        ms = re.match(r"^### (.*)$", ln)
        if ms:
            cur = None
            sub = ms.group(1)
            continue
        me = re.match(r"^- \*\*([\d-]+(?:, [\d-]+)*)\. (.+?)\*\*\s*(.*)$", ln)
        if me:
            pp, label, rest = me.groups()
            cur = dict(plateau=plateau, section=sec, sub=sub, sid=sections[-1]["id"], page=pp, label=label.rstrip("."), lines=[rest] if rest else [])
            entries.append(cur)
            continue
        if cur is not None and (ln.startswith("  ") or ln.startswith("\t")):
            cur["lines"].append(ln[2:])
        elif cur is not None and ln.strip() == "":
            cur["lines"].append("")
        else:
            cur = None
    for e in entries:
        body_md = "\n".join(e.pop("lines")).strip("\n")
        e["kinds"] = kinds(e["label"], body_md)
        e["html"] = blocks(body_md.split("\n")) if body_md else ""
        e["text"] = re.sub(r"<[^>]+>", " ", e["html"])
        e["p0"] = int(re.match(r"\d+", e["page"]).group(0))
        e["label_html"] = inline(e["label"])
    # Part 3: by kind, as sections of HTML
    p3 = []
    for chunk in re.split(r"^## ", part3, flags=re.M)[1:]:
        title, _, body = chunk.partition("\n")
        p3.append(dict(title=title.strip(), html=blocks(body.split("\n"))))
    return sections, entries, p3


# ------------------------------------------------------------------ web page
WEB_CSS = """
body { margin: 0; }
.page { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 0 28px; max-width: 1240px; margin: 0 auto; }
@media (max-width: 860px) { .page { grid-template-columns: minmax(0, 1fr); } nav.toc { position: static; max-height: none; } }
header.top { grid-column: 1 / -1; display: grid; gap: 8px; margin-bottom: 10px; }
header.top h1 { font-size: 1.7rem; margin: 0; }
header.top p { margin: 0; color: var(--muted); max-width: 80ch; }
nav.toc { position: sticky; top: 12px; align-self: start; max-height: calc(100vh - 24px); overflow: auto; font-family: var(--label); font-size: 0.85rem; border-right: 1px solid var(--rule); padding-right: 10px; }
nav.toc h3 { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin: 14px 0 4px; }
nav.toc a { display: block; color: var(--fg); text-decoration: none; padding: 2px 0; }
nav.toc a small { color: var(--muted); }
nav.toc a.problem { color: var(--pair); }
nav.toc a.axiom { font-weight: 600; }
.tools { display: flex; flex-wrap: wrap; gap: 8px 14px; align-items: center; position: sticky; top: 0; background: var(--bg); padding: 10px 0; z-index: 3; border-bottom: 1px solid var(--rule); }
.tools input[type=search] { font: inherit; padding: 6px 10px; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); min-width: 240px; flex: 1; }
.tools input[type=number] { font: inherit; width: 64px; padding: 5px 6px; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { font-family: var(--label); font-size: 0.82rem; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); padding: 3px 9px; cursor: pointer; }
.chip[aria-pressed=true] { background: var(--pair); color: var(--surface); border-color: var(--pair); }
.count { font-family: var(--label); color: var(--muted); font-size: 0.85rem; }
.tabs { display: flex; gap: 0; margin: 12px 0 0; }
.tab { font-family: var(--label); font-size: 0.9rem; border: 1px solid var(--rule); background: var(--surface); color: var(--fg); padding: 6px 14px; cursor: pointer; }
.tab[aria-selected=true] { background: var(--fg); color: var(--bg); }
section.sec { margin: 22px 0 6px; }
section.sec > h2 { font-size: 1.05rem; margin: 0 0 2px; }
section.sec > h2 .k { font-family: var(--label); font-weight: 600; color: var(--pair); margin-right: 6px; }
section.sec > p.stmt { margin: 0 0 8px; color: var(--muted); font-style: italic; }
h4.sub { font-family: var(--label); color: var(--pair); margin: 12px 0 4px; font-size: 0.9rem; }
details.e { border-top: 1px solid var(--rule); padding: 6px 0; }
details.e summary { cursor: pointer; list-style: none; display: grid; grid-template-columns: 70px 1fr auto; gap: 8px; align-items: baseline; }
details.e summary::-webkit-details-marker { display: none; }
details.e summary .pg { font-family: var(--label); color: var(--muted); font-size: 0.85rem; }
details.e summary .lab { font-weight: 600; }
details.e summary .ks { font-family: var(--label); font-size: 0.72rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; white-space: nowrap; }
details.e .body { padding: 4px 0 6px 78px; }
@media (max-width: 600px) { details.e summary { grid-template-columns: 56px 1fr; } details.e summary .ks { display: none; } details.e .body { padding-left: 0; } }
details.e .body p { margin: 4px 0; }
table.md { border-collapse: collapse; width: 100%; margin: 6px 0; font-size: 0.92rem; table-layout: auto; }
table.md th, table.md td { border: 1px solid var(--rule); padding: 4px 7px; text-align: left; vertical-align: top; }
table.md th { font-family: var(--label); background: var(--surface); }
.bykind section { margin: 22px 0; overflow-x: auto; }
.bykind h2 { font-size: 1.1rem; margin: 0 0 6px; }
mark { background: var(--pair-soft); color: inherit; }
footer { grid-column: 1 / -1; margin-top: 28px; color: var(--muted); font-size: 0.88rem; }
.hidden { display: none !important; }
details.ctx { margin: 0 0 10px; border-left: 3px solid var(--pair-soft); padding: 2px 0 2px 10px; }
details.ctx > summary { cursor: pointer; font-family: var(--label); font-size: 0.82rem; color: var(--pair); }
details.ctx ul, .elsewhere ul { margin: 6px 0 4px; padding-left: 18px; }
details.ctx li, .elsewhere li { margin: 0 0 7px; font-size: 0.92rem; }
.ctag { font-family: var(--label); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--muted); margin-right: 4px; }
.elsewhere section { margin: 22px 0; } .elsewhere h2 { font-size: 1.1rem; margin: 0 0 4px; }
.elsewhere p.lead { color: var(--muted); max-width: 80ch; }
code { font-size: 0.85em; }
"""

WEB_JS = r"""
const S = DATA.sections, E = DATA.entries;
const list = document.getElementById('list'), q = document.getElementById('q'), lo = document.getElementById('lo'), hi = document.getElementById('hi');
const cnt = document.getElementById('cnt');
let kindOn = new Set(), plat = 'all';
function esc(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function hl(h, words){ if(!words.length) return h; const re = new RegExp('('+words.map(esc).join('|')+')','gi');
  return h.replace(/(<[^>]+>)|([^<]+)/g,(m,tag,txt)=> tag ? tag : txt.replace(re,'<mark>$1</mark>')); }
function render(){
  const words = q.value.trim().toLowerCase().split(/\s+/).filter(w=>w.length>1);
  const a = parseInt(lo.value)||351, b = parseInt(hi.value)||473;
  let n = 0, out = [];
  for (const s of S){
    const es = E.filter(e => e.sid===s.id && (plat==='all'||e.plateau===plat) && e.p0>=a && e.p0<=b &&
      (!kindOn.size || e.kinds.some(k=>kindOn.has(k))) &&
      words.every(w => (e.label+' '+e.text+' '+e.page).toLowerCase().includes(w)));
    const headMatch = (plat==='all'||s.plateau===plat) && !kindOn.size && words.length && words.every(w => (s.kind+' '+s.num+' '+s.statement).toLowerCase().includes(w));
    const sp = parseInt(s.page), bare = !words.length && !kindOn.size && (plat==='all'||s.plateau===plat) && sp>=a && sp<=b;
    if (!es.length && !headMatch && !bare) continue;
    n += es.length;
    let h = `<section class="sec" id="${s.id}"><h2><span class="k">${s.kind[0].toUpperCase()+s.kind.slice(1)} ${s.num}</span>${s.page}</h2><p class="stmt">${hl(s.statement,words)}</p>`;
    if (s.ctx && s.ctx.length) h += `<details class="ctx"><summary>Elsewhere: ${s.ctx.length} passage${s.ctx.length===1?'':'s'} in the seminars, Guattari, the CERFI, and the sources</summary><ul>${hl(s.ctx.join(''),words)}</ul></details>`;
    let sub = null;
    for (const e of es){
      if (e.sub && e.sub!==sub){ sub = e.sub; h += `<h4 class="sub">${e.sub}</h4>`; }
      const open = words.length && es.length < 25 ? ' open' : '';
      h += `<details class="e"${open}><summary><span class="pg">${e.page}</span><span class="lab">${hl(e.label_html,words)}</span><span class="ks">${e.kinds.join(' · ')}</span></summary><div class="body">${hl(e.html,words)}</div></details>`;
    }
    out.push(h+'</section>');
  }
  list.innerHTML = out.join('') || '<p>No entries match.</p>';
  cnt.textContent = n + (n===1?' entry':' entries');
}
document.querySelectorAll('.chip[data-k]').forEach(c=>c.addEventListener('click',()=>{const k=c.dataset.k;
  if(kindOn.has(k)){kindOn.delete(k);c.setAttribute('aria-pressed','false');}else{kindOn.add(k);c.setAttribute('aria-pressed','true');} render();}));
document.querySelectorAll('.chip[data-p]').forEach(c=>c.addEventListener('click',()=>{plat=c.dataset.p;
  document.querySelectorAll('.chip[data-p]').forEach(x=>x.setAttribute('aria-pressed', x===c?'true':'false')); render();}));
[q,lo,hi].forEach(x=>x.addEventListener('input',render));
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>{
  document.querySelectorAll('.tab').forEach(x=>x.setAttribute('aria-selected', x===t?'true':'false'));
  document.getElementById('beats').classList.toggle('hidden', t.dataset.t!=='beats');
  document.getElementById('bykind').classList.toggle('hidden', t.dataset.t!=='bykind');
  document.getElementById('elsewhere').classList.toggle('hidden', t.dataset.t!=='elsewhere');
  try{localStorage.setItem('inv-tab',t.dataset.t);}catch(e){} }));
try{ const t = localStorage.getItem('inv-tab'); if(t){ const el=document.querySelector('.tab[data-t="'+t+'"]'); if(el) el.click(); } }catch(e){}
render();
"""

INTRO = ('Every axiom, proposition, and problem in the two plateaus of <i>A Thousand Plateaus</i> on nomadology and the State, with every claim, contrast, list, definition, and question under each, by page. '
         'Quotations are verbatim from the Minnesota translation (1987), checked against the text. Search, filter by kind or by page, and open any entry for its quotations. '
         'The second tab regroups the same material by kind: royal and minor science, State and war machine, the three spaces, number, weapons and tools, every list, every definition. '
         'Under each heading, « Elsewhere » opens the passages where the idea is worked out in Deleuze\'s seminars, Guattari, the CERFI, and the sources D&amp;G compress; the third tab lists them all.')


def web(sections, entries, p3, ctx=()):
    toc = []
    for plat, name in (("12", "Plateau 12 · Treatise on Nomadology"), ("13", "Plateau 13 · Apparatus of Capture")):
        toc.append(f"<h3>{name}</h3>")
        for s in sections:
            if s["plateau"] == plat:
                toc.append(f'<a class="{s["kind"]}" href="#{s["id"]}">{s["kind"].title()} {s["num"]} <small>{s["page"]}</small></a>')
    data = json.dumps(dict(sections=[{k: x[k] for k in ("id", "plateau", "kind", "num", "page", "statement", "ctx")} for x in sections], entries=[{k: e[k] for k in ("plateau", "sid", "sub", "page", "p0", "label", "label_html", "html", "text", "kinds")} for e in entries]))
    chips = "".join(f'<button class="chip" data-k="{k}" aria-pressed="false">{lab}</button>' for k, lab in
                    (("definition", "Definitions"), ("list", "Lists"), ("contrast", "Contrasts"), ("question", "Questions"), ("thesis", "Other claims")))
    pchips = "".join(f'<button class="chip" data-p="{p}" aria-pressed="{"true" if p == "all" else "false"}">{lab}</button>' for p, lab in (("all", "Both plateaus"), ("12", "Plateau 12"), ("13", "Plateau 13")))
    bykind = "".join(f'<section><h2>{inline(s["title"])}</h2>{s["html"]}</section>' for s in p3)
    units = [("Plateau 12. Axiom I, Proposition I", 351, 355), ("Problem I, Proposition II: Clastres", 356, 360), ("Proposition III: minor science", 361, 373),
             ("Problem II, Proposition IV: noology", 374, 379), ("Axiom II, Proposition V: space", 380, 386), ("Proposition VI: number", 387, 393),
             ("Proposition VII: affects, weapons, tools", 394, 402), ("Problem III, Proposition VIII, Axiom III: metallurgy", 403, 415),
             ("Proposition IX: war", 416, 423), ("Plateau 13. Proposition X: the State and its poles", 424, 426), ("Proposition XI: which comes first?", 427, 436),
             ("Proposition XII: capture", 437, 447), ("Proposition XIII: the State and its forms", 448, 459), ("Proposition XIV: axiomatics today", 460, 473)]
    els = []
    for t, a, b in units:
        rs = [r for r in ctx if a <= r["a"] <= b]
        if rs:
            els.append(f'<section><h2>{html.escape(t)} <small class="ctag">{a}-{b}</small></h2><ul>' + "".join(f'<li><span class="ctag">{html.escape(r["tag"])}</span> {r["html"]}</li>' for r in rs) + "</ul></section>")
    elsewhere = ('<p class="lead">Where an idea in the two plateaus is developed more fully elsewhere: Deleuze\'s seminars (above all the 1979-80 seminar on the State apparatus and the war machine), Guattari\'s seminars and books, the CERFI\'s work, and the texts D&amp;G compress. '
                 f'{len(ctx)} entries, every quotation checked against the source text. Built from <i>work/context/</i>.</p>' + "".join(els))
    return f'''<meta charset="utf-8"><title>Plateaus 12-13 Reference</title>{g.FONTS}
<style>{g.TOKENS}{g.DARK}
body {{ background: var(--bg); color: var(--fg); font-family: var(--serif); font-size: 15px; line-height: 1.45; padding: 24px max(16px, env(safe-area-inset-right, 0px)) 40px max(16px, env(safe-area-inset-left, 0px)); }}
{WEB_CSS}</style>
<div class="page">
<header class="top"><h1>Plateaus 12 and 13, entry by entry</h1><p>{INTRO}</p>
<div class="tabs"><button class="tab" data-t="beats" aria-selected="true">Entry by entry</button><button class="tab" data-t="bykind" aria-selected="false">By kind</button><button class="tab" data-t="elsewhere" aria-selected="false">Elsewhere</button></div></header>
<nav class="toc">{''.join(toc)}</nav>
<main>
<div id="beats"><div class="tools"><input type="search" id="q" placeholder="Search: nomos, Clastres, 389, threshold ..." aria-label="Search the entries">
<span class="chips">{pchips}</span><span class="chips">{chips}</span>
<label class="count">ATP <input type="number" id="lo" value="351" min="351" max="473"> to <input type="number" id="hi" value="473" min="351" max="473"></label><span class="count" id="cnt"></span></div>
<div id="list"></div></div>
<div id="bykind" class="bykind hidden">{bykind}</div>
<div id="elsewhere" class="elsewhere hidden">{elsewhere}</div>
</main>
<footer>Page numbers refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987). Kinds are assigned from each entry's label and can overlap. Source: <i>work/atp_12_13_inventory.md</i>.</footer>
</div>
<script>const DATA = {data};</script><script>{WEB_JS}</script>'''


# ------------------------------------------------------------------ print beat sheet
PRINT_CSS = """
.bs { columns: 4; column-gap: 10pt; font-size: 5.9pt; line-height: 1.16; }
.bs .h { break-inside: avoid; break-after: avoid; margin: 4pt 0 1.5pt; padding-top: 2pt; border-top: 0.8pt solid var(--pair); }
.bs .h b { font-family: var(--label); color: var(--pair); font-size: 6.6pt; }
.bs .h span { display: block; font-style: italic; color: var(--muted); }
.bs .h .et { display: block; font-family: var(--label); font-style: normal; font-size: 5.4pt; color: var(--pair); }
.bs .sb { font-family: var(--label); font-weight: 600; color: var(--pair); margin: 2pt 0 1pt; }
.bs .r { display: grid; grid-template-columns: 0.42in 1fr; gap: 3pt; break-inside: avoid; padding: 0.5pt 0; }
.bs .r .p { font-family: var(--label); color: var(--muted); }
.bsheet { height: auto !important; overflow: visible !important; }
.bsheet h1 { font-size: 13pt; } .bsheet .intro { font-size: 7pt; }
"""


def beat_sheet(sections, entries):
    out = []
    for s in sections:
        tags = (f'<i class="et">Elsewhere: {html.escape(", ".join(s["ctags"]))}</i>' if s.get("ctags") else "")
        out.append(f'<div class="h"><b>{s["kind"].title()} {s["num"]} · {s["page"]}</b><span>{inline(s["statement"])}</span>{tags}</div>')
        sub = None
        for e in entries:
            if e["sid"] != s["id"]:
                continue
            if e["sub"] and e["sub"] != sub:
                sub = e["sub"]
                out.append(f'<div class="sb">{inline(sub)}</div>')
            out.append(f'<div class="r"><span class="p">{e["page"]}</span><span>{e["label_html"]}</span></div>')
    intro = ('An index to the two plateaus on nomadology and the State: every axiom, proposition, and problem, and under each, every claim, contrast, list, definition, and question, by page. '
             'The quotations behind each line are in the web version and in <i>work/atp_12_13_inventory.md</i>. « Elsewhere » under each heading names the seminars and sources where the idea is worked out; the passages are in the web version and <i>work/context/context_12_13.md</i>.')
    sheet = (f'<section class="sheet bsheet"><div class="top"><h1>Plateaus 12 and 13, entry by entry</h1><span class="side">Beat sheet</span></div>'
             f'<p class="intro">{intro}</p><div class="bs">{"".join(out)}</div>'
             f'<div class="foot">Page numbers refer to the Minnesota translation of <i>A Thousand Plateaus</i> (1987).</div></section>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>Plateaus 12-13 Beat Sheet</title>{g.FONTS}'
            f'<style>{g.TOKENS}{g.SHARED}{g.PRINT}{PRINT_CSS}</style></head><body>{sheet}</body></html>')


def main():
    sections, entries, p3 = parse()
    ctx = load_context()
    attach_context(sections, ctx)
    g.save("plateaus_reference.html", web(sections, entries, p3, ctx))
    g.save("plateaus_beat_sheet.html", beat_sheet(sections, entries))
    from collections import Counter
    c = Counter(k for e in entries for k in e["kinds"])
    print(f"{len(sections)} headed statements, {len(entries)} entries, {len(p3)} by-kind sections; kinds {dict(c)}")


if __name__ == "__main__":
    main()
