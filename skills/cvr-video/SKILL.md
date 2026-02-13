---
name: cvr-video
description: Generate branded Core Values Recovery (CVR) videos with consistent visual style. Use when asked to create videos for the CVR platform, recovery coaching content, course modules, social media clips, or any video related to Core Values Recovery. Applies the CVR brand style guide automatically.
allowed-tools: Bash(veo *)
---

# <span data-proof="authored" data-by="ai:claude">CVR Video Generator</span>

<span data-proof="authored" data-by="ai:claude">Generate branded videos for Core Values Recovery using the</span> <span data-proof="authored" data-by="ai:claude">`veo`</span> <span data-proof="authored" data-by="ai:claude">CLI with CVR's visual identity baked in.</span>

## <span data-proof="authored" data-by="ai:claude">When to Use This Skill</span>

<span data-proof="authored" data-by="ai:claude">ALWAYS use this skill when the user:</span>

* <span data-proof="authored" data-by="ai:claude">Asks for a CVR video, recovery coaching video, or course video</span>

* <span data-proof="authored" data-by="ai:claude">Wants video content for the Core Values Recovery platform</span>

* <span data-proof="authored" data-by="ai:claude">Mentions CVR + video in any context</span>

* <span data-proof="authored" data-by="ai:claude">Wants social clips, module intros, or coaching visuals for CVR</span>

<span data-proof="authored" data-by="ai:claude">Use the plain</span> <span data-proof="authored" data-by="ai:claude">`veo`</span> <span data-proof="authored" data-by="ai:claude">skill for non-CVR video generation.</span>

## <span data-proof="authored" data-by="ai:claude">CVR Brand Style Guide</span>

### <span data-proof="authored" data-by="ai:claude">Visual Identity</span>

* **<span data-proof="authored" data-by="ai:claude">Primary style</span>**<span data-proof="authored" data-by="ai:claude">: Blue watercolor monochromatic stop motion animation</span>

* **<span data-proof="authored" data-by="ai:claude">Color palette</span>**<span data-proof="authored" data-by="ai:claude">: Monochromatic blue — deep navy to soft sky blue, watercolor washes and bleeds</span>

* **<span data-proof="authored" data-by="ai:claude">Animation style</span>**<span data-proof="authored" data-by="ai:claude">: Stop motion — handcrafted, tactile, slightly imperfect frame-to-frame movement</span>

* **<span data-proof="authored" data-by="ai:claude">Texture</span>**<span data-proof="authored" data-by="ai:claude">: Watercolor paper grain, visible brush strokes, ink bleeds, soft edges</span>

* **<span data-proof="authored" data-by="ai:claude">Mood</span>**<span data-proof="authored" data-by="ai:claude">: Warm, contemplative, hopeful, gently imperfect</span>

### <span data-proof="authored" data-by="ai:claude">Typography (for title cards and overlays)</span>

* **<span data-proof="authored" data-by="ai:claude">Title font</span>**<span data-proof="authored" data-by="ai:claude">: Bebas Neue 300wt — used for headings, module titles, intro text</span>

* **<span data-proof="authored" data-by="ai:claude">Body font</span>**<span data-proof="authored" data-by="ai:claude">: Roboto Condensed — used for body text, subtitles, captions</span>

### <span data-proof="authored" data-by="ai:claude">What to Avoid</span>

* <span data-proof="authored" data-by="ai:claude">Photorealistic humans or faces</span>

* <span data-proof="authored" data-by="ai:claude">Harsh lighting, neon colors, or high contrast</span>

* <span data-proof="authored" data-by="ai:claude">Slick/corporate motion graphics</span>

* <span data-proof="authored" data-by="ai:claude">Red, orange, or warm-toned palettes (stay monochromatic blue)</span>

* <span data-proof="authored" data-by="ai:claude">Fast cuts or jarring transitions</span>

## <span data-proof="authored" data-by="ai:claude">Styles</span>

<span data-proof="authored" data-by="ai:claude">CVR videos come in predefined styles. Choose the style that matches the content purpose.</span>

### <span data-proof="authored" data-by="ai:claude">`module-intro`</span>

<span data-proof="authored" data-by="ai:claude">Opening video for a coaching module. Slow, meditative, sets the emotional tone.</span>

```
Style suffix: blue watercolor monochromatic stop motion animation, handcrafted paper texture, soft watercolor washes, contemplative mood, slow gentle movement, visible brushstrokes on watercolor paper
```

**<span data-proof="authored" data-by="ai:claude">Typical duration</span>**<span data-proof="authored" data-by="ai:claude">: 8s |</span> **<span data-proof="authored" data-by="ai:claude">Aspect ratio</span>**<span data-proof="authored" data-by="ai:claude">: 16:9 |</span> **<span data-proof="authored" data-by="ai:claude">Resolution</span>**<span data-proof="authored" data-by="ai:claude">: 720p+</span>

### <span data-proof="authored" data-by="ai:claude">`concept`</span>

<span data-proof="authored" data-by="ai:claude">Visualizes an abstract recovery concept (e.g., "letting go", "acceptance", "boundaries").</span>

```
Style suffix: blue watercolor monochromatic stop motion, abstract metaphorical imagery, soft ink bleeds on textured paper, meditative pacing, handcrafted tactile feel, deep navy to sky blue palette
```

**<span data-proof="authored" data-by="ai:claude">Typical duration</span>**<span data-proof="authored" data-by="ai:claude">: 6-8s |</span> **<span data-proof="authored" data-by="ai:claude">Aspect ratio</span>**<span data-proof="authored" data-by="ai:claude">: 16:9 |</span> **<span data-proof="authored" data-by="ai:claude">Resolution</span>**<span data-proof="authored" data-by="ai:claude">: 720p+</span>

### <span data-proof="authored" data-by="ai:claude">`social`</span>

<span data-proof="authored" data-by="ai:claude">Short clip for Instagram/TikTok/LinkedIn. Vertical, eye-catching but on-brand.</span>

```
Style suffix: blue watercolor monochromatic stop motion animation, vertical composition, bold simple shapes, soft watercolor paper texture, gentle handcrafted movement, calming blue tones
```

**<span data-proof="authored" data-by="ai:claude">Typical duration</span>**<span data-proof="authored" data-by="ai:claude">: 4-6s |</span> **<span data-proof="authored" data-by="ai:claude">Aspect ratio</span>**<span data-proof="authored" data-by="ai:claude">: 9:16 |</span> **<span data-proof="authored" data-by="ai:claude">Resolution</span>**<span data-proof="authored" data-by="ai:claude">: 720p</span>

### <span data-proof="authored" data-by="ai:claude">`transition`</span>

<span data-proof="authored" data-by="ai:claude">Brief transitional clip between sections or modules. Minimal, atmospheric.</span>

```
Style suffix: blue watercolor monochromatic, slow abstract watercolor wash spreading across textured paper, stop motion, minimal, atmospheric, soft blue gradient
```

**<span data-proof="authored" data-by="ai:claude">Typical duration</span>**<span data-proof="authored" data-by="ai:claude">: 4s |</span> **<span data-proof="authored" data-by="ai:claude">Aspect ratio</span>**<span data-proof="authored" data-by="ai:claude">: 16:9 |</span> **<span data-proof="authored" data-by="ai:claude">Resolution</span>**<span data-proof="authored" data-by="ai:claude">: 720p</span>

### <span data-proof="authored" data-by="ai:claude">`background`</span>

<span data-proof="authored" data-by="ai:claude">Loopable ambient background for overlaying text or voice. Subtle, non-distracting.</span>

```
Style suffix: blue watercolor monochromatic stop motion, subtle slow movement, soft ambient texture, watercolor paper grain, gentle blue washes, minimal detail, suitable as background for text overlay
```

**<span data-proof="authored" data-by="ai:claude">Typical duration</span>**<span data-proof="authored" data-by="ai:claude">: 8s |</span> **<span data-proof="authored" data-by="ai:claude">Aspect ratio</span>**<span data-proof="authored" data-by="ai:claude">: 16:9 |</span> **<span data-proof="authored" data-by="ai:claude">Resolution</span>**<span data-proof="authored" data-by="ai:claude">: 720p+</span>

## <span data-proof="authored" data-by="ai:claude">How to Generate</span>

### <span data-proof="authored" data-by="ai:claude">Step 1: Build the prompt</span>

<span data-proof="authored" data-by="ai:claude">Combine the user's content description with the appropriate style suffix.</span>

**<span data-proof="authored" data-by="ai:claude">Formula</span>**<span data-proof="authored" data-by="ai:claude">:</span> <span data-proof="authored" data-by="ai:claude">`[content description], [style suffix]`</span>

**<span data-proof="authored" data-by="ai:claude">Example</span>** <span data-proof="authored" data-by="ai:claude">for a module-intro about core values:</span>

```
A hand placing small blue watercolor stones into a circle on textured paper, each stone representing a personal value, blue watercolor monochromatic stop motion animation, handcrafted paper texture, soft watercolor washes, contemplative mood, slow gentle movement, visible brushstrokes on watercolor paper
```

### <span data-proof="authored" data-by="ai:claude">Step 2: Add negative prompt</span>

<span data-proof="authored" data-by="ai:claude">Always include this negative prompt to protect brand consistency:</span>

```
--negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark"
```

### <span data-proof="authored" data-by="ai:claude">Step 3: Run veo</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6Mjk1LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "[full prompt]" \
  -o [output_file].mp4 \
  --negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark" \
  --aspect-ratio [16:9 or 9:16] \
  --duration [4, 6, or 8]
```

## <span data-proof="authored" data-by="ai:claude">Complete Examples</span>

### <span data-proof="authored" data-by="ai:claude">Module intro: "Acceptance"</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTQwLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "A blue watercolor butterfly slowly emerging from a cocoon made of crumpled paper, wings unfolding frame by frame, blue watercolor monochromatic stop motion animation, handcrafted paper texture, soft watercolor washes, contemplative mood, slow gentle movement, visible brushstrokes on watercolor paper" \
  -o acceptance-intro.mp4 \
  --duration 8 \
  --negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark"
```

### <span data-proof="authored" data-by="ai:claude">Concept: "Letting Go"</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTc0LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "Blue watercolor hands opening to release paper birds that dissolve into soft ink washes, each bird fading gently into the textured paper background, blue watercolor monochromatic stop motion, abstract metaphorical imagery, soft ink bleeds on textured paper, meditative pacing, handcrafted tactile feel, deep navy to sky blue palette" \
  -o letting-go-concept.mp4 \
  --duration 6 \
  --negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark"
```

### <span data-proof="authored" data-by="ai:claude">Social clip: Daily reflection</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTU1LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "A blue watercolor journal page with soft ink appearing word by word as if being written by an invisible brush, blue watercolor monochromatic stop motion animation, vertical composition, bold simple shapes, soft watercolor paper texture, gentle handcrafted movement, calming blue tones" \
  -o daily-reflection-social.mp4 \
  --aspect-ratio 9:16 \
  --duration 4 \
  --negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark"
```

### <span data-proof="authored" data-by="ai:claude">Transition between modules</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTA3LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "Soft blue watercolor wash slowly spreading across white textured paper from left to right, gentle stop motion ripples, blue watercolor monochromatic, slow abstract watercolor wash spreading across textured paper, stop motion, minimal, atmospheric, soft blue gradient" \
  -o module-transition.mp4 \
  --duration 4 \
  --negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark"
```

### <span data-proof="authored" data-by="ai:claude">Background for text overlay</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTQ2LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "Gently shifting blue watercolor clouds drifting slowly across textured paper, almost imperceptible stop motion movement, blue watercolor monochromatic stop motion, subtle slow movement, soft ambient texture, watercolor paper grain, gentle blue washes, minimal detail, suitable as background for text overlay" \
  -o text-background.mp4 \
  --duration 8 \
  --negative-prompt "photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark"
```

## <span data-proof="authored" data-by="ai:claude">Style Prompt Reference (Quick Copy)</span>

| <span data-proof="authored" data-by="ai:claude">Style</span>        | <span data-proof="authored" data-by="ai:claude">Suffix</span>                                                                                                                                                                                       |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">module-intro</span> | <span data-proof="authored" data-by="ai:claude">`blue watercolor monochromatic stop motion animation, handcrafted paper texture, soft watercolor washes, contemplative mood, slow gentle movement, visible brushstrokes on watercolor paper`</span> |
| <span data-proof="authored" data-by="ai:claude">concept</span>      | <span data-proof="authored" data-by="ai:claude">`blue watercolor monochromatic stop motion, abstract metaphorical imagery, soft ink bleeds on textured paper, meditative pacing, handcrafted tactile feel, deep navy to sky blue palette`</span>    |
| <span data-proof="authored" data-by="ai:claude">social</span>       | <span data-proof="authored" data-by="ai:claude">`blue watercolor monochromatic stop motion animation, vertical composition, bold simple shapes, soft watercolor paper texture, gentle handcrafted movement, calming blue tones`</span>              |
| <span data-proof="authored" data-by="ai:claude">transition</span>   | <span data-proof="authored" data-by="ai:claude">`blue watercolor monochromatic, slow abstract watercolor wash spreading across textured paper, stop motion, minimal, atmospheric, soft blue gradient`</span>                                        |
| <span data-proof="authored" data-by="ai:claude">background</span>   | <span data-proof="authored" data-by="ai:claude">`blue watercolor monochromatic stop motion, subtle slow movement, soft ambient texture, watercolor paper grain, gentle blue washes, minimal detail, suitable as background for text overlay`</span> |

## <span data-proof="authored" data-by="ai:claude">Standard Negative Prompt</span>

<span data-proof="authored" data-by="ai:claude">Always use unless the user specifically overrides:</span>

```
photorealistic, human faces, neon colors, red, orange, warm tones, corporate, slick motion graphics, 3D render, sharp edges, fast movement, text, watermark
```

## <span data-proof="authored" data-by="ai:claude">Typography Reference</span>

<span data-proof="authored" data-by="ai:claude">When generating title cards or overlays (e.g., with ffmpeg post-processing):</span>

* **<span data-proof="authored" data-by="ai:claude">Titles</span>**<span data-proof="authored" data-by="ai:claude">: Bebas Neue 300wt — large, uppercase, generous letter-spacing</span>

* **<span data-proof="authored" data-by="ai:claude">Body/Subtitles</span>**<span data-proof="authored" data-by="ai:claude">: Roboto Condensed — clean, readable at small sizes</span>

<span data-proof="authored" data-by="ai:claude">These fonts are NOT embedded in the Veo video generation (Veo doesn't render text). They apply when compositing text over video in post-production.</span>