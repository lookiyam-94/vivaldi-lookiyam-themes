# Lookiyam themes for Vivaldi

My Omarchy themes as Vivaldi browser themes, so the browser matches the
desktop: the eight from
[omarchy-lookiyam-themes](https://github.com/lookiyam-94/omarchy-lookiyam-themes),
plus Cursor Dark.

## Install

Download a `.zip` from [`themes/`](themes/), then in Vivaldi:
_Settings > Themes > Import Theme..._ and pick it.

Vivaldi will not open files from inside `~/.config` or other system folders, so
keep the archives somewhere like `~/Downloads`.

Each archive has a Markdown description next to it (`themes/<theme>.md`),
ready to paste into the Vivaldi Themes gallery.

## Themes

| File | Theme | Mode | Toolbars | Tab bar | Highlight | Start Page |
|---|---|---|---|---|---|---|
| `bramble.zip` | Bramble | dark | `#140d12` | `#090b0d` | `#c791a9` | `01-bramble` |
| `carbon.zip` | Carbon | dark | `#121212` | `#0e0e0e` | `#ff7b54` | `01-carbon` |
| `cursor-dark.zip` | Cursor Dark | dark | `#191919` | `#141414` | `#8fbfff` | `01-cube` |
| `graphite.zip` | Graphite | dark | `#191919` | `#141414` | `#8fbfff` | `08-graphite-mark` |
| `meridian.zip` | Meridian | dark | `#101216` | `#0c0e11` | `#7cc8ff` | `01-meridian` |
| `northline.zip` | Northline | dark | `#0c1013` | `#090c0f` | `#6ee7b7` | `01-northline` |
| `strata.zip` | Strata | dark | `#14120f` | `#100e0c` | `#e6b072` | `01-strata` |
| `umbra.zip` | Umbra | dark | `#0d0f14` | `#0a0b0f` | `#a8c8ff` | `01-umbra` |
| `vesper.zip` | Vesper | dark | `#100d15` | `#090b0d` | `#b6a0d6` | `01-vesper` |

### Theme descriptions

#### Bramble

Plum-black toolbars over a darker tab bar, soft grey-white text, and a
berry-pink highlight. The Start Page shows an arching, thorned cane with one
glowing blackberry.

#### Carbon

Neutral charcoal toolbars and a darker tab bar, warm off-white text, and an
ember-orange highlight for focus and selection. The Start Page shows a single
hexagon with one glowing corner, like a carbon atom.

#### Cursor Dark

Inspired by Cursor, Grok and Grok Bot. The greys are lifted from Cursor's
built-in Cursor Dark: toolbars on the editor's `#191919`, the tab bar on the
title bar's `#141414`, with soft white text. Cursor's link blue marks focus and
selection, and the white Cursor cube sits alone on the Start Page. All 14 of its
backgrounds are in [`backgrounds/cursor-dark/`](backgrounds/cursor-dark/).

Moved here from
[omarchy-vivaldi-themes](https://github.com/lookiyam-94/omarchy-vivaldi-themes),
with the same theme ID, so re-importing it updates the copy you already have.

#### Graphite

Soft graphite-grey toolbars over a deeper tab bar, near-white text, and a calm
blue highlight. The Start Page shows the Graphite mark: an open ring with a bar
of blue light through its gap.

#### Meridian

Slate-black chrome with cool silver text and a bright sky-blue highlight. The
Start Page shows a thin triangle with a point of light at its apex.

#### Northline

Cold blue-black toolbars and tab bar, icy silver text, and a mint-green
highlight. The Start Page shows a rounded square split by a vertical line of
light.

#### Strata

Warm brown-black chrome, cream text and an amber highlight, like layers of
rock. The Start Page shows three stacked bars with the lowest one glowing.

#### Umbra

Deep blue-black toolbars, cool silver text and a pale ice-blue highlight. The
Start Page shows an eclipse: a dark disc with a thin crescent of light.

#### Vesper

Violet-black toolbars over a darker tab bar, soft grey-white text, and a
twilight-violet highlight. The Start Page shows the evening star above a sun
half set behind a line of violet light.

## Backgrounds

Every current background from each Omarchy theme lives in
[`backgrounds/`](backgrounds/), one folder per theme, at full size — use them
as desktop wallpapers too. Graphite's former `11-orbits.png` is preserved in
[`retired-backgrounds/graphite/`](retired-backgrounds/graphite/).

| Folder | Count |
|---|---|
| [`bramble/`](backgrounds/bramble/) | 11 |
| [`carbon/`](backgrounds/carbon/) | 10 |
| [`cursor-dark/`](backgrounds/cursor-dark/) | 14 |
| [`graphite/`](backgrounds/graphite/) | 10 |
| [`meridian/`](backgrounds/meridian/) | 10 |
| [`northline/`](backgrounds/northline/) | 10 |
| [`strata/`](backgrounds/strata/) | 10 |
| [`umbra/`](backgrounds/umbra/) | 10 |
| [`vesper/`](backgrounds/vesper/) | 11 |

## How a palette maps onto Vivaldi

Each theme is read from its `colors.toml`:

| Vivaldi | Omarchy | |
|---|---|---|
| Background | `background` | Toolbars, panels, address field |
| Accent | `dark_background` | Tab bar — one step off the toolbars |
| Foreground | `foreground` | Text |
| Highlight | `accent` | Focus and selection |

The Start Page shows the theme's first background (Graphite uses its mark,
`08-graphite-mark`, instead of the first photograph), scaled to 2560px WebP.
Pages are never allowed to tint the tab bar, and there is no transparency, blur
or contrast boost — Vivaldi's contrast setting draws light strokes around the
chrome. Corners are a 4px radius.

## Rebuilding

The archives are generated, not hand-made. `sources/<theme>/` holds each
theme's `colors.toml`, and the Start Page image comes from
`backgrounds/<theme>/`. With ImageMagick installed:

```bash
python3 build.py                      # every theme in sources/
python3 build.py --only umbra carbon  # just these
```

To build straight from the installed Omarchy themes instead:

```bash
python3 build.py --themes ~/.config/omarchy/themes --only graphite umbra meridian strata northline carbon bramble vesper
```

Graphite still gets its mark there, as long as the theme has
`08-graphite-mark.png`.

## License

MIT
