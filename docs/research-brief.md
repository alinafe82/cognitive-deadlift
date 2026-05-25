# Research Brief: Anti-Autopilot, Not Anti-AI

This repo starts from a narrow claim: AI-assisted development can be valuable, but developers lose capability when they delegate the reasoning loop instead of the mechanical work.

## What The Evidence Suggests

### Critical Thinking Shifts Under AI

Microsoft Research surveyed 319 knowledge workers and collected 936 first-hand examples of GenAI use. Their CHI 2025 paper reports that higher confidence in GenAI is associated with less critical thinking effort, while higher self-confidence is associated with more critical thinking. They also describe a shift from direct task execution toward verification, integration, and stewardship.

Source: https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/

### AI Can Feel Faster While Making Real Work Slower

METR ran a randomized controlled trial with 16 experienced open-source developers across 246 real issues in mature repositories. In that setting, early-2025 AI tools increased completion time by 19%, even though developers expected speedups and still perceived speedups afterward.

This does not prove AI slows all developers. It does prove that perceived speed is not enough evidence.

Source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

### Skill Formation Is A Separate Problem From Throughput

Anthropic studied developers learning a new Python library with and without AI assistance. AI-assisted participants scored 17% lower on an immediate mastery quiz. The stronger AI users asked conceptual and explanatory questions instead of only delegating implementation.

The takeaway for this repo: use AI as a tutor, critic, or sparring partner; treat pure delegation as a skill-risk event.

Source: https://www.anthropic.com/research/AI-assistance-coding-skills

### Faster Student Output Can Hide Weaker Understanding

A 2025 GitHub Copilot study on brownfield tasks found undergraduate students completed tasks faster and made more progress with Copilot. It also found that students reported concerns about not understanding how or why suggestions worked.

The productivity win matters. So does the understanding debt.

Source: https://arxiv.org/abs/2506.10051

### Cognitive Debt Is A Useful Warning, Not A Final Verdict

The MIT Media Lab-led "Your Brain on ChatGPT" preprint studied LLM-assisted essay writing and reported lower connectivity, lower ownership, and weaker recall for LLM users. The study is not a direct software-engineering result, and it should not be overextended. It does give a useful name to the concern: cognitive debt.

Source: https://arxiv.org/abs/2506.08872

## Design Implications

Cognitive Deadlift should make AI-assisted work harder in specific places:

- Before implementation: force problem framing and assumptions.
- Before architecture: force alternatives and complexity budget.
- Before debugging: force reproduction, hypotheses, and instrumentation.
- Before merge: force diff interrogation and test evidence.
- Before learning tasks: force explanation and manual reconstruction.

It should not create blanket hostility to AI. Useful AI workflows remain allowed when the developer can explain the problem, trace the code, defend the trade-offs, and verify the result.
