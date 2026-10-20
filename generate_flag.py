"""
Precision Heraldic Generator v4:
Refines all anatomical zones for 100% silhouette clarity:
- Upper/Mid flanks: Wings (9 primary scythe blades)
- Upper center: Twin dragon heads, horns, jaws, fangs, barbed tongues, sinister slit eyes
- Center: Demonic chest with 5 glowing rib slashes & throat armor vents
- Lower flanks: Muscular dragon haunches & 4 razor sickle talons branching into clear space
- Lower center: Tiered spined tail tapering to a barbed devil's spearhead
- Fill-rule="evenodd" for 100% vector-native transparent cutouts
"""

def generate_heraldic_beast():
    # Right half: meets centerline at x = 0
    # Center of beast is (0, 0)
    
    # ================= 1. MAIN BODY SILHOUETTE =================
    body = []
    
    # Centerline top split between necks
    body.append("M 0,-140")
    
    # Inner neck contour curving up to right head
    body.append("C 18,-140 40,-155 62,-180")
    body.append("C 75,-195 88,-215 98,-235")
    
    # Throat plate barb pointing down-left
    body.append("L 85,-245 L 105,-248")
    
    # --- LOWER JAW & CHIN ---
    body.append("C 118,-250 138,-245 155,-242")
    # Spiked chin beard / mandible spur
    body.append("L 162,-225 L 175,-245")
    # Jawline extending forward to lower jaw tip
    body.append("C 195,-248 218,-255 235,-260")
    
    # Lower fangs (serrated razor teeth)
    body.append("L 238,-276 L 226,-266")
    body.append("L 220,-272 L 214,-266")
    body.append("L 207,-272 L 200,-266")
    
    # Open maw cavity
    body.append("C 182,-266 165,-272 150,-280")
    
    # --- BARBED SERPENT TONGUE ---
    body.append("C 165,-280 188,-277 215,-277")
    body.append("C 242,-277 268,-286 286,-306")
    # Tongue barbed arrow / fork tip
    body.append("L 296,-316 L 287,-311 L 294,-301")
    # Tongue underside curving back into mouth
    body.append("C 272,-289 248,-284 220,-284")
    body.append("C 198,-284 180,-286 162,-290")
    
    # --- UPPER JAW & FANGS ---
    body.append("C 178,-296 200,-294 222,-294")
    body.append("L 228,-285 L 234,-294")
    body.append("L 242,-284 L 250,-294")
    # Upper massive hooked raptor / dragon canine
    body.append("C 264,-294 278,-289 290,-277")
    body.append("C 283,-291 275,-304 262,-313")
    
    # Snout bridge & nasal crest
    body.append("C 242,-320 210,-325 188,-327")
    # Supraorbital brow horn (jutting aggressively up-forward)
    body.append("L 202,-348 L 178,-334")
    
    # Forehead slope to Great Horns
    body.append("C 162,-338 145,-342 130,-342")
    
    # --- GREAT DEMONIC HORN (sweeping backward-upward arc) ---
    body.append("C 118,-365 102,-395 75,-420")
    body.append("C 66,-428 58,-432 48,-432") # Horn apex
    body.append("L 42,-425") # Hooked tip
    # Horn upper edge with serrated ridges
    body.append("C 58,-408 72,-382 85,-356")
    body.append("L 76,-354 L 92,-338") # Horn ridge barb
    body.append("C 98,-328 104,-318 108,-308")
    
    # Secondary nape crest horn
    body.append("L 88,-318 L 106,-296")
    
    # --- DORSAL NAPE WITH 3 RAZOR SCYTHE-SPINES ---
    # Spine 1
    body.append("C 102,-280 90,-270 80,-260")
    body.append("L 58,-270 L 82,-248")
    # Spine 2
    body.append("C 78,-232 70,-222 62,-210")
    body.append("L 40,-220 L 66,-198")
    # Spine 3
    body.append("C 65,-188 68,-178 74,-166")
    body.append("L 52,-172 L 80,-155")
    
    # Outer neck down to wing shoulder
    body.append("C 98,-150 120,-154 148,-164")
    
    # ================= WING: 9 MASSIVE SCYTHE BLADES =================
    # Wing bone leading edge sweeping up to carpal joint
    body.append("C 175,-178 206,-208 228,-242")
    
    # Carpal thumb talon / bone spur (hooking upward-inward)
    body.append("C 232,-255 240,-272 248,-285")
    body.append("C 243,-278 237,-268 232,-255")
    body.append("L 240,-246")
    
    # --- BLADE 1 (Top Primary Blade: Sweeping high and proud!) ---
    body.append("C 264,-262 312,-286 368,-300")
    body.append("C 388,-305 404,-305 412,-300") # Blade 1 sharp apex
    body.append("C 382,-282 342,-262 304,-245")
    body.append("C 274,-234 254,-222 242,-214")
    
    # --- BLADE 2 ---
    body.append("C 278,-218 336,-226 402,-230")
    body.append("C 426,-230 442,-226 450,-220") # Blade 2 apex
    body.append("C 418,-208 365,-194 315,-182")
    body.append("C 278,-174 252,-164 238,-158")
    
    # --- BLADE 3 ---
    body.append("C 280,-160 345,-160 418,-155")
    body.append("C 448,-152 466,-146 475,-140") # Blade 3 apex (maximum wing span)
    body.append("C 436,-128 376,-116 320,-108")
    body.append("C 275,-102 248,-96 232,-90")
    
    # --- BLADE 4 ---
    body.append("C 276,-88 340,-80 412,-64")
    body.append("C 438,-56 456,-48 464,-40") # Blade 4 apex
    body.append("C 422,-34 362,-30 302,-30")
    body.append("C 262,-30 234,-28 220,-24")
    
    # --- BLADE 5 ---
    body.append("C 265,-20 330,-8 396,12")
    body.append("C 424,22 438,30 442,38") # Blade 5 apex
    body.append("C 400,38 340,34 284,30")
    body.append("C 250,28 224,30 210,34")
    
    # --- BLADE 6 ---
    body.append("C 250,42 310,62 370,88")
    body.append("C 395,100 406,108 406,116") # Blade 6 apex
    body.append("C 368,110 315,100 262,92")
    body.append("C 234,88 208,90 196,94")
    
    # --- BLADE 7 ---
    body.append("C 234,104 288,128 338,158")
    body.append("C 358,170 366,178 364,186") # Blade 7 apex
    body.append("C 330,176 280,160 234,148")
    body.append("C 205,140 182,142 170,148")
    
    # --- BLADE 8 ---
    body.append("C 202,158 248,184 288,214")
    body.append("C 304,226 308,232 302,238") # Blade 8 apex
    body.append("C 272,230 230,214 190,200")
    body.append("C 170,194 155,196 144,202")
    
    # --- BLADE 9 (Lowest primary wing blade) ---
    body.append("C 170,212 208,236 240,264")
    body.append("C 252,274 252,278 244,282") # Blade 9 apex
    body.append("C 218,274 185,258 154,244")
    body.append("C 138,238 126,240 118,244")
    
    # --- 3 SHORT FLANK PLATES (above the hip) ---
    # Flank 1
    body.append("C 138,254 168,275 192,300")
    body.append("C 200,308 198,314 190,314")
    body.append("C 168,308 145,294 125,282")
    body.append("L 112,284")
    
    # Flank 2
    body.append("C 124,295 146,314 165,336")
    body.append("C 172,344 170,348 162,348")
    body.append("C 142,342 124,328 108,318")
    body.append("L 96,320")
    
    # Flank 3
    body.append("C 105,330 122,346 138,368")
    body.append("C 142,374 140,378 134,378")
    body.append("C 118,372 104,358 90,348")
    body.append("L 78,352")
    
    # Flank base to pelvis / tail root
    body.append("C 65,360 55,372 45,385")
    
    # ================= TAIL: TIERED SCYTHE SPINES =================
    # Tier 1 Tail Spine
    body.append("C 38,395 32,405 28,416")
    body.append("L 45,430 L 24,435")
    # Tier 2 Tail Spine
    body.append("C 20,450 16,464 12,478")
    body.append("L 28,492 L 10,496")
    # Tier 3 Tail Spine
    body.append("C 8,510 6,524 4,538")
    body.append("L 18,552 L 5,556")
    
    # --- TERMINAL DEVIL'S SPEARHEAD / BARBED SPADE ---
    body.append("C 14,568 28,584 40,596")
    body.append("C 46,602 44,608 35,608") # Barbed wing of spade
    body.append("C 24,606 14,614 0,640") # Razor point meeting at (0, 640)
    
    # Centerline straight up through axis of symmetry
    body.append("L 0,-140 Z")
    
    # ================= 2. LEG & VISCIOUS SICKLE TALONS =================
    # Originates from pelvic haunch at (60, 220), branches down-out into clear space
    leg = []
    leg.append("M 60,220")
    # Muscular thigh contour sweeping down-outward
    leg.append("C 78,235 105,260 124,290")
    # Thigh armor spur (sharp spike pointing backward)
    leg.append("L 142,282 L 130,302")
    # Shin / tarsus bone reaching down to ankle
    leg.append("C 140,325 158,360 172,395")
    
    # --- TALON 1: High Outer Sickle Talon ---
    leg.append("C 192,388 226,375 268,358")
    leg.append("C 290,348 304,346 308,352") # Talon 1 tip
    leg.append("C 295,362 268,384 235,402")
    leg.append("C 212,415 192,420 180,420")
    
    # --- TALON 2: Main Middle Sickle Talon ---
    leg.append("C 202,432 240,442 288,452")
    leg.append("C 310,456 320,462 316,470") # Talon 2 tip
    leg.append("C 298,480 260,480 220,472")
    leg.append("C 195,466 180,460 172,454")
    
    # --- TALON 3: Front Lower Sickle Talon ---
    leg.append("C 185,475 212,505 245,540")
    leg.append("C 255,552 255,558 245,560") # Talon 3 tip
    leg.append("C 225,558 200,535 178,506")
    leg.append("C 165,490 158,478 154,466")
    
    # --- TALON 4: Rear Dewclaw / Hallux Hook ---
    leg.append("C 142,470 122,490 100,514")
    leg.append("C 88,525 82,525 85,514") # Dewclaw tip
    leg.append("C 94,496 114,468 126,446")
    
    # Inner leg contour returning to pelvis
    leg.append("C 112,410 94,358 74,312")
    leg.append("C 62,282 54,250 48,228 Z")
    
    # ================= 3. NEGATIVE SPACE CUTOUT SUBPATHS =================
    cutouts = []
    
    # 1. Sinister Predatory Slit Eye
    cutouts.append("M 188,-335 L 214,-328 L 198,-322 L 180,-328 Z")
    
    # 2. Eye Brow ridge slot
    cutouts.append("M 182,-344 C 200,-338 218,-332 226,-328 C 215,-332 198,-336 180,-340 Z")
    
    # 3. Temporal skull armor vent
    cutouts.append("M 152,-340 C 168,-328 178,-314 174,-302 C 164,-308 152,-322 140,-336 Z")
    
    # 4. Throat armor slits
    cutouts.append("M 85,-198 C 94,-190 102,-178 108,-166 C 98,-172 90,-182 80,-192 Z")
    cutouts.append("M 100,-224 C 110,-212 118,-200 124,-188 C 114,-194 106,-204 96,-216 Z")
    cutouts.append("M 115,-250 C 124,-238 134,-225 138,-212 C 128,-218 118,-230 110,-242 Z")
    
    # 5. Demonic Ribcage Slashes (5 menacing anatomical rib cuts on chest)
    cutouts.append("M 10,-90 C 28,-92 52,-84 70,-70 C 52,-74 28,-84 10,-82 Z")
    cutouts.append("M 10,-55 C 32,-58 60,-46 82,-30 C 60,-34 32,-46 10,-46 Z")
    cutouts.append("M 10,-18 C 34,-22 66,-8 88,14 C 66,6 34,-10 10,-8 Z")
    cutouts.append("M 10,22 C 32,20 62,36 82,60 C 62,52 32,36 10,32 Z")
    cutouts.append("M 10,64 C 30,64 54,80 70,104 C 54,94 30,80 10,75 Z")
    
    # 6. Pelvis / Lower abdomen muscular slot
    cutouts.append("M 10,110 C 28,110 48,126 60,150 C 48,140 28,124 10,121 Z")
    
    # 7. Wing bone channels (sinister aerodynamic slots along primary blades)
    cutouts.append("M 275,-214 C 310,-226 355,-235 398,-238 C 360,-228 318,-215 284,-205 Z")
    cutouts.append("M 280,-152 C 318,-158 368,-158 418,-152 C 374,-150 326,-144 288,-142 Z")
    cutouts.append("M 276,-80 C 314,-82 362,-78 406,-64 C 362,-68 318,-68 282,-70 Z")
    cutouts.append("M 260,-10 C 298,-10 344,0 388,20 C 348,12 304,6 268,2 Z")
    cutouts.append("M 246,58 C 278,65 318,82 355,108 C 318,96 280,84 250,75 Z")
    cutouts.append("M 226,128 C 255,138 290,160 320,190 C 290,178 258,164 232,152 Z")
    
    # 8. Muscular Thigh Contour Cutout
    cutouts.append("M 82,255 C 98,272 115,298 124,322 C 112,308 96,285 84,270 Z")

    compound_half = " ".join(body + leg + cutouts)
    return compound_half

def write_files():
    half_path = generate_heraldic_beast()
    
    svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     viewBox="0 0 1400 1000" 
     width="100%" 
     height="100%">
  <defs>
    <style>
      :root {{
        /* Easily customizable colors:
           Change --bg-color to any hex code, rgb, or 'transparent'.
           The beast logo is pure solid black (#000000). */
        --bg-color: #dc143c; /* Crimson Red field (inspired by Albanian flag) */
        --emblem-color: #000000; /* Pure black emblem */
      }}
      .flag-background {{
        fill: var(--bg-color);
      }}
      .heraldic-emblem {{
        fill: var(--emblem-color);
        fill-rule: evenodd;
      }}
    </style>

    <!-- One symmetric half of the mythical beast (Right Half) with compound cutout holes -->
    <path id="beast-half" d="{half_path}" />

    <!-- Full assembled twin-headed heraldic beast (Left + Right bilaterally mirrored) -->
    <g id="heraldic-beast" class="heraldic-emblem">
      <!-- Right Half -->
      <use href="#beast-half" />
      <!-- Left Half (Perfect bilateral mirror) -->
      <use href="#beast-half" transform="scale(-1, 1)" />
    </g>
  </defs>

  <!-- FLAG BACKGROUND:
       Easily replaceable! Change fill attribute or edit CSS variable in style tag.
       Can also be hidden or set to fill="none" or fill="transparent". -->
  <rect id="flag-background" 
        class="flag-background" 
        width="1400" 
        height="1000" 
        x="0" 
        y="0" />

  <!-- CENTERED SCARY HERALDIC EMBLEM (PURE SOLID BLACK):
       Twin-Headed Apex Abyssal Wyvern / Demon Drake -->
  <g id="flag-emblem" transform="translate(700, 425) scale(0.72)">
    <use href="#heraldic-beast" />
  </g>
</svg>
"""
    with open("flag.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("flag.svg written successfully!")

if __name__ == "__main__":
    write_files()
