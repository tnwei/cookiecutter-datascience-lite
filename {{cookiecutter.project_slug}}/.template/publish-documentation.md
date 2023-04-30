# Templates for project documentation

## Publish to PDF using LaTeX via pandoc

This option is perhaps as simple as it gets; write everything in markdown, then publish to PDF.

In `docs.md`:

```markdown
---
title: "Docs title"
subtitle: "Subtitle"
author: "Your name here"
date: Apr 30, 2023
lang: en-US
---

# H1

## H2

### H3

Body text
```

Run the following command to generate `output.pdf`, requires `pandoc` and `xelatex` installed:

```bash
# ref for TOC: https://jdhao.github.io/2019/05/30/markdown2pdf_pandoc/#use-numbered-section-and-add-toc
# ref for title page before TOC: https://stackoverflow.com/a/44670330/13095028

# rm'ed options
# --filter pandoc-fignos \

pandoc --pdf-engine=xelatex -V geometry:margin=1in \
-f markdown+hard_line_breaks -o output.pdf \
--highlight-style tango \
--toc \
--number-sections  \
*.md
```

## mkdocs

If what you need is a documentation website, `mkdocs` can do a great job. 
Useful commands, taken from the pre-generated `index.md`:

```markdown
# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
    ¦   index.md  # The documentation homepage.
    ¦   ...       # Other markdown pages, images and other files.
```

Running `mkdocs new` will set up a blank template. Use the following instead to get started faster. Put all the relevant files in `docs/`, and create `mkdocs.yml`. 

```bash
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    chapter1.md  # Other markdown pages, images and other files.
    ...
```

In `mkdocs.yml`:

```yaml
# mkdocs template for documentation
# refer to https://www.mkdocs.org/getting-started/
site_name: projectname
nav:
  ¦ - Home: index.md
  ¦ - Chapter 1: chapter1.md
theme:
    # pip install mkdocs-material or pip install mkdocs-gitbook
  ¦ name: material # gitbook
plugins: [ ] 
```

`mkdocs serve` to see what the website looks like locally. Continue learning how to use `mkdocs` at https://www.mkdocs.org/getting-started.


## Jupyter Book

Jupyter Book allows both setting up a documentation website and also exporting as a typsetted book PDF. Definitely a lot more involved than the other options outlined above.

Install Jupyter book, and get started by modifying the template created using `jb create mynewbook`. 
