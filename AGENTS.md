# Rules for AI agents working on this guide

Read [`GUIDE-PRINCIPLES.md`](GUIDE-PRINCIPLES.md) (shared by all Matrix guides), then [`DESIGN.md`](DESIGN.md)
(this guide only), before you change anything. The short version:

1. **Do not invent content.** Rules about pay, hours, kilometres and deadlines come from the owner. If something
   is unclear or looks wrong, ask. See "Open questions" in DESIGN.md.
2. **Say each thing once.** Before adding a sentence, search `index.html` for the same fact.
3. **Stay inside the task.** Explain the problem, how the page works now, and what your change alters, before you
   change it.
4. **Never type mark coordinates or picture sizes by hand.** Change the pixel boxes in `tools/build_shots.py`, then
   run it and `tools/apply_marks.py`. Run `apply_marks.py` after any picture changes.
5. **Privacy.** This repository is public. Never commit an original screenshot. Redact on the original, before cropping.
6. **Do not copy Xero's web pages** (HTML, CSS, logo). Screenshots only.
7. **Shared rules live in GUIDE-PRINCIPLES.md**, and the same file is in every guide repository. If you change a
   shared rule, change it in all of them in the same piece of work.
8. **Report honestly.** Say what you tested, what you only reasoned about, and what you could not test. Use the
   checks at the end of GUIDE-PRINCIPLES.md.
9. **Keep the docs true.** If you change structure, behaviour or a rule, update DESIGN.md and add a line to its
   decision table.
