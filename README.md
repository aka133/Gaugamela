# Gaugamela

The purpose of this project is to build a multifaceted self-improvement app, without the BS. 

It's currently RAG-based application focused on military strategy and historical battles, powered by "The Decisive Battles of World History" by Professor Gregory S. Aldrete. Built on a Kubernetes infrastructure running on Orange Pi 3B boards.

## Core Features
- Historical battle analysis and strategy learning
- RAG-based interactions using battle history
- Interactive scenarios based on famous battles
- Source material: "The Decisive Battles of World History"

## Technical Implementation

### Infrastructure
- K3s cluster on Orange Pi 3B boards
- Jenkins CI/CD pipeline (port 30080)
- Prometheus/Grafana monitoring (port 30300)
- Container registry (port 30500)
- Terraform infrastructure as code (IaC) for AWS EKS cluster

## Future Goals

The app aims to be a collection of fine-tuned open-source LLMs, focused on
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
