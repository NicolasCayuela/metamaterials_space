![Metamaterials research space](demo.gif)

# Metamaterials Research Space

An interactive map of the metamaterials literature. Around 615,000 papers
(Semantic Scholar, arXiv, OpenAlex and HAL, 1987 to 2026) embedded with
[Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) and
projected to 2D with UMAP. Every dot is a publication and neighbourhoods are
research topics.

**Live:** https://nicolascayuela.github.io/metamaterials_space/

## The map

Three continents split the field by physical domain: Electromagnetic and
Optical (blue), Acoustic and Phononic (green), Elastic and Mechanical (amber).
White cells are fields such as Photonic Crystals, Phononic Crystals,
Metasurfaces, Negative Index or Auxetics. Amber labels are subfields that
appear as you zoom in. Hover a point to read its title, zoom for finer
structure, and search any topic or author.

Search and per-paper details query the [OpenAlex](https://openalex.org) API
live, so the site stays fully static on GitHub Pages with no backend.

## How it is built

A static viewer (`index.html` plus `data/`) drawing pre-baked binary point and
label assets with [deck.gl](https://deck.gl). The data pipeline lives in the
companion `paper_space` project.

## Data sources

The map relies on open scholarly infrastructure for titles, abstracts, venues,
authors, DOIs and citation counts. Thanks to the teams who maintain these free
services:

- [Semantic Scholar](https://www.semanticscholar.org/product/api): bulk paper
  search, paper batches and title search, the backbone of the corpus.
- [arXiv](https://arxiv.org): preprint metadata snapshot and API.
- [OpenAlex](https://openalex.org): lookups by DOI and ID, full-text title
  search, abstract reconstruction, venues and authors.
- [Crossref](https://www.crossref.org): DOI metadata and bibliographic title
  search, which recovered DOIs for papers that had none.
- [OpenAIRE](https://www.openaire.eu): extra open-access metadata.
- [HAL](https://hal.science): French open archive.
- Unpaywall and publisher landing pages: abstracts read from standard
  citation_abstract and Dublin Core meta tags.
