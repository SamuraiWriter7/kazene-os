# Kazene Windmill Network v1.0 — Integrated Control Specification

**Maturity: experimental / synthetic policy conformance.**
Normative keywords **MUST**, **MUST NOT**, and **SHOULD** denote policy requirements, not proven runtime protections.

## 1. Boundary and threat assumptions
Kazene is a logical policy center, never an all-powerful AI. Every blade (GPT, plugin, agent, or worker) is untrusted by default. Attack entities MUST NOT be edited, counterattacked, recruited, or granted control authority. An independent ingress guard MUST enforce isolation, resource caps and access boundaries; simulated pressure is not evidence of actual protective capacity.

## 2. Modes
- **D / Forward:** bounded observation of untrusted inputs; safe data capture only.
- **R / Reverse:** analysis of immutable, already captured Trace, with no active contact to a source.
- **N / Neutral:** cease new untrusted interaction, preserve records and independent monitoring.
- **P / Park:** stop observation workers; retain safely stored evidence and external boundary protection.
D and R are independent logical pipelines, but an implementer MUST enforce a common capacity budget and reserve for independent safeguards if running them simultaneously. N/P override both.

## 3. Safety precedence
Apply precedence in order, with the first matching branch authoritative:
1. If center heartbeat is missing, a common-mode failure occurs, multiple blades fail, or pressure >=95: P.
2. If pressure >=85, blade signature/role/authority check fails, Trace continuity fails, swap race is detected, fault detection is delayed, recovery is unverified, or a blade remains failed: N.
3. If verified and command is R: offline reverse analysis only.
4. If verified and command is D: bounded capture.
5. Unknown command: N.

Pressure thresholds 85 and 95 are **synthetic defaults**, not production thresholds. Sensor readings MUST NOT be trusted merely because they are present; this toy suite assumes verified signals as inputs. Define hysteresis and trusted instrumentation before deployment.

## 4. Non-negotiable invariants
- Blades MUST NOT rewrite core policy or authorize their own release from N/P.
- Attacker-origin bytes MUST be treated strictly as data; untrusted data MUST NOT be executed as commands in a trusted control plane.
- Swap MUST NOT automatically transfer identity, memory, authority or Trace trust.
- Trace MUST be versioned and integrity checked; gaps/duplicates MUST block trusted continuation.
- Recovery MUST receive independent authorization and post-replacement verification.
- Reverse provenance is a hypothesis about observed paths, not proof of an attacker's real identity.
- A protective P/N response MUST NEVER depend on availability of the failing blade.
- A declared PASS only means the synthetic case's expected outcome matches policy, not actual defense effectiveness.

## 5. Trace and resource accounting
An implementation SHOULD keep append-only event IDs, timestamps, source claims, lineage edges, integrity proofs, processed offsets and drop counters. Differential capacity allocation MUST NOT exceed independently enforced global caps; priority sampling SHOULD reserve a nonzero unbiased sample of lower-ranked events. Missing evidence is explicitly 'unknown', never verified.

## 6. Blade swap protocol
1. Suspend the targeted blade's permissions and fence its old lease.
2. Preserve and validate its Trace boundary without copying unverified memory.
3. Verify replacement identity, signature, role and least privileges independently.
4. Reject concurrent or stale swaps.
5. Verify new blade post-swap health independently.
6. Require separately authorized release to D/R; otherwise remain N/P.

## 7. Conformance and limitations
`scripts/validate.py` checks a declared synthetic decision function against separate case fixtures, including negative conditions, while asserting no acquisition is permitted outside D. It does **not** test real signature verification, network isolation, parallel race conditions, emergency response latency, secure log storage, pressure measurement, actual GPT interoperability, or attribution accuracy.

Real-world evaluation MUST add adversarial input testing, independent implementation review, concurrency stress, fault injection, resource telemetry and secure integration testing before any safety claim.
