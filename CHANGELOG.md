# Origin License Policy Registry

AI-readable usage policy and license template registry for origin-based structural assets.

# Changelog

All notable changes to this project will be documented in this file.

## v0.2.0-candidate

### Added

* Added `schemas/license-template.schema.json`
* Added `examples/license-template.example.yaml`
* Added `docs/license-template-registry.md`
* Updated `scripts/validate_examples.py` to validate both:

  * Usage Policy
  * License Template

### License Template Registry

The v0.2 schema defines reusable AI-readable license templates for origin-based structural assets.

A license template provides reusable default rules for:

* commercial use permission
* derivative use permission
* AI training permission
* AI inference permission
* generated output ownership
* attribution requirements
* royalty requirements
* trace preservation requirements
* redistribution conditions
* human review requirements
* allowed policy overrides

### Relationship to Usage Policy

This release introduces the following structure:

```text
License Template
        ↓
Usage Policy
        ↓
Origin Asset / Derivative Asset / Marketplace Listing
```

A License Template is a reusable policy pattern.

A Usage Policy is a concrete policy instance attached to a specific asset.

### Validation

* Confirmed that `examples/license-template.example.yaml` passes validation
* Confirmed that the updated validation script validates both v0.1 and v0.2 examples
* Confirmed that GitHub Actions passes

### Purpose

This release upgrades the repository from a single usage policy record into a reusable license template registry.

It allows origin-based structural assets to share common license patterns without rewriting the same policy rules for every asset.

### Design Notes

The v0.2 template model preserves the same controlled-readability boundary introduced in v0.1:

```text
read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required
```

AI agents may read and evaluate license templates, but sensitive actions such as payment execution, rights transfer, metadata removal, royalty modification, commercial sublicensing, and bulk AI training remain subject to human review.

### Candidate Status

This release is marked as a candidate because the initial License Template schema and example have passed validation, while asset-policy binding and deeper trace/royalty preservation rules are reserved for later versions.

---

## v0.1.0-candidate

### Added

* Added `schemas/usage-policy.schema.json`
* Added `examples/usage-policy.example.yaml`
* Added `scripts/validate_examples.py`
* Added `.github/workflows/validate-examples.yml`
* Added initial `README.md`
* Defined the first AI-readable Usage Policy Record

### Usage Policy Fields

The v0.1 schema defines structured fields for:

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
* policy notes

### Validation

* Added JSON Schema validation for YAML examples
* Added GitHub Actions workflow for automated validation
* Confirmed that the v0.1 example passes validation

### Purpose

This candidate release establishes the first machine-readable usage policy layer for origin-based structural assets.

It separates usage permission, trace preservation, royalty preservation, redistribution conditions, and human review boundaries into a structured format.

### Design Notes

The v0.1 record is designed to support the following policy boundary:

```text
read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required
```

This allows AI agents to understand and evaluate usage policies while keeping sensitive actions under human review.

### Relationship to Origin Structure Market

This repository is designed as a separated policy layer from `origin-structure-market`.

```text
origin-structure-market
  -> marketplace listing and asset discovery

origin-license-policy-registry
  -> usage policy and license rules
```

### Candidate Status

This release is marked as a candidate because the initial schema and example have passed validation, but the broader license template registry and asset-policy binding layers are reserved for later versions.


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
