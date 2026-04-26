---
title: Chain of Thought
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Chain of Thought (CoT) is a prompting technique where LLMs explicitly verbalize their reasoning step-by-step, rather than jumping directly to an answer. It improves model reasoning capabilities on complex tasks.

## How It Works

Instead of just asking a question, CoT prompts include intermediate reasoning:
- "Let's think step by step..."
- Show the LLM examples of intermediate steps
- The model then generates explicit reasoning steps before the final answer

## Why It Helps

CoT gives the model space to "think" through problems, reducing one-step errors. It's particularly effective for:
- Arithmetic reasoning
- Logical puzzles
- Multi-step planning
- Complex decision making

## HRM Critique

The Hierarchical Reasoning Model (HRM) critiques CoT as "shallow" — one wrong step can derail the entire process. CoT is also slower since each step must be generated as text. [Source: Hierarchical Reasoning Model_ Ultra-Efficient, Brain-Inspired AI.md]

## Limitations

- Verbose: many tokens spent on reasoning
- One error can cascade
- Slower inference
- Not suitable for all tasks

## Related Concepts

- [[Hierarchical Reasoning Model]]: Architecture that performs reasoning internally (latent space), avoiding CoT's step-by-step approach