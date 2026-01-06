# Set-of-Mark (SoM) Prompting — Simple Explanation + OS/GUI Notes

This README explains **Set-of-Mark (SoM) prompting** from the paper *“Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V”* in plain language: what it is, why it helps, how it works, where it applies (web/GUI + general OS), and key limitations.

---

## What problem is SoM solving?

Multimodal models like GPT-4V can describe an image, but they often struggle with **visual grounding**: being *precise about where* something is in an image when there are many objects/UI elements.

A common approach is to ask the model to output **coordinates** (boxes/points), but mixing free-form language with precise numeric outputs is brittle and often performs poorly.

**SoM’s idea:** don’t force coordinates—give the model **visible IDs** it can read and refer to.

---

## Key terms (plain English)

### Visual grounding
**Grounding** = linking words to the correct part of an image.
Example: “Click the ‘Save’ button” requires identifying the right pixels/UI element, not guessing.

### Segmentation
**Segmentation** = splitting an image into meaningful pieces *at the pixel level*.
Instead of just drawing a loose box around an object, segmentation identifies the object’s pixels.

### Mask
A **mask** is the computer representation of a segmented region:
- a pixel map where pixels inside the region are “on” and pixels outside are “off”
- often called a **binary mask** (0/1)

### Region
A **region** is one segmented piece (e.g., a button, icon, person, mug, etc.).
SoM uses many regions per image.

### Segmentation tools
“Segmentation tools” are models/systems that produce masks/regions automatically or with minimal interaction.
The paper uses off-the-shelf segmentation methods (a toolbox of different ones) to get regions at different granularities (big objects vs smaller parts).

---

## What is Set-of-Mark (SoM) prompting?

**SoM prompting** = take an image, partition it into regions, and overlay a unique “mark” (usually a number/letter) onto each region so the model can *say the mark*.

Instead of:
- “The button is at x=421, y=88…”

You get:
- “It’s region 7.”

**Core trick:** marks are **“speakable”** (easy to read + easy to mention in text).

---

## How SoM works (pipeline)

### 1) Partition the image into regions (make masks)
Use segmentation tools to split the image into many regions.
Each region has a mask.

### 2) Overlay marks (IDs) on regions
Add labels like:
- numbers (1, 2, 3…)
- letters (A, B, C…)
Optionally also add visual cues like boxes/boundaries.

The goal is: the model can visually read “7” and reference it in language.

### 3) Prompt the model in one of two styles

**A) Plain prompt**
Ask normally. The model may still refer to marks naturally.

**B) Interleaved prompt**
Explicitly reference marks:
- “What is region 12?”
- “Which region is the ‘Save’ button?”
- “Click region 5.”

---

## Does it only work for web/GUI? What about general OS tasks?

SoM is **not limited to web/GUI**. It applies to any task where the state can be represented visually (screenshots/photos/video frames).

### For OS / desktop tasks
A typical loop looks like:

1. Take a screenshot of the current screen
2. Partition into regions (icons/buttons/windows/text blocks)
3. Overlay marks (SoM image)
4. Ask the model which region to interact with
5. Map the region back to an actionable target (e.g., click point / bounding box)
6. Execute via an external controller (mouse/keyboard automation)

SoM improves the **“which thing is it?”** step (grounding).
You still need a **tool/controller layer** to actually click/type.

---

## Why SoM helps (intuition)

Coordinates are fragile and unnatural for language models.
SoM converts “point to it” into “name it”:

- Hard: output exact numbers for a location
- Easier: read a visible ID and mention it in text

SoM turns visual grounding into a symbolic reference problem:
**region ↔ mark ↔ text**

---

## Mark placement (why it matters)

If marks overlap or sit on ambiguous boundaries, the model can get confused.

The paper proposes a placement heuristic:
- place marks in “safe” interior spots of each region
- avoid overlaps/collisions in dense scenes
- keep IDs unique

---

## Limitations / failure modes

### 1) Depends on the region generator (segmentation quality)
If segmentation tools miss an object/UI element (or split it poorly), SoM can’t label it correctly.

### 2) Mark type can conflict with image content
If the image already contains lots of numbers (spreadsheets, dashboards), adding numeric marks may confuse the model.
Same for text-heavy documents and letter marks.

### 3) Not all multimodal models show the same “mark understanding”
The paper reports this behavior works strongly with GPT-4V + SoM, but isn’t guaranteed across other models.

### 4) Dense scenes are harder
Crowded images cause mark collisions and small regions that are hard to label.

### 5) SoM improves grounding, not full agency
SoM doesn’t “do OS automation” by itself.
You still need:
- a way to take screenshots
- a way to overlay marks
- a way to execute clicks/keystrokes based on selected regions
- handling for non-visual state (permissions, filesystems, background processes, etc.)

---

## Practical guidance (quick checklist)

- ✅ Use SoM when: you need reliable “which object/element?” selection
- ✅ Use interleaved prompts (“region 7”) when precision matters
- ✅ Pick mark styles that won’t clash with the screen content
- ✅ Expect better results if regions/masks are high quality
- ❗ Don’t expect SoM alone to solve end-to-end OS tasks (it’s the grounding component)

---

## One-sentence takeaway

**SoM labels image regions with readable IDs so the model can refer to exact parts of the image reliably—making grounding easier for GUIs and general OS screenshots, but still dependent on good segmentation and an external action layer.**