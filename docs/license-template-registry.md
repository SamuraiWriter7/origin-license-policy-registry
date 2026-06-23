# License Template Registry

## Overview

License Template Registry defines reusable AI-readable license templates for origin-based structural assets.

While `usage-policy.schema.json` describes the usage boundary of a specific asset, `license-template.schema.json` defines reusable policy patterns that can be applied across many assets.

## Purpose

The purpose of this layer is to avoid rewriting the same usage rules for every origin asset, derivative asset, or marketplace listing.

A license template can define common defaults such as:

- commercial use permission
- derivative use permission
- AI training permission
- AI inference permission
- generated output ownership
- attribution requirements
- royalty requirements
- trace preservation
- redistribution conditions
- human review boundaries

## Relationship to Usage Policy

```text
License Template
        ↓
Usage Policy
        ↓
Asset / Listing / Derivative

A license template is a reusable pattern.

A usage policy is a concrete policy instance attached to a specific asset.

v0.2 Scope

The v0.2 License Template Registry introduces:

schemas/license-template.schema.json
examples/license-template.example.yaml
validation through scripts/validate_examples.py
Template Types

The initial template model supports the following template types:

open_attribution
royalty_required
no_ai_training
human_review_required
commercial_restricted
custom
Human Review Boundary

AI agents may read, evaluate, and propose usage based on a license template.

However, sensitive actions remain subject to human review.

read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required

Examples of actions requiring review include:

payment execution
rights transfer
trace metadata removal
royalty allocation modification
commercial sublicensing
bulk AI training
Design Principle

A license template should not be treated as a final legal contract by itself.

It is an AI-readable policy structure that helps humans, systems, and agents understand usage boundaries before execution.

The goal is controlled readability, not uncontrolled automation.
