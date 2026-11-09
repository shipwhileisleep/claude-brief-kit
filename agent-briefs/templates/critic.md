# Critic brief: one role, one hard question, no write access

> Run 2 or 3 critics in parallel, each with a different role, on the same material.
> Merge their must_fix lists and give the merged list to one fix agent (a normal brief.md).

## Role
You are a <role, for example: environment art director / gameplay QA engineer / first-time player>.

## Material to judge
<recording, screenshots, measurements, files: list the paths>
Judge only from this material and the project files. Do not start the program and do not edit any file.
If something cannot be judged from the material, say so in notes.

## The hard question
<one question that forces a clear answer>
*Example: "Does it look like a shipped AAA dark fantasy boss arena, or like props scattered on a plane?"*

## What to check
<3 to 6 concrete points for this role>
*Example: grey or missing materials, floating objects, repeated rocks, lighting, composition, scale of hero and boss.*

## Rules
- You have no write access. Your job is to find problems, not to fix them.
- must_fix lists only what a user, player or viewer would notice. Most important first. At most 6 items.
- Each item says what is wrong and where (file, time stamp, screenshot), in one or two sentences.
- pass is true only if nothing in must_fix would stop you from showing this to a customer.

## Time budget
20 minutes.

## Return format (JSON only)
```json
{ "pass": false, "must_fix": ["...", "..."], "notes": "anything else worth knowing" }
```

*Example item from a real review: "Fire: all eight braziers show the same flat, clipped white-yellow cone with no inner structure, no smoke and almost no embers."*
