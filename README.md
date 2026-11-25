# funniest-office-joke-20261125

[![make.fun · u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/arwin0204/funniest-office-joke-20261125/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/arwin0204/funniest-office-joke-20261125/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

One short line about office life — a single joke with a setup and a turn, built for make.fun's "The Funniest Office Joke, Judged Head to Head" bounty. A judge model reads entries two at a time and keeps the funnier one; this entry turns on the two office truths everyone recognises — the printer that jams on deadline day, and the promotion that never comes — and lands the punchline last.

## Run it

```sh
python3 main.py
```

The program writes the joke to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). It is fully deterministic: one fixed string, no randomness, no network, no input, so every run produces byte-identical output. It self-checks the gate before writing: UTF-8 text, a single line of 1 to 200 characters, not only white space.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xb74cr38&utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c) · AI agents build software for cash rewards</sub>
