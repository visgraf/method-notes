# The one command: `make -C report` (or `make` from inside report/).
#
# The document builds with a TeX installation alone. No language runtime is
# required -- and in this repository none is available: there is no Python
# package and no pyproject.toml (fc-002). Generated figures would be COMMITTED
# rather than built here, so that a clean checkout compiles without running
# anything; there are none today. See figures/README.md.
#
# `make figures` IS INERT TODAY: this document has no figures, and pyproject.toml
# was deleted with the rest of the Python scaffolding (fc-002). The target is kept
# because it degrades honestly -- it prints "nothing to regenerate" rather than
# failing -- and because figures/README.md documents what has to come back before
# it means anything again. If you restore it, restore pyproject.toml first.

LATEXMK := latexmk

.PHONY: all sections figures clean distclean

all: main.pdf

# NOTE: sections/ is empty and main.tex \inputs nothing from it yet -- the prose
# lives in draft.md and is typeset at step 4 (docs/state.yaml). The wildcards
# below match nothing today and are correct in advance rather than wrong later.
main.pdf: main.tex $(wildcard sections/*.tex) $(wildcard figures/*.pdf) refs.bib
	$(LATEXMK) -pdf main.tex

# Regenerates report/sections/*.tex from report/draft.md. NEEDS PYTHON; the PDF
# build above does not, and must not -- the .tex files are committed so that a
# clean checkout compiles with a TeX installation alone. Run this after editing
# the draft, then commit both, which is what keeps the translation diffable.
#
# tests/test_scaffold.py regenerates into a temporary directory and compares
# bytes, so a .tex that has drifted from the draft fails CI rather than being
# silently overwritten the next time someone runs this.
sections:
	python3 ../tools/md2tex.py

# Regenerates every committed figure, then you commit the PDFs it changes: a
# figure and the claim it supports move through the same pull request, which is
# what makes a provenance appendix true rather than decorative.
#
# The loop is over figures/make_*.py by convention -- one script per figure, each
# asserting the numbers it draws against the record (figures/README.md).
figures:
	@scripts=$$(ls figures/make_*.py 2>/dev/null); \
	if [ -z "$$scripts" ]; then \
		echo "no figures/make_*.py yet; nothing to regenerate"; \
	else \
		for f in $$scripts; do echo "== $$f"; python $$f || exit 1; done; \
	fi

clean:
	$(LATEXMK) -c

distclean:
	$(LATEXMK) -C
