# pandoc-drawio-filter

This repository contains the python package `pandoc-drawio-filter` with the tool
`pandoc-drawio`, which helps [`pandoc`](https://pandoc.org/) convert `.drawio`
files to PDF before embedding them when referenced as images in markdown.

## Usage

Make sure that you have the following command line tools in your `PATH`
environment:

- `xvfb`
- [`drawio`](https://github.com/jgraph/drawio-desktop)
- (plus the usual tools that you use with `pandoc`, like TeX etc.)

Write markdown documents as usual, with drawio images like this:

```

![my pretty drawio image](my-image.drawio)

```

Then, run pandoc like this:

```sh
pandoc -F pandoc-drawio my-document.md -o my-document.pdf
```

## Python Package Management

I currently only use the [`nix`](https://nixos.org) package manager for
everything.
It may be the case that the `setup.py` can be easily extended in order to upload
the package to the usual python package infrastructure.
I am happy to accept pull requests as i have neither the expertise nor the
bandwidth.
