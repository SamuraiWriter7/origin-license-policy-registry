# Origin License Policy Registry

AI-readable usage policy and license template registry for origin-based structural assets.

## Overview

Origin License Policy Registry defines machine-readable usage policies for origin-based structural assets.

This repository separates usage permissions, license conditions, trace preservation, royalty preservation, and human review boundaries into structured records that can be read by both humans and AI agents.

It is designed as a policy layer connected to origin-based marketplaces, royalty systems, trace receipts, and future agent economy protocols.

## Purpose

Traditional licenses are usually written as human-readable legal text.

This repository explores a complementary structure:

```text
human-readable license
        +
AI-readable usage policy
```

The goal is not to replace legal agreements.

The goal is to define structured policy records that can answer questions such as:

* Can this asset be used commercially?
* Can it be transformed into a derivative asset?
* Can it be used for AI training?
* Can it be used for AI inference?
* Who owns generated outputs?
* Is attribution required?
* Is royalty preservation required?
* What trace metadata must be preserved?
* Which actions require human review?

## Core Concept

Origin-based structural assets require more than ordinary marketplace metadata.

They also need clear rules for:

* usage permission
* derivative creation
* AI training boundaries
* AI inference boundaries
* generated output handling
* attribution
* royalty preservation
* redistribution
* trace metadata preservation
* human review gates

This repository defines those rules as structured records.

## Current Version

```text
v0.1.0-candidate — Usage Policy Record
```

This candidate release introduces the first AI-readable usage policy schema.

It defines how an origin-based structural asset may be used, transformed, redistributed, attributed, and reviewed.

## Repository Structure

```text
schemas/
  usage-policy.schema.json

examples/
  usage-policy.example.yaml

scripts/
  validate_examples.py

.github/
  workflows/
    validate-examples.yml
```

## v0.1 — Usage Policy Record

The v0.1 Usage Policy Record defines the first machine-readable usage boundary for origin-based structural assets.

It includes:

* asset reference
* commercial use permission
* derivative use permission
* AI training permission
* AI inference permission
* generated output ownership
* attribution requirement
* royalty requirement
* redistribution conditions
* trace preservation requirements
* human review requirements

## Usage Policy Example

```yaml
usage_policy:
  id: usage-policy-2026-0001
  version: "0.1.0"
  asset_reference:
    asset_id: origin-2026-0001
    asset_type: origin_asset
    origin_reference: origin-structure-market/origin-2026-0001
    royalty_pointer: royalty-allocation-graph-2026-0001
    trace_pointer: trace-receipt-2026-0001

  permissions:
    commercial_use: royalty_required
    derivative_use: allowed_with_attribution
    ai_training: prohibited
    ai_inference: allowed

  generated_outputs:
    ownership: downstream_creator
    attribution_required: true
    royalty_required: true

  redistribution:
    allowed: true
    conditions:
      - preserve_trace_metadata
      - preserve_origin_reference
      - preserve_royalty_pointer
      - preserve_license_terms

  trace_preservation:
    required: true
    required_metadata:
      - origin_asset_id
      - trace_receipt_id
      - royalty_allocation_id
      - license_policy_id

  human_review:
    required_for:
      - execute_payment
      - transfer_rights
      - remove_trace_metadata
      - modify_royalty_allocation
      - bulk_ai_training
```

## Human Review Boundary

This repository assumes that AI agents may read, evaluate, and propose usage.

However, sensitive actions should remain under human review.

```text
read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required
```

Examples of actions that may require human review:

* payment execution
* rights transfer
* trace metadata removal
* royalty allocation modification
* commercial sublicensing
* bulk AI training

## Validation

Run the validation script:

```bash
python scripts/validate_examples.py
```

The script validates YAML examples against JSON Schemas.

GitHub Actions also runs validation automatically on:

* push to `main`
* pull requests to `main`
* manual workflow dispatch

## Relationship to Origin Structure Market

This repository is separated from `origin-structure-market`.

```text
origin-structure-market
  -> origin asset registration
  -> derivative asset registration
  -> audit record
  -> royalty allocation graph
  -> marketplace listing

origin-license-policy-registry
  -> usage policy
  -> license template
  -> permission rules
  -> trace preservation rules
  -> human review boundary
```

In other words:

```text
origin-structure-market
  = where structural assets are listed

origin-license-policy-registry
  = how structural assets may be used
```

## Roadmap

```text
v0.1 — Usage Policy Record
AI-readable usage permission record.

v0.2 — License Template Registry
Reusable license templates for origin-based structural assets.

v0.3 — Asset Policy Binding
Binding layer between assets, listings, and usage policies.

v0.4 — Trace and Royalty Preservation Rules
Explicit preservation rules for trace metadata, origin references, and royalty pointers.

v0.5 — Agent-Readable Policy Validation
Validation layer for AI agents evaluating usage policies.
```

## Design Principle

The purpose of this repository is controlled readability.

AI agents should be able to understand the policy structure.

But high-impact execution should remain reviewable by humans.

```text
AI can read.
AI can evaluate.
AI can propose.
Humans approve execution.
```

## Status

```text
v0.1.0-candidate
```

The initial Usage Policy Record has passed validation through GitHub Actions.
