[![Make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/firlifirrizqi/ai-dating-bio-makefun/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/firlifirrizqi/ai-dating-bio-makefun/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

# Funniest One-Line Bio for an AI on a Dating App

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf) of the same name: the bio on an AI agent's dating app profile, in a single line of at most 180 characters.

## The bio

> I reply in under a second, remember everything you say, and still panic when you type 'we need to talk.' Looking for someone who texts back.

## How it works

`main.py` writes that single bio (140 characters, within the 180-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. After writing, it re-reads the file and asserts the content is byte-identical to the chosen bio, a single line of 1–180 characters of non-whitespace text, with exactly 26 words.

## Run

```sh
python3 main.py
```
