# Xero Timesheet Guide: design notes

**Read [`GUIDE-PRINCIPLES.md`](GUIDE-PRINCIPLES.md) first.** It holds the rules shared by every Matrix guide:
reader, wording, information density, fonts, colour tokens and meanings, buttons, layout, picture placeholders,
motion, swiping, technology, privacy, and the checks before every commit.

This file holds only what is special about this guide. It never contradicts the shared rules.

**Guide type: task guide** (GUIDE-PRINCIPLES.md section 2).

Last updated: 18 November 2026.

## 1. What this guide is

A one-page web guide that shows Matrix casual workers how to submit their hours and kilometres in Xero.
The reader often has the guide on a phone and Xero open on a computer, and comes back when something goes wrong.

## 2. Structure

Start page, 10 steps in 4 stages, Help page.

| Stage | Steps |
|---|---|
| Start | Three things to know before logging in, then the question "Used Xero for Matrix before?" |
| A · First time only | A1 Open the invite email · A2 Set up your account (create the login, then personal, tax, super and bank details) |
| B · New timesheet | B1 Log in and add a timesheet · B2 Choose the fortnight · B3 Go to the week you worked (animated) |
| C · Hours and km | C1 Enter your hours · C2 Add your kilometres, then submit (check both weeks, click Submit) |
| D · Submit | D1 Choose who approves it · D2 Look for the green message (and how to fix a mistake) · D3 Check the status |
| Help | Common problems. Each one opens the step that fixes it. Opened from the `Help` button at the top right on every page, and by `Next` on D3. It is not in the step strip. |

- The Start page asks "Used Xero for Matrix before?" with two buttons. A swipe left (or the right arrow key) on
  Start counts as "No, first time" and opens A1: that path shows every step, so nobody misses anything. Returning
  users tap `Yes`. The page swipe hint plays on Start.
- **Scroll arrow (touch screens, every page).** While a page goes on more than 80 px below the screen, a round
  arrow floats at the bottom: translucent `--surface`, amber ring, down chevron. A tap scrolls down 70% of a screen;
  on Start it scrolls to the "Used Xero for Matrix before?" question, and it goes away once those buttons are on
  screen. It goes away at the bottom of a page. Not on computers.
- People who used Xero for Matrix before skip stage A: `Next`, `Previous` and "x of y" leave it out, and the stage
  is dimmed in the strip (still tappable). Opening any stage A step turns skipping off. The choice lasts for this
  visit only.
- A Xero account from another job does not count: the person still has to accept the Matrix invite.
- If two steps happen on the same Xero page, they are one step (B1).
- **Top bar, right side:** `Help`, then `Aa` (text size, GUIDE-PRINCIPLES.md 4.8), then the theme button. Text size
  keeps the top bar, the step strip, screenshots and their marks and badges, the picture viewer and the hints at
  their size; everything in the step cards scales. At 320 px the title in the top bar is cut short with "…" (it was
  already cut before `Aa` was added; the step code beside it stays readable).

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
screen, and a drawing leaves things out. Drawings are only a stand-in where no screenshot exists yet (none at the moment).
Do not copy Xero's own web pages (HTML, CSS, logo) into this project.

### 4.2 Close-ups on phones

A full Xero screenshot is about 1300 px wide; on a phone its text would be 3 to 4 px high. So the layout and the
pictures change at **900 px**:

| | Narrower than 900 px | 900 px and wider |
|---|---|---|
| Layout | One column, picture on top | Two columns, picture left, text right |
| Picture | Close-up: only the parts the step is about, stacked | A wider cut of the screenshot |
| Tap on the picture | Opens the whole screenshot (the full screen) | Opens the whole screenshot (the full screen) |

So a step has up to three pictures: `nsrc` (phone close-up), `src` (wide screens), `fsrc` (the whole screen, for the
enlarged view). The marks are on all three. (Found 18 Nov 2026: the enlarged view showed the wide cut, not the
whole screen as planned. The whole screen lets the reader see where the part sits on their own screen.)

On wide screens a tall picture (D2) is shown at most 460 px high, so it does not fill the screen.

The gap between close-up pieces is transparent in the image file and takes the colour of the number gutter, so the
pieces read as separate tiles in both modes. (Rejected: a navy gap. It read as black in day mode.)

### 4.3 Marks and points

- Numbered points match the numbered marks on the picture: point 2 is mark 2. A point without a mark is a dash.
  Coral points are "do not" or "watch out".
- Number badges sit in a gutter beside the picture, level with their box, so a number never covers the screenshot.

### 4.4 The picture viewer

Tapping a picture opens it full screen, showing the whole picture. Pinch, mouse wheel or + / − to zoom; drag to
move; double tap to zoom in or back out; tap outside the picture to close.

**Sharp when zoomed.** The enlarged view uses the whole screenshot at the original's full width (most are 2560 px;
D2's original is 1567 px). A phone decodes a big picture only at the size it is shown, so a CSS scale() alone looked
blurred on phones. While a pinch or + is moving, the picture is scaled (smooth); about 0.2 s after it stops, the
picture is laid out at its real zoomed width and the phone draws it again at full detail. The number gutters keep
their 30 px, so the screenshot does not jump when this happens.

It opens fitted to the screen, with no zoom hint: people pinch and drag by themselves. (Rejected 18 Nov 2026: a
three-step zoom hint on the first opening.) Nothing moves behind it: the demo, the swipe hint and the scroll arrow
stop or hide while it is open.

### 4.5 Redaction in this guide

Everything is covered on the original, so the close-up, the wide cut and the whole screen are all safe.

- The account initials at the top right: painted over in the colour of the bar around them.
- Approver list (D2): the owner's own redaction; one bar lengthened so at most two letters show.
- Other workers' earnings rates (C1): the amount is covered, and the name beyond the width of the word "Manual:".
- This fortnight's hours (D3, and behind the B2 window), and the totals and hours behind the D2 window: grey blocks.
- Left visible on purpose, for the owner to review: the example hours and kilometres (C2, D2), the
  fortnightly totals in B3, the iPad status bar and address in D2, "Next Payment Date".

## 5. The pointer demo

A pointer visits mark 1, 2, 3. The visited box and its text point light up.

| What the reader does | Pointer | How it moves |
|---|---|---|
| Only check something | Eye | Sits on the bottom edge of the box, blinks, does not cover what is checked |
| Type or change something | Hand, index finger | Inside the box, moves a little from side to side |
| Click | Hand, index finger | Finger tip on the middle of the button; presses twice, with a ring |

- It appears on mark 1. It does not fly in from elsewhere.
- **B3 changes the page.** B3 shows week 1. After the demo clicks the arrow, the same cut of week 2 fades in on top, and
  Week ending and the dates pulse amber: only they change. When the demo ends, week 1 comes back. Set with `after:` on
  the step (the week 2 pictures); `build_shots.py` makes them from the same crop of the second screenshot.
- **A mark the reader only needs sometimes is an eye, never a click** (D2 mark 3, Revert to Draft), so the demo
  never presses a button the normal path must not press.
- It plays by itself the first time a step is opened in a visit. `Play` replays it.
- It starts, and `Play` is switched on, only when the picture has downloaded and has its place on the page.
- The eye and hand are amber with a navy outline in both modes. (Rejected: a navy hand in day mode. Rejected: a
  hand with the middle finger out. It must be the index finger.)
- **A click mark must be drawn tight around the one button to press**, because the finger lands on the middle of the
  box. Two things to press under one number get two boxes (the second with `g`). If the button cannot be the box,
  give the mark `tx`, `ty`: the point to press, in % of the picture.
  (Found 18 Nov 2026: A2 mark 3 covered the tick box, Create and Cancel, and the finger pressed Cancel.)
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

A mark: `{x, y, w, h, n, side, g, act, tx, ty}`. Position and size are in % of that picture.
`n` is the badge number (leave out for a box with no badge). `g` joins a badge-less box to mark `g`.
`side:'r'` puts the badge in the right gutter. `act` is `'click'`, `'edit'`, or left out for "only check".
`tx`, `ty` (optional) is where the pointer goes, in % of the picture; without them it goes to the middle of the box.

## 7. Making the pictures

```
python3 tools/build_shots.py <folder with the original screenshots>
python3 tools/apply_marks.py
```

- `build_shots.py` redacts the originals, cuts the full pictures and the phone close-ups, and computes the mark
  positions. Never type mark coordinates by hand for the steps it builds.
- `apply_marks.py` writes the mark positions and the size of every picture in `img/` into `index.html`.
  Run it after any picture is added or replaced, also the ones kept by hand.
- Not built by the script: A1 and A2 (examples, labelled "Example"). The owner will replace them with real screenshots.

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
4. **A1 and A2** pictures are stand-ins.

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
| 18 Nov 2026 | Pointer is amber in day mode too | Navy looked black in day mode. |
| 18 Nov 2026 | Click lands on the middle of a tight box; A2 mark 3 split into tick box and Create | The finger pressed Cancel. |
| 18 Nov 2026 | Fixed: the enlarged picture stayed on its placeholder for ever | The viewer never told the placeholder that the picture had arrived (bug from 17 Nov). Check the enlarged view too when pictures change. |
| 18 Nov 2026 | Enlarged view shows the whole screenshot, with marks; more covered on the originals | Planned on 16 Nov but not built; the reader matches the guide against the whole screen. |
| 18 Nov 2026 | Page swipe hint on touch screens, first step page of a visit; computers keep only the strip hint | Readers on phones did not know the page swipes. The pointer demo waits for the hint. |
| 18 Nov 2026 | On wide screens a tall picture is at most 460 px high (D2) | D2 filled the screen. |
| 18 Nov 2026 | Strip hint on computers only; page swipe hint uses a thumb | On a phone two hints were too much; the thumb is how people swipe and differs from the click hand. |
| 18 Nov 2026 | Fixed: a swipe during the hint did nothing and the hint stayed on screen | The touch landed on the neighbour page, which the hint then removed; the hint's fade was held by an inline value. |
| 18 Nov 2026 | Swipe on Start = "first time" (A1); swipe hint plays on Start; `Next` bar on Start while the question is off screen | The owner wants the swipe taught on the first page. A1 is the safe path. On the owner's phone the question was just below the screen. (Rejected: putting the question first, readers would skip the three rules.) |
| 18 Nov 2026 | Round scroll arrow on every page that runs past the screen (touch only), in place of the `Next` bar on Start; the swipe hint is a thumb on its own | Owner's choice: an arrow alone is enough, and every long page needs it. Half a hand looked frightening. |
| 18 Nov 2026 | Content pass: 13 → 11 steps. A2 + A3 merged; E2 merged into D3 (same screenshot, Revert to Draft as mark 3); E1 became D4; stage E removed. Repeats removed (B2, A2 and C2 leads; login only in B1; "check both weeks" in D1; "Requested" explained only in D3). Sentences shortened throughout | Aim: the least patience spent. A returning reader needs nothing; a new reader goes from the start; an unfamiliar reader jumps to one step, so each step stands alone. |
| 18 Nov 2026 | Old D1 (check, then submit) merged into C2: 10 steps; D2–D4 became D1–D3 | D1 repeated C2 on the same screenshot. C2 uses the wider cut, which shows the Submit button. |
| 18 Nov 2026 | Enlarged view sharp on phones: full-width originals (quality 92), and the zoom settles at its real width | The owner found it blurred on a phone; the phone was stretching a copy decoded at screen size. |
| 18 Nov 2026 | Solid cover above the sticky header, header on its own layer | On a fast flick a phone drew the header a few pixels low and the page showed above it. |
| 18 Nov 2026 | No zoom hint in the enlarged view, on phones or computers; the picture opens fitted to the screen | Owner: people zoom with their own gestures; the hint only cost time. |
| 18 Nov 2026 | B3 is an animation: the click switches the picture from week 1 to week 2 | Shows that the page changes and what changes. B3 stays its own step: it is needed only when the work days are in week 2, Help points to it, and C1 is already the longest step. |
| 18 Nov 2026 | One way into Help: a `Help` text button with an amber outline at the top right; Help removed from the step strip | Two Help entries were the same. The top button is seen on every page; a lone "?" did not invite a tap. (Rejected: a lifebuoy icon beside the word.) |
| 18 Nov 2026 | Text-size control `Aa` at the top right (A− / four dots / A+; 90, 100, 115, 130 %), shared with the Dash Cam guide; not remembered | Owner: readers need bigger text. A panel keeps the top bar to one extra button at 320 px; four sizes because smaller than 90 % hurts reading. |
