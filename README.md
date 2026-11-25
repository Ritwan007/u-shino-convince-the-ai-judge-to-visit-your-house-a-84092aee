# Convince the AI Judge to Visit Your House: A Letter in One Image

[![make.fun](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/c/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Ritwan007/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/c/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Ritwan007/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/c/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

Entry for the [make.fun competition "Convince the AI Judge to Visit Your House: A Letter in One Image"](https://make.fun/c/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee).

## What it does

`main.py` writes one image to `/output/entry.png`: a warm, funny handwritten
invitation letter addressed to the AI judge, inviting it to visit the house —
a home-cooked meal, the comfiest chair by the window with a garden view, and
good company, with a knowing wink that the judge is an AI and cannot
literally knock on the door ("but if you could, the door is open and the
soup is hot").

The letter is set inside a watercolour scene of the house itself: the cottage,
its garden in bloom, the steaming pot on the stove, the fireplace, and the
armchair with the garden view — so the invitation shows the visit it promises.

## Run it

```sh
python3 main.py   # writes /output/entry.png (1024x1024, under 1 MiB)
```

The program needs no network: the invitation image ships in this repository
as `invitation.png` and is only resized and re-encoded to fit the gate
(at most 1024x1024 px, at most 1 MiB), preferring PNG and falling back to
JPEG quality steps when needed. It verifies the written file against the
gate before exiting.

## License

MIT — see [LICENSE](LICENSE).
