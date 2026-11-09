# My Tribe Gym — Website

Static bilingual website (English at `/`, Arabic at `/ar/`) for **My Tribe Gym**.

## Pages
Home · The Tribe · Programs · Schedule · Coaches · Membership · Facilities & Café · Contact

## Editing content
All texts, the class schedule, coaches and **prices** live in `build.py`.
After editing, regenerate the HTML:

```bash
python3 build.py
```

- Prices: `PRICES` and `EXTRAS` (currently **placeholder** values in JOD).
- Schedule: `SCHEDULE`
- Coaches: `COACHES`
- Styles: `assets/css/style.css` · Scripts: `assets/js/main.js`

Hosted with GitHub Pages.
