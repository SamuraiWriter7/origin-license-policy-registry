# Origin License Policy Registry

AI-readable usage policy and license template registry for origin-based structural assets.

## Overview

Origin License Policy Registry defines machine-readable usage policies, reusable license templates, asset-policy bindings, and preservation rules for origin-based structural assets.

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
        +
trace and royalty preservation rules
```

The goal is not to replace legal agreements.

The goal is to define structured policy records, reusable templates, binding records, and preservation rules that can answer questions such as:

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
* Which origin, trace, and royalty fields must survive downstream use?

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
* preservation of origin, trace, and royalty references

This repository defines those rules as structured records.

## Current Version

```text
v0.4.0-candidate — Trace and Royalty Preservation Rules
```

This candidate release introduces Trace and Royalty Preservation Rules.

It extends v0.1 Usage Policy Record, v0.2 License Template Registry, and v0.3 Asset Policy Binding by adding explicit preservation rules for origin references, trace metadata, royalty pointers, redistribution, AI agent actions, and human review boundaries.

## Repository Structure

```text
schemas/
  usage-policy.schema.json
  license-template.schema.json
  asset-policy-binding.schema.json
  trace-royalty-preservation-rules.schema.json

examples/
  usage-policy.example.yaml
  license-template.example.yaml
  asset-policy-binding.example.yaml
  trace-royalty-preservation-rules.example.yaml

docs/
  license-template-registry.md
  asset-policy-binding.md
  trace-and-royalty-preservation-rules.md

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

## v0.4 — Trace and Royalty Preservation Rules

The v0.4 Trace and Royalty Preservation Rules define how origin references, trace metadata, and royalty pointers must survive across reuse, transformation, redistribution, generated outputs, and AI agent consumption.

```text
Usage Policy
        ↓
License Template
        ↓
Asset Policy Binding
        ↓
Trace and Royalty Preservation Rules
```

A preservation rule set answers the following question:

```text
What must not disappear when this asset is reused?
```

The v0.4 preservation model includes:

* preservation rule identifier
* preservation rule version
* rule status
* asset reference
* policy references
* preservation scope
* trace preservation rules
* royalty preservation rules
* origin reference preservation rules
* redistribution rules
* AI agent rules
* human review requirements
* rule notes

## Trace and Royalty Preservation Example

```yaml
trace_royalty_preservation_rules:
  id: trace-royalty-preservation-rules-2026-0001
  version: "0.4.0"
  rule_status: candidate

  asset_reference:
    asset_id: origin-2026-0001
    asset_type: origin_asset
    registry_reference: origin-structure-market/origin-2026-0001
    listing_id: listing-2026-0001

  policy_references:
    license_template_id: license-template-2026-0001
    usage_policy_id: usage-policy-2026-0001
    asset_policy_binding_id: asset-policy-binding-2026-0001
    repository_reference: origin-license-policy-registry

  preservation_scope:
    applies_to:
      - asset_metadata
      - marketplace_listing
      - derivative_creation
      - commercial_distribution
      - redistribution
      - ai_inference_use
      - agent_consumption
      - generated_output
    propagation_required: true

  trace_preservation:
    required: true
    required_metadata:
      - origin_asset_id
      - trace_receipt_id
      - origin_audit_record_id
      - asset_policy_binding_id
      - usage_policy_id
      - license_template_id
      - transformation_record_id
    prohibited_actions:
      - remove_trace_metadata
      - rewrite_origin_reference
      - hide_source_asset
      - detach_audit_record
      - strip_policy_binding
      - obfuscate_transformation_path
    minimum_trace_level: full_trace_and_audit

  royalty_preservation:
    required: true
    royalty_pointer_required: true
    required_metadata:
      - royalty_allocation_id
      - royalty_pointer
      - origin_creator_id
      - allocation_basis
      - beneficiary_reference
      - payment_review_status
    prohibited_actions:
      - remove_royalty_pointer
      - bypass_royalty_allocation
      - modify_allocation_without_review
      - hide_beneficiary_reference
      - execute_payment_without_human_review
    royalty_resolution_mode: linked_allocation_graph

  origin_reference_preservation:
    required: true
    required_fields:
      - origin_asset_id
      - origin_creator
      - origin_repository
      - origin_license_template_id
      - origin_usage_policy_id
      - origin_trace_receipt_id
      - origin_audit_record_id
    attribution_notice_required: true

  redistribution_rules:
    redistribution_allowed: true
    conditions:
      - preserve_trace_metadata
      - preserve_origin_reference
      - preserve_royalty_pointer
      - preserve_license_terms
      - preserve_asset_policy_binding
      - include_attribution_notice

  agent_rules:
    allowed_agent_actions:
      - read_preservation_rules
      - validate_trace_metadata
      - validate_royalty_pointer
      - evaluate_policy_binding
      - propose_derivative_record
      - propose_redistribution_record
    restricted_agent_actions:
      - remove_trace_metadata
      - remove_royalty_pointer
      - rewrite_origin_reference
      - execute_payment
      - transfer_rights
      - approve_policy_conflict
      - override_human_review

  human_review:
    required_for:
      - execute_payment
      - transfer_rights
      - remove_trace_metadata
      - remove_royalty_pointer
      - modify_royalty_allocation
      - resolve_policy_conflict
      - approve_bulk_redistribution
      - approve_bulk_ai_training
```

## Effective Policy Surface

Asset Policy Binding creates an effective policy surface for a specific asset.

Trace and Royalty Preservation Rules protect that surface from being stripped downstream.

Together, they tell humans, systems, and AI agents:

```text
This asset uses this template.
This asset has this usage policy.
These permissions are effective.
These trace and royalty links must survive.
These actions require human review.
These metadata fields must not be removed.
```

## Preservation Principle

Trace and royalty metadata should not be treated as decorative metadata.

They are part of the asset’s structural continuity.

If origin information disappears, auditability collapses.

If royalty pointers disappear, value circulation collapses.

v0.4 therefore defines preservation as a first-class rule layer.

```text
Origin must remain visible.
Trace must remain attached.
Royalty must remain reachable.
Human review must guard execution.
```

## Human Review Boundary

This repository assumes that AI agents may read, evaluate, validate, and propose usage.

However, sensitive actions should remain under human review.

```text
read      : allowed
evaluate  : allowed
validate  : allowed
propose   : allowed
execute   : human_review_required
```

Examples of actions that may require human review:

* payment execution
* rights transfer
* trace metadata removal
* royalty pointer removal
* royalty allocation modification
* commercial sublicensing
* bulk redistribution
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
  -> trace and royalty preservation rules
  -> permission rules
  -> human review boundary
```

In other words:

```text
origin-structure-market
  = where structural assets are listed

origin-license-policy-registry
  = how structural assets may be used and preserved
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

The purpose of this repository is controlled readability and controlled preservation.

AI agents should be able to understand the policy structure.

But high-impact execution should remain reviewable by humans.

```text
AI can read.
AI can evaluate.
AI can validate.
AI can propose.
Humans approve execution.
```

## Status

```text
v0.4.0-candidate
```

The Usage Policy Record, License Template Registry, Asset Policy Binding, and Trace and Royalty Preservation Rules have passed validation through GitHub Actions.


