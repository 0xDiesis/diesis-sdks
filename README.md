<div align="center">

<img src="https://github.com/0xDiesis/diesis/raw/main/docs/diesis.png" alt="Diesis" width="120">

<pre>
 ___ ___ ___ ___ ___ ___
|   \_ _| __/ __|_ _/ __|
| |) | || _|\__ \| |\__ \
|___/___|___|___/___|___/
 -  -  -  -  -  -  -  -
</pre>

**Language SDKs for Diesis**

Build apps, services, trading bots, and smart contracts with Diesis chain
definitions, system contract addresses, and generated bindings in your language.

Native token **DS** · Ethereum-compatible contracts · Independent SDK repositories

_Greek δίεσις: the smallest interval in music.<br>Diesis aims for the smallest interval between blocks._

</div>

---

## Why this repository

Diesis builds trading, fee sponsorship, names, staking, and private transfers
into the chain itself. The SDKs give applications the contract interfaces and
chain data needed to use those services without copying addresses or writing
ABI definitions by hand.

This repository pins the language SDKs as Git submodules. Each SDK keeps its own
source, history, package identity, dependencies, and release process. One commit
here records the selected SDK revisions; install an individual SDK when building
an application, or clone this repository to work across languages.

## Choose an SDK

| Language | Repository and guide | Integration | What you get |
|---|---|---|---|
| JavaScript and TypeScript | [diesis-js](diesis-js/README.md) | viem; generated viem, wagmi, ethers, and web3.js bindings | Native RPC actions, signing helpers, contract bindings, addresses, and chain definitions. Package `@diesis/sdk`. |
| Python | [diesis-py](diesis-py/README.md) | web3.py | A Diesis client, native RPC methods, signing helpers, contract ABIs, addresses, and chain definitions. Distribution `diesis-sdk`, import `diesis`. |
| Rust | [diesis-rs](diesis-rs/README.md) | alloy | Typed contract calls, events, errors, and tuples, with addresses and chain definitions. Crate `diesis`. |
| Go | [diesis-go](diesis-go/README.md) | go-ethereum | Contract ABIs, typed parameters, selectors, event topics, addresses, and chain definitions. Module `github.com/0xDiesis/diesis-go`. |
| Swift | [diesis-swift](diesis-swift/README.md) | web3swift | Contract ABIs and typed parameters, events, errors, and tuples, with addresses and chain definitions. Product `Diesis`. |
| Kotlin and Java | [diesis-kotlin](diesis-kotlin/README.md) | web3j | JVM contract bindings, typed arguments, events, errors, and tuples, with addresses and chain definitions. |
| F# | [diesis-fsharp](diesis-fsharp/README.md) | Nethereum | Contract bindings with reads, writes, ABI codecs, events, errors, and canonical chain data. |
| OCaml | [diesis-ocaml](diesis-ocaml/README.md) | Zarith and abi-typegen-runtime | Contract bindings and ABI codecs through a C bridge, with exact integers and application-supplied transport. |
| q/kdb+ | [diesis-q](diesis-q/README.md) | abi-typegen-runtime | Event schemas, tables, and lossless log decoding for analytics. |
| Solidity | [diesis-sol](diesis-sol/README.md) | Foundry or Hardhat | Contract interfaces with structs, events, and errors, plus system address and chain ID constants. |

The SDKs have different capabilities. TypeScript and Python provide Diesis-specific
RPC and signing helpers alongside contract access. The other application SDKs
focus on generated contract bindings and their language's Ethereum tooling.
q/kdb+ provides event decoding, with no RPC or transaction submission.
Solidity interfaces call system contracts from your own contracts.

Use each linked guide for installation, supported toolchain versions, examples,
and tests. Contract bindings alone do not provide every native RPC workflow.

## Quick start

To check out all SDKs at this repository's pinned revisions:

```sh
git clone --recurse-submodules https://github.com/0xDiesis/diesis-sdks.git
cd diesis-sdks
```

If you cloned without submodules:

```sh
git submodule update --init --recursive
```

To initialize only the SDK you need in an existing checkout:

```sh
git submodule update --init --recursive -- diesis-js
```

Applications can install an SDK directly from its repository. Replace `<commit>`
with an immutable revision and follow that SDK's guide for dependencies and setup.
Use authenticated Git access where the repository requires it.

```sh
# JavaScript and TypeScript
pnpm add 'git+https://github.com/0xDiesis/diesis-js.git#<commit>' viem

# Python
python -m pip install 'diesis-sdk @ git+https://github.com/0xDiesis/diesis-py.git@<commit>'

# Solidity with Foundry
forge install '0xDiesis/diesis-sol@<commit>'
```

For Solidity, add `diesis-sol/=lib/diesis-sol/src/` to `remappings.txt`.
Application consumers use the committed bindings; the full contracts checkout
is needed for regeneration.

## Chain definitions and addresses

[diesis-js/canonical.json](diesis-js/canonical.json) defines the shared chain
configuration and addresses. SDKs copy or test against this data and expose it
through their own constants and types.

| Network definition | Chain ID | Native currency |
|---|---|---|
| Diesis | `1980` | DS, 18 decimals |
| Diesis Testnet | `19803` | DS, 18 decimals |

Use the SDK's chain definitions and address constants instead of duplicating
them in application code. Select the RPC endpoint for your deployment and
verify its chain ID before signing. Default URLs in the chain data describe
configuration; they do not establish endpoint availability.

System contract bindings cover trading, margin and settlement, staking, assets,
fee sponsorship, privacy, and `.ds` names. Some contracts have dynamic addresses.
For example, `IValidatorShare` uses a validator's deployed share address rather
than a single system constant.

## Contract generation

Generated bindings come from artifacts built from the Diesis contracts source.
Do not substitute hand-maintained ABI JSON files or edit generated code by hand.
Chain and address changes also require updating canonical data and its consumers.

In the full `0xdiesis` workspace, the repositories are siblings:

```text
0xdiesis/
├── diesis-core/
│   └── diesis/contracts/
└── diesis-sdks/
    ├── diesis-js/
    ├── diesis-py/
    └── ...
```

The Rust, Go, Swift, Kotlin, F#, OCaml, q, and Solidity generators default to
`../../diesis-core/diesis/contracts` from the SDK root. For a standalone checkout,
set `DIESIS_CONTRACTS_DIR` to a contracts source checkout with compiled artifacts.
Build with that repository's compiler wrapper and instructions.

TypeScript and Python require independently qualified artifacts and an explicitly
verified generator executable. Follow their code generation guides for the
required absolute paths and provenance checks:
[TypeScript](diesis-js/scripts/CODEGEN.md) and [Python](diesis-py/scripts/CODEGEN.md).

| SDKs | Generation entry point, run from the individual SDK root |
|---|---|
| TypeScript | `pnpm codegen` and `pnpm codegen:check`, with the qualified inputs above. |
| Python | `make codegen` and `make codegen-check`, with the qualified inputs above. Check mode does not edit generated source. |
| Rust, Go, Swift, Kotlin, F#, OCaml, q, Solidity | `python3 scripts/generate.py` and `python3 scripts/generate.py --check`. See each guide for toolchain and runtime requirements. |

From this repository's root, the shared helper runs the F#, OCaml, and q
generators in sequence:

```sh
python3 scripts/generate-preview-sdks.py
python3 scripts/generate-preview-sdks.py --check
```

### Generator version policy

All SDKs should use the latest published
[abi-typegen release](https://github.com/doublesharp/abi-typegen/releases/latest).
Pin the selected release exactly so the same inputs reproduce the same bindings.
Upgrade the pins and regenerate together when adopting a new release; do not
resolve a floating `latest` version during builds.

TypeScript and Python own their package pins and generator provenance checks:
[TypeScript](diesis-js/package.json) and [Python](diesis-py/package.json).
The contracts package supplies the default pinned executable for Rust, Go, Swift,
and Kotlin.
F#, OCaml, q, and Solidity record their exact version and contract selection in
their respective `generation.json` files. `ABI_TYPEGEN` selects an executable
for generators that support the override; it must meet that SDK's version and
provenance requirements.

When upgrading, keep the OCaml and q shared runtime libraries at the matching
abi-typegen-runtime release. Run each affected SDK's generation check, compilation,
codec tests, and consumer checks before recording new submodule pins.

## Development and pinning

Work inside the relevant SDK repository and run its documented quality commands.
There is no single build or test command for every language in this repository.
Local compilation and codec fixtures verify bindings; live RPC, signing,
submission, and receipt behavior require checks against the intended node and
network as well.

Inspect the selected revisions with:

```sh
git submodule status --recursive
```

A leading `-` means a submodule is not initialized, `+` means its checkout differs
from the recorded pin, and `U` means the gitlink has a merge conflict.
`git submodule update --init --recursive` restores recorded revisions; it does
not advance SDKs to their latest releases. Preserve local work before switching
revisions.

For a coordinated update, validate and publish changed SDK commits first, then
record their gitlinks here. Verify every child commit is available from its
remote before publishing the parent pin. Applications that depend directly on an
SDK also need their own dependency pins and lockfiles updated and checked.

### Add a language SDK

Create the SDK in its own repository, then add it here:

```sh
git submodule add https://github.com/0xDiesis/diesis-LANGUAGE.git diesis-LANGUAGE
```

Add its guide to the language table. Generate bindings from the contracts source
with the shared generator release, verify canonical chain data and ABI codecs,
and document installation, runtime requirements, capabilities, and validation
limits before publishing its pin.

## Related repositories

- [Diesis Core](https://github.com/0xDiesis/diesis-core) coordinates the node,
  execution-client base, and benchmark harness.
- [Diesis contracts](https://github.com/0xDiesis/diesis-contracts) supplies the
  Solidity source and compiled artifacts used by SDK generation.
- [abi-typegen](https://github.com/doublesharp/abi-typegen) supplies the binding
  generators and shared native runtime.
