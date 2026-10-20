# HRL International Official Corporate Flag - Mathematical & Design Specification

## 1. Dimensional Standards & Coordinate System
- **Total Resolution**: 1024 × 682 px
- **Standard Aspect Ratio**: 3:2 (Exact: 1.5015 : 1)
- **Modular Unit Grid**: $\mathbf{U} = 83\text{ px}$
- **Coordinate System**: SVG Origin $(0, 0)$ top-left, $+X$ horizontal right, $+Y$ vertical down.

## 2. Mathematical Geometry & Placement

### A. The Nordic Cross
- **Vertical Cross Stripe**:
  - Top-left: $(85, 0)$
  - Dimensions: $W = 83\text{ px}$, $H = 682\text{ px}$
  - Color: Pure White (`#FFFFFF`, `rgb(255, 255, 255)`)
- **Horizontal Cross Stripe**:
  - Top-left: $(0, 297)$
  - Dimensions: $W = 1024\text{ px}$, $H = 83\text{ px}$
  - Color: Pure White (`#FFFFFF`, `rgb(255, 255, 255)`)

### B. Canton Hoist Stripes
Positioned in the upper hoist quadrant immediately adjacent to the vertical cross stripe $(x: 168..240, y: 0..297)$:
- **Stripe 1**: $X = 168$, $W = 10\text{ px}$, $H = 297\text{ px}$, Fill `#000000`
- **Gap 1**: $X = 178$, $W = 12\text{ px}$, Fill `#BF1F1F` (Red Field)
- **Stripe 2**: $X = 190$, $W = 9\text{ px}$, $H = 297\text{ px}$, Fill `#000000`
- **Gap 2**: $X = 199$, $W = 11\text{ px}$, Fill `#BF1F1F`
- **Stripe 3**: $X = 210$, $W = 10\text{ px}$, $H = 297\text{ px}$, Fill `#000000`
- **Gap 3**: $X = 220$, $W = 12\text{ px}$, Fill `#BF1F1F`
- **Stripe 4**: $X = 232$, $W = 8\text{ px}$, $H = 297\text{ px}$, Fill `#000000`

### C. Official HRL Brand Insignia
Superimposed along the horizontal white cross bar $(y: 297..380)$:
- **Corporate Initial 'H'**:
  - Bounding Box: $X \in [32, 84]$, $Y \in [310, 355]$
  - Color: Crimson Red (`#BF1F1F`, matching field)
  - Features: Slab serif top-left flag, dual vertical stems, center crossbar.
- **Corporate Mark 'RL'**:
  - Bounding Box: $X \in [104, 219]$, $Y \in [312, 366]$
  - Color: Solid Black (`#000000`)
  - Features: Classical high-contrast serif 'R' transitioning into fluid calligraphic script 'L' with sweeping horizontal baseline terminal.

### D. Lower Hoist Heraldic Triad
Positioned symmetrically across the three lower hoist units beneath the horizontal cross:
- **Left Emblem - Double-Headed Heraldic Eagle**:
  - Bounding Box: $X \in [6, 77]$, $Y \in [386, 467]$ (Width 71px, Height 81px)
  - Color: Solid Black (`#000000`)
  - Sits on: Sovereign Red Field
- **Center Emblem - 8-Pointed Compass Star**:
  - Center: $(125.5, 428.0)$
  - Cardinal Point Extents: Radius $R_1 \approx 44\text{ px}$ (Tips at $(125, 384)$, $(126, 472)$, $(86, 428)$, $(165, 428)$)
  - Diagonal Point Extents: Radius $R_2 \approx 22.5\text{ px}$ (Tips at $(103, 405)$, $(148, 405)$, $(103, 450)$, $(148, 450)$)
  - Color: Crimson Red (`#BF1F1F`)
  - Sits on: White Vertical Cross Bar
- **Right Emblem - Double-Headed Heraldic Eagle**:
  - Bounding Box: $X \in [177, 247]$, $Y \in [384, 464]$ (Width 70px, Height 80px)
  - Color: Solid Black (`#000000`)
  - Sits on: Sovereign Red Field

## 3. Official Color Swatches
| Name | Hex | sRGB | CMYK (Approx) | Pantone (Approx) |
| :--- | :--- | :--- | :--- | :--- |
| **HRL Crimson Red** | `#BF1F1F` | `191, 31, 31` | `0, 84, 84, 25` | PMS 186 C |
| **Stark White** | `#FFFFFF` | `255, 255, 255` | `0, 0, 0, 0` | Opaque White |
| **Abyssal Black** | `#000000` | `0, 0, 0` | `0, 0, 0, 100` | Process Black C |

## 4. Software Implementation & Architecture
- **Root Elements**: Pure SVG XML namespace with `viewBox="0 0 1024 682"`.
- **CSS Variable Hooks**:
  ```css
  :root {
    --field-color: #BF1F1F;
    --cross-color: #FFFFFF;
    --stripe-color: #000000;
    --emblem-dark: #000000;
    --emblem-red: #BF1F1F;
  }
  ```
- **Fallback Attributes**: Hardcoded inline `fill` attributes on all elements guarantee 100% rendering fidelity even in restricted markdown rendering environments (e.g. GitHub/GitLab READMEs) where CSS variables may be stripped.
