# Nomadology reference

Reference sheets and handouts on *A Thousand Plateaus*, plateaus 12 and 13 ("Treatise on Nomadology" and "Apparatus of Capture"), made for a response to John Protevi's *Regimes of Violence*.

Each sheet is a printable PDF (the `*_handout.pdf` files) with a web version of the same material:

| Sheet | PDF | Web |
|---|---|---|
| Plateaus 12–13 beat sheet | `plateaus_beat_sheet.pdf` | `plateaus_beat_sheet.html`, `plateaus_reference.html` |
| Nomadology bibliography | `library_handout.pdf` | `library_handout.html`, `library.html` |
| Five machinic processes | `five_processes_handout.pdf` | `five_processes_handout.html`, `five_processes.html`, `five_processes_marronage.html` (with Protevi's marronage column) |
| Two sciences | `sciences_handout.pdf` | `two_sciences.html`, `sciences_handout.html` |
| Concepts, and how they have moved | `concordance_handout.pdf` | `concordance.html`, `concordance_handout.html` |
| After 1980 | `after1980_handout.pdf` | `after1980.html`, `after1980_handout.html` |
| State forms | `state_forms_handout.pdf` | `state_forms_handout.html`, `state_forms.html` |

All eight handouts are also gathered in one PDF, `nomadology_reference_packet.pdf` (27 pages: cover, guide and contents, the sheets in the order of the index, and a page about the project), with `nomadology_reference_packet_print.pdf` (32 pages) for double-sided printing, in which each sheet starts on a right-hand page. `build_packet.py` builds it from the handout PDFs, so rerun it after any handout changes: `python build_packet.py` (needs `pypdf` and Google Chrome).

The `.html` files are self-contained: open them in a browser. The `build_*.py` scripts generate the sheets, and the `*_text.md` files are plain-text dumps of their contents; they read further source material from the project they were made in, so they are included to show how the sheets were built rather than to run as is.

Page references are to the Minnesota edition of *A Thousand Plateaus* (trans. Brian Massumi, 1987).
