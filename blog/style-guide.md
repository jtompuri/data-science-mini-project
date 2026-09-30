# Party Map blog – style guide

The page's visual language in one place. `styles.css` implements these tokens;
change values there, not in the article. Scope: the blog only (the report has
its own, plainer style).

## Typography

Two families with fixed roles:

| Role | Family | Why |
|---|---|---|
| Narrative (body, headings, lede, subtitle, big numbers) | **Source Serif 4** | the "story" voice; classic editorial look |
| Data & apparatus (captions, chart text, tiles' labels, chips, callouts, metadata) | **Inter** | the "data" voice; compact and neutral at small sizes |

Type scale: **ratio 1.125 (major second), base 1.15 rem** — each step is a
natural, visible but calm change. The title jumps three steps for display
contrast.

| Token | rem | Used for | Weight / line-height |
|---|---|---|---|
| `--fs-xs` | 0.81 | figure captions, tile labels, footer | 400 / 1.4 |
| `--fs-s` | 0.91 | chips, year strip, chart source notes | 400–700 / 1.4 |
| `--fs-m` | 1.02 | callout body | 400 / 1.55 |
| `--fs-base` | 1.15 | body text | 400 / 1.75 |
| `--fs-lede` | 1.29 | opening standfirst | 500 / 1.55 |
| `--fs-sub` | 1.46 | page subtitle | 600 / 1.35 |
| `--fs-h3` | 1.64 | h3 (if needed) | 700 / 1.25 |
| `--fs-h2` | 1.85 | section headings | 700 / 1.2 |
| `--fs-h1` | 2.63 | page title | 700 / 1.12 |

Stat-tile numbers: serif 700, `clamp(1.46rem, 4vw, 2.08rem)`; long numbers one
step smaller. Plotly (px, set per figure): base 14, takeaway title 20 bold
serif, annotations 13.

## Colour

One brand hue (navy) plus neutrals; everything else is data colour. Party
colours are **identity colours**: used only to mark a party (map points,
party chips), never as decoration. The chart categorical palette
(`#2a78d6 #eb6834 #1baf7a #eda100 #e87ba4`, validated for CVD) is used only
inside charts for non-party series.

| Token | Hex | Role | Contrast on white |
|---|---|---|---|
| `--ink` | `#222c36` | body text | 13.3:1 |
| `--ink-strong` | `#16283b` | headings | 15.2:1 |
| `--brand` | `#1f4e79` | accent bar, links, stat numbers, chart emphasis, annotations | 8.0:1 |
| `--brand-deep` | `#16324f` | lede text | 11.9:1 |
| `--muted` | `#5b6673` | captions, labels, secondary text | 5.9:1 |
| `--chart-neutral` | `#8a94a0` | "random labels" series, de-emphasised marks | (charts only) |
| `--surface-1` | `#f4f6f9` | stat tiles, map background | – |
| `--surface-2` | `#eef2f7` | chips, year strip | – |
| `--line` | `#d8dee6` | hairlines, chart gridlines | – |

Rules of thumb:

- Text is always an ink/muted token — never a party colour, never a chart hue.
- The page title, subtitle and lede share `--brand-deep`, forming one navy
  opening block on the warm top zone; section headings stay in
  `--ink-strong` with the navy accent bar, so navy in running text keeps
  its meaning (links, our measure).
- Navy is the only colour that appears in both prose and charts; it marks
  "our measure".
- Surfaces get no borders; separation comes from the tint itself.
- No gridlines or frames on the MDS map (its axes carry no meaning);
  gridlines on value charts stay on `--line`.

## Spacing & layout

- Vertical rhythm ~0.5 rem steps; sections start at 3 rem with the 3 rem × 5 px
  navy accent bar above the heading.
- Tiles and chips: 10 px radius (tiles), full radius (chips), no shadows.
- Content column: the theme default (~46 rem); charts span the column and are
  responsive; everything must survive a 375 px viewport (tiles wrap, chips
  wrap, charts autosize).

## Voice in figures

Titles state the finding, not the variable ("One step, not a slow drift").
Captions carry method and source in `--fs-xs`. Direct labels over legends
when there are ≤ 5 series; annotations point at the one thing the reader
should see.

## Accessibility

- All text/background pairs meet WCAG AA 4.5:1; party-chip backgrounds are
  darkened shades of the official colours chosen to pass with white text
  (Finns `#8a6f00`, Left `#c70853`, Greens `#3c7a10`; the official hues stay
  on the map markers, where colour is graphic, paired with text labels).
- Every number shown only in a figure is also stated in the prose, so the
  page reads without the charts; captions carry method and source.
- Identity is never colour-alone: map points and chips carry text labels,
  chart series are directly labelled.
- Known limitation: Plotly's term buttons and tooltips are not reachable by
  keyboard (an upstream Plotly issue). The default view shows the current
  term and the other terms' story is told in the prose, so no information is
  interaction-locked.
- The map animation runs only when the reader presses a button
  (user-initiated motion; nothing autoplays).
