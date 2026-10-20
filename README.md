# 🚩 HRL Corporate Flag: The Twin-Headed Shadow Wyvern

<div align="center">

[![Architect](https://img.shields.io/badge/Chief%20Architect-Pavan%20Kumar%20Sadashiv-0A66C2?style=for-the-badge&logo=linkedin)](https://github.com/hrlpavan)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/hrlpavan/hrl-corporate-flag)
[![GitLab Repository](https://img.shields.io/badge/GitLab-Repository-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/hrlpavan/hrl-corporate-flag)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-HRL%20International%20Pvt.%20Ltd.-orange?style=for-the-badge)](https://github.com/hrlpavan/hrl-international-website-)
[![Vector Format](https://img.shields.io/badge/Format-Scalable%20Vector%20Graphics%20(.SVG)-brightgreen?style=for-the-badge&logo=svg)](flag.svg)
[![Color Constraint](https://img.shields.io/badge/Emblem%20Color-Pure%20Black%20%23000000-black?style=for-the-badge)](flag.svg)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <b>The official corporate flag and heraldic vector identity system for HRL International Private Limited. Engineered with pure black compound vector paths, true negative-space transparency, and an instantly replaceable background architecture.</b>
</p>

</div>

---

## 📌 Table of Contents
- [Executive Overview](#-executive-overview)
- [Design Manifesto & Heraldic Anatomy](#-design-manifesto--heraldic-anatomy)
- [Technical Specifications & Architecture](#-technical-specifications--architecture)
- [Dynamic Background Customization](#-dynamic-background-customization)
- [Repository File Inventory](#-repository-file-inventory)
- [Interactive Flag Previewer](#-interactive-flag-previewer)
- [Statutory Trademark & Brand Notice](#-statutory-trademark--brand-notice)
- [License](#-license)

---

## 🌟 Executive Overview

The **HRL Corporate Flag** embodies the engineering philosophy, uncompromising authority, and technological sovereignty of **HRL International Private Limited**. 

Inspired by the classical heraldic bilateral symmetry of historical flags (notably the iconic double-headed eagle motif), this mark synthesizes traditional statecraft heraldry with dark, aggressive, deep-tech mythology: the **Twin-Headed Abyssal Wyvern / Demon Drake**.

Every contour, curve, and cutout is mathematically balanced across the vertical axis of symmetry, calibrated for immediate readability across all scales—from physical silk flag deployments to 4K displays and micro-favicon resolutions.

---

## 🐉 Design Manifesto & Heraldic Anatomy

```
                   ▲ Horn Spires (Barbed Ridges)
             \   /   \   /
         ◄──(Head)   (Head)──► Twin Outward Roaring Maws (Razor Fangs & Stinger Tongue)
            /  |       |  \
          /   /         \   \
        /    /    (Chest)  \   \  ◄── 9 Upward-Sweeping Razor Scythe Primary Blades
      /     /    [ Ribs ]   \    \
     │     │     [ Slits ]   │    │ ◄── Negative Space Skeletal Rib Slits
     │     │                 │    │
            \   ( Pelvis )  /
           / \             / \
      ◄──(Claw)           (Claw)──► 4 Outstretched Sickle Talons & Dewclaws
               \  [Tail] /
                \ [Spines]/
                 ▼ [Spade] ◄── Barbed Devil's Spearhead
```

1. **Twin Menacing Draconic Heads**:
   - Outward-facing predatory profiles with sweeping curved ram/wyvern horns, supraorbital brow spires, and dorsal nape armor spines.
   - Open roaring maws exposing interlocking razor fangs and a bifurcated serpent tongue tipped with an upward venomous barb.
   - Sinister predatory slit eyes cut directly through the silhouette so they glow with the chosen background color.
2. **The Crown of Scythe-Blades (Wings)**:
   - 9 upward-curving razor primary blades per wing, echoing the rhythm of heraldic eagle wings while delivering a draconic silhouette.
   - Carpal joint thumb spurs and aerodynamic patagium slots providing structural depth.
3. **Skeletal Armored Torso**:
   - 5 anatomical negative-space rib slashes radiating across the breastplate, allowing the background field to radiate through the torso.
4. **Predatory Sickle Talons**:
   - Muscular dragon haunches extending outward into 4 razor sickle claws with pronounced knuckles and hooked rear dewclaws.
5. **Tiered Spined Tail**:
   - Descending central column flanked by 3 tiers of scythe fins, terminating in a lethal barbed devil's spearhead spade.

---

## 📐 Technical Specifications & Architecture

| Parameter | Specification | Details |
| :--- | :--- | :--- |
| **Canvas Dimensions** | `1400 × 1000 px` | Standard international flag aspect ratio (7:5 / 1.4:1). |
| **Primary File Format** | `.svg` (Scalable Vector Graphics) | 100% loss-free vector, infinite resolution scaling. |
| **Emblem Color Constraint** | `#000000` (Pure Solid Black) | Strictly black silhouette as mandated by design specifications. |
| **Cutout Methodology** | `fill-rule="evenodd"` | Native compound vector path. Eliminates clipping mask errors across vector engines. |
| **Horizontal Alignment** | Left: `255.71 px` \| Right: `255.73 px` | Symmetrical to within 0.02 px. |
| **Vertical Alignment** | Top: `81.40 px` \| Bottom: `81.57 px` | Mathematically centered with balanced breathing margins. |
| **Vector Weight** | Scaled at `0.72` | Perfectly balanced visual mass relative to field canvas. |

---

## 🎨 Dynamic Background Customization

The flag includes a dedicated background layer (`#flag-background`) engineered for instant recoloring via CSS, SVG attributes, or vector editing tools:

### Method 1: CSS Variable
In the `<style>` block of [`flag.svg`](flag.svg), modify `--bg-color`:
```css
:root {
  --bg-color: #dc143c; /* HRL Crimson Red (Default) */
}
```

### Method 2: Element Fill Attribute
Directly edit the `<rect>` tag on line 57 of [`flag.svg`](flag.svg):
```xml
<rect id="flag-background" class="flag-background" width="1400" height="1000" fill="#dc143c" />
```

### Brand Color Swatches
| Palette Name | Hex Code | Visual Application |
| :--- | :--- | :--- |
| **HRL Crimson** | `#dc143c` | Official corporate flag field (Inspired by the reference design) |
| **Stark White** | `#ffffff` | High-contrast documentation, print letterheads, and formal stationery |
| **Midnight Navy** | `#0f172a` | Executive presentations, tech conferences, and evening banquets |
| **Imperial Gold** | `#f59e0b` | Ceremonial honors, legal patents, and executive tier milestones |
| **Toxic Emerald** | `#059669` | AI runtime releases, performance benchmarks, and developer tooling |
| **Charcoal Stealth** | `#1f2937` | Hardware chassis badges, dark mode applications, and studio banners |
| **Transparent** | `transparent` | Watermarks, video overlays, embroidery, and apparel screen-printing |

---

## 📂 Repository File Inventory

```
hrl-corporate-flag/
├── flag.svg                 # Production-ready master vector flag (.SVG)
├── index.html               # Interactive browser previewer with instant color swatches
├── generate_flag.py         # Parametric Python generator with precision Bézier curves
├── DESIGN_SPECIFICATION.md  # Formal heraldic specifications and vector geometry audit
├── LICENSE                  # MIT Open Source License (HRL Brand Asset)
└── README.md                # Master architectural documentation and usage guidelines
```

---

## 🖥️ Interactive Flag Previewer

An interactive HTML5 preview suite is included in [`index.html`](index.html). To view locally:
```bash
python3 -m http.server 8085
```
Open **`http://localhost:8085`** in any web browser to:
- Test real-time background color swaps with one click.
- Experiment with custom RGB/hex colors using the color picker.
- Copy raw SVG markup to your clipboard.
- Download the production `.svg` directly.

---

## ⚖️ Statutory Trademark & Brand Notice

`HRL™`, `HRL INTERNATIONAL™`, the **Twin-Headed Shadow Wyvern Emblem**, and all associated corporate visual assets are proprietary trademarks of **HRL International Private Limited**. Unauthorized reproduction for deceptive commercial use or counterfeit software distribution is strictly prohibited under international IP treaties and the Trade Marks Act, 1999.

---

## 📜 License

This project and its vector assets are licensed under the [MIT License](LICENSE).

<div align="center">
  <b>HRL INTERNATIONAL PRIVATE LIMITED</b><br>
  <i>"We Can Do Everything Related To Software Sector Without Any Excuses!"</i><br>
  Mangaluru, Karnataka, India
</div>
