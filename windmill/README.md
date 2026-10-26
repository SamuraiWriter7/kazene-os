# Kazene Windmill Network v1.0

**Status:** experimental, synthetic conformance specification; **not** a verified real-world defensive system.

A detachable-blade control model beneath KazeneOS. External attack entities remain unmodified and untrusted; only isolated, bounded observations and provenance records are analyzed. The central policy guard, rather than an AI/GPT blade, authorizes transitions.

## Scope
- D: bounded forward observation; R: offline reverse traversal of previously stored Trace.
- N: neutral/disengage; P: park observation workers while retaining independent boundary protections.
- Dual D/R work may run in parallel only inside independently enforced budgets; the policy outcome here represents the guard's permitted mode, not actual parallel execution.
- Replaceable blades have fixed roles, least authority, and independently verified recovery.

## Files
- [Integrated specification](SPEC.md)
- [Example cases](examples/v1.0/policy-cases.json)
- [Independent test harness](scripts/validate.py)
- GitHub Actions: `.github/workflows/kazene-windmill-validation.yml`

Run from repository root:

```bash
python3 windmill/scripts/validate.py
```

All expected FAIL cases describe forbidden actions that the policy must reject. A PASS here confirms only consistency of the modeled policy under synthetic signals. It does not prove attack isolation, cryptographic signature verification, anomaly detection accuracy, or attribution.

## Design provenance
Concept evolution: v0.1 basic circulation → v0.2 reverse analysis → v0.3 parallel channels → v0.4 differential allocation → v0.5 prioritization → v0.6 adaptation → v0.7–0.9 blade replacement and recovery → v1.0 integrated policy.

**Compatibility:** This module supplements KazeneOS without changing its governance or existing protocols.
