# 🚩 HRL International Official Corporate Flag

<div align="center">

[![Architect](https://img.shields.io/badge/Chief%20Architect-Pavan%20Kumar%20Sadashiv-0A66C2?style=for-the-badge&logo=linkedin)](https://github.com/hrlpavan)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/hrlpavan/hrl-corporate-flag)
[![GitLab Repository](https://img.shields.io/badge/GitLab-Repository-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/hrlpavan/hrl-corporate-flag)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-HRL%20International%20Pvt.%20Ltd.-orange?style=for-the-badge)](https://github.com/hrlpavan/hrl-international-website-)
[![Vector Format](https://img.shields.io/badge/Format-Scalable%20Vector%20Graphics%20(.SVG)-brightgreen?style=for-the-badge&logo=svg)](flag.svg)
[![Standard Aspect Ratio](https://img.shields.io/badge/Ratio-3%3A2%20(1024x682)-blue?style=for-the-badge)](flag.svg)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br />

<p align="center">
  <img src="flag.svg" alt="HRL International Official Corporate Flag" width="750" style="border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);" />
</p>

<p align="center">
  <b>The Official Sovereign Flag and Heraldic Vector Identity System for HRL International Private Limited.<br />
  Engineered with mathematical precision, Nordic Cross geometry, quad-stripe canton module, official brand insignia, dual heraldic eagles, and an 8-pointed compass star.</b>
</p>

</div>

---

## 📌 Table of Contents
- [Executive Overview](#-executive-overview)
- [Design Architecture & Geometry](#-design-architecture--geometry)
- [Symbolic Elements & Heraldic Anatomy](#-symbolic-elements--heraldic-anatomy)
- [Color Palette & Specifications](#-color-palette--specifications)
- [Dynamic Background Customization](#-dynamic-background-customization)
- [Repository & File Inventory](#-repository--file-inventory)
- [Interactive Showcase](#-interactive-showcase)
- [Statutory Trademark & Brand Notice](#-statutory-trademark--brand-notice)

---

## 🌟 Executive Overview

The **Official HRL Corporate Flag** represents the foundational sovereign identity, technical discipline, and global vision of **HRL International Private Limited**.

Constructed upon a strict 83-pixel modular unit grid, the flag synthesizes:
1. **The Nordic Cross**: Unbroken white cross symbolizing stability, structure, and international enterprise.
2. **Canton Accent Stripes**: 4 vertical black stripes representing the core technological pillars.
3. **Official HRL Brand Mark**: Integrated directly on the white horizontal crossbar (Crimson 'H' and Black 'RL').
4. **The Lower Hoist Triad**: Twin heraldic double-headed eagles flanking an 8-pointed crimson compass star.

---

## 📐 Design Architecture & Geometry

The flag is drafted on a standard **3:2 proportion** with a canvas grid of **1024 × 682 px**:

```
+----------------------------------------------------------------------------------+
| (0,0)                                                                            |
| Red Hoist     | White Vertical | Black Stripes |           Solid Crimson         |
| Canton        | Cross (w=83)   | (4x stripes)  |           Fly Field             |
| (w=85, h=297) | (x: 85..168)   | (x: 168..240) |           (x: 240..1024)        |
+---------------+----------------+---------------+---------------------------------+
| [  H  ]       | [ R   L ]      |               White Horizontal Cross (h=83)     |
| (y: 297..380) | (y: 297..380)  |               (y: 297..380, w=1024)             |
+---------------+----------------+---------------+---------------------------------+
| Eagle 1       | 8-Pointed Star | Eagle 2       |           Solid Crimson         |
| (x: 6..77)    | (x: 86..165)   | (x: 177..247) |           Lower Fly Field       |
| Black Heraldic| Crimson Red    | Black Heraldic|                                 |
+----------------------------------------------------------------------------------+
```

### Modular Proportions:
- **Modular Unit**: `83px`
- **Vertical Cross Stripe**: `x = 85` to `168` (width: `83px`, height: `682px`)
- **Horizontal Cross Stripe**: `y = 297` to `380` (height: `83px`, width: `1024px`)
- **Upper Canton Black Stripes**: 4 vertical stripes at `x = 168` (w=10), `x = 190` (w=9), `x = 210` (w=10), `x = 232` (w=8)
- **Lower Hoist Triad**:
  - Left Canton (Red Field): Double-headed eagle `(x: 6..77, y: 386..467)`
  - Center Cross (White Stripe): 8-pointed star `(x: 86..165, y: 384..472)`
  - Right Canton (Red Field): Twin double-headed eagle `(x: 177..247, y: 384..464)`

---

## 🦅 Symbolic Elements & Heraldic Anatomy

1. **Twin Heraldic Double-Headed Eagles**:
   - Flanking the lower hoist canton in pure solid black (`#000000`).
   - Represents vigilance, sovereignty, looking simultaneously to past foundations and future technological frontiers.
2. **8-Pointed Compass Star**:
   - Crimson red (`#BF1F1F`) positioned at the intersection of the lower vertical white bar.
   - 4 primary cardinal points (radius 44px) and 4 secondary diagonal points (radius 22.5px), symbolizing global navigation and omnipresence.
3. **Official HRL Brand Insignia**:
   - Situated across the horizontal white crossbar.
   - Left: Crimson red serif `'H'` (`#BF1F1F`).
   - Right: Black high-contrast serif `'R'` and flowing calligraphic script `'L'` (`#000000`).

---

## 🎨 Color Palette & Specifications

| Element | Hex Code | RGB | Role |
| :--- | :--- | :--- | :--- |
| **Field Background** | `#BF1F1F` | `rgb(191, 31, 31)` | Sovereign Crimson Red field |
| **Cross Bars** | `#FFFFFF` | `rgb(255, 255, 255)` | Pure White Nordic Cross |
| **Canton Stripes** | `#000000` | `rgb(0, 0, 0)` | Hoist accent stripes |
| **Heraldic Eagles** | `#000000` | `rgb(0, 0, 0)` | Pure black vector emblems |
| **Compass Star** | `#BF1F1F` | `rgb(191, 31, 31)` | Crimson red starburst on white bar |
| **Brand 'H'** | `#BF1F1F` | `rgb(191, 31, 31)` | Crimson red corporate initial |
| **Brand 'RL'** | `#000000` | `rgb(0, 0, 0)` | Pure black serif & calligraphic mark |

---

## 🛠️ Dynamic Background Customization

The background field supports dynamic, instant recoloring via CSS custom variables or direct SVG manipulation:

```css
/* Change background field via CSS variables */
svg {
  --field-color: #111111; /* Switch to Obsidian Black */
}
```

Or via JavaScript in web applications:
```javascript
const flagSvg = document.querySelector('svg');
flagSvg.style.setProperty('--field-color', '#0D1B2A'); // Midnight Navy
```

---

## 📁 Repository & File Inventory

- [`flag.svg`](flag.svg): Production-grade master vector flag with inline CSS variable support.
- [`index.html`](index.html): Interactive browser preview with real-time color switcher and SVG export.
- [`DESIGN_SPECIFICATION.md`](DESIGN_SPECIFICATION.md): Mathematical geometry, coordinates, and rendering standards.
- [`LICENSE`](LICENSE): Official MIT Open Source License.

---

## 🏛️ Statutory Trademark & Brand Notice

© 2026 HRL International Private Limited. Chief Architect: Pavan Kumar Sadashiv.  
All brand insignias, flag designs, and visual identity systems are proprietary assets protected under applicable statutory intellectual property frameworks.
