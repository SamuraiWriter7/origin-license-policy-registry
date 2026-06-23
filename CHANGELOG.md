# Changelog

All notable changes to this project will be documented in this file.

## v0.3.0-candidate

### Added

* Added `schemas/asset-policy-binding.schema.json`
* Added `examples/asset-policy-binding.example.yaml`
* Added `docs/asset-policy-binding.md`
* Updated `scripts/validate_examples.py` to validate:

  * Usage Policy
  * License Template
  * Asset Policy Binding

### Asset Policy Binding

The v0.3 schema defines how a specific origin-based structural asset is connected to a reusable license template and a concrete usage policy.

It introduces an effective asset-level policy surface.

```text
License Template
        ↓
Usage Policy
        ↓
Asset Policy Binding
        ↓
Origin Asset / Derivative Asset / Marketplace Listing
```

### Binding Fields

The v0.3 schema defines structured fields for:

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

### Effective Permissions

The Asset Policy Binding exposes the effective permissions that apply to the target asset.

These include:

* commercial use
* derivative use
* AI training
* AI inference

### Trace and Royalty Links

The binding record also preserves links to:

* origin asset ID
* license template ID
* usage policy ID
* trace receipt ID
* royalty allocation ID
* origin audit record ID

This makes the binding useful for marketplaces, audit systems, royalty systems, and AI agents.

### Conflict Resolution

The v0.3 binding model supports policy conflict resolution modes such as:

```text
usage_policy_overrides_template
template_overrides_usage_policy
most_restrictive_rule_wins
human_review_required
```

### Validation

* Confirmed that `examples/asset-policy-binding.example.yaml` passes validation
* Confirmed that the updated validation script validates v0.1, v0.2, and v0.3 examples
* Confirmed that GitHub Actions passes

### Purpose

This release upgrades the repository from a usage-policy and license-template registry into an effective policy binding layer.

It answers the key question:

```text
Which policy actually applies to this asset?
```

### Design Notes

The v0.3 binding model preserves the controlled-readability boundary introduced in earlier versions:

```text
read      : allowed
evaluate  : allowed
propose   : allowed
execute   : human_review_required
```

AI agents may read and evaluate binding records, but sensitive actions such as payment execution, rights transfer, metadata removal, royalty modification, commercial sublicensing, bulk AI training, and conflict resolution remain subject to human review.

### Candidate Status

This release is marked as a candidate because the initial Asset Policy Binding schema and example have passed validation, while deeper trace and royalty preservation rules are reserved for later versions.

---

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
