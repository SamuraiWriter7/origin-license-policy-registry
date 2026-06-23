# Agent-Readable Policy Validation

## Overview

Agent-Readable Policy Validation defines how AI agents may evaluate usage policies, license templates, asset-policy bindings, and trace/royalty preservation rules.

v0.5 turns the policy registry into an agent-readable validation layer.

```text
Usage Policy
        ↓
License Template
        ↓
Asset Policy Binding
        ↓
Trace and Royalty Preservation Rules
        ↓
Agent-Readable Policy Validation
```

## Purpose

AI agents may need to read marketplace listings, evaluate license conditions, validate trace metadata, check royalty pointers, or propose derivative records.

However, AI agents should not automatically execute high-impact actions such as payment, rights transfer, metadata removal, royalty modification, or bulk AI training.

This layer defines the boundary.

```text
read      : allowed
evaluate  : allowed
validate  : allowed
propose   : allowed
execute   : human_review_required
```

## What This Layer Answers

Agent-Readable Policy Validation answers:

* What action is the AI agent requesting?
* Which policy records are being evaluated?
* Does the usage policy allow this action?
* Does the license template allow this action?
* Does the asset-policy binding permit this action?
* Are trace metadata and royalty pointers preserved?
* Is human review required?
* What may the agent output?
* What must the agent not output?

## v0.5 Scope

The v0.5 layer introduces:

* `schemas/agent-policy-validation.schema.json`
* `examples/agent-policy-validation.example.yaml`
* validation through `scripts/validate_examples.py`

## Core Relationship

```text
Usage Policy
  = concrete usage boundary

License Template
  = reusable policy pattern

Asset Policy Binding
  = effective connection between asset and policy

Trace and Royalty Preservation Rules
  = survival rules for origin, trace, and royalty metadata

Agent-Readable Policy Validation
  = agent-facing validation and action boundary
```

## Agent Context

The validation record identifies the agent context, including:

* agent ID
* agent role
* agent mode
* agent notes

Supported roles may include:

* reader
* validator
* marketplace agent
* royalty agent
* audit agent
* derivative proposal agent

Supported modes include:

* read only
* evaluate
* validate
* propose
* execute

## Requested Action

The validation record defines the requested action.

Examples include:

* read policy
* evaluate license
* validate policy binding
* validate trace metadata
* validate royalty pointer
* propose derivative
* propose redistribution
* request quote
* execute payment
* transfer rights
* bulk AI training
* remove trace metadata
* remove royalty pointer

## Validation Checks

The record evaluates the requested action against:

* usage policy
* license template
* asset-policy binding
* trace preservation rules
* royalty preservation rules
* human review boundary

Each check may return:

```text
pass
fail
not_applicable
requires_human_review
```

## Decision Result

The validation result may be:

```text
allowed
allowed_with_conditions
prohibited
human_review_required
```

The allowed agent response may be:

```text
read
evaluate
validate
propose
stop_and_request_human_review
deny_action
```

## Human Review Boundary

Human review is required for execution-level or rights-changing actions, including:

* payment execution
* rights transfer
* trace metadata removal
* royalty pointer removal
* royalty allocation modification
* bulk redistribution
* bulk AI training
* policy conflict resolution

## Agent Output Boundary

The validation record defines what an agent may output.

Allowed outputs include:

* policy summary
* validation result
* risk summary
* derivative proposal
* redistribution proposal
* human review request

Prohibited outputs include:

* payment execution
* rights transfer
* metadata removal instruction
* royalty bypass instruction
* human review override
* policy conflict auto-approval

## Design Principle

The goal is not to create fully autonomous rights execution.

The goal is controlled agent participation.

```text
AI can read.
AI can evaluate.
AI can validate.
AI can propose.
Humans approve execution.
```

## v0.5 Completion Meaning

With v0.5, the first arc of `origin-license-policy-registry` becomes complete.

The repository now defines:

```text
v0.1 — Usage Policy Record
v0.2 — License Template Registry
v0.3 — Asset Policy Binding
v0.4 — Trace and Royalty Preservation Rules
v0.5 — Agent-Readable Policy Validation
```

This makes the repository a practical AI-readable license and policy layer for origin-based structural assets.
