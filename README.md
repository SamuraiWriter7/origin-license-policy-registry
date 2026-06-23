# Origin License Policy Registry

AI-readable usage policy and license template registry for origin-based structural assets.

## Overview

Origin License Policy Registry defines machine-readable usage policies, reusable license templates, and asset-policy bindings for origin-based structural assets.

This repository separates usage permissions, license conditions, trace preservation, royalty preservation, redistribution boundaries, and human review gates into structured records that can be read by both humans and AI agents.

It is designed as a policy layer connected to origin-based marketplaces, royalty systems, trace receipts, audit records, and future agent economy protocols.

## Purpose

Traditional licenses are usually written as human-readable legal text.

This repository explores a complementary structure:

```text
human-readable license
        +
AI-readable usage policy
        +
reusable license template
        +
asset-policy binding
```

The goal is not to replace legal agreements.

The goal is to define structured policy records, reusable templates, and binding records that can answer questions such as:

* Can this asset be used commercially?
* Can it be transformed into a derivative asset?
* Can it be used for AI training?
* Can it be used for AI inference?
* Who owns generated outputs?
* Is attribution required?
* Is royalty preservation required?
* What trace metadata must be preserved?
* Which actions require human review?
* Which license pattern should be applied to this asset?
* Which policy actually applies to this asset or listing?

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
* reusable license templates
* concrete binding between assets and policies

This repository defines those rules as structured records.

## Current Version

```text
v0.3.0-candidate — Asset Policy Binding
```

This candidate release introduces Asset Policy Binding.

It extends v0.1 Usage Policy Record and v0.2 License Template Registry by adding a binding layer that connects a specific asset, license template, and usage policy into an effective asset-level policy surface.

## Repository Structure

```text
schemas/
  usage-policy.schema.json
  license-template.schema.json
  asset-policy-binding.schema.json

examples/
  usage-policy.example.yaml
  license-template.example.yaml
  asset-policy-binding.example.yaml

docs/
  license-template-registry.md
  asset-policy-binding.md

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

## v0.2 — License Template Registry

The v0.2 License Template Registry defines reusable AI-readable license templates.

A license template is a reusable policy pattern.

A usage policy is a concrete policy instance attached to a specific asset.

```text
License Template
        ↓
Usage Policy
        ↓
Origin Asset / Derivative Asset / Marketplace Listing
```

The v0.2 template model includes:

* template identifier
* template version
* template name
* template type
* template status
* compatible asset types
* default permissions
* generated output rules
* attribution rules
* royalty rules
* trace preservation rules
* redistribution rules
* human review rules
* allowed policy overrides

## v0.3 — Asset Policy Binding

The v0.3 Asset Policy Binding defines how a specific asset is connected to a license template and a usage policy.

```text
License Template
        ↓
Usage Policy
        ↓
Asset Policy Binding
        ↓
Origin Asset / Derivative Asset / Marketplace Listing
```

A binding record answers the following question:

```text
Which policy actually applies to this asset?
```

The v0.3 binding model includes:

* binding identifier
* binding version
* binding status
* target asset reference
* license template reference
* usage policy reference
* binding scope
* effective permissions
* inheritance rules
* conflict resolution rules
* trace and royalty links
* human review requirements
* binding notes

## Asset Policy Binding Example

```yaml
asset_policy_binding:
  id: asset-policy-binding-2026-0001
  version: "0.3.0"
  binding_status: candidate

  target_asset:
    asset_id: origin-2026-0001
    asset_type: origin_asset
    registry_reference: origin-structure-market/origin-2026-0001
    listing_id: listing-2026-0001
    description: >
      Origin-based structural asset listed in the Origin Structure Market.

  license_template_reference:
    template_id: license-template-2026-0001
    template_version: "0.2.0"
    template_status: candidate
    repository_reference: origin-license-policy-registry
    applied_fields:
      - commercial_use
      - derivative_use
      - ai_training
      - ai_inference
      - generated_outputs
      - attribution
      - royalty
      - trace_preservation
      - redistribution
      - human_review

  usage_policy_reference:
    policy_id: usage-policy-2026-0001
    policy_version: "0.1.0"
    policy_status: active
    repository_reference: origin-license-policy-registry
    overrides_template: true
    override_summary: >
      The concrete usage policy inherits the default license template
      but explicitly prohibits bulk AI training and requires human review.

  binding_scope:
    applies_to:
      - asset_metadata
      - marketplace_listing
      - derivative_creation
      - ai_inference_use
      - commercial_distribution
      - redistribution
      - agent_consumption
    territory: global
    duration: until_revoked
    starts_at: "2026-06-23"

  effective_permissions:
    commercial_use: royalty_required
    derivative_use: allowed_with_attribution
    ai_training: prohibited
    ai_inference: allowed

  inheritance:
    inherits_from_template: true
    inherits_from_usage_policy: true
    conflict_resolution: usage_policy_overrides_template

  trace_and_royalty_links:
    trace_preservation_required: true
    royalty_pointer_required: true
    trace_receipt_id: trace-receipt-2026-0001
    royalty_allocation_id: royalty-allocation-graph-2026-0001
    origin_audit_record_id: origin-audit-record-2026-0001
    required_preservation_fields:
      - origin_asset_id
      - license_template_id
      - usage_policy_id
      - trace_receipt_id
      - royalty_allocation_id
      - origin_audit_record_id

  human_review:
    required_for:
      - execute_payment
      - transfer_rights
      - remove_trace_metadata
      - modify_royalty_allocation
      - commercial_sublicense
      - bulk_ai_training
      - resolve_policy_conflict
```

## Effective Policy Surface

Asset Policy Binding creates an effective policy surface for a specific asset.

It tells humans, systems, and AI agents:

```text
This asset uses this template.
This asset has this usage policy.
These permissions are effective.
These trace and royalty links must survive.
These actions require human review.
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
* policy conflict resolution

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
  -> asset-policy binding
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
Binding layer between assets, listings, license templates, and usage policies.

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
v0.3.0-candidate
```

The Usage Policy Record, License Template Registry, and Asset Policy Binding have passed validation through GitHub Actions.

