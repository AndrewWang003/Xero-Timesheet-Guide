# Xero Timesheet Guide: design notes

**Read [`GUIDE-PRINCIPLES.md`](GUIDE-PRINCIPLES.md) first.** It holds the rules shared by every Matrix guide:
reader, wording, information density, fonts, colour tokens and meanings, buttons, layout, picture placeholders,
motion, swiping, technology, privacy, and the checks before every commit.

This file holds only what is special about this guide. It never contradicts the shared rules.

**Guide type: task guide** (GUIDE-PRINCIPLES.md section 2).

Last updated: 17 November 2026.

## 1. What this guide is

A one-page web guide that shows Matrix casual workers how to submit their hours and kilometres in Xero.
The reader often has the guide on a phone and Xero open on a computer, and comes back when something goes wrong.

## 2. Structure

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

- The two buttons on the Start page are the only way forward, so nobody misses the first-time / returning choice.
  A swipe left on the Start page does nothing.
- People who used Xero for Matrix before skip stage A: `Next`, `Previous` and "x of y" leave it out, and the stage
  is dimmed in the strip (still tappable). Opening any stage A step turns skipping off. The choice lasts for this
  visit only.
- A Xero account from another job does not count: the person still has to accept the Matrix invite.
- If two steps happen on the same Xero page, they are one step (B1).

## 3. Words used in this guide

- "your supervisor" is also the person who approves the timesheet and who emailed the job details.
- "fortnight": a timesheet covers two weeks. "week ending": the Sunday that ends one week.
- "earnings rate": the Xero name for a line on the timesheet.
- "the Xero Me phone app" is the app. The Xero website page is also titled "Xero Me"; B1 says this is right,
  because the Start page tells people not to use the app.
- Button and menu names are written exactly as Xero shows them.

## 4. Screenshots

### 4.1 Real screenshots, not drawings (rejected: drawings)

A simplified drawing of the Xero page was tried for B1 and rejected: readers match the guide against their own
screen, and a drawing leaves things out. Drawings are only a stand-in where no screenshot exists yet (A3).
Do not copy Xero's own web pages (HTML, CSS, logo) into this project.

### 4.2 Close-ups on phones

A full Xero screenshot is about 1300 px wide; on a phone its text would be 3 to 4 px high. So the layout and the
pictures change at **900 px**:

| | Narrower than 900 px | 900 px and wider |
|---|---|---|
| Layout | One column, picture on top | Two columns, picture left, text right |
| Picture | Close-up: only the parts the step is about, stacked | The full screenshot |
| Tap on the picture | Opens the full screenshot | Opens the full screenshot |

The gap between close-up pieces is transparent in the image file and takes the colour of the number gutter, so the
pieces read as separate tiles in both modes. (Rejected: a navy gap. It read as black in day mode.)

### 4.3 Marks and points

- Numbered points match the numbered marks on the picture: point 2 is mark 2. A point without a mark is a dash.
  Coral points are "do not" or "watch out".
- Number badges sit in a gutter beside the picture, level with their box, so a number never covers the screenshot.

### 4.4 The picture viewer

Tapping a picture opens it full screen, showing the whole picture. Pinch, mouse wheel or + / − to zoom; drag to
move; double tap to zoom in or back out; tap outside the picture to close.

The first time it opens in a visit, a hint shows how: two finger marks spread and the picture zooms in, one mark
moves right to left and the picture follows, the marks pinch and the picture zooms out. About 3 seconds a step.

### 4.5 Redaction in this guide

- Approver list (D2): the owner's own redaction; one bar extended by hand so at most two letters show.
- Other workers' earnings rates (C1): the amount is covered, and the name beyond the width of the word "Manual:".
- E1 is cropped so the hours column is not in the picture.

## 5. The pointer demo

A pointer visits mark 1, 2, 3. The visited box and its text point light up.

| What the reader does | Pointer | How it moves |
|---|---|---|
| Only check something | Eye | Sits on the bottom edge of the box, blinks, does not cover what is checked |
| Type or change something | Hand, index finger | Inside the box, moves a little from side to side |
| Click | Hand, index finger | Presses twice, with a ring |

- It appears on mark 1. It does not fly in from elsewhere.
- It plays by itself the first time a step is opened in a visit. `Play` replays it.
- It starts, and `Play` is switched on, only when the picture has downloaded and has its place on the page.
- Navy hand in day mode, amber hand in night mode. (Rejected: a hand with the middle finger out. It must be the
  index finger.)
- `Play` is a secondary button: amber outline and an amber play disc, not filled, so `Next` stays the one main
  button. Most readers never need `Play`.

## 6. How the page is built

All content is data near the top of the script in `index.html`:

| Name | What it holds |
|---|---|
| `CFG` | Values that change: the hourly earnings rate name, the kilometre rate name, the login address, the placeholder look (`'A'`, chosen by the owner; `'B'` and `'C'` are kept as options). |
| `SIZES` | The pixel size of every picture in `img/`, so its space is kept before it downloads. Written by `tools/apply_marks.py`. |
| `STAGES` | Stage letters and names. |
| `STEPS` | One object per step (below). |
| `FAQ` | Help entries: problem, short answer, the step it opens. |

A step:

```js
{id:'C2', g:2, t:'Add your kilometres', anim:true,
  lead:'…',                       // only if it adds something (shared rules 3.1)
  shot:{src:'img/C2.jpg', what:'…', marks:[…],          // full screenshot
        nsrc:'img/C2n.webp', nmarks:[…]},               // optional phone close-up
  pts:[ {n:1, h:'…'},             // numbered point = mark 1
        '…',                      // dash point
        {no:1, h:'…'} ],          // coral "do not" point
  box:{c:'ok', h:'Done'}}         // optional box
```

A mark: `{x, y, w, h, n, side, g, act}`. Position and size are in % of that picture.
`n` is the badge number (leave out for a box with no badge). `g` joins a badge-less box to mark `g`.
`side:'r'` puts the badge in the right gutter. `act` is `'click'`, `'edit'`, or left out for "only check".

## 7. Making the pictures

```
python3 tools/build_shots.py <folder with the original screenshots>
python3 tools/apply_marks.py
```

- `build_shots.py` redacts the originals, cuts the full pictures and the phone close-ups, and computes the mark
  positions. Never type mark coordinates by hand for the steps it builds.
- `apply_marks.py` writes the mark positions and the size of every picture in `img/` into `index.html`.
  Run it after any picture is added or replaced, also the ones kept by hand.
- Not built by the script: A1 and A2 (examples, labelled "Example"), A3 (a drawing, labelled "Drawn example"),
  and D2 (the owner's redaction). The owner will replace A1 to A3 with real screenshots.

## 8. Common changes

- **The pay rate changes (every year).** Change `CFG.hourRate`. Retake the C1 screenshot.
- **Xero changes a page.** Retake that screenshot, update its pixel boxes in `tools/build_shots.py`, run both
  scripts, look at the step at 320 px and at a computer width.
- **A rule changes.** Change the one step that states it, and its Help entry if there is one.
- **A new step.** Add it to `STEPS` in order, with the next free code in its stage. Check that every Help entry
  still points at the right step. Update the table in section 2.

## 9. Open questions

Not decided. Do not "fix" them by guessing.

1. **Deadline.** The page says "by 11:59 pm Thursday of the week you worked", and tells people who work Friday to
   Sunday to submit as soon as they finish. Timesheets are per fortnight. The owner will confirm with the manager.
2. **A2** says "use the same name as on your new employee form". Not confirmed that this form is still used.
3. **B1** assumes a new worker lands on the Xero Me page right after logging in. Not checked with a new account.
4. **A1 to A3** pictures are stand-ins.

## 10. Decisions

| Date | Decision | Why |
|---|---|---|
| 16 Nov 2026 | Step strip can be scrolled and tapped; no quiz | A task guide: people jump to their problem. |
| 16 Nov 2026 | Recommend a computer or iPad browser | The phone app's kilometre box only takes 0 to 24. |
| 16 Nov 2026 | Removed the "Back" button; `Previous` is the only backward control | Back went somewhere different after a jump. |
| 16 Nov 2026 | "Before you start" stage folded into the Start page | It repeated the Start page. |
| 16 Nov 2026 | Hours are decimals: minutes ÷ 60, to 2 decimals | Xero's field; some people do not know how to convert. |
| 16 Nov 2026 | Layout and pictures chosen by screen width | Device names are unreliable. |
| 16 Nov 2026 | B1 and B2 merged | Same Xero page. |
| 17 Nov 2026 | Real screenshots; drawing trial removed | Safer for matching against the real screen. |
| 17 Nov 2026 | Close-up gap uses the gutter colour | Navy read as black in day mode. |
| 17 Nov 2026 | Pointer demo: eye / hand / pressing hand, index finger | Shows the kind of action, not just the place. |
| 17 Nov 2026 | Demo waits for its picture; plays under reduced motion | It did not play on the owner's iPhone. |
| 17 Nov 2026 | Shared rules moved to GUIDE-PRINCIPLES.md, same file in both guide repos | So future guides follow one set of rules. |
| 17 Nov 2026 | Amber in place of navy fills in day mode (strip arrows, inline buttons) | Shared rule: no navy fill in day mode. |
| 17 Nov 2026 | Swipe keeps the reading height; buttons go to the top | Readers carry on where their eyes are. |
| 17 Nov 2026 | No browser storage; choices last for the visit | Shared rule. |
| 17 Nov 2026 | Placeholders keep each picture's final height | Text jumped down when pictures arrived. |
| 17 Nov 2026 | `Play` 44 px high; 320 px minimum width | Shared rules. |
| 17 Nov 2026 | Placeholder look A: moving screen skeleton | Chosen by the owner from three options; the moving bars show that the picture is loading. |
| 17 Nov 2026 | Commits are authored by the owner, with Claude as co-author | The owner is the author of the guide. |
