# Gaugamela

The purpose of this project is to build a multifaceted self-improvement app, without the BS. The app is a collection of fine-tuned open-source LLMs with RAGS, focused on
- Vocabulary
- Storytelling ability
- Writing and exposition
- Understanding sociology and social patterns (social engineering)
- Situational awareness/presence of mind
- Puzzle solving
- Memory
- Strategy (especially war strategy)
    - "Build your own strategy" given certain war scenarios from historical figures and battles
- Quotes/phrases/aphorisms (from philosophers, entrepreneurs, general, athletes, etc.)

Each "task" should take no longer than 5 minutes to complete.

The app will use spaced repetition and a combination of direct recall for the knowledge tasks and open-ended LLM-generated problems/scenarios/conversations for the more flexible tasks.

Technical setup:
- The app will be deployed on a Kubernetes cluster of Orange Pi 3B boards.


Spreadsheet will have the following columns:
- Task category
- Task name
- Task description
- Task RAG (if any)
- Task system prompt (include a difficulty scale)
- Task LLM (if a particular fine-tuned LLM is used)
