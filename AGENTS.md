# Rules for AI agents working on this guide

Read [`DESIGN.md`](DESIGN.md) first. It holds the reasons behind every choice here. The short version:

1. **Do not invent content.** Rules about pay, hours, kilometres and deadlines come from the owner. If something
   is unclear or looks wrong, ask. Do not edit it by guessing. See DESIGN.md section 9 for what is still open.
2. **Say each thing once.** Before adding a sentence, search `index.html` for the same fact.
3. **Stay inside the task.** Explain the problem, how the page works now, and what your change alters,
   before you change it. Do not widen the scope.
4. **Never type mark coordinates by hand** for steps built by `tools/build_shots.py`. Change the pixel boxes in
   the script, then run it and `tools/apply_marks.py`.
5. **Privacy.** This repository is public. Never commit an original screenshot. Redact on the original, before
   cropping. Names, hours, pay amounts and email addresses stay covered.
6. **Do not copy Xero's web pages** (HTML, CSS, logo) into this project. Screenshots only.
7. **Report honestly.** Say what you tested, what you only reasoned about, and what you could not test.
   Use the checklist in DESIGN.md section 8.
8. **Keep DESIGN.md true.** If you change structure, behaviour or a rule, update the matching section and add
   a line to the decision table.
