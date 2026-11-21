# Lookiyam themes for Vivaldi

My six Omarchy themes from
[omarchy-lookiyam-themes](https://github.com/lookiyam-94/omarchy-lookiyam-themes),
as Vivaldi browser themes, so the browser matches the desktop.

## Install

Download a `.zip` from [`themes/`](themes/), then in Vivaldi:
_Settings > Themes > Import Theme..._ and pick it.

Vivaldi will not open files from inside `~/.config` or other system folders, so
keep the archives somewhere like `~/Downloads`.

## Themes

| File | Theme | Mode | Toolbars | Tab bar | Highlight | Start Page |
|---|---|---|---|---|---|---|
| `carbon.zip` | Carbon | dark | `#121212` | `#0e0e0e` | `#ff7b54` | `01-carbon` |
| `graphite.zip` | Graphite | dark | `#191919` | `#141414` | `#8fbfff` | `08-graphite-mark` |
| `meridian.zip` | Meridian | dark | `#101216` | `#0c0e11` | `#7cc8ff` | `01-meridian` |
| `northline.zip` | Northline | dark | `#0c1013` | `#090c0f` | `#6ee7b7` | `01-northline` |
| `strata.zip` | Strata | dark | `#14120f` | `#100e0c` | `#e6b072` | `01-strata` |
| `umbra.zip` | Umbra | dark | `#0d0f14` | `#0a0b0f` | `#a8c8ff` | `01-umbra` |

### Theme descriptions

#### Carbon

Neutral charcoal toolbars and a darker tab bar, warm off-white text, and an
ember-orange highlight for focus and selection. The Start Page shows a single
hexagon with one glowing corner, like a carbon atom.

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

## How a palette maps onto Vivaldi

Each theme is read from its `colors.toml`:

| Vivaldi | Omarchy | |
|---|---|---|
| Background | `background` | Toolbars, panels, address field |
| Accent | `dark_background` | Tab bar — one step off the toolbars |
| Foreground | `foreground` | Text |
| Highlight | `accent` | Focus and selection |

The Start Page shows the first image in the theme's `backgrounds/`, scaled to
2560px WebP. Pages are never allowed to tint the tab bar, and there is no
transparency, blur or contrast boost — Vivaldi's contrast setting draws light
strokes around the chrome. Corners are a 4px radius.

## Rebuilding

The archives are generated, not hand-made. `sources/<theme>/` holds each
theme's `colors.toml` and its Start Page image. With ImageMagick installed:

```bash
python3 build.py                      # every theme in sources/
python3 build.py --only umbra carbon  # just these
```

To build straight from the installed Omarchy themes instead:

```bash
python3 build.py --themes ~/.config/omarchy/themes --only graphite umbra meridian strata northline carbon
```

That uses the first background of each theme, which for Graphite is a
photograph rather than its mark.

## License

MIT
