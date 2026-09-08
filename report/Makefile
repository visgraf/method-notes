# The one command: `make -C report` (or `make` from inside report/).
#
# The document builds with a TeX installation alone. No language runtime is
# required: report/figures/*.pdf are generated artifacts and are COMMITTED, so a
# clean checkout compiles without running anything. See figures/README.md for why
# they are committed and why nothing diffs their bytes.
#
# `make figures` regenerates them and needs the project installed (pip install -e .).

LATEXMK := latexmk

.PHONY: all figures clean distclean

all: main.pdf

main.pdf: main.tex $(wildcard sections/*.tex) $(wildcard figures/*.pdf) refs.bib
	$(LATEXMK) -pdf main.tex

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
