# Xero Timesheet Guide: design logic

This document explains why the guide is built the way it is. Read it before you change anything.
It is written for two readers: a programmer who maintains the page, and an AI agent asked to edit it.

Last updated: 17 November 2026.

## 1. What this is, and who it is for

A one-page web guide that shows Matrix casual workers how to submit their hours and kilometres in Xero.

The reader:

- Is a short-term worker. Many have never used Xero.
- Is impatient. They want to get paid, not to read.
- Often reads the guide on a phone while Xero is open on a computer.
- May not have English as a first language.
- Comes back when something goes wrong, and wants to jump straight to one step.

Everything below follows from that reader.

## 2. Principles

### 2.1 Say each thing once, in the place where it is used

The goal is the highest information density that is still clear and complete. An impatient reader only
finishes the guide if nothing in it is repeated.

- A fact appears once in the flow, at the step where the reader acts on it. The Help page may point to it.
- A step has a `lead` sentence only when the lead says something the title and the points do not.
- No filler ("Two clicks.", "Look at the whole timesheet one more time.").
- Before adding a sentence, search the page for the same fact.

### 2.2 One step, one screen, one small set of actions

- Each step shows one picture and a short list of points.
- Numbered points match the numbered marks on the picture: point 2 is mark 2. A point without a mark is a dash.
- Coral points are "do not" or "watch out". Amber is "do this".
- If two steps happen on the same Xero page, they are one step (see B1).

### 2.3 Plain words, and one word for one thing

- Short sentences. Common words. No idioms.
- One name for each thing, everywhere: "your supervisor", "fortnight", "earnings rate", "the Xero Me phone app".
- The Xero website page is also called "Xero Me". B1 says so, because the Start page tells people not to use
  the Xero Me phone app.
- Button names are written exactly as Xero shows them.

### 2.4 The content comes from the owner, not from the page builder

Rules about pay, hours, kilometres and deadlines come from the company's instructions and from the owner
(Andrew Wang). Do not invent, guess or "improve" them. If a rule is unclear or looks wrong, do not change
the text: add it to section 9 and ask.

### 2.5 Real screenshots, not drawings

A simplified drawing of the Xero page was tried for B1 and rejected. Readers match what they see on their
screen against the guide, and a drawing leaves things out. Real screenshots are safer. Drawings are only a
stand-in where no screenshot exists yet (A3).

Do not copy Xero's own web pages (HTML, CSS, logo) into this project. Screenshots only.

### 2.6 Choose by screen width, not by device name

The page never asks "is this an iPhone?". It asks "how wide is the screen?". One breakpoint: 900 px.

| | Narrower than 900 px | 900 px and wider |
|---|---|---|
| Layout | One column, picture on top | Two columns, picture left, text right |
| Picture | Close-up pieces cut from the screenshot | The full screenshot |
| Tap on the picture | Opens the full screenshot | Opens the full screenshot |

A full Xero screenshot is about 1300 px wide. On a phone its text would be 3 to 4 px high. So the phone gets
close-ups: only the parts the step is about, stacked, with a gap between pieces. The gap is transparent in the
image file and takes the colour of the number gutter, so the pieces read as separate tiles in day and night mode.

### 2.7 Colour has meaning

| Colour | Meaning |
|---|---|
| Amber `#F2A93B` | Do this. Marks, numbers, the current step, the main button. |
| Coral `#D94A22` | Do not, or watch out. |
| Sage `#5E8F88` | Done, or correct. |
| Navy `#141B3C` | Text and ink. |

Do not add a new accent colour. A second orange next to amber and coral would blur these meanings.

### 2.8 One main button per page

`Next` is the only filled button on a step. It is the action every reader takes on every step.
`Play` is secondary (most readers never need it), so it has an amber ring but no fill.
On the Start page the main button is "No, first time", because most readers are new.

### 2.9 Animation must teach something

Motion is allowed only where it explains what to do. Three places:

1. **Pointer demo on a step.** A pointer visits mark 1, 2, 3. The visited box and its text point light up.
   - Eye = only check this.
   - Hand (index finger) = type or change something here.
   - Hand that presses twice, with a ring = click here.
   - It starts on mark 1. It does not fly in from somewhere else.
   - It plays by itself the first time a step is opened, and never before the picture is downloaded and laid out.
     `Play` replays it, and is switched off until the picture is ready.
2. **Swipe hint on the step strip.** A finger drags the strip once, to show it scrolls sideways.
3. **Zoom hint in the picture viewer.** Three slow steps: zoom in, move to the right side, zoom out. The finger
   marks and the picture are driven by the same progress value, so they always move together. First open only.

Rules for any animation here: slow enough to follow, in step with what it shows, stops the moment the reader
touches the screen, and never hides content.

Known trade-off: the pointer demo also plays when the device asks for reduced motion. The owner chose this
after it failed to play on an iPhone. The motion is small (a pointer moving inside the picture).

### 2.10 The reader is always in control of where they are

- The step strip at the top is always visible. Any step is one tap away.
- `Next` shows the code and title of the next step, so the reader knows where it leads.
- There is no separate "Back" (history) button. It was removed because it looked like `Previous` but went
  somewhere different after a jump.
- Swiping left or right changes step. The page follows the finger and the neighbour page comes in beside it,
  so the reader sees how far they have dragged. Up and down still scrolls.
- Left and right arrow keys change step on a computer.
- Every step has its own link (`#C1`), so a supervisor can send "look at C1".

### 2.11 Privacy in screenshots

The repository is public. Before a screenshot goes in:

- Names of people: covered. In the approver list, at most the first two letters stay visible, so the reader can
  still see that it is a list of names.
- Hours, pay amounts, email addresses, the account avatar: covered or cut out.
- Other workers' earnings rates: the amount is covered, and the name beyond the width of the word "Manual:".
- The original, unredacted screenshots are never committed.

Redaction is done on the original before anything is cut from it (see `tools/build_shots.py`), so no crop can
leak what the full picture hides.

### 2.12 Fail safe

- The page works with browser storage switched off. Storage only remembers small conveniences (section 6).
- No step depends on an animation having played.
- A step whose picture is not set yet (`src` left out) shows a grey placeholder with the picture's description.

## 3. Structure

Start page, 13 steps in 5 stages, Help page.

| Stage | Steps |
|---|---|
| Start | Three things to know before logging in, then the question "Used Xero for Matrix before?" |
| A · First time only | A1 Open the invite email · A2 Create your account, or log in · A3 Fill in your employee details |
| B · New timesheet | B1 Log in and add a timesheet · B2 Choose the fortnight · B3 Go to the week you worked |
| C · Hours and km | C1 Enter your hours · C2 Add your kilometres |
| D · Submit | D1 Check, then submit · D2 Choose who approves it · D3 Look for the green message |
| E · After you submit | E1 Check the status · E2 Fix a mistake |
| Help | Common problems. Each one opens the step that fixes it. |

Why it looks like this:

- There is no "Before you start" stage. Its three steps repeated the Start page, so they were folded into it.
- The two buttons on the Start page are the only way forward. Nobody can miss the first-time / returning choice.
- People who used Xero for Matrix before skip stage A. Then `Next`, `Previous` and "x of y" leave stage A out,
  and the stage is dimmed in the strip (still tappable). Opening any stage A step turns skipping off.
- A Xero account from another job does not count: the person still has to accept the Matrix invite.

## 4. How the page is built

One file, `index.html`: markup, styles and script together. No build step, no framework. It runs from any
static host (GitHub Pages) or straight from disk. Pictures are in `img/`.

All content is data near the top of the script:

| Name | What it holds |
|---|---|
| `CFG` | Values that change over time: the hourly earnings rate name, the kilometre rate name, the login address. |
| `STAGES` | Stage letters and names. |
| `STEPS` | One object per step (below). |
| `FAQ` | Help page entries: problem, short answer, the step it opens. |

A step:

```js
{id:'C2', g:2, t:'Add your kilometres', anim:true,
  lead:'…',                       // optional, see 2.1
  shot:{src:'img/C2.jpg', what:'…', marks:[…],          // full screenshot
        nsrc:'img/C2n.webp', nmarks:[…]},               // optional phone close-up
  pts:[ {n:1, h:'…'},             // numbered point = mark 1
        '…',                      // dash point
        {no:1, h:'…'} ],          // coral "do not" point
  box:{c:'ok', h:'Done'}}         // optional box
```

A mark: `{x, y, w, h, n, side, g, act}`. Position and size are in % of that picture.

- `n` is the number badge. Leave it out for a box with no badge.
- `g` joins a badge-less box to mark number `g` (one point, two boxes).
- `side:'r'` puts the badge in the right gutter.
- `act` is what the pointer demo does there: `'click'`, `'edit'`, or left out for "only check".

Number badges sit in a gutter beside the picture, level with their box, so a number never covers the screenshot.

## 5. Pictures

`tools/build_shots.py` cuts every picture from the original screenshots and computes the mark positions.
`tools/apply_marks.py` writes those positions into `index.html`. Never type mark coordinates by hand for the
steps the script builds.

```
python3 tools/build_shots.py <folder with the original screenshots>
python3 tools/apply_marks.py
```

Not built by the script:

- **A1, A2**: example pictures, labelled "Example". **A3**: a drawing, labelled "Drawn example".
  The owner will replace these when real screenshots are available.
- **D2**: the owner's own redaction, with one bar extended by hand.

## 6. What the browser remembers

| Key | Meaning |
|---|---|
| `xero-guide-skip-a` | The person chose "Yes" on the Start page: skip stage A. |
| `xero-guide-zoom-hint-2` | The zoom hint has been shown once. |

In memory only (lost on reload): which steps were opened in this visit. It drives the green chip border and
"demo plays on first visit".

## 7. Common changes

- **The pay rate changes (every year).** Change `CFG.hourRate`. Retake the C1 screenshot.
- **Xero changes a page.** Retake that screenshot, update the pixel boxes for that step in
  `tools/build_shots.py`, run both scripts, look at the step on a phone width and a computer width.
- **A rule changes.** Change the text in the one step that states it, and its Help entry if there is one.
- **A new step.** Add it to `STEPS` in order, with the next free code in its stage. Check every Help entry's
  `to:` still points at the right step, and update the table in section 3.

## 8. Checking a change

Do not report "it works". Say what was looked at. At minimum, at 390 px and at 1280 px wide, in day and night mode:

- Every step loads its picture, and each mark sits on the right element.
- First-time path walks all 13 steps in order. Returning path skips A1 to A3.
- Each Help entry opens the step it names.
- No sideways scrolling of the page.
- Pointer demo: order and type match the points. `Play` is off until the picture is ready.
- Picture viewer: opens showing the whole picture; zoom, drag and close work.
- Swipe: a long sideways drag changes step, a short one springs back, a vertical drag only scrolls.

State plainly what could not be tested. Real pinch and swipe feel can only be judged on a real phone.

## 9. Open questions

These are not decided. Do not "fix" them by guessing.

1. **Deadline.** The page says "by 11:59 pm Thursday of the week you worked", and tells people who work
   Friday to Sunday to submit as soon as they finish. Timesheets are per fortnight. The owner will confirm
   the exact rule with the manager.
2. **A2** says "use the same name as on your new employee form". It is not confirmed that this separate form
   is still used.
3. **B1** assumes a new worker lands on the Xero Me page right after logging in. Not checked with a new account.
4. **A1 to A3** pictures are stand-ins.

## 10. Decisions, in order

| Date | Decision | Why |
|---|---|---|
| 16 Nov 2026 | Step strip can be swiped and tapped; no quiz | It is a self-help guide; people jump to their problem. |
| 16 Nov 2026 | Recommend a computer or iPad browser | The phone app's kilometre box only takes 0 to 24. |
| 16 Nov 2026 | Removed the "Back" button | Confused with `Previous`. |
| 16 Nov 2026 | "Before you start" stage folded into the Start page | It repeated the Start page. |
| 16 Nov 2026 | Hours are typed as decimals; minutes ÷ 60, to 2 decimals | Xero's field; some people do not know how to convert. |
| 16 Nov 2026 | Layout and pictures chosen by screen width | Device names are unreliable. |
| 16 Nov 2026 | B1 and B2 merged | Same Xero page. |
| 17 Nov 2026 | Keep real screenshots; drawing trial removed | Safer for matching against the real screen. |
| 17 Nov 2026 | Gap between close-up pieces uses the gutter colour | Navy read as black in day mode. |
| 17 Nov 2026 | `Next` is amber in day mode too | Matches the theme and night mode. |
| 17 Nov 2026 | Pointer demo: eye / hand / pressing hand; index finger | Shows the kind of action, not just the place. |
| 17 Nov 2026 | Swipe changes step and follows the finger | The reader sees how far they have dragged. |
| 17 Nov 2026 | Demo plays under reduced motion; waits for the picture | It did not play on the owner's iPhone. |
