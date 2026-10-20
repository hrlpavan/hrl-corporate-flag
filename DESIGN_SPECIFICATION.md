# Company Flag Design: The Twin-Headed Shadow Wyvern

This vector flag design was created directly from the heraldic silhouette aesthetic of your reference flag (the Albanian double-headed eagle), transformed into a scary mythical apex predator: the **Twin-Headed Abyssal Wyvern**.

---

## 🚩 Files & Locations

- **Production Vector Flag**: [flag.svg](file:///Users/pavankumars/.gemini/antigravity/scratch/hrl-corporate-flag/flag.svg)
- **Interactive Flag Previewer**: [index.html](file:///Users/pavankumars/.gemini/antigravity/scratch/hrl-corporate-flag/index.html)
- **Live Local Preview**: [http://localhost:8085](http://localhost:8085)
- **Project Directory**: `/Users/pavankumars/.gemini/antigravity/scratch/hrl-corporate-flag`

---

## 📐 Design & Heraldry Breakdown

| Feature | Design Specification | Heraldic Purpose |
| :--- | :--- | :--- |
| **Creature** | **Twin-Headed Abyssal Wyvern / Demon Drake** | Non-regular mythical predator evoking power, dominion, and terror. |
| **Color Rule** | **Strictly Solid Black (`#000000`)** | 100% compliant with the single-color constraint. |
| **Negative Space Cutouts** | Standard SVG `fill-rule="evenodd"` | Slit eyes, razor teeth, glowing skeletal rib slits, and wing bone channels are genuine transparent vector cutouts. Whatever background color you select naturally shines through. |
| **Symmetry** | Exact bilateral mirror (`transform="scale(-1, 1)"`) | Flawless geometric balance down to sub-pixel accuracy. |
| **Head & Jaws** | Menacing curved horns, brow spires, open jaws with serrated fangs, and a protruding barbed serpent tongue | Delivers the requested terrifying and aggressive presence. |
| **Wing Span** | 9 razor scythe primary blades + 3 flank plates | Replicates the soaring, commanding rhythm of the reference flag feathers. |
| **Talons** | 4 outstretched sickle claws with distinct knuckles & spurs | Vicious predatory stance commanding the lower field. |
| **Tail** | Tiered lateral scythe spines ending in a barbed devil's spearhead | Clean vertical convergence anchoring the emblem. |

---

## 🎨 How to Replace the Background

### Option 1: Edit the CSS Variable (Recommended)
Open [flag.svg](file:///Users/pavankumars/.gemini/antigravity/scratch/hrl-corporate-flag/flag.svg) in any text editor and change `--bg-color`:

```css
:root {
  --bg-color: #dc143c; /* Crimson Red (default) */
  /* Or change to:
     --bg-color: #ffffff;      (Stark White)
     --bg-color: #0f172a;      (Midnight Navy)
     --bg-color: #f59e0b;      (Imperial Gold)
     --bg-color: #059669;      (Toxic Emerald)
     --bg-color: transparent;  (Transparent cutout)
  */
}
```

### Option 2: Edit the Background `<rect>` Directly
Locate line 57 in [flag.svg](file:///Users/pavankumars/.gemini/antigravity/scratch/hrl-corporate-flag/flag.svg):

```xml
<rect id="flag-background" 
      class="flag-background" 
      width="1400" 
      height="1000" 
      fill="#dc143c" />
```
Set `fill="transparent"` or `fill="none"` if you need a transparent sticker / icon asset.

### Option 3: In Adobe Illustrator, Figma, or Inkscape
Open [flag.svg](file:///Users/pavankumars/.gemini/antigravity/scratch/hrl-corporate-flag/flag.svg). The bottom layer is named `flag-background`. You can toggle its visibility, apply gradients, or delete it with a single click.
