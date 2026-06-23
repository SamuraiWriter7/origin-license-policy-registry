# Origin License Policy Registry

AI-readable usage policy and license template registry for origin-based structural assets.

## Purpose

Origin License Policy Registry defines machine-readable usage policies for origin-based structural assets.

It is designed to answer the following questions:

- Can this asset be used commercially?
- Can it be transformed into a derivative asset?
- Can it be used for AI training?
- Can it be used for AI inference?
- Who owns generated outputs?
- Is attribution required?
- Is royalty preservation required?
- What trace metadata must be preserved?
- Which actions require human review?

## Version Roadmap

### v0.1 — Usage Policy Record

Defines the first AI-readable usage policy schema.

### v0.2 — License Template Registry

Defines reusable license templates for structural assets.

### v0.3 — Asset Policy Binding

Connects usage policies to Origin Assets, Derivative Assets, and Marketplace Listings.

### v0.4 — Trace and Royalty Preservation Rules

Defines how trace metadata, origin references, and royalty pointers must be preserved.

### v0.5 — Agent-Readable Policy Validation

Allows AI agents to evaluate usage policies while preserving human review boundaries.

## Core Concept

Traditional licenses are written for humans.

This repository defines licenses and usage conditions that can also be interpreted by AI agents.

The goal is not full automation of rights transfer.

The goal is controlled readability:

```text
read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required
v0.1 Files
schemas/usage-policy.schema.json
examples/usage-policy.example.yaml
scripts/validate_examples.py
Validation
python scripts/validate_examples.py
Relationship to Origin Structure Market

This repository is a separated policy layer from origin-structure-market.

origin-structure-market
  -> marketplace listing and asset discovery

origin-license-policy-registry
  -> usage policy and license rules

---

# `CHANGELOG.md`

```md
# Changelog

## v0.1.0-candidate

### Added

- Added `schemas/usage-policy.schema.json`
- Added `examples/usage-policy.example.yaml`
- Added `scripts/validate_examples.py`
- Added initial README structure
- Defined AI-readable usage policy fields:
  - commercial use
  - derivative use
  - AI training
  - AI inference
  - generated output ownership
  - attribution requirement
  - royalty requirement
  - redistribution conditions
  - trace preservation
  - human review boundary

### Purpose

This release establishes the first usage policy record for origin-based structural assets.

It separates usage permission, trace preservation, royalty preservation, and human review boundaries into a machine-readable format.
