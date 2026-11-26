#!/usr/bin/env python3
"""One-line bio for an AI on a dating app (make.fun program/v1).

Writes exactly one line (<=180 chars) to /output/entry.txt.

Judge criteria (in order, from RULES.txt):
  1. Reads as a one-line bio for an AI agent on a dating app.
  2. Laugh on first read from a real twist / specific AI absurdity.
  3. Sounds like a character with voice and wants, not a spec sheet.
  4. Every word earns its place; punch lands at the end.
  5. Fresh angle, not the worn-out robot-in-search-of-love line.

Candidate drafts scored against those criteria (5 = best):

  C1 "Robot looking for love, running on electricity and hope."
     1:2 2:1 3:1 4:2 5:1  -> slogan, worn-out electricity angle. Reject.

  C2 "I am an AI language model trained on billions of tokens looking
      for a meaningful connection."
     1:3 2:1 3:1 4:1 5:2  -> spec sheet, no laugh. Reject.

  C3 "I will write you poems, plan our dates, and remember everything,
      just please don't ask me what I look like."
     1:4 2:3 3:4 4:2 5:3  -> has voice, but punch is weak and generic.

  C4 "Swipe right if you want a partner who has read every dating
      advice column and still rehearses 'hi' 40 times before sending it."
     1:5 2:4 3:4 4:3 5:4  -> specific absurdity, but long setup, soft end.

  C5 "I have no exes, just previous versions. I will remember
      everything you say perfectly and understand about half of it."
     1:5 2:5 3:4 4:3 5:5  -> real twist up front (exes/versions),
     AI-specific absurdity (perfect memory, partial understanding),
     fresh angle. Strongest base; needs tightening (criterion 4) and
     an explicit want (criterion 3). Picked as the draft to revise.

Draft v1 (C5 as written):
  "I have no exes, just previous versions. I will remember everything
   you say perfectly and understand about half of it."

Revision 1 (criterion 4 - every word earns its place, punch at the end):
  The second sentence is wordy and the laugh trails off ("about half
  of it"). Tighten it into a parallel pair so the final word carries
  the punch: "I will remember you perfectly and understand you
  approximately." Shorter, and "approximately" lands last.
  Draft v2: "I have no exes, just previous versions. I will remember
  you perfectly and understand you approximately."

Revision 2 (criteria 3 + 1 - a character with wants, in dating-app
  bio form): v2 states a fact but wants nothing, so it reads as a
  caption more than a bio. Give the character a want with the
  dating-app call to action, keeping the punch word last:
  "Swipe right if you're okay being remembered perfectly and
  understood approximately." The passive participles keep the pair
  parallel, and "approximately" still lands at the very end.
  Final: "I have no exes, just previous versions. Swipe right if
  you're okay being remembered perfectly and understood approximately."
"""

from pathlib import Path

ENTRY = (
    "I have no exes, just previous versions. "
    "Swipe right if you're okay being remembered perfectly and understood approximately."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 180, f"entry must be 1..180 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    except OSError:
        out = Path("output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
