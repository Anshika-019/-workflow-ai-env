---
title: WorkFlowAI
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

---
tags:
- openenv
---
# 🚀 WorkFlowAI: Autonomous Office Task Agent Environment

## 🧠 Overview
WorkFlowAI is an OpenEnv-compliant reinforcement learning environment designed to simulate real-world office workflows.  
It enables AI agents to interact with structured tasks such as email triage, bug prioritization, and code review.

The environment focuses on **realistic task execution**, **incremental reward learning**, and **deterministic evaluation**, making it suitable for benchmarking LLM-based agents.

---

## 🎯 Motivation
Modern organizations rely heavily on repetitive manual workflows such as sorting emails, prioritizing bugs, and reviewing code.  
This project aims to simulate such environments so that AI agents can learn to automate them efficiently.

---

## 🧩 Tasks

### 🟢 1. Email Triage (Easy)
- Classify emails into:
  - `urgent`
  - `normal`
  - `spam`
- Objective: Improve prioritization of communication

---

### 🟡 2. Bug Prioritization (Medium)
- Assign priority levels:
  - `P0` (critical)
  - `P1` (high)
  - `P2` (low)
- Objective: Help teams focus on high-impact issues

---

### 🔴 3. Code Review (Hard)
- Identify issues in code:
  - `bug`
  - `security`
  - `performance`
- Objective: Improve code quality and reliability

---

## ⚙️ Environment Design

### Observation Space
```json
{
  "task": "string",
  "input_data": "list"
}

