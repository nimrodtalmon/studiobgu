# studiobgu — סטודיו למחקר (BGU IEM MSc)

Slide decks for the mandatory MSc course "סטודיו למחקר", served by GitHub Pages
(branch `main`, root): https://nimrodtalmon.github.io/studiobgu/

## Layout
- `index.html` — course page, links to the decks.
- `NN.html` — one deck per session (03 = מאמרים). Plain HTML, no build step.
- `assets/deck.css`, `assets/deck.js` — shared slide engine (1920×1080 canvas scaled to the window, RTL).
- `assets/img/` — images used by the decks.

## Writing a slide
Each slide is a `<section class="slide dark|light|accent [center|middle]">` inside `#stage`.
Building blocks (see deck.css): `h1` (`.huge`, `.q`), `h2`, `h3`, `p` (`.eyebrow`, `.muted`, `.hl`, `.big`, `.small`),
`.cards > .card(.top)` with `.num`/`.label`, `.chips > .chip(.on)` + `.arrow`, `.rows(.ruled) > .row` with `.n` or `.k`,
`.shot > img`, `.node` + `svg.diagram` for diagrams, `.ref` for a bottom reference line, `<aside>` for speaker notes (N key).
Wrap English runs inside Hebrew text in `<span class="ltr">`.

## Style (Nimrod's)
- Very little text: one idea per slide, a short title and at most 2–4 short lines.
- Many light slides over few dense ones; question slides, then the answer on the next slide.
- Dry, light humor is fine. No invented facts, numbers or quotes; references as name + year.
- Palette: dark #26282C, light #F3F3F1, orange #F7941D; font Heebo.

## Deploy
Commit and push to `main`; Pages redeploys in about a minute.
