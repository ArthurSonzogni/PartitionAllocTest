# PartitionAlloc Standalone CI

This repository provides an unofficial Continuous Integration (CI) setup for the
[PartitionAlloc](https://chromium.googlesource.com/chromium/src/base/allocator/partition_allocator.git)
project when built in its **standalone** configuration.

## What is PartitionAlloc?

PartitionAlloc is a high-performance memory allocator developed for the Chromium
browser. It's designed for security and efficiency and is used by many other
projects, including:

- Pdfium
- Dawn
- V8
- Skia (pending)
- Angle (soon)

## Why this CI?

The official PartitionAlloc CI is part of the larger Chromium build
infrastructure. This is often good enough, but it can let incompatible changes
slip through. For instance, a build dependency on Chromium or breaking C++17
compatibility that is still required for Skia.

This project is fully generated using [`gemini-cli`](https://github.com/google-gemini/gemini-cli)

## Build Results

**2026-02**: 🟩🟩🟩🟩<br>
**2026-01**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-12**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-11**: 🟩🟩🟩🟥🟥🟥🟥🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-10**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-09**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-08**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-07**: 🟥🟥🟥🟩🟩🟩🟩🟩🟩🟥🟥🟥🟥🟥🟥🟥🟥🟥🟩🟩🟩<br>
**2025-06**: 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥<br>
**2025-05**: 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥<br>
**2025-04**: 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥<br>
**2025-03**: 🟩🟩🟥🟥🟥🟥🟥🟥🟥🟥<br>
**2025-02**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2025-01**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2024-12**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2024-11**: 🟩🟩🟩🟩🟩🟩🟩<br>
**2024-10**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2024-09**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟥🟥🟥🟥🟥🟩🟩🟩<br>
**2024-08**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2024-07**: 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2024-06**: 🟥🟥🟥🟥🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩<br>
**2024-05**: 🟥🟥🟥🟥<br>

<details>
<summary>🟩 Configuration: `release`</summary>

| Email | Date | Title | ? |
|---|---|---|---|
| nuskos | 2026-02-05 | [Add nuskos@ to PartitionAlloc OWNERS.](./output/release/7289d97695f40ba6a8ae56618d45786eadffdc7b.log) | 🟩 |
| hellofroser | 2026-02-05 | [Fix some PA_UNSAFE_TODOs in //base/allocator/partit...](./output/release/bb5a3e33f5ea17a2e27059d99b12273b1b1c3604.log) | 🟩 |
| tasak | 2026-02-03 | [[3/4] Implement AsanRawPtrService V2](./output/release/24e411a428ae1128d44850dc0b98376da84bddd5.log) | 🟩 |
| mikt | 2026-02-02 | [[PA] Refactor and merge PA/AC shim logic](./output/release/f9fe9152fca91e24bfc495f91b42a36800b952a0.log) | 🟩 |
| awillia | 2026-01-30 | [Fix comment references to "_unittests.cc" files (ba...](./output/release/baaa6670c23c19485d0a5a538bc43d3332def328.log) | 🟩 |
| arthursonzogni | 2026-01-29 | [PartitionAlloc: Do not assert C++20.](./output/release/4344806135c21081ac9c2551b9d8e26fd1894280.log) | 🟩 |
| ayumiohno | 2026-01-27 | [PA: Implement AllocToken support in PartitionAlloc](./output/release/936619c71ecb17c0e2482cf86be3f3f417b2f683.log) | 🟩 |
| mcnee | 2026-01-27 | [Prepare for making BindOnce and BindRepeating nodis...](./output/release/492f8c119a98911c17bdfc1559b10b6431ea419d.log) | 🟩 |
| sdefresne | 2026-01-27 | [Add transparent version of std::equal_to<> and std:...](./output/release/e1b3bee8ba37d08bb642265ccb78e54cedd00a77.log) | 🟩 |
| mikt | 2026-01-27 | [Reland "[PA] Make PartitionRoot a class"](./output/release/f7b856afab03e211acdfef1467992e98c274d13b.log) | 🟩 |
| ayumiohno | 2026-01-26 | [PA: Remove __throw_out_of_range in address_pool_man...](./output/release/1e050ef1abfc2d85451625b1f257eba703670a65.log) | 🟩 |
| ayumiohno | 2026-01-20 | [PA: Remove thread_local in parition_alloc_base Plat...](./output/release/6ad9a9a880baebe89850beec18ebd506419b18af.log) | 🟩 |
| tsepez | 2026-01-20 | [Remove base::MakeClampedNum()](./output/release/329ff99d5d81aca88c066dce706136846abd5553.log) | 🟩 |
| ayumiohno | 2026-01-19 | [PA: Use system allocator in ASan even when kNoHooks.](./output/release/cb11b9bc34c2183fa5049a69cd1ea09511289235.log) | 🟩 |
| arthursonzogni | 2026-01-19 | [PartitionAlloc: Additional C++23 presubmit.](./output/release/a663ade348e34ae02e7db69a51e0a5ab92770372.log) | 🟩 |
| victorvianna | 2026-01-15 | [Improve PRESUBMIT against C++23 features in partiti...](./output/release/5b70baa1fd02c684fb68f7dc6fad54decabbcaee.log) | 🟩 |
| tsepez | 2026-01-15 | [Remove base::MakeCheckedNum<>().](./output/release/24446349a7656b671465493504dfdcf3f638419a.log) | 🟩 |
| mliedtke | 2026-01-15 | [[base] Undo consteval usages in base/allocator/part...](./output/release/b6c5ed1c618f27a1a3402b126cb1e9ab9aff4785.log) | 🟩 |
| victorvianna | 2026-01-14 | [[styleguide] Allow if consteval](./output/release/e2ebbb786efdde6cb5440c4d2386f5acc2fba85f.log) | 🟩 |
| ayumiohno | 2026-01-14 | [Reland "PA: Support multiple ThreadCache instances ...](./output/release/46fd97ba8656535accce5e53ab59c23a6f12f9f0.log) | 🟩 |
| koerber | 2026-01-14 | [Revert "[PA] Make PartitionRoot a class"](./output/release/9f81c694ae53d37f01e11bd015dcb9dfebba55ea.log) | 🟩 |
| mikt | 2026-01-14 | [[PA] Make PartitionRoot a class](./output/release/0388f4caa3d4e5809f741bd1c0c8642d20a98fd4.log) | 🟩 |
| elkurin | 2026-01-13 | [Revert "PA: Support multiple ThreadCache instances ...](./output/release/b2283b2f8a113742a70daa64a861a85b933e6733.log) | 🟩 |
| ayumiohno | 2026-01-13 | [PA: Support multiple ThreadCache instances per thread.](./output/release/a759a7b189d64e43a04d4179103d0f00b8fd4ee8.log) | 🟩 |
| hans | 2026-01-12 | [Fix/suppress -Wunsafe-buffer-usage for printf-style...](./output/release/9149542aa89480668d5d044f50706dbe2d74b0a8.log) | 🟩 |
| victorvianna | 2026-01-12 | [Promote #warnings to #error](./output/release/245dbb7bebfba6e48599342e3aa4f17f32f8b7bc.log) | 🟩 |
| ayumiohno | 2026-01-09 | [PA: Consistently pass BucketSizeDetails to free/qua...](./output/release/b2155fca494c5b6266d42f9129ae3a7b85482c95.log) | 🟩 |
| ayumiohno | 2026-01-09 | [PA: Optimize FreeWithSizeAndAlignment in simple path](./output/release/b809160344d7900a2e0ddd735f187ffe48576649.log) | 🟩 |
| pmonette | 2026-01-07 | [Migrate off legacy MOCK_METHODn macros](./output/release/9cce6259aef60f8dbea52f421bb0234eb7cdadd5.log) | 🟩 |
| glaubitz | 2026-01-06 | [base/{allocator,numerics}: Fix incorrect ARM prepro...](./output/release/ca88a350fcbf85c268d741cf8acd248d7f5529a0.log) | 🟩 |
| mikt | 2026-01-05 | [[PA] Parametrize Empty Slot Span Ring Buffer size](./output/release/4b623f0c69ff979206bc7788fedbb27ddffbdcb3.log) | 🟩 |
| mikt | 2025-12-25 | [[PA] Persist MemoryReclaimer data on caller side](./output/release/8bfdd5d9316a1883935190b61280c4765bfa14c4.log) | 🟩 |
| hans | 2025-12-12 | [Fixes for nodiscard std::optional, std::set operations](./output/release/c6560eb97899b82a2869b7af638cab5063b48b79.log) | 🟩 |
| ayumiohno | 2025-12-09 | [PA: Upgrade DCHECKs to CHECKs in FreeWithSize, guar...](./output/release/e711e98faec702084c26a43a411eb4bd3747bcbb.log) | 🟩 |
| mikt | 2025-12-08 | [[PA] Narrow down locked section](./output/release/d2b46c259f0bd47fcc5d20c2cca97043ca5c71fe.log) | 🟩 |
| arthursonzogni | 2025-12-07 | [Reapply "Convert to UNSAFE_TODO in partition_alloc ...](./output/release/fe0329b346753191011b073535fc9f2fe64da141.log) | 🟩 |
| yukishiino | 2025-12-04 | [PA: Share allocator_shim::IsAlreadyRegistered betwe...](./output/release/090a06003985436a6e146838dbb3a5ec71c958b7.log) | 🟩 |
| anandrv | 2025-12-03 | [[partition_alloc] Increase amount of spinning in lo...](./output/release/d0ab85f4a6da9905487bb0301251102c03625c56.log) | 🟩 |
| arthursonzogni | 2025-12-03 | [Convert to UNSAFE_TODO in partition_alloc in base_2](./output/release/b231448a17e4c078154f29a28e2f9e9bbe210fac.log) | 🟩 |
| arthursonzogni | 2025-12-03 | [Convert to UNSAFE_TODO in partition_alloc in base_1](./output/release/2a811452fe4f79a9f8910ccb8df1f348a92a6236.log) | 🟩 |
| arthursonzogni | 2025-12-03 | [Convert to UNSAFE_TODO in partition_alloc in posix](./output/release/aa7166796bb04ae800c7b0e59abbf5e0816689c3.log) | 🟩 |
| thestig | 2025-12-01 | [PartitionAlloc: Remove RawPtrTraits::kDisableBRP](./output/release/39d55c5da2324729af9e76abc3c293bdeda48a06.log) | 🟩 |
| luci-bisection | 2025-11-30 | [Revert "Convert to UNSAFE_TODO in partition_alloc i...](./output/release/ebda611438a5eb6b3e3a2b6c67ddc49fa2b29ac1.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in mac_li...](./output/release/5793f657f4dd960addd95a2d6022c4f785e46c2e.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in partit...](./output/release/9f17d115d835fc782f48648cea5bc7b4fe83ae4f.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in windows](./output/release/cf2789c6634d68aa9acafc91d34a27462c54743d.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in fuchsia](./output/release/dc1590b9fe1c12e4746a6d7c7a903f2ea6af19a5.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in partit...](./output/release/3c6388b2fcda07db5e6753c2309030de942747a7.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in shim](./output/release/d2c2747ffe3d648338366e9df117b3984a43509a.log) | 🟩 |
| thestig | 2025-11-28 | [Forward declare PartitionRoot in scheduler_loop_qua...](./output/release/af595168d6ebc1aa751159affaf0d7f8c1b6e520.log) | 🟩 |
| ayumiohno | 2025-11-26 | [PA: Add finch feature flag to enable/disable FreeWi...](./output/release/ee9dae5f4046d8f40a2559250b6067691f10683c.log) | 🟩 |
| ayumiohno | 2025-11-26 | [PA: Optimize FreeWithSize in simple path.](./output/release/db3681ad5c220f81f5189e3f0bd616a4b2df6365.log) | 🟩 |
| mikt | 2025-11-20 | [[PA/AC] Batch-free quarantined entries](./output/release/c0a91c99639bc5e15f420ae8a6c764f3bcd0bccf.log) | 🟩 |
| thestig | 2025-11-20 | [Include <features.h> directly in build_config.h on ...](./output/release/4b1c1547ba19d65c3900cf790b1dc493997a80b4.log) | 🟩 |
| rgod | 2025-11-20 | [Revert "Convert to UNSAFE_TODO in partition_alloc"](./output/release/86291accf55223eec529e421f57e126e3e663963.log) | 🟩 |
| arthursonzogni | 2025-11-20 | [Convert to UNSAFE_TODO in partition_alloc](./output/release/a5480754481fa0e6ea26242701345819fc391d98.log) | 🟩 |
| arthursonzogni | 2025-11-20 | [partition_alloc: Move to C++20](./output/release/a626491f4bc59f8bfd6c77db93dabebc4cd30466.log) | 🟩 |
| tasak | 2025-11-18 | [[PA] Make PartitionAllocExternalMetadata 100%-enabl...](./output/release/21d8011dfea14a95cc2baaa3d76f6d25c2bbcc9d.log) | 🟥 |
| tarcisio.fischer | 2025-11-18 | [Enable and improve Death Tests for Partition Alloca...](./output/release/ac53ec3334499e9ee36eb2623f1344b8e5afeef3.log) | 🟥 |
| mikt | 2025-11-13 | [Reland "[PA] Refactor to use a typed SlotStart to r...](./output/release/1551e3ebf56ad234661c79a5e9d2dbe94988e744.log) | 🟥 |
| tasak | 2025-11-11 | [[PA] Ramp up External Metadata trial to 25% on canary](./output/release/37d717b2583271f64d41d2e09e560bd7baae4c5e.log) | 🟥 |
| jood | 2025-11-11 | [Revert "[PA] Refactor to use a typed SlotStart to r...](./output/release/a9912a4b18c048484e96aa3ce106da21930ed8b6.log) | 🟥 |
| mikt | 2025-11-11 | [[PA] Refactor to use a typed SlotStart to replace u...](./output/release/495c1417ff2f7ce3a4a37f2d54d57712a4379ef2.log) | 🟥 |
| ayumiohno | 2025-11-06 | [PA: remove if PA_BUILDFLAG(ASSESRT_CPP_20)](./output/release/3c92a87d2c9f9319118e951e64bd6f9c1e0306d2.log) | 🟥 |
| mikt | 2025-11-04 | [[PA/AC] Implement size-based filtering](./output/release/f228d5a6170573dba10189f5a8d32623954c39c4.log) | 🟩 |
| kaiyilin | 2025-11-02 | [Revert "Track SchedulerLoopQuarantine zap/purge tim...](./output/release/fd571058170087fff09fcac020c9e32c36032387.log) | 🟩 |
| nuskos | 2025-11-02 | [Track SchedulerLoopQuarantine zap/purge timings](./output/release/300767b01ec7f3260d09820c564dc47219691061.log) | 🟩 |
| dloehr | 2025-10-31 | [Revert "Disable test until next clang roll"](./output/release/fa63bd8319311b5c5f5a4e63678830c4a3655b04.log) | 🟩 |
| yukishiino | 2025-10-31 | [PA: Add shim/HowToInterposeOrIntercept.md](./output/release/abae057a0b75d5cb4738606734d4f3492ad4e2bc.log) | 🟩 |
| tasak | 2025-10-29 | [[PA] Ramp up External Metadata trial to 10% on canary](./output/release/a8bbea7ea2d6e41cd0a8687756e42c8b32a9b0c1.log) | 🟩 |
| mikt | 2025-10-29 | [[PA] Mitigate shutdown hang from Scheduler-Loop Qua...](./output/release/2f4069fb8d7afbd9e3c078a14a5bab8280a68cf6.log) | 🟩 |
| tasak | 2025-10-17 | [[PA] Make PartitionAllocExternalMetadata enabled at...](./output/release/db8446987dfff3cfc0c100b7d58e6a404ef639eb.log) | 🟩 |
| ahaas | 2025-10-13 | [Cleanup MiracleParameter implementation of ThreadCa...](./output/release/eb106c8d4435c9c513b7623be5e114d8d45b216d.log) | 🟩 |
| dloehr | 2025-10-09 | [Revert "Roll clang+rust llvmorg-22-init-8940-g4d4cb...](./output/release/81b93883f50bc4948aa65711dc8bd12ef51351b1.log) | 🟩 |
| kjlubick | 2025-10-09 | [Add const to boolean operators](./output/release/081932d24e1f06bd1eea2fd42a21df0721c8faa5.log) | 🟩 |
| dloehr | 2025-10-09 | [Roll clang+rust llvmorg-22-init-8940-g4d4cb757-84 :...](./output/release/e56f65cd966122c386a74d5fbfcadbbcc46d494b.log) | 🟩 |
| aattar | 2025-10-08 | [Map commit failure exit code to a memory eviction s...](./output/release/11372dd73e164e7cc7cfe4e4cd75bdb26ec2b4c5.log) | 🟩 |
| mikt | 2025-10-06 | [Reland "[PA/BRP] Enable BRP-ASan on iOS"](./output/release/1fd5c75f3b3683a004d2494a184a15b6bcef463a.log) | 🟩 |
| dloehr | 2025-10-01 | [Disable test until next clang roll](./output/release/7032e49a7847caf235a4d67459a0d417c1ebf251.log) | 🟩 |
| lpromero | 2025-09-29 | [Revert "[PA/BRP] Enable BRP-ASan on iOS"](./output/release/e3fec0a6803f0228bad652b12645ab19574e8bc9.log) | 🟩 |
| mikt | 2025-09-26 | [[base/PA] Add scheduler loop quarantine support to ...](./output/release/cca2b369b2f8895cb14e24740e1f9bf91d5b371e.log) | 🟩 |
| lizeb | 2025-09-26 | [[PartitionAlloc] Remove launched feature for "use f...](./output/release/ee6c8d0716e9d10d1ad25de97e690ddfa54f2c4a.log) | 🟩 |
| justincohen | 2025-09-25 | [ios:  Re-enable PA-E ReadExecutePages test on iOS 1...](./output/release/9d3ee7c25f88e6e070308f0f80f2025646278355.log) | 🟩 |
| mikt | 2025-09-23 | [[PA/BRP] Enable BRP-ASan on iOS](./output/release/ecbbabb292b5e07a332dfdb206591aa2ee7e8f44.log) | 🟩 |
| noemies | 2025-09-22 | [[iOS Gardener] Disable ReadExecutePages on device](./output/release/ae5f94430c494db73fdcd2106269d3b08ea8e24f.log) | 🟩 |
| justincohen | 2025-09-22 | [ios: Enable some disabled PartitionAlloc unittests.](./output/release/84a41f2a2242f43d95fc8333725a89ba38b1f8f1.log) | 🟩 |
| stefanoduo | 2025-09-19 | [Cronet: Disable PartitionAlloc via GN arg definitio...](./output/release/e3b4f7b28213398c1891b27c23cca7581d7cec90.log) | 🟩 |
| mikt | 2025-09-19 | [[PA] Configure default stack size for iOS](./output/release/78467db77680f3c375dcff3ff79ed5a7578bb3e5.log) | 🟩 |
| nuskos | 2025-09-19 | [Enable PartitionAlloc External Metadata feature at ...](./output/release/5af527282d75750fe12450ca508fb2fe95ea0810.log) | 🟩 |
| rop | 2025-09-18 | [Setting Update Mechanism for these dependencies:](./output/release/eb93de534d21673c0a860c373ae9bce1a360eba8.log) | 🟩 |
| thakis | 2025-09-16 | [Roll libc++ from 0257666efcf9 to 7b8dc07adc0f (9 re...](./output/release/2c06e4c19773cdfc60f0a4a947363f0b7748f4ca.log) | 🟩 |
| avi | 2025-09-15 | [Remove Darwin version TODO](./output/release/bb8643420b21841d7530b343cb247e061c0eb3b8.log) | 🟩 |
| tasak | 2025-09-14 | [[PA] Disable PartitionAlloc External Metadata](./output/release/ccbdeaaeb633a85f317a1d27c17a118fab789b64.log) | 🟩 |
| acondor | 2025-09-12 | [Implement unchecked calloc via shim](./output/release/fae4df38cef9720a13dd55a6b1d20600919e671b.log) | 🟩 |
| tasak | 2025-09-12 | [[PA] Deflake and re-enable PartitionAllocTest.Check...](./output/release/cb2ed1009c4d5e310bc4ccc2bfd2d38a54e0461b.log) | 🟩 |
| kojii | 2025-09-11 | [[icu] Disables a `PartitionAllocTest` that seems fl...](./output/release/9d08d0ef84ae6525bac4f69cb967bed38858dce5.log) | 🟩 |
| anandrv | 2025-09-09 | [[partition_alloc] Report acquisition time for conte...](./output/release/dd3fc2d811574cf24220d2010bf3a7d00d644aee.log) | 🟩 |
| rop | 2025-09-07 | [LSC Metadata fix](./output/release/09c9e8d5f0d23bd46bfb1f7bc10a294ea7a60774.log) | 🟩 |
| zhoumingtao | 2025-09-05 | [partition_alloc: Support dynamic page size for Loon...](./output/release/3926658b1b5124b0c85bc9f2bac450214d3bf7a4.log) | 🟩 |
| lizeb | 2025-09-04 | [[PartiitonAlloc] Suppress TSAN error due to constan...](./output/release/c001374914bffb3db6ed024a521f3a38f11d0911.log) | 🟩 |
| justincohen | 2025-09-03 | [Re-enable BRP zapping on iOS](./output/release/7e1a38e21c908deac07090d1a8e7e49bbd0f862a.log) | 🟩 |
| justincohen | 2025-08-29 | [Revert "[PA] Add configuration for iOS binary exper...](./output/release/51d0a558ecdf5cac58509d08263c36764c270ca6.log) | 🟩 |
| mikt | 2025-08-28 | [[PA] Separate Scheduler-Loop quarantine branch for ...](./output/release/b12f7b4f52f41aa7bfb690cf3b766a00c55261fd.log) | 🟩 |
| justincohen | 2025-08-27 | [ios: Enable PartitionAlloc BackupRefPtr by default ...](./output/release/18feb39705cfd694c878286497d6929c25b6a82d.log) | 🟩 |
| ivan.pavlotsky | 2025-08-27 | [Disable Xclang and target-feature flags for non-Cla...](./output/release/f35da6421e88228655ec1d5dbe1dcdc870a4741a.log) | 🟩 |
| tasak | 2025-08-26 | [[PA] Make PartitionAlloc External Metadata 50% enab...](./output/release/ba5e9459f6ad57cffa4800e08baa01ea6c811ffc.log) | 🟩 |
| tasak | 2025-08-21 | [Reland "[PA] Enable External Metadata on canary."](./output/release/ce17d3c2126ae2b3611eac90d6b54035f1e595f4.log) | 🟩 |
| tasak | 2025-08-20 | [Revert "[PA] Enable External Metadata on canary."](./output/release/22124931fa99556ec56b4ac30476b594f9f1b80a.log) | 🟩 |
| dsanders11 | 2025-08-20 | [Remove unused include in scheduler_loop_quarantine_...](./output/release/180844cd9919d753d40b55409996c659f55250e2.log) | 🟩 |
| tasak | 2025-08-18 | [[PA] Enable External Metadata on canary.](./output/release/1a0ba72ed0a07107cf2398a93561f44c855c58b0.log) | 🟩 |
| tkent | 2025-08-18 | [Remove `WTF::` in base/](./output/release/902c2e234fc94d82df3eab27070600db88e9f63e.log) | 🟩 |
| tasak | 2025-08-17 | [[PA] Skip HardeningTest.(PoolOffset)MetadataPointer...](./output/release/f81bc9851284fe29f2a946f1dfd793b77941fd01.log) | 🟩 |
| tasak | 2025-08-14 | [Revert "[PA] Enable external metadata on canary"](./output/release/5566f889c0c929938fb11a0c04235b3b7932a4c7.log) | 🟩 |
| tasak | 2025-08-14 | [[PA] Enable external metadata on canary](./output/release/ecbda5f809e71d995d4002a1530c625ef848b073.log) | 🟩 |
| tasak | 2025-08-13 | [[PA] Check `metadata_start_` at InitThreadIsolatedP...](./output/release/6003b144a5c796206271fb2337709fa506c44fa6.log) | 🟩 |
| aeubanks | 2025-08-12 | [Update nocompile tests](./output/release/a40ae6084cc3d928e1284eef447cae38a224f36a.log) | 🟩 |
| tasak | 2025-08-12 | [Revert "[PA] Enable PartitionAllocExternalMetadata ...](./output/release/c9620c2ad14f777a1873426e11d34573e211557e.log) | 🟩 |
| tasak | 2025-08-11 | [[PA] Enable PartitionAllocExternalMetadata on canary](./output/release/ea91c2f570f1d3be3d29f27f1d1a099fb368c325.log) | 🟩 |
| tsepez | 2025-08-07 | [Remove some pragma allow_unsafe_buffers from partit...](./output/release/8f2ac09151b3a0cf713bcf93bb112b21f91c63c2.log) | 🟩 |
| tasak | 2025-08-07 | [Revert "[PA] Enable ExternalMetadata feature on can...](./output/release/4a3b2fb6d953a9ad17e7da948645fa7e180926b0.log) | 🟩 |
| tasak | 2025-08-06 | [[PA] Enable ExternalMetadata feature on canary Enab...](./output/release/69da7baf768c4edb1cd77a5be1538ce4283b7736.log) | 🟩 |
| arthursonzogni | 2025-08-06 | [PA: Suppress REALLOC_GROWTH_FACTOR_MITIGATION limit.](./output/release/5c2d24bfafe63e10a61ec335509d5d83acd7db11.log) | 🟩 |
| mikt | 2025-08-05 | [[PA] Fix PartitionRoot::CheckMetadataIntegrity](./output/release/356065b030e6194a732705e86a11248db2728786.log) | 🟩 |
| rulongchen | 2025-08-05 | [[PartitionAlloc] Fix crash when nullptr is passed t...](./output/release/659d300ab723b5ea128984dda1d0e94d456ab665.log) | 🟩 |
| tsepez | 2025-08-04 | [Remove file-wide unsafe buffer pragamas in partitio...](./output/release/218e32d7878cfa006a9e90df6dc16a377cffbdb3.log) | 🟩 |
| tsepez | 2025-08-04 | [Propagate UNSAFETY through partition alloc raw poin...](./output/release/a25ec884fd1dd0d9f50f7baf1883982e8db46b41.log) | 🟩 |
| tsepez | 2025-08-04 | [Mark unsafe raw_ptr<T> operations as unsafe.](./output/release/4e92c91bb300e840f586f504e6fc6ea2adb329b2.log) | 🟩 |
| mikt | 2025-08-04 | [[PA] Scheduler-Loop Quarantine is configured via JSON](./output/release/f79cd042e21bc40da52829e883813b4f3f093ff2.log) | 🟩 |
| mikt | 2025-08-03 | [[PA] Purge Scheduler-Loop Quarantine on UI Thread T...](./output/release/22ea4eaebb2458920d56eb68a1db74028375303e.log) | 🟩 |
| tsepez | 2025-08-01 | [Remove base/allocator from unsafe_buffers_paths.txt...](./output/release/57104f156773d81ca03b0c41d118821475646bf5.log) | 🟩 |
| tsepez | 2025-08-01 | [Add PA_UNSAFE_BUFFER_USAGE macro to partition alloc.](./output/release/f5d9c0b9bfccf8b0e7716f9c70623ce6129fea9b.log) | 🟩 |
| tasak | 2025-07-31 | [[PA] Propose "ExternalMetadata" synthetic finch tri...](./output/release/ec5fa718c5470c1f4840f50f72b2815545ee09e8.log) | 🟩 |
| dsanders11 | 2025-07-29 | [Remove unused include in partition_address_space.h](./output/release/f5c8626fa2949908146d00fdc3a182b16e5c32b5.log) | 🟩 |
| arthursonzogni | 2025-07-27 | [[PA] Fix unused `use_libcxx_modules`.](./output/release/aee60823002b0e80d96e76e56951446ce0eb58b2.log) | 🟩 |
| tasak | 2025-07-27 | [[PA] Move Metadata outside of GigaCage (6/7)](./output/release/5ab2ac91deaf53dbbd612e779b3f51253bf02243.log) | 🟩 |
| tasak | 2025-07-27 | [[PA] Move Metadata outside of GigaCage (5/7)](./output/release/828b52630e80e619f057deba245c83644a4066c6.log) | 🟩 |
| tikuta | 2025-07-24 | [partition_allocator: Disable libcxx module for unit...](./output/release/0df75035937ddb4efd66639f25b08d53d7b4f8ec.log) | 🟩 |
| thestig | 2025-07-24 | [Auto-format //base GN files](./output/release/fd0128b7cc4a5ee2e1d9f6eec022b6bf73694fe6.log) | 🟩 |
| tasak | 2025-07-23 | [[PA] Move Metadata outside of GigaCage (4/6)](./output/release/1e3b00f0a40be8ea75dd4709821b71b2c079912b.log) | 🟩 |
| chrdavis | 2025-07-23 | [ThreadTicks GetForThread should include kernel time...](./output/release/d7ae27f0e2a0c03b9f80ca1195b04fedcdf1193c.log) | 🟩 |
| tasak | 2025-07-22 | [[PA] Move Metadata outside of GigaCage (3/5)](./output/release/39ba710d71b750335e1438d30ba62b1c0736e73e.log) | 🟩 |
| mikt | 2025-07-22 | [[PA] Allow to ensure ThreadCache without PartitionR...](./output/release/833fe8d5e0a9d775255cc8a09fdb71183c5f587f.log) | 🟩 |
| tikuta | 2025-07-21 | [partition_allocator: Disable libcxx module for allo...](./output/release/49e207e96bec179c82e609cf0a052d42d4c2ac2c.log) | 🟩 |
| tasak | 2025-07-18 | [[PA] Add pa_check.md](./output/release/b7aff97e9add16d7a0f04c9eb2e752d6f7dff85d.log) | 🟩 |
| tasak | 2025-07-18 | [[PA] Move Metadata outside of GigaCage (2/5)](./output/release/75b1cb38a7826527337da4ba4b3b6926bba29675.log) | 🟩 |
| tasak | 2025-07-17 | [[PA] Move Metadata outside of GigaCage (1/5)](./output/release/369c817c900ed3796da34b973b4b95391a836941.log) | 🟩 |
| cdesouza | 2025-07-17 | [[exit-time-destructors] Exclude target with warnings](./output/release/7186dfd2903897b1cfde4a36cfc5ede25c9c6f3d.log) | 🟩 |
| arthursonzogni | 2025-07-16 | [partition_alloc: Fix missing include on Windows.](./output/release/f5822de8f74df009da56681cca82a3c986bbfc67.log) | 🟩 |
| arthursonzogni | 2025-07-15 | [partition_alloc: Resolve C++20 compile errors.](./output/release/328d516729e7e9edc833244c73cc9013828e5a1a.log) | 🟩 |
| thakis | 2025-07-14 | [Remove remaining __pnacl__ and __native_client__ in...](./output/release/7b2807165fad397df23f5f749b15e9e43269ccf5.log) | 🟥 |
| tikuta | 2025-07-09 | [base: Remove references to BUILDFLAG(IS_NACL)](./output/release/a54ac8d0dd78019fb41d2e376726d45b287e856b.log) | 🟥 |
| lizeb | 2025-07-09 | [[PartitionAlloc] Use fewer VMAs by default on Linux...](./output/release/db340435e8d7e8eb89925d3006ecaf6427e3ab4f.log) | 🟥 |
| mikt | 2025-06-27 | [[PA] Fix pool offset freelist DCHECK with MTE](./output/release/79b418050876e0c4187a80f668e81ce956b32bf2.log) | 🟥 |
| lizeb | 2025-06-26 | [[base/allocator] Remove launched features](./output/release/11aaded5a31dc53a08781ca47f146f3795d021c4.log) | 🟥 |
| mikt | 2025-06-25 | [[PA] Add callback for DoubleFreeDetected or Corrupt...](./output/release/3d6e246fc6014fd3f9f850876eae0fcd8f97921e.log) | 🟥 |
| thiabaud | 2025-06-25 | [[partition_alloc] Add more threading annotations](./output/release/983d556a9aed36814954a4463bb0b508d2af133a.log) | 🟥 |
| tikuta | 2025-06-24 | [partition_alloc: Add a missing include for std::ignore](./output/release/f8a48647751d44a0497a76633f6dc22ab28f51ad.log) | 🟥 |
| tasak | 2025-06-23 | [[PA] Make PartitionAllocMemoryAllocationPerfTest hu...](./output/release/85594a8469649294d3b365e0637256a87dc74602.log) | 🟥 |
| dcheng | 2025-06-20 | [base: remove NaCl from BUILD.gn, as well as NaCl-on...](./output/release/9b8de412d87c20117d2d04836bc5fa85866eaa08.log) | 🟥 |
| mikt | 2025-06-18 | [[PA] Add option not to crash on Double-Free or Corr...](./output/release/ffa6d285560e810ab57e9a026b58f0a722658a6a.log) | 🟥 |
| bikineev | 2025-06-18 | [PA: Fix an include to be relative to PA source dir](./output/release/a28c3c3d01412a17ebf145bfe2d73c8071c686e3.log) | 🟥 |
| rop | 2025-06-17 | [LSC Add 'Update Mechanism:' to README.chromium](./output/release/49c08e7ea1746f671ce75b96f6ca444f6d6065ab.log) | 🟥 |
| avi | 2025-06-12 | [Update MacOSVersion() for macOS 26](./output/release/73de62811794a78ccb95ed3e197180ec8fb666c2.log) | 🟥 |
| thiabaud | 2025-06-09 | [[partition_alloc] Add threading annotations](./output/release/50a84f34499cdfdc040a9d2c8fc1f031d31bbc78.log) | 🟥 |
| fdoray | 2025-06-06 | [[partition_alloc] Add mechanism to terminate a proc...](./output/release/a585fc502ffa23ddce3412973eba2fe677325f02.log) | 🟥 |
| kdlee | 2025-06-05 | [PA: Remove seam code for 4S](./output/release/76e5e3ac91101d2976805205fb51585c266e548f.log) | 🟥 |
| thestig | 2025-06-05 | [[PA] Use PA_LOG() instead of LOG()](./output/release/37c90018cca427ce66d7f2fc3f43fca9d6ee9b6b.log) | 🟥 |
| mikt | 2025-06-03 | [[PA] Optimize Purging mechanism for Scheduler-Loop ...](./output/release/e3668842ccb3173913161900ec731508f0655604.log) | 🟥 |
| mikt | 2025-06-03 | [[PA] Replace usable_size with slot_size in Schedule...](./output/release/b1a4a44e2310b4661acf418a3524778969943919.log) | 🟥 |
| mikt | 2025-06-03 | [[PA] Do Scheduler-Loop Quarantine after BRP Quarant...](./output/release/b95054240369556471d5c438217480a23089aa4a.log) | 🟥 |
| mikt | 2025-06-03 | [[PA/E-LUD] Refactor: Fork LightweightQuarantine](./output/release/ffb614650932ce01003b1f1cbf26c1709f68c364.log) | 🟥 |
| hans | 2025-05-30 | [Mark pointer in PartitionAllocPageAllocatorTest.Dec...](./output/release/d617778ed253822ee4c1bb9d03826f01e5f09e32.log) | 🟥 |
| avi | 2025-05-29 | [Remove the macOS 11 malloc size hack from Partition...](./output/release/3ae30e4cf9d6f59ba825dcc96af9940ab35bf27b.log) | 🟥 |
| nuskos | 2025-05-29 | [Use std::array instead of a c style array in PurgeP...](./output/release/a160ae6759caac1e19e3bf51b3660b649a9aba2e.log) | 🟥 |
| mikt | 2025-05-28 | [Reland "[PA] Cache ReservationOffsetTable instead o...](./output/release/964c6996d56bd2167f4f6fdb2d88acfeba32c5d8.log) | 🟥 |
| caseq | 2025-05-28 | [Remove redundant std::max(x, x)](./output/release/e85940b94442a391f6b528d9202e8c66eaca87be.log) | 🟥 |
| mpdenton | 2025-05-27 | [GWP-ASan: raise kMaxMetadata and kMaxRequestedSlots](./output/release/f44457d2f971ec0a45c271e093b6aa56044d0ec1.log) | 🟥 |
| jonross | 2025-05-21 | [Revert "[PA] Cache ReservationOffsetTable instead o...](./output/release/c858ce950cf900f168772e5e7c8f7cfa3e66ce96.log) | 🟥 |
| mikt | 2025-05-20 | [[PA] Cache ReservationOffsetTable instead of lookup...](./output/release/29111157f1454c5a52fe83c7da9f57cb07a35b82.log) | 🟥 |
| mikt | 2025-05-18 | [[PA/shim] Fix shim test failure on mac component build](./output/release/57f3d1311ce54e7c528608f2df77951920903451.log) | 🟥 |
| tikuta | 2025-05-15 | [base: Disable libc++ modules build in partition all...](./output/release/1d9d02e434059dbdb74e10e28ad42fd97c25a85c.log) | 🟥 |
| tasak | 2025-05-14 | [[PA] Remove libc++ string object dependency from al...](./output/release/269b4081447bcef3f64ad87116d9c6d8cfcf4645.log) | 🟥 |
| thestig | 2025-05-14 | [Clean up PA's instance_tracer.h](./output/release/299f793686af3b7ea3facf647464a15622c27466.log) | 🟥 |
| mikt | 2025-05-14 | [[PA] Fix PoolOffsetLookup for Configurable Pool](./output/release/fc79edffac58c4d59925412bf378eaf0f454688e.log) | 🟥 |
| mikt | 2025-05-12 | [[PA] Cache PoolInfo instead of lookup by address](./output/release/f0e2e7a786cda3a52feaff9c7894ebcf68b13fb3.log) | 🟥 |
| thestig | 2025-05-07 | [Remove <ostream> from PA's safe_conversions.h](./output/release/2b1d9301c925673637b3ff6e6412686ecfe66d02.log) | 🟥 |
| antoniosartori | 2025-05-07 | [Revert "gardening: Disable PartitionAllocPageAlloca...](./output/release/60903e2555a42eeac93dc7c91eedbca746943842.log) | 🟥 |
| yukishiino | 2025-05-06 | [gardening: Disable PartitionAllocPageAllocatorTest....](./output/release/988f84a803953c0874cffadcb0ded36ba174582c.log) | 🟥 |
| mikt | 2025-05-06 | [[PA/docs] Update buckets.md](./output/release/5c18e6e9b5fc4cb6748df24c2f63003e8ad3b81e.log) | 🟥 |
| dloehr | 2025-05-06 | [Exported things should always be visible](./output/release/843601306bff485f15960ef0c7b23dd34e2d7ee5.log) | 🟥 |
| mikt | 2025-05-02 | [[PA] Remove Freelist Dispatcher](./output/release/196ca28d1e516424ab24d9a798e13473895f8b71.log) | 🟥 |
| mikt | 2025-05-02 | [[PA] Remove free slot bitmap](./output/release/93234db35d91c7af0ff75025fc4be90cc99dfcb9.log) | 🟥 |
| tasak | 2025-05-02 | [[PA] Replace std::unordered_map with base::flat_map](./output/release/3a86115ff7330669c596355e7d7786703d4f2082.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Remove unused free functions](./output/release/971c92b116187e9f5ebe2e3c84cf84b04161edbe.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Remove unchecked freelist iteration](./output/release/2686355087336647c1d9aa5579eed6836dd71617.log) | 🟥 |
| nuskos | 2025-05-01 | [Reland "spanification: remove `#pragma allow_unsafe...](./output/release/84e59bb4cda4ba071548ede290d44fcfa44f1a42.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Simplify bucket lookup](./output/release/1397a7c24bc0e506cb7bfa2b5eaac48c144f7540.log) | 🟥 |
| luci-bisection | 2025-05-01 | [Revert "spanification: remove `#pragma allow_unsafe...](./output/release/afa6432ee9ba7108018c52f8f8e68cc84d2f3370.log) | 🟥 |
| nuskos | 2025-05-01 | [spanification: remove `#pragma allow_unsafe_buffers...](./output/release/46f7b646565a2f60129a68806b8615347556a08b.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Remove ZERO_RANDOMLY_ON_FREE](./output/release/a0068b7420952f0093c6149796d81039284e888c.log) | 🟥 |
| wangqing-hf | 2025-04-29 | [[PA] Add stack scan supported for loongarch64.](./output/release/b6a1dfdeb69381c36187ce9e7a4e9f24ec1a9065.log) | 🟥 |
| mikt | 2025-04-29 | [[PA] Check ThreadCache validity in DoubleFreeOrCorr...](./output/release/5ce629459a2c3b6ef5f56490805cd26169ac6969.log) | 🟥 |
| tasak | 2025-04-29 | [[PA] Copy base/containers/flat_{map,tree}.h to part...](./output/release/4170769c13d02df7bcff9a90112f36ed552dcf3b.log) | 🟥 |
| mikt | 2025-04-28 | [[PA] Scoped Scheduler-Loop Quarantine opt-out](./output/release/2d19fedeb02734e543c21c46b966835ce217ceea.log) | 🟥 |
| abhijeet | 2025-04-24 | [[tvOS][base_unittests] Replace host_info with sysct...](./output/release/862506deb382f3f8a8fa9689c8d5136a48e9b778.log) | 🟥 |
| mikt | 2025-04-24 | [[PA] Remove ghost of alternate bucket distribution](./output/release/b6040b2b33d28d064c2167c878deed3b49e4aeb2.log) | 🟥 |
| smaier | 2025-04-23 | [Roll Android NDK to r28](./output/release/a9ae8c0fd665f61acca4633d828a1061fbd461cc.log) | 🟥 |
| mikt | 2025-04-23 | [[PA/shim] Support sized-delete](./output/release/d691f607f29e8ca39c37917be7a69629f80a0dbd.log) | 🟥 |
| tasak | 2025-04-22 | [[PA] Fix wrong includes.](./output/release/a5083e082d03f4f7d3b0ee35df7cfa3e2ccf8680.log) | 🟥 |
| tasak | 2025-04-20 | [[PA] Fix PartitionAlloc windows component build](./output/release/471d99073bd4a042dd17aed9fb7604a6c3277ad9.log) | 🟥 |
| anandrv | 2025-04-17 | [[PartitionAlloc] Enable priority inheritance in Spi...](./output/release/21fe3be95a6c4372f6b3e467c05be49f8cd5279f.log) | 🟥 |
| mikt | 2025-04-16 | [[PA] Refactor: move Scheduler-Loop Quarantine relat...](./output/release/94efd06f8629f3ee91888150d16d2c2fafd898a5.log) | 🟥 |
| thestig | 2025-04-14 | [Forward declare base::NoDestructor in headers when ...](./output/release/4b0f19307639826f8fca1a41882781540ff2fb50.log) | 🟥 |
| lizeb | 2025-04-09 | [[base/allocator] Add aligned_alloc to shims on Android](./output/release/932177a9b8f06e7f478fcb22ac7b7184908738a8.log) | 🟥 |
| lizeb | 2025-04-09 | [[PartitionAlloc] Make ENOMEM issues have a separate...](./output/release/5144c01d94d24360ec0cecb91319bde84e9acec7.log) | 🟥 |
| dloehr | 2025-04-08 | [Change expected message in nocompile test](./output/release/2041003ba674f918c33b1afaaad74e652f34bcea.log) | 🟥 |
| lizeb | 2025-04-08 | [[PartitionAlloc] Crash in AddressPoolManager when d...](./output/release/836a8ac2ba51ad26527eee243edda043586f7390.log) | 🟥 |
| mikt | 2025-04-07 | [Reland "[PA] Disable BRP zapping on iOS"](./output/release/799310f3bf7d3cdbee28a086035eefc38732b548.log) | 🟥 |
| dtapuska | 2025-04-04 | [[ios blink] Add support for arm64e target](./output/release/4cc11b45843b513ee6cd469c21dde9c607624865.log) | 🟥 |
| ginnyhuang | 2025-04-04 | [Revert "[PA] Disable BRP zapping on iOS"](./output/release/20e84b3ed75698f1fb19149a640573f2bd420195.log) | 🟥 |
| mikt | 2025-04-04 | [[PA] Disable BRP zapping on iOS](./output/release/5a43d8f11eeef195a27b6f0d4373e1a4f1a53581.log) | 🟥 |
| ritownsend | 2025-04-03 | [chore: migrate ritownsend OWNERS/TODOs](./output/release/3ef26d8c8a8886277a41d4ae1e9d1801320eb274.log) | 🟥 |
| mikt | 2025-04-02 | [Reland "[PA] Add base::CheckHeapIntegrity to invest...](./output/release/53e916ce2c2835fbe66f639a1c4a8a010efa0514.log) | 🟥 |
| tasak | 2025-03-31 | [[PA] Split DoubleFreeOrCorruptionDetected into Doub...](./output/release/a9e3cecf8ea5c8da254d98bab323142e17229b0c.log) | 🟥 |
| dloehr | 2025-03-28 | [Export things to prevent accidental duplication](./output/release/ab56923a27b2793f21994589b0c39bc3324ff49f.log) | 🟥 |
| wcwang | 2025-03-25 | [Revert "[PA] Add base::CheckHeapIntegrity to invest...](./output/release/01d2444accdc1f985d3cfd0c512222de507eb3a4.log) | 🟥 |
| wcwang | 2025-03-25 | [Revert "[PA] Fix compile failure in PartitionRoot::...](./output/release/771d9b82c8daa8f1ae68cb33c5a1c3c8cfaf1267.log) | 🟥 |
| mikt | 2025-03-24 | [[PA] Fix compile failure in PartitionRoot::CheckMet...](./output/release/13a351f4d27353ed972aa4fc37104d872ed576dd.log) | 🟥 |
| mikt | 2025-03-24 | [[PA] Add base::CheckHeapIntegrity to investigate co...](./output/release/c381bec7b1db2e8aec822a8a6217736f4d70cc9c.log) | 🟥 |
| justincohen | 2025-03-21 | [ios: Correct gwp_asan_unittests out of memory](./output/release/0abfd4c40e8124de0d14f0d95f5bfe9a4ddd8a8b.log) | 🟥 |
| pmeuleman | 2025-03-20 | [Deactivate MTE in HWASan builds](./output/release/df5d4c1b2bdc8d18253cec8a3be4e0fa9194a2bb.log) | 🟥 |
| lokokung | 2025-03-18 | [[wasm] Adds rudimentary support for WASM/Emscripten...](./output/release/fb60666cb1896901bb14a5feb10001d20c8833c3.log) | 🟩 |
| mikt | 2025-03-07 | [[PA] Add EnsureThreadCache() for blocking thread ca...](./output/release/d3191727ef81ba9daefb0bd3b90d9e4043a4bfa1.log) | 🟩 |
| mikt | 2025-02-27 | [[PA] Add unittest to verify extra extras protecting...](./output/release/46d880ff62f340854a5a70142b0abf604c7af221.log) | 🟩 |
| jbroman | 2025-02-24 | [Remove an unused include of <unistd.h>](./output/release/bd46928f4b41532c457fa8834ab56d729f4c6c67.log) | 🟩 |
| arthursonzogni | 2025-02-20 | [PA: Fix compilation error about `LiftThreadIsolatio...](./output/release/f32541744d6a7305af151078470f0cb07bc3ea4f.log) | 🟩 |
| kdlee | 2025-02-20 | [PA: Remove pool offset freelists feature](./output/release/98d198364f616abebfbcec16edf45e640fe00ca4.log) | 🟩 |
| arthursonzogni | 2025-02-17 | [partition_alloc: fix missing `basic_common_referenc...](./output/release/879c3028e66ee96ba147c583315b2fd58c99b43d.log) | 🟩 |
| arthursonzogni | 2025-02-17 | [PartitionAlloc: realloc growth factor mitigation fo...](./output/release/09ea5ed6c63f10582a6e67cd0db5549597bf25d5.log) | 🟩 |
| marshall | 2025-02-13 | [Fix extra qualification on member 'basic_common_ref...](./output/release/2e370e26c52803f2524c51c3c7a3d2c21ebabcd8.log) | 🟩 |
| dtapuska | 2025-02-13 | [[ios blink] Set MAP_JIT pages to RWX by default](./output/release/5ce79ef9d981e6e60ee9a1f5bd905b1ee076965c.log) | 🟩 |
| mikt | 2025-02-13 | [[PA] Add a test for backup_ref_ptr_extra_extras_size](./output/release/0ebfead86460d7744f604f31717fbcf9ea348def.log) | 🟩 |
| mikt | 2025-02-12 | [[PA] Fix backup_ref_ptr_extra_extras_size not being...](./output/release/3005f069de69d77fcb06b9184d25c1f54ed8717c.log) | 🟩 |
| hans | 2025-02-11 | [Roll libc++ from 12150825ca73 to 492ff432ef34 (56 r...](./output/release/f3153d2c69cfaae76414e3e3a7fa15408ffba479.log) | 🟩 |
| dtapuska | 2025-02-07 | [Reland "[ios blink] Enable MAP_JIT unconditionally"](./output/release/4b9edec2ee9cfdcf63edc195622fd66a8506d65f.log) | 🟩 |
| asamidoi | 2025-02-07 | [Revert "[ios blink] Enable MAP_JIT unconditionally"](./output/release/21e5eb503a278ed29bf9b88fd383f2c94d8da612.log) | 🟩 |
| dtapuska | 2025-02-05 | [[ios blink] Enable MAP_JIT unconditionally](./output/release/2c0dac296b692fee8a92f47a7237823d6cbde44f.log) | 🟩 |
| neis | 2025-02-05 | [Remove Lacros leftovers from base/](./output/release/66a65af8596ab076424176fbbad0f02ac4fcae0f.log) | 🟩 |
| dsanders11 | 2025-02-03 | [Remove some unused includes of <tuple>](./output/release/185644689122812d475d0507e3bc1aa0c0156782.log) | 🟩 |
| arthursonzogni | 2025-02-03 | [PA: Remove 'NDEBUG' and make is_debug configurable.](./output/release/85d14cbcf203ad6b4059683b1700f00cc677b29c.log) | 🟩 |
| mikt | 2025-01-28 | [[PA] Unify FreeFlags::kZap with kSchedulerLoopQuara...](./output/release/6944ecdfe98cc0f76f02d0ec6643ff78c8d5c191.log) | 🟩 |
| tasak | 2025-01-21 | [[PA, MTE] Fix PartitionAllocTest.FewerMemoryRegions...](./output/release/a004bba90aa8ac07a7071dbf1a09d0e4e99513bc.log) | 🟩 |
| yukishiino | 2025-01-16 | [ELUD: Reduce the usage of machine stack](./output/release/088f9a5921a6fc929fdffb27577dddc5a01f4a71.log) | 🟩 |
| pkasting | 2025-01-10 | [Manually fix remaining clang-tidy errors in base/.](./output/release/bad4d8a87337475db378ebb64706a4fdebb641a2.log) | 🟩 |
| lizeb | 2025-01-09 | [[PartitionAlloc] Add feature to use fewer memory re...](./output/release/ba505b4478daf573942664233c75a23d706607dd.log) | 🟩 |
| lizeb | 2025-01-09 | [[PartitionAlloc] Document apple lock options](./output/release/a77103c1816d48a72e528c58d78993d45a9c0343.log) | 🟩 |
| pkasting | 2025-01-08 | [Apply clang-tidy autofixes to base/.](./output/release/5430b75fd1cc5429fc41b18561c0439b2ae16670.log) | 🟩 |
| mikt | 2025-01-08 | [Reland "[PA/AC] UI thread specific capacity configu...](./output/release/51b0fb5b1c36366f7e174b2637407ad964a9bcf7.log) | 🟩 |
| pkasting | 2025-01-08 | [Mark raw_ptr<T> and T* as having a common reference...](./output/release/33fbaf834c7673bd75b829b775775ac42e418c09.log) | 🟩 |
| yyanagisawa | 2025-01-07 | [Revert "[PA/AC] UI thread specific capacity configu...](./output/release/dc027d58406d26da0786910c51720935ebd3b3fc.log) | 🟩 |
| mikt | 2025-01-07 | [[PA/AC] UI thread specific capacity configuration f...](./output/release/6cdc138f18001b0ba6dbe12a7c95530052b6ac32.log) | 🟩 |
| lizeb | 2025-01-07 | [[PartitionAlloc] Name anonymous VMAs on Linux and C...](./output/release/6548aa3fdc79179a5b558892afad7e71fa473757.log) | 🟩 |
| verwaest | 2025-01-06 | [[pa] Use adaptive-spin and data-sync on macos](./output/release/934bddc37b89df34cf8adeb6dd3d12246143df89.log) | 🟩 |
| pkasting | 2024-12-27 | [[cleanup] clang-format base.](./output/release/9cab8b0d103998c4552b3ac14ef8429b7fe652c4.log) | 🟩 |
| tasak | 2024-12-20 | [[PA] Copy //base/files/platform_file.h to Partition...](./output/release/165d75a6241b0c43e2c3e1404b22500bada3b5cc.log) | 🟩 |
| edechamps | 2024-12-19 | [Don't build partition_alloc if it is not needed](./output/release/616b272794c79c5c19f87508ce86448e18afde6c.log) | 🟩 |
| mikt | 2024-12-17 | [[BRP] Allow extras size to be controlled via Finch](./output/release/847c1e77f386c103aeef42ecee6529d625d045ec.log) | 🟩 |
| pkasting | 2024-12-17 | [Don't use base::internal:: APIs outside base/.](./output/release/f240d41100751bac9a2528caea233da8d7d3750b.log) | 🟩 |
| fdoray | 2024-12-13 | [[perfcombined2024] Enable PartitionAlloc parameter ...](./output/release/b15cea87c55341ede2956f7e2bf09eb0332b33d1.log) | 🟩 |
| tikuta | 2024-12-09 | [base: add missing includes for the build with use_l...](./output/release/e8eba702d878a8cad8d97963f838f2ccee0e7f8a.log) | 🟩 |
| ivan.murashov | 2024-12-09 | [partition_alloc: Remove duplicated includes of buil...](./output/release/89c828e21c494b6220723c04997a8639633cc7f9.log) | 🟩 |
| tasak | 2024-12-09 | [[PA] Fix flaky test failure of memory reclaimer uni...](./output/release/3faa9b05d6777335f964cbf901c8ea1b23de07ea.log) | 🟩 |
| kdlee | 2024-12-06 | [PA: Remove *Scan config from `PartitionOptions`](./output/release/155df0f49332dbf69aec0614d7a89c6a09c0bc3e.log) | 🟩 |
| kdlee | 2024-12-06 | [PA: Remove *Scan references in unit tests](./output/release/394945644da7df29c4262a0b69c79e0b0c91944c.log) | 🟩 |
| arthursonzogni | 2024-12-04 | [Style: Fix array initializations with size mismatch...](./output/release/f96b908c9a5edb49a61287aa7fe4e9a311f44766.log) | 🟩 |
| pkasting | 2024-12-03 | [Introduce a "same as any" template and use it to si...](./output/release/b7a17328404dac7bfc9be2a07190aaf6bbd2c36a.log) | 🟩 |
| tasak | 2024-11-20 | [[PA] Make EnableShadowMetadata() and PartitionDirec...](./output/release/c551156ef8ccc090e52941d58c22647326066ff3.log) | 🟩 |
| rop | 2024-11-18 | [LSC Updating README.chromium license names to use s...](./output/release/7b91772e38c3d928d2170cd5cbcef81b8b2dbf5d.log) | 🟩 |
| arthursonzogni | 2024-11-14 | [DanglingPtr: Improve error message.](./output/release/6a3eb3e3cff5b3f6a0938992c921fd534520af9f.log) | 🟩 |
| pbos | 2024-11-14 | [Replace CHECK(false) in base/](./output/release/fff6771d53cfd6b9bb8d53180090b2679670c2fc.log) | 🟩 |
| glazunov | 2024-11-08 | [[BRP] Make sure all quarantined allocations are zapped](./output/release/bd0c0ab0f94f8b9c21e4e9207f66a4832477e96e.log) | 🟩 |
| tikuta | 2024-11-08 | [base: include stdlib.h for malloc/realloc](./output/release/972d0c921eeba6ee2ecc49762eb6e0676e8ea84f.log) | 🟩 |
| yukishiino | 2024-11-07 | [PA: Narrow the critical section of LightweightQuara...](./output/release/5720e2701e416a4e8e9b423413659e925ab4dbbb.log) | 🟩 |
| lizeb | 2024-10-30 | [[PartitionAlloc] Add option to eventually memset() ...](./output/release/72ae2afeb4d373b900683a82919e8d4a0d139f82.log) | 🟩 |
| yukishiino | 2024-10-28 | [ELUD: Do not quarantine direct-mapped allocations](./output/release/2bc4745c33b44da415fad88ccfdf2900ed835dce.log) | 🟩 |
| lauren | 2024-10-24 | [PA: check for <sys/ifunc.h> to enable MTE/BTI](./output/release/e11fdbafa549101c04b028e940bf59963229569f.log) | 🟩 |
| lizeb | 2024-10-23 | [[PartitionAlloc] Don't memset() direct-mapped alloo...](./output/release/914c30a91ad47f1f60de28bc10cfeef910dec161.log) | 🟩 |
| arthursonzogni | 2024-10-22 | [PA: check readability-static-accessed-through-instance](./output/release/dbaab7e744c75e9c5411397d6a61e8217053ce22.log) | 🟩 |
| yukishiino | 2024-10-21 | [PA: Remove runtime conditional branches from Lightw...](./output/release/ce13777cb731e0a60c606d1741091fd11a0574d7.log) | 🟩 |
| arthursonzogni | 2024-10-14 | [PA: link against winmm.lib.](./output/release/49e7d5b5b0bd7342e469b6ff8a6266a2cfe3c489.log) | 🟩 |
| mikt | 2024-10-11 | [[PA] Add configuration for iOS binary experiment](./output/release/1d1d7753cd2489252833ab2398ff7b94230aa9ca.log) | 🟩 |
| mikt | 2024-10-11 | [[PA] Put some debug data on stack on cookie corruption](./output/release/67d020b3b9c6e0674b863786ccbdcb2dde2fea4a.log) | 🟩 |
| mikt | 2024-10-10 | [[PA] Clean-up assuming core pools are glued everywhere](./output/release/325b94b1de054e716ebe86f796acb8e90fc84b29.log) | 🟩 |
| tasak | 2024-10-10 | [[PA] UnmapShadowMetadata() must be invoked before U...](./output/release/ece815bd85c86702e994cde9ccd79c02335aa4d5.log) | 🟩 |
| pkasting | 2024-10-10 | [Use three-way comparison when available in Partitio...](./output/release/4f1c8275f78acb2eabcb441f9f09d17e4c129448.log) | 🟩 |
| mikt | 2024-10-10 | [[PA] Glue core pools on iOS](./output/release/ce32b10a09cfe6be075b586e2a25959d76a6b647.log) | 🟩 |
| mikt | 2024-10-10 | [[PA] Fix PartitionAddressSpace::RegularPoolSize() i...](./output/release/6034b95817c2a5d4df72f5772c23fcd59bdb8261.log) | 🟩 |
| pkasting | 2024-10-09 | [Remove bartekn@ as OWNER.](./output/release/4ac2023e4f7fca06b496a85447a12d53ef5ffaf8.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Add FORCE_DISABLE_BACKUP_REF_PTR_FEATURE build...](./output/release/5eb3834d17db690156ea257d6cad9452b3dd4b92.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Fix enable_partition_lock_reentrancy_check wit...](./output/release/cfded4a9ba2fd07e08ed66a8b4a1e3d01db52384.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Add "smaller" partition cookie build option](./output/release/f4b2dd0e30f90470d5400606d72581d9d910937b.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Add partition cookie check build option](./output/release/242f8277ece89fecca2c9561c0d6c7d681fc9a99.log) | 🟩 |
| sorin | 2024-10-09 | [base: eliminate empty parameter list in lambdas whe...](./output/release/524cf957f0260f857928401ec3502c9ec663c6fa.log) | 🟩 |
| sorin | 2024-10-08 | [base: eliminate empty parameter list in lambdas whe...](./output/release/1ced11f214ead902b40019f031852137f84827c2.log) | 🟩 |
| mikt | 2024-10-04 | [[PA] Add lock reentrancy check build option](./output/release/7939e34ad2e5c769f8856957cc7f8166c20bd954.log) | 🟩 |
| mikt | 2024-10-03 | [[MO] Enable Partition Alloc with Advanced Checks su...](./output/release/b986110c534670f28e49969325ee2ab7eca8b114.log) | 🟩 |
| mikt | 2024-10-02 | [[PA-E] Use FreeFlags::kNoHooks consistently](./output/release/3c7d09f6032e951cbf837608a3d18396c71dbee9.log) | 🟩 |
| mikt | 2024-10-02 | [[MO] Support more functions in PA with Advanced Checks](./output/release/9011cae703eb8ee0a1ac431a4ffb10f945458e81.log) | 🟩 |
| danakj | 2024-10-01 | [Disable PA-based features in the Rust host tools to...](./output/release/2850bbe7e393f36419d1df3c0dbbfcda4403092d.log) | 🟩 |
| jdapena | 2024-10-01 | [GCC: do not add redundant template spec in constructor](./output/release/ccc8b69a92a8f5472b6359190c17e86c91ce0775.log) | 🟩 |
| arthursonzogni | 2024-09-30 | [PA: check readability-redundant-smartptr-get](./output/release/d3a666931363ad6ea6ff9e633948a26fe4639530.log) | 🟩 |
| pbos | 2024-09-27 | [Mark TerminateBecauseOutOfMemory [[noreturn]]](./output/release/eb4c8ad8053e37bc0ca11f19cad1405bc0912676.log) | 🟩 |
| arthursonzogni | 2024-09-27 | [PA: Fix #include for memcpy/memset.](./output/release/2409a3774b4f25a09c3232af60aa717b2d67aee4.log) | 🟩 |
| marshall | 2024-09-26 | [win: Add missing <limits> include](./output/release/672834421883ed82745701ef948e27175b0a21cf.log) | 🟥 |
| fdoray | 2024-09-25 | [[partition alloc] Add PA_NOT_TAIL_CALLED to out of ...](./output/release/6d508e4ef47ae3b932648cef6ccb65f1ce931341.log) | 🟥 |
| fdoray | 2024-09-25 | [[partition alloc] Allow foreground/background empty...](./output/release/85b0685f68760491b20e634f8370be55bba04795.log) | 🟥 |
| arthursonzogni | 2024-09-24 | [partition_alloc: Stop using anonymous namespace in ...](./output/release/c97fac45ba2b636db5a7505b656c324a48dd4578.log) | 🟥 |
| tasak | 2024-09-20 | [[PA] Add PartitionAllocShadowMetadata feature](./output/release/c0fe75b0b5e1bfb65aaf60a5abb8a568da3a5590.log) | 🟥 |
| sergionso | 2024-09-19 | [base: Improve CurrentWallclockMicroseconds() on Win...](./output/release/7605153ca556d38d81429fcebf53b85fb9fe044e.log) | 🟩 |
| pkasting | 2024-09-18 | [Attempt to improve comments in compiler_specific.h.](./output/release/fb47d3dad7415dfb71a50c76d38a65085c7105c2.log) | 🟩 |
| pkasting | 2024-09-17 | [More consistent macro definitions in base/compiler_...](./output/release/ee6bf744537f90293b9e21c9be52b5aa32d2b50e.log) | 🟩 |
| rsworktech | 2024-09-17 | [[PA] Use kPartitionCachelineSize instead of hardcod...](./output/release/c146ea4f65525c50a0a26eeac8a773e886dbe38c.log) | 🟩 |
| fdoray | 2024-09-16 | [[oom] Add commit limit/available to OOM exception a...](./output/release/ea476c2c12d824c1c89c36b78903276c5c645bf5.log) | 🟩 |
| pkasting | 2024-09-13 | [Prerequisites for changing macro definitions in com...](./output/release/ca4487e127c2e071da5d4a36a9f71fd7b65b1434.log) | 🟩 |
| kdlee | 2024-09-13 | [PA: Make `SlotStart` methods const](./output/release/719c912ed6faac0547b91bd5485ba37e516eb978.log) | 🟩 |
| arthursonzogni | 2024-09-12 | [Reland "PA: Invert MiraclePtr Platform Enablement L...](./output/release/5576de467696ec80ac16be5daaa9e0ec86eb7564.log) | 🟩 |
| sroettger | 2024-09-10 | [[cfi] Implement PageAllocator::SealPages on Linux](./output/release/1ae169f5bd37d782c885821ed4e60fe39e711cc8.log) | 🟩 |
| mikt | 2024-09-10 | [[PA] Use dispatch with advanced checks when feature...](./output/release/9b58a78cc026d3088bf954daadfeec7b294b11d4.log) | 🟩 |
| keishi | 2024-09-10 | [Update apple_apsl/README.chromium](./output/release/65d4191fc0703d5c3b98d002091c93746be24e9a.log) | 🟩 |
| arthursonzogni | 2024-09-09 | [PA: Stop using `constinit`.](./output/release/69b922bdaae80e2dfe65b1ca5c5583446e3a582c.log) | 🟩 |
| arthursonzogni | 2024-09-09 | [Revert "PA: Invert MiraclePtr Platform Enablement L...](./output/release/81ff602c377ade97134a29b681068ee4a2f132f2.log) | 🟩 |
| arthursonzogni | 2024-09-09 | [PA: Invert MiraclePtr Platform Enablement Logic](./output/release/d81b3b062e4b40432a65225a16a5bb2d1590a8ef.log) | 🟩 |
| arthursonzogni | 2024-09-08 | [PA: Revert "Allow std::hardware_destructive_interfe...](./output/release/b69741434d0a8a8c6a089255866d1cef7ed48778.log) | 🟩 |
| tasak | 2024-09-06 | [[PA] Fix ShadowMetadata issues](./output/release/51001c0d0378ce34b34d3d6ce0f9899b4d832bab.log) | 🟩 |
| yzshen | 2024-09-06 | [Remove the old gpu::Scheduler.](./output/release/cff0048aa56a0ac7bf4da8009679b877500af6fa.log) | 🟩 |
| pkasting | 2024-09-04 | [Allow (and use) std::hardware_destructive_interfere...](./output/release/dbd5fd7ca188b19955dd6fd221a44f79efc39998.log) | 🟩 |
| yukishiino | 2024-09-04 | [PA: Minor tweaks on LightweightQuarantine](./output/release/18e11e59adc3bf1407bc8433b7cf9cc8c3503867.log) | 🟩 |
| arthursonzogni | 2024-09-04 | [PartitionAlloc: stop depending on "defined(ANDROID)"](./output/release/21f94456b3ec9d432075dc1d0aeba26d955871a9.log) | 🟩 |
| tasak | 2024-09-02 | [[PA] Split SlotSpanMetadata into read-only one and ...](./output/release/d0b9630d2515effb20b939cb5e526f8e0b5fd5f1.log) | 🟩 |
| arthursonzogni | 2024-09-02 | [PA: Fix compile error encountered on Skia.](./output/release/a2ce75ec98d94852baada5d6d98e6b1050099e38.log) | 🟩 |
| kdlee | 2024-08-30 | [PA: Upgrade `DCheckIsValidSlotSpan()`](./output/release/774e27628835d8580f58b420a6b2b608f22db3c2.log) | 🟩 |
| pkasting | 2024-08-29 | [Switch from `ALIGNAS()` to `alignas()`.](./output/release/4419c7daa9cc1e08af8769d0bb2314f9c7dfca27.log) | 🟩 |
| tasak | 2024-08-27 | [[PA,shim] Fix compile error of allocator_shim_..._w...](./output/release/60162d5aab8ebd147e04889e2d56a2f33e0b0adb.log) | 🟩 |
| keishi | 2024-08-23 | [[MTE] Fix tagging after r1344621](./output/release/9513f560d7de3d8afb6c742e0641c32e56bd22cc.log) | 🟩 |
| pkasting | 2024-08-22 | [Move arch-specific feature macros to build_config.h.](./output/release/1ca611f5fd7838eae38927063b5e30f35e0b20f3.log) | 🟩 |
| bwwilliams | 2024-08-22 | [Strengthen Warning Enforcement for Assignments in C...](./output/release/995176567d7c95dfdfa5862cb743bb811d942b41.log) | 🟩 |
| tasak | 2024-08-22 | [[PA,shim] Support allocator_shim on Windows debug b...](./output/release/bcebe831fd166b7540502cbc3d4a2ba763047c78.log) | 🟩 |
| pkasting | 2024-08-22 | [Remove [UN]LIKELY().](./output/release/97be0f3c5b04f1d2fda3d4e3e3d585868eb77efd.log) | 🟩 |
| keishi | 2024-08-21 | [[MTE] Do retagging right before RawFreeWithThreadCa...](./output/release/81cccdaee388163b04970911891f5a6349e19bbc.log) | 🟩 |
| tasak | 2024-08-21 | [[PA] Split PartitionPageMetadata into read-only one...](./output/release/a07ce06347ac8ac1540b6d08e86194c3e8c37a6a.log) | 🟩 |
| keishi | 2024-08-15 | [Remove *Scan settings related code](./output/release/cf28c12c0a65f752691ba60583dcfeb84dc84518.log) | 🟩 |
| sky | 2024-08-15 | [pa: puts buildflags in public_deps](./output/release/8b28072c61a1152b0b7eb0c506d00b24535a47bb.log) | 🟩 |
| tasak | 2024-08-09 | [[shim] Move kPartitionAllocDispatch into another he...](./output/release/1515d142bda42bc4f6364e2fa11cb79f9014c3cd.log) | 🟩 |
| yukishiino | 2024-08-08 | [PA: Remove the self pointer from shim functions](./output/release/091b58c775288e29d03ba6776bfa0e444c0b27c7.log) | 🟩 |
| pkasting | 2024-08-07 | [Switch to [[(un)likely]]: .../partition_alloc/](./output/release/d374cbc2685c6354f1eda1bdd1be0c3ee45f009d.log) | 🟩 |
| tasak | 2024-08-07 | [[PA] Support PartitionAlloc-Everywhere on Windows c...](./output/release/c362d7a79a023b0693f872527b9d7c1077eb2fd4.log) | 🟩 |
| pkasting | 2024-08-06 | [Switch to [[(un)likely]]: .../partition_alloc_base/](./output/release/a5626351a84e33d5fee2a5906be9dc85a242aa8e.log) | 🟩 |
| tasak | 2024-08-06 | [[PA] Split PartitionSuperPageExtentEntry into read-...](./output/release/54cdf4e94899d81db9dd367228300754301f5fd0.log) | 🟩 |
| olivierrobin | 2024-08-02 | [Mark TimeTicks::UnixEpoch deprecated](./output/release/be025bf066fd720e53fed43ad7906e4b278e85ef.log) | 🟩 |
| derinel | 2024-08-02 | [Add IWYU statement for base::raw_ptr](./output/release/813f717135e29158905bff102e6261499bb93106.log) | 🟩 |
| mikt | 2024-08-01 | [[PA/shim] Add a new dispatch to switch malloc backe...](./output/release/be977e0d870ad3d6db2dd92d6076cfe4908db7eb.log) | 🟩 |
| yukishiino | 2024-08-01 | [PA: Fix ineffective PA_UNLIKELY applied to do ... w...](./output/release/e41031670a9c4a93549ba0f672d2ed3367d9fcac.log) | 🟩 |
| keishi | 2024-07-31 | [[MTE] Use a random value to update a tag](./output/release/581d48913faf389f935ecb0be5a75fa5f789a4b2.log) | 🟩 |
| dloehr | 2024-07-30 | [Remove uses of variable-length arrays](./output/release/9930a27ceca75a0d831b0bd1098add097d352aa1.log) | 🟩 |
| tasak | 2024-07-30 | [[PA] Remove unused kCookie from PartitionAllocDeath...](./output/release/6eb5e6cf980ae8ceee135e5ccd0638a01a9948e9.log) | 🟩 |
| tasak | 2024-07-30 | [[PA] Split DirectMapExtentMetadata into read-only o...](./output/release/0627742f7ee966d5ab4547963941a2224911083f.log) | 🟩 |
| tasak | 2024-07-26 | [[PA] Deflake PartitionAlloctest.CheckeReservationTy...](./output/release/540ef1d89bfb64f8078919854dfed17b0ca9deaa.log) | 🟩 |
| arthursonzogni | 2024-07-25 | [partition_alloc: Cleanup never called functions.](./output/release/6a94c13fbac1e24eaa64161f58e9f566cc965d54.log) | 🟩 |
| tasak | 2024-07-25 | [[MTE] Fix flaky BackupRefPtrTest.GetDeltaElems fail...](./output/release/bd54734c0467af9fb4ff3610578718d6869f5a38.log) | 🟩 |
| arthursonzogni | 2024-07-24 | [partition_alloc: Disable MTE for benchmark use to a...](./output/release/561c0d214fe68a31a0fed180ccc8e5bf090b6bbe.log) | 🟩 |
| mikt | 2024-07-24 | [[PA] Optimize IsManagedByPartitionAlloc()](./output/release/91610144c44e3e96f33b7acd72609d84744a4de1.log) | 🟩 |
| tasak | 2024-07-24 | [PA: Fix EncodedPoolOffset::Encode().](./output/release/877eaedbfd0c5e851d4f63ff2cbf659bdf036446.log) | 🟩 |
| keishi | 2024-07-23 | [[MTE] Disable MTE during StackCopier::CopyStackCont...](./output/release/0abdba1e1048de44c4d9d112d48afaf96a14f441.log) | 🟩 |
| mikt | 2024-07-12 | [[PA/*Scan] Remove StarScan](./output/release/b0cb752ab120cb7c5b46e6612eb7597f7b4153e8.log) | 🟩 |
| arthursonzogni | 2024-07-11 | [partition_alloc: remove cpu_features:ndk_compat dep...](./output/release/f085b61ade6a84bc24bedcc2d381a4a558431e9c.log) | 🟩 |
| yukishiino | 2024-07-11 | [PA: Add PA_UNLIKELY to allocation failure handlers](./output/release/29179883f32e3ea25f199238befdd1a09d488f37.log) | 🟩 |
| yukishiino | 2024-07-11 | [PA: Let LightweightQuarantineBranch.Quarantine() ta...](./output/release/0c714aaffcedd7a77562578e51ef3e2e427a1f4b.log) | 🟩 |
| kdlee | 2024-07-11 | [PA: Precalculate Mac alignment kludge](./output/release/4188dcd78c5267eacb3c0364f8e580898972c9cb.log) | 🟩 |
| arthursonzogni | 2024-07-10 | [partition_alloc: Use PA_CONSTEXPR_DTOR](./output/release/2e6b2efb6f435aa3dd400cb3bdcead2a601f8f9a.log) | 🟩 |
| mikt | 2024-07-09 | [[PA/shim] Guarantee tail call optimization](./output/release/575f1a0af46e358b4cdd6b3769caa754bf720bcb.log) | 🟩 |
| arthursonzogni | 2024-07-09 | [partition_alloc: Follow-up moving tests.](./output/release/f83b78cb7dc3363149149725b62876efcc995f89.log) | 🟩 |
| arthursonzogni | 2024-07-08 | [partition_alloc: Check support for C++17](./output/release/880ba2b2e2121f4c37c87b61cd7bd4659fa7690d.log) | 🟩 |
| jdapena | 2024-07-08 | [IWYU: add again required missing include for Histog...](./output/release/fd1ad7b90ad02af8d2993c2e757b7615dcc1cff7.log) | 🟩 |
| arthursonzogni | 2024-07-08 | [partition_alloc: support cpp17](./output/release/0ab14762072efc3c894aeebdd1b8578a74b99cda.log) | 🟩 |
| arthursonzogni | 2024-07-05 | [Reland #2 "partition_alloc: Move pa tests into pa.""](./output/release/36601cb520f4749418d0737cc65ecfda7ddb7500.log) | 🟩 |
| danakj | 2024-07-05 | [Make all allocation routines from Rust fallible whe...](./output/release/824fb852dc756ae4347d37779d0a7e8e67c04199.log) | 🟩 |
| arthursonzogni | 2024-07-05 | [partition_alloc Fix violations of the PRESUBMIT](./output/release/c0d55ba698b669900208466f858a9eee93d5ec0f.log) | 🟩 |
| arthursonzogni | 2024-07-05 | [Revert "Reland "partition_alloc: Move pa tests into...](./output/release/3508fb8a67265256667e6e0586f9b2dcce7ecda9.log) | 🟩 |
| arthursonzogni | 2024-07-04 | [Reland "partition_alloc: Move pa tests into pa."](./output/release/feb5861c7ee60df986d446ee84ff8b00c90924f3.log) | 🟩 |
| titouan | 2024-07-04 | [Revert "partition_alloc: Move pa tests into pa."](./output/release/f1888f8b851999367d99c83277527bddfbeef1d0.log) | 🟩 |
| arthursonzogni | 2024-07-04 | [partition_alloc: Move pa tests into pa.](./output/release/0abbaa1cc0759915e1234da4956ca8b4b231445c.log) | 🟩 |
| tpearson | 2024-07-03 | [partition_alloc: Use 64k pages for ppc64 partition ...](./output/release/22ca21545058c5fbef24f54c1b1c16ac7ed82590.log) | 🟩 |
| danakj | 2024-07-03 | [Reland "Reland "Reland "Reland "Add toolchains with...](./output/release/69258b7057b6cf183695ba8e2d6160edcd03d50e.log) | 🟩 |
| mjwilson | 2024-07-02 | [Revert "Reland "Reland "Reland "Add toolchains with...](./output/release/dc397419b98dc37a18c55a4bcefc43eb30189097.log) | 🟩 |
| danakj | 2024-07-02 | [Reland "Reland "Reland "Add toolchains without Part...](./output/release/37fa7c1ca9b94e63dc969a69668bcd53d89657e8.log) | 🟩 |
| tpearson | 2024-07-02 | [partition_alloc: Autodetect page size on ppc64 systems](./output/release/12d49fbf174022a0e5275d87ef9e3c71c3f05547.log) | 🟩 |
| tpearson | 2024-07-02 | [partition_alloc: Allow variable page sizes on ppc64...](./output/release/24f50b3bd0e30b804855b24c0125e93f7a197d20.log) | 🟩 |
| casey.smalley | 2024-07-01 | [Add support for 64K pages on Linux/AArch64](./output/release/43ae3905f7007916c04d92fb92fc8167dc2e469f.log) | 🟩 |
| bartekn | 2024-07-01 | [[PA] Enable glue_core_pools](./output/release/7ac10c8f375123fd71ace5038c27b8fa77b69ed8.log) | 🟩 |
| kdlee | 2024-07-01 | [PA: Untag pool offset freelist entries](./output/release/0eb0d6bfeba06d4adbae9d82512acc7b565454b2.log) | 🟩 |
| danakj | 2024-06-28 | [Test realloc in the realloc test](./output/release/89101f0456b29a762c3d4c4e2e85491dd989d225.log) | 🟩 |
| tpearson | 2024-06-28 | [partition_alloc: Prioritize non-constant POSIX page...](./output/release/773457d3f3772c646a07e59a23758039bcc50089.log) | 🟩 |
| tarcisio.fischer | 2024-06-26 | [Enable MTE by default on ConfigurePartitionsForTesting](./output/release/45a05505a83e303d704fe088dc01e568bf33e038.log) | 🟩 |
| lizeb | 2024-06-26 | [[PartitionAlloc] Purge more buckets from time to ti...](./output/release/be8e0bd57d74a7031a7b1e0decd782d3601dd623.log) | 🟩 |
| arthursonzogni | 2024-06-26 | [partition_alloc: merge buildflags.h #cleanup](./output/release/2d3ec4ceaf5fce669fde51e187f3559a30832f0a.log) | 🟩 |
| wyeager | 2024-06-26 | [Revert "Reland "Reland "Add toolchains without Part...](./output/release/c29d2bc0167380bd0b0cef6274cd3e7cd02dd9b9.log) | 🟩 |
| arthursonzogni | 2024-06-25 | [PA: Minimize DEPS for tests.](./output/release/c718a2c1cc43cf34ea6422d64ad14d3d24595635.log) | 🟩 |
| arthursonzogni | 2024-06-25 | [partition_alloc: Fix and simplify SpinningMutex.](./output/release/c1d59d0456ffb430742563e18f461e8065e40cad.log) | 🟩 |
| danakj | 2024-06-24 | [Reland "Reland "Add toolchains without PartitionAll...](./output/release/8cdb01ad13cef64377e510814dafa2ca32eea2f7.log) | 🟩 |
| lukasza | 2024-06-24 | [s/ `std::unique_ptr<char[]>` / std::vector<char> / ...](./output/release/770d1a5a8a4a16f24a002cc51a4f2af4f68152c5.log) | 🟩 |
| bartekn | 2024-06-21 | [[BRP] Test raw_ptr::operator=(T* ptr) when assigned...](./output/release/efb545e8823213f553fdcb3b0c6af5b8ca5aefa2.log) | 🟩 |
| arthursonzogni | 2024-06-19 | [partition_alloc: #cleanup unnecessary PA_ prefix](./output/release/26b47cb849db9fbb0a89f1691efd0659f2d832ba.log) | 🟩 |
| bartekn | 2024-06-18 | [[BRP] Handle case where raw_ptr::operator=(T* p) ge...](./output/release/3c8b6517c927396a3c9767d488aa8af73d4467e9.log) | 🟩 |
| lizeb | 2024-06-18 | [[base/allocator] Add documentation about discard vs...](./output/release/f7d9f07348e454ed3e7ec3d6e8acf24388750e18.log) | 🟩 |
| kdlee | 2024-06-17 | [PA: Add `SlotStart` death test](./output/release/16c47e1a56f460b190083a114d39871e917c8492.log) | 🟩 |
| bartekn | 2024-06-17 | [[PA] Fix BUILDFLAG->PA_BUILDFLAG under #if](./output/release/b7d5ab0f5fa14c0981c6ffe5afbcfb5adc728d6b.log) | 🟩 |
| kdlee | 2024-06-13 | [PA: Enable freelist dispatcher](./output/release/7864cdced1d6ee0aae78768a808dd798480d76f0.log) | 🟩 |
| bartekn | 2024-06-13 | [Remove USE_ASAN_UNOWNED_PTR](./output/release/35643f54fd6309713d96266a17543e1e04dcc846.log) | 🟩 |
| kdlee | 2024-06-13 | [PA: Adjust corruption test](./output/release/2d4fa48c99b41f38c6df296b87954be94c8ee2f6.log) | 🟩 |
| kdlee | 2024-06-13 | [PA: Hide GN arg](./output/release/db10b18b633a65ea10d649b533d6848dbe7e4224.log) | 🟩 |
| bartekn | 2024-06-12 | [[PA] Work around Adreno-GSL mmap address conflict](./output/release/4b46ebdc43523f7f6ec2e8e6dbc151293ad115c5.log) | 🟩 |
| kdlee | 2024-06-12 | [PA: Remove `TaggedSlotStart`](./output/release/a1a8f60c590447fd1f9a93235c6e3552c462c549.log) | 🟩 |
| kdlee | 2024-06-12 | [PA: Add `SlotStart::{From,To}Object()`](./output/release/d5c2aacddbf420bc6385d4b3bc2b2afdcdbda1bd.log) | 🟩 |
| kdlee | 2024-06-10 | [PA: Adjust bucketing comment](./output/release/402d95788326f22ba4d06846d983bcb44da0fa07.log) | 🟩 |
| kdlee | 2024-06-07 | [PA: Return slot size from `MaybePutInCache()`](./output/release/ebfce4880cbffeea184c5b8e1ab0c7227878b7f3.log) | 🟩 |
| kdlee | 2024-06-04 | [PA: Introduce `SlotStart` type](./output/release/596919c38e416762842d3dabfeca9795de390f43.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [partition_alloc: Remove unused files.](./output/release/4bc9d0c84a830f8883ad6558e54b2b3c3072583b.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [partition_alloc: Remove temporary exception for bui...](./output/release/7013d1fbc8ae4a63addb2d8b3809290649469f20.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [Partition Alloc: Cutting the Cord!](./output/release/ae870b571ec44a11de1bb2eba3376ad41779b5d1.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [partition_alloc: Check no external dependencies in GN.](./output/release/195dd3d1a28e04dfe8a50d9911414a7f75fa0038.log) | 🟥 |
| kdlee | 2024-06-04 | [PA: Introduce `ObjectToSlotStartUnchecked()`](./output/release/b06c973eedc38f49bdfc18c3f594dd4f0e9cea77.log) | 🟥 |
| arthursonzogni | 2024-06-03 | [partition_alloc: Stop using chromium's build_config...](./output/release/8d08a407ab68da324863ebc274f20fefc4713e78.log) | 🟥 |
| arthursonzogni | 2024-06-03 | [PA: Stop depending on `IS_CHROMEOS`.](./output/release/77aad2ab99d3b15766dac04552911da4d892a08a.log) | 🟥 |
| arthursonzogni | 2024-06-03 | [partition_alloc: provide build_config.h](./output/release/b99a401f457eb03adae9c873c835a5ab736d126a.log) | 🟥 |
| kdlee | 2024-06-03 | [PA: Adjust `PA_USE_DEATH_TESTS()`](./output/release/89029ef39983240e0d9834340c5bf56c3f219868.log) | 🟥 |
| lizeb | 2024-05-31 | [[PartitionAlloc] Do less work in fast MemoryReclaim...](./output/release/4e54cefb1472e8fa0e4e120266c57b716c7f4cbc.log) | 🟥 |
| arthursonzogni | 2024-05-30 | [partition_alloc: remove -Wl,--start-group, --end-group](./output/release/f941becc7efa75971aa4e83d0cd3217f4f1ef57f.log) | 🟥 |
| lizeb | 2024-05-30 | [[PartitionAlloc] Add a feature capping memory recla...](./output/release/e9b1e467c32d80a904df8efddb8ed542aaf8171d.log) | 🟥 |
| arthursonzogni | 2024-05-30 | [Define partition_alloc standalone GN config.](./output/release/087911ce77bce70f277fda09e10db56fe577ed53.log) | 🟥 |

</details>

<details>
<summary>🟩 Configuration: `debug`</summary>

| Email | Date | Title | ? |
|---|---|---|---|
| nuskos | 2026-02-05 | [Add nuskos@ to PartitionAlloc OWNERS.](./output/debug/7289d97695f40ba6a8ae56618d45786eadffdc7b.log) | 🟩 |
| hellofroser | 2026-02-05 | [Fix some PA_UNSAFE_TODOs in //base/allocator/partit...](./output/debug/bb5a3e33f5ea17a2e27059d99b12273b1b1c3604.log) | 🟩 |
| tasak | 2026-02-03 | [[3/4] Implement AsanRawPtrService V2](./output/debug/24e411a428ae1128d44850dc0b98376da84bddd5.log) | 🟩 |
| mikt | 2026-02-02 | [[PA] Refactor and merge PA/AC shim logic](./output/debug/f9fe9152fca91e24bfc495f91b42a36800b952a0.log) | 🟩 |
| awillia | 2026-01-30 | [Fix comment references to "_unittests.cc" files (ba...](./output/debug/baaa6670c23c19485d0a5a538bc43d3332def328.log) | 🟩 |
| arthursonzogni | 2026-01-29 | [PartitionAlloc: Do not assert C++20.](./output/debug/4344806135c21081ac9c2551b9d8e26fd1894280.log) | 🟩 |
| ayumiohno | 2026-01-27 | [PA: Implement AllocToken support in PartitionAlloc](./output/debug/936619c71ecb17c0e2482cf86be3f3f417b2f683.log) | 🟩 |
| mcnee | 2026-01-27 | [Prepare for making BindOnce and BindRepeating nodis...](./output/debug/492f8c119a98911c17bdfc1559b10b6431ea419d.log) | 🟩 |
| sdefresne | 2026-01-27 | [Add transparent version of std::equal_to<> and std:...](./output/debug/e1b3bee8ba37d08bb642265ccb78e54cedd00a77.log) | 🟩 |
| mikt | 2026-01-27 | [Reland "[PA] Make PartitionRoot a class"](./output/debug/f7b856afab03e211acdfef1467992e98c274d13b.log) | 🟩 |
| ayumiohno | 2026-01-26 | [PA: Remove __throw_out_of_range in address_pool_man...](./output/debug/1e050ef1abfc2d85451625b1f257eba703670a65.log) | 🟩 |
| ayumiohno | 2026-01-20 | [PA: Remove thread_local in parition_alloc_base Plat...](./output/debug/6ad9a9a880baebe89850beec18ebd506419b18af.log) | 🟩 |
| tsepez | 2026-01-20 | [Remove base::MakeClampedNum()](./output/debug/329ff99d5d81aca88c066dce706136846abd5553.log) | 🟩 |
| ayumiohno | 2026-01-19 | [PA: Use system allocator in ASan even when kNoHooks.](./output/debug/cb11b9bc34c2183fa5049a69cd1ea09511289235.log) | 🟩 |
| arthursonzogni | 2026-01-19 | [PartitionAlloc: Additional C++23 presubmit.](./output/debug/a663ade348e34ae02e7db69a51e0a5ab92770372.log) | 🟩 |
| victorvianna | 2026-01-15 | [Improve PRESUBMIT against C++23 features in partiti...](./output/debug/5b70baa1fd02c684fb68f7dc6fad54decabbcaee.log) | 🟩 |
| tsepez | 2026-01-15 | [Remove base::MakeCheckedNum<>().](./output/debug/24446349a7656b671465493504dfdcf3f638419a.log) | 🟩 |
| mliedtke | 2026-01-15 | [[base] Undo consteval usages in base/allocator/part...](./output/debug/b6c5ed1c618f27a1a3402b126cb1e9ab9aff4785.log) | 🟩 |
| victorvianna | 2026-01-14 | [[styleguide] Allow if consteval](./output/debug/e2ebbb786efdde6cb5440c4d2386f5acc2fba85f.log) | 🟩 |
| ayumiohno | 2026-01-14 | [Reland "PA: Support multiple ThreadCache instances ...](./output/debug/46fd97ba8656535accce5e53ab59c23a6f12f9f0.log) | 🟩 |
| koerber | 2026-01-14 | [Revert "[PA] Make PartitionRoot a class"](./output/debug/9f81c694ae53d37f01e11bd015dcb9dfebba55ea.log) | 🟩 |
| mikt | 2026-01-14 | [[PA] Make PartitionRoot a class](./output/debug/0388f4caa3d4e5809f741bd1c0c8642d20a98fd4.log) | 🟩 |
| elkurin | 2026-01-13 | [Revert "PA: Support multiple ThreadCache instances ...](./output/debug/b2283b2f8a113742a70daa64a861a85b933e6733.log) | 🟩 |
| ayumiohno | 2026-01-13 | [PA: Support multiple ThreadCache instances per thread.](./output/debug/a759a7b189d64e43a04d4179103d0f00b8fd4ee8.log) | 🟩 |
| hans | 2026-01-12 | [Fix/suppress -Wunsafe-buffer-usage for printf-style...](./output/debug/9149542aa89480668d5d044f50706dbe2d74b0a8.log) | 🟩 |
| victorvianna | 2026-01-12 | [Promote #warnings to #error](./output/debug/245dbb7bebfba6e48599342e3aa4f17f32f8b7bc.log) | 🟩 |
| ayumiohno | 2026-01-09 | [PA: Consistently pass BucketSizeDetails to free/qua...](./output/debug/b2155fca494c5b6266d42f9129ae3a7b85482c95.log) | 🟩 |
| ayumiohno | 2026-01-09 | [PA: Optimize FreeWithSizeAndAlignment in simple path](./output/debug/b809160344d7900a2e0ddd735f187ffe48576649.log) | 🟩 |
| pmonette | 2026-01-07 | [Migrate off legacy MOCK_METHODn macros](./output/debug/9cce6259aef60f8dbea52f421bb0234eb7cdadd5.log) | 🟩 |
| glaubitz | 2026-01-06 | [base/{allocator,numerics}: Fix incorrect ARM prepro...](./output/debug/ca88a350fcbf85c268d741cf8acd248d7f5529a0.log) | 🟩 |
| mikt | 2026-01-05 | [[PA] Parametrize Empty Slot Span Ring Buffer size](./output/debug/4b623f0c69ff979206bc7788fedbb27ddffbdcb3.log) | 🟩 |
| mikt | 2025-12-25 | [[PA] Persist MemoryReclaimer data on caller side](./output/debug/8bfdd5d9316a1883935190b61280c4765bfa14c4.log) | 🟩 |
| hans | 2025-12-12 | [Fixes for nodiscard std::optional, std::set operations](./output/debug/c6560eb97899b82a2869b7af638cab5063b48b79.log) | 🟩 |
| ayumiohno | 2025-12-09 | [PA: Upgrade DCHECKs to CHECKs in FreeWithSize, guar...](./output/debug/e711e98faec702084c26a43a411eb4bd3747bcbb.log) | 🟩 |
| mikt | 2025-12-08 | [[PA] Narrow down locked section](./output/debug/d2b46c259f0bd47fcc5d20c2cca97043ca5c71fe.log) | 🟩 |
| arthursonzogni | 2025-12-07 | [Reapply "Convert to UNSAFE_TODO in partition_alloc ...](./output/debug/fe0329b346753191011b073535fc9f2fe64da141.log) | 🟩 |
| yukishiino | 2025-12-04 | [PA: Share allocator_shim::IsAlreadyRegistered betwe...](./output/debug/090a06003985436a6e146838dbb3a5ec71c958b7.log) | 🟩 |
| anandrv | 2025-12-03 | [[partition_alloc] Increase amount of spinning in lo...](./output/debug/d0ab85f4a6da9905487bb0301251102c03625c56.log) | 🟩 |
| arthursonzogni | 2025-12-03 | [Convert to UNSAFE_TODO in partition_alloc in base_2](./output/debug/b231448a17e4c078154f29a28e2f9e9bbe210fac.log) | 🟩 |
| arthursonzogni | 2025-12-03 | [Convert to UNSAFE_TODO in partition_alloc in base_1](./output/debug/2a811452fe4f79a9f8910ccb8df1f348a92a6236.log) | 🟩 |
| arthursonzogni | 2025-12-03 | [Convert to UNSAFE_TODO in partition_alloc in posix](./output/debug/aa7166796bb04ae800c7b0e59abbf5e0816689c3.log) | 🟩 |
| thestig | 2025-12-01 | [PartitionAlloc: Remove RawPtrTraits::kDisableBRP](./output/debug/39d55c5da2324729af9e76abc3c293bdeda48a06.log) | 🟩 |
| luci-bisection | 2025-11-30 | [Revert "Convert to UNSAFE_TODO in partition_alloc i...](./output/debug/ebda611438a5eb6b3e3a2b6c67ddc49fa2b29ac1.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in mac_li...](./output/debug/5793f657f4dd960addd95a2d6022c4f785e46c2e.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in partit...](./output/debug/9f17d115d835fc782f48648cea5bc7b4fe83ae4f.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in windows](./output/debug/cf2789c6634d68aa9acafc91d34a27462c54743d.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in fuchsia](./output/debug/dc1590b9fe1c12e4746a6d7c7a903f2ea6af19a5.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in partit...](./output/debug/3c6388b2fcda07db5e6753c2309030de942747a7.log) | 🟩 |
| arthursonzogni | 2025-11-30 | [Convert to UNSAFE_TODO in partition_alloc in shim](./output/debug/d2c2747ffe3d648338366e9df117b3984a43509a.log) | 🟩 |
| thestig | 2025-11-28 | [Forward declare PartitionRoot in scheduler_loop_qua...](./output/debug/af595168d6ebc1aa751159affaf0d7f8c1b6e520.log) | 🟩 |
| ayumiohno | 2025-11-26 | [PA: Add finch feature flag to enable/disable FreeWi...](./output/debug/ee9dae5f4046d8f40a2559250b6067691f10683c.log) | 🟩 |
| ayumiohno | 2025-11-26 | [PA: Optimize FreeWithSize in simple path.](./output/debug/db3681ad5c220f81f5189e3f0bd616a4b2df6365.log) | 🟩 |
| mikt | 2025-11-20 | [[PA/AC] Batch-free quarantined entries](./output/debug/c0a91c99639bc5e15f420ae8a6c764f3bcd0bccf.log) | 🟩 |
| thestig | 2025-11-20 | [Include <features.h> directly in build_config.h on ...](./output/debug/4b1c1547ba19d65c3900cf790b1dc493997a80b4.log) | 🟩 |
| rgod | 2025-11-20 | [Revert "Convert to UNSAFE_TODO in partition_alloc"](./output/debug/86291accf55223eec529e421f57e126e3e663963.log) | 🟩 |
| arthursonzogni | 2025-11-20 | [Convert to UNSAFE_TODO in partition_alloc](./output/debug/a5480754481fa0e6ea26242701345819fc391d98.log) | 🟩 |
| arthursonzogni | 2025-11-20 | [partition_alloc: Move to C++20](./output/debug/a626491f4bc59f8bfd6c77db93dabebc4cd30466.log) | 🟩 |
| tasak | 2025-11-18 | [[PA] Make PartitionAllocExternalMetadata 100%-enabl...](./output/debug/21d8011dfea14a95cc2baaa3d76f6d25c2bbcc9d.log) | 🟥 |
| tarcisio.fischer | 2025-11-18 | [Enable and improve Death Tests for Partition Alloca...](./output/debug/ac53ec3334499e9ee36eb2623f1344b8e5afeef3.log) | 🟥 |
| mikt | 2025-11-13 | [Reland "[PA] Refactor to use a typed SlotStart to r...](./output/debug/1551e3ebf56ad234661c79a5e9d2dbe94988e744.log) | 🟥 |
| tasak | 2025-11-11 | [[PA] Ramp up External Metadata trial to 25% on canary](./output/debug/37d717b2583271f64d41d2e09e560bd7baae4c5e.log) | 🟥 |
| jood | 2025-11-11 | [Revert "[PA] Refactor to use a typed SlotStart to r...](./output/debug/a9912a4b18c048484e96aa3ce106da21930ed8b6.log) | 🟥 |
| mikt | 2025-11-11 | [[PA] Refactor to use a typed SlotStart to replace u...](./output/debug/495c1417ff2f7ce3a4a37f2d54d57712a4379ef2.log) | 🟥 |
| ayumiohno | 2025-11-06 | [PA: remove if PA_BUILDFLAG(ASSESRT_CPP_20)](./output/debug/3c92a87d2c9f9319118e951e64bd6f9c1e0306d2.log) | 🟥 |
| mikt | 2025-11-04 | [[PA/AC] Implement size-based filtering](./output/debug/f228d5a6170573dba10189f5a8d32623954c39c4.log) | 🟩 |
| kaiyilin | 2025-11-02 | [Revert "Track SchedulerLoopQuarantine zap/purge tim...](./output/debug/fd571058170087fff09fcac020c9e32c36032387.log) | 🟩 |
| nuskos | 2025-11-02 | [Track SchedulerLoopQuarantine zap/purge timings](./output/debug/300767b01ec7f3260d09820c564dc47219691061.log) | 🟩 |
| dloehr | 2025-10-31 | [Revert "Disable test until next clang roll"](./output/debug/fa63bd8319311b5c5f5a4e63678830c4a3655b04.log) | 🟩 |
| yukishiino | 2025-10-31 | [PA: Add shim/HowToInterposeOrIntercept.md](./output/debug/abae057a0b75d5cb4738606734d4f3492ad4e2bc.log) | 🟩 |
| tasak | 2025-10-29 | [[PA] Ramp up External Metadata trial to 10% on canary](./output/debug/a8bbea7ea2d6e41cd0a8687756e42c8b32a9b0c1.log) | 🟩 |
| mikt | 2025-10-29 | [[PA] Mitigate shutdown hang from Scheduler-Loop Qua...](./output/debug/2f4069fb8d7afbd9e3c078a14a5bab8280a68cf6.log) | 🟩 |
| tasak | 2025-10-17 | [[PA] Make PartitionAllocExternalMetadata enabled at...](./output/debug/db8446987dfff3cfc0c100b7d58e6a404ef639eb.log) | 🟩 |
| ahaas | 2025-10-13 | [Cleanup MiracleParameter implementation of ThreadCa...](./output/debug/eb106c8d4435c9c513b7623be5e114d8d45b216d.log) | 🟩 |
| dloehr | 2025-10-09 | [Revert "Roll clang+rust llvmorg-22-init-8940-g4d4cb...](./output/debug/81b93883f50bc4948aa65711dc8bd12ef51351b1.log) | 🟩 |
| kjlubick | 2025-10-09 | [Add const to boolean operators](./output/debug/081932d24e1f06bd1eea2fd42a21df0721c8faa5.log) | 🟩 |
| dloehr | 2025-10-09 | [Roll clang+rust llvmorg-22-init-8940-g4d4cb757-84 :...](./output/debug/e56f65cd966122c386a74d5fbfcadbbcc46d494b.log) | 🟩 |
| aattar | 2025-10-08 | [Map commit failure exit code to a memory eviction s...](./output/debug/11372dd73e164e7cc7cfe4e4cd75bdb26ec2b4c5.log) | 🟩 |
| mikt | 2025-10-06 | [Reland "[PA/BRP] Enable BRP-ASan on iOS"](./output/debug/1fd5c75f3b3683a004d2494a184a15b6bcef463a.log) | 🟩 |
| dloehr | 2025-10-01 | [Disable test until next clang roll](./output/debug/7032e49a7847caf235a4d67459a0d417c1ebf251.log) | 🟩 |
| lpromero | 2025-09-29 | [Revert "[PA/BRP] Enable BRP-ASan on iOS"](./output/debug/e3fec0a6803f0228bad652b12645ab19574e8bc9.log) | 🟩 |
| mikt | 2025-09-26 | [[base/PA] Add scheduler loop quarantine support to ...](./output/debug/cca2b369b2f8895cb14e24740e1f9bf91d5b371e.log) | 🟩 |
| lizeb | 2025-09-26 | [[PartitionAlloc] Remove launched feature for "use f...](./output/debug/ee6c8d0716e9d10d1ad25de97e690ddfa54f2c4a.log) | 🟩 |
| justincohen | 2025-09-25 | [ios:  Re-enable PA-E ReadExecutePages test on iOS 1...](./output/debug/9d3ee7c25f88e6e070308f0f80f2025646278355.log) | 🟩 |
| mikt | 2025-09-23 | [[PA/BRP] Enable BRP-ASan on iOS](./output/debug/ecbbabb292b5e07a332dfdb206591aa2ee7e8f44.log) | 🟩 |
| noemies | 2025-09-22 | [[iOS Gardener] Disable ReadExecutePages on device](./output/debug/ae5f94430c494db73fdcd2106269d3b08ea8e24f.log) | 🟩 |
| justincohen | 2025-09-22 | [ios: Enable some disabled PartitionAlloc unittests.](./output/debug/84a41f2a2242f43d95fc8333725a89ba38b1f8f1.log) | 🟩 |
| stefanoduo | 2025-09-19 | [Cronet: Disable PartitionAlloc via GN arg definitio...](./output/debug/e3b4f7b28213398c1891b27c23cca7581d7cec90.log) | 🟩 |
| mikt | 2025-09-19 | [[PA] Configure default stack size for iOS](./output/debug/78467db77680f3c375dcff3ff79ed5a7578bb3e5.log) | 🟩 |
| nuskos | 2025-09-19 | [Enable PartitionAlloc External Metadata feature at ...](./output/debug/5af527282d75750fe12450ca508fb2fe95ea0810.log) | 🟩 |
| rop | 2025-09-18 | [Setting Update Mechanism for these dependencies:](./output/debug/eb93de534d21673c0a860c373ae9bce1a360eba8.log) | 🟩 |
| thakis | 2025-09-16 | [Roll libc++ from 0257666efcf9 to 7b8dc07adc0f (9 re...](./output/debug/2c06e4c19773cdfc60f0a4a947363f0b7748f4ca.log) | 🟩 |
| avi | 2025-09-15 | [Remove Darwin version TODO](./output/debug/bb8643420b21841d7530b343cb247e061c0eb3b8.log) | 🟩 |
| tasak | 2025-09-14 | [[PA] Disable PartitionAlloc External Metadata](./output/debug/ccbdeaaeb633a85f317a1d27c17a118fab789b64.log) | 🟩 |
| acondor | 2025-09-12 | [Implement unchecked calloc via shim](./output/debug/fae4df38cef9720a13dd55a6b1d20600919e671b.log) | 🟩 |
| tasak | 2025-09-12 | [[PA] Deflake and re-enable PartitionAllocTest.Check...](./output/debug/cb2ed1009c4d5e310bc4ccc2bfd2d38a54e0461b.log) | 🟩 |
| kojii | 2025-09-11 | [[icu] Disables a `PartitionAllocTest` that seems fl...](./output/debug/9d08d0ef84ae6525bac4f69cb967bed38858dce5.log) | 🟩 |
| anandrv | 2025-09-09 | [[partition_alloc] Report acquisition time for conte...](./output/debug/dd3fc2d811574cf24220d2010bf3a7d00d644aee.log) | 🟩 |
| rop | 2025-09-07 | [LSC Metadata fix](./output/debug/09c9e8d5f0d23bd46bfb1f7bc10a294ea7a60774.log) | 🟩 |
| zhoumingtao | 2025-09-05 | [partition_alloc: Support dynamic page size for Loon...](./output/debug/3926658b1b5124b0c85bc9f2bac450214d3bf7a4.log) | 🟩 |
| lizeb | 2025-09-04 | [[PartiitonAlloc] Suppress TSAN error due to constan...](./output/debug/c001374914bffb3db6ed024a521f3a38f11d0911.log) | 🟩 |
| justincohen | 2025-09-03 | [Re-enable BRP zapping on iOS](./output/debug/7e1a38e21c908deac07090d1a8e7e49bbd0f862a.log) | 🟩 |
| justincohen | 2025-08-29 | [Revert "[PA] Add configuration for iOS binary exper...](./output/debug/51d0a558ecdf5cac58509d08263c36764c270ca6.log) | 🟩 |
| mikt | 2025-08-28 | [[PA] Separate Scheduler-Loop quarantine branch for ...](./output/debug/b12f7b4f52f41aa7bfb690cf3b766a00c55261fd.log) | 🟩 |
| justincohen | 2025-08-27 | [ios: Enable PartitionAlloc BackupRefPtr by default ...](./output/debug/18feb39705cfd694c878286497d6929c25b6a82d.log) | 🟩 |
| ivan.pavlotsky | 2025-08-27 | [Disable Xclang and target-feature flags for non-Cla...](./output/debug/f35da6421e88228655ec1d5dbe1dcdc870a4741a.log) | 🟩 |
| tasak | 2025-08-26 | [[PA] Make PartitionAlloc External Metadata 50% enab...](./output/debug/ba5e9459f6ad57cffa4800e08baa01ea6c811ffc.log) | 🟩 |
| tasak | 2025-08-21 | [Reland "[PA] Enable External Metadata on canary."](./output/debug/ce17d3c2126ae2b3611eac90d6b54035f1e595f4.log) | 🟩 |
| tasak | 2025-08-20 | [Revert "[PA] Enable External Metadata on canary."](./output/debug/22124931fa99556ec56b4ac30476b594f9f1b80a.log) | 🟩 |
| dsanders11 | 2025-08-20 | [Remove unused include in scheduler_loop_quarantine_...](./output/debug/180844cd9919d753d40b55409996c659f55250e2.log) | 🟩 |
| tasak | 2025-08-18 | [[PA] Enable External Metadata on canary.](./output/debug/1a0ba72ed0a07107cf2398a93561f44c855c58b0.log) | 🟩 |
| tkent | 2025-08-18 | [Remove `WTF::` in base/](./output/debug/902c2e234fc94d82df3eab27070600db88e9f63e.log) | 🟩 |
| tasak | 2025-08-17 | [[PA] Skip HardeningTest.(PoolOffset)MetadataPointer...](./output/debug/f81bc9851284fe29f2a946f1dfd793b77941fd01.log) | 🟩 |
| tasak | 2025-08-14 | [Revert "[PA] Enable external metadata on canary"](./output/debug/5566f889c0c929938fb11a0c04235b3b7932a4c7.log) | 🟩 |
| tasak | 2025-08-14 | [[PA] Enable external metadata on canary](./output/debug/ecbda5f809e71d995d4002a1530c625ef848b073.log) | 🟩 |
| tasak | 2025-08-13 | [[PA] Check `metadata_start_` at InitThreadIsolatedP...](./output/debug/6003b144a5c796206271fb2337709fa506c44fa6.log) | 🟩 |
| aeubanks | 2025-08-12 | [Update nocompile tests](./output/debug/a40ae6084cc3d928e1284eef447cae38a224f36a.log) | 🟩 |
| tasak | 2025-08-12 | [Revert "[PA] Enable PartitionAllocExternalMetadata ...](./output/debug/c9620c2ad14f777a1873426e11d34573e211557e.log) | 🟩 |
| tasak | 2025-08-11 | [[PA] Enable PartitionAllocExternalMetadata on canary](./output/debug/ea91c2f570f1d3be3d29f27f1d1a099fb368c325.log) | 🟩 |
| tsepez | 2025-08-07 | [Remove some pragma allow_unsafe_buffers from partit...](./output/debug/8f2ac09151b3a0cf713bcf93bb112b21f91c63c2.log) | 🟩 |
| tasak | 2025-08-07 | [Revert "[PA] Enable ExternalMetadata feature on can...](./output/debug/4a3b2fb6d953a9ad17e7da948645fa7e180926b0.log) | 🟩 |
| tasak | 2025-08-06 | [[PA] Enable ExternalMetadata feature on canary Enab...](./output/debug/69da7baf768c4edb1cd77a5be1538ce4283b7736.log) | 🟩 |
| arthursonzogni | 2025-08-06 | [PA: Suppress REALLOC_GROWTH_FACTOR_MITIGATION limit.](./output/debug/5c2d24bfafe63e10a61ec335509d5d83acd7db11.log) | 🟩 |
| mikt | 2025-08-05 | [[PA] Fix PartitionRoot::CheckMetadataIntegrity](./output/debug/356065b030e6194a732705e86a11248db2728786.log) | 🟩 |
| rulongchen | 2025-08-05 | [[PartitionAlloc] Fix crash when nullptr is passed t...](./output/debug/659d300ab723b5ea128984dda1d0e94d456ab665.log) | 🟩 |
| tsepez | 2025-08-04 | [Remove file-wide unsafe buffer pragamas in partitio...](./output/debug/218e32d7878cfa006a9e90df6dc16a377cffbdb3.log) | 🟩 |
| tsepez | 2025-08-04 | [Propagate UNSAFETY through partition alloc raw poin...](./output/debug/a25ec884fd1dd0d9f50f7baf1883982e8db46b41.log) | 🟩 |
| tsepez | 2025-08-04 | [Mark unsafe raw_ptr<T> operations as unsafe.](./output/debug/4e92c91bb300e840f586f504e6fc6ea2adb329b2.log) | 🟩 |
| mikt | 2025-08-04 | [[PA] Scheduler-Loop Quarantine is configured via JSON](./output/debug/f79cd042e21bc40da52829e883813b4f3f093ff2.log) | 🟩 |
| mikt | 2025-08-03 | [[PA] Purge Scheduler-Loop Quarantine on UI Thread T...](./output/debug/22ea4eaebb2458920d56eb68a1db74028375303e.log) | 🟩 |
| tsepez | 2025-08-01 | [Remove base/allocator from unsafe_buffers_paths.txt...](./output/debug/57104f156773d81ca03b0c41d118821475646bf5.log) | 🟩 |
| tsepez | 2025-08-01 | [Add PA_UNSAFE_BUFFER_USAGE macro to partition alloc.](./output/debug/f5d9c0b9bfccf8b0e7716f9c70623ce6129fea9b.log) | 🟩 |
| tasak | 2025-07-31 | [[PA] Propose "ExternalMetadata" synthetic finch tri...](./output/debug/ec5fa718c5470c1f4840f50f72b2815545ee09e8.log) | 🟩 |
| dsanders11 | 2025-07-29 | [Remove unused include in partition_address_space.h](./output/debug/f5c8626fa2949908146d00fdc3a182b16e5c32b5.log) | 🟩 |
| arthursonzogni | 2025-07-27 | [[PA] Fix unused `use_libcxx_modules`.](./output/debug/aee60823002b0e80d96e76e56951446ce0eb58b2.log) | 🟩 |
| tasak | 2025-07-27 | [[PA] Move Metadata outside of GigaCage (6/7)](./output/debug/5ab2ac91deaf53dbbd612e779b3f51253bf02243.log) | 🟥 |
| tasak | 2025-07-27 | [[PA] Move Metadata outside of GigaCage (5/7)](./output/debug/828b52630e80e619f057deba245c83644a4066c6.log) | 🟥 |
| tikuta | 2025-07-24 | [partition_allocator: Disable libcxx module for unit...](./output/debug/0df75035937ddb4efd66639f25b08d53d7b4f8ec.log) | 🟥 |
| thestig | 2025-07-24 | [Auto-format //base GN files](./output/debug/fd0128b7cc4a5ee2e1d9f6eec022b6bf73694fe6.log) | 🟥 |
| tasak | 2025-07-23 | [[PA] Move Metadata outside of GigaCage (4/6)](./output/debug/1e3b00f0a40be8ea75dd4709821b71b2c079912b.log) | 🟥 |
| chrdavis | 2025-07-23 | [ThreadTicks GetForThread should include kernel time...](./output/debug/d7ae27f0e2a0c03b9f80ca1195b04fedcdf1193c.log) | 🟥 |
| tasak | 2025-07-22 | [[PA] Move Metadata outside of GigaCage (3/5)](./output/debug/39ba710d71b750335e1438d30ba62b1c0736e73e.log) | 🟥 |
| mikt | 2025-07-22 | [[PA] Allow to ensure ThreadCache without PartitionR...](./output/debug/833fe8d5e0a9d775255cc8a09fdb71183c5f587f.log) | 🟥 |
| tikuta | 2025-07-21 | [partition_allocator: Disable libcxx module for allo...](./output/debug/49e207e96bec179c82e609cf0a052d42d4c2ac2c.log) | 🟥 |
| tasak | 2025-07-18 | [[PA] Add pa_check.md](./output/debug/b7aff97e9add16d7a0f04c9eb2e752d6f7dff85d.log) | 🟩 |
| tasak | 2025-07-18 | [[PA] Move Metadata outside of GigaCage (2/5)](./output/debug/75b1cb38a7826527337da4ba4b3b6926bba29675.log) | 🟩 |
| tasak | 2025-07-17 | [[PA] Move Metadata outside of GigaCage (1/5)](./output/debug/369c817c900ed3796da34b973b4b95391a836941.log) | 🟩 |
| cdesouza | 2025-07-17 | [[exit-time-destructors] Exclude target with warnings](./output/debug/7186dfd2903897b1cfde4a36cfc5ede25c9c6f3d.log) | 🟩 |
| arthursonzogni | 2025-07-16 | [partition_alloc: Fix missing include on Windows.](./output/debug/f5822de8f74df009da56681cca82a3c986bbfc67.log) | 🟩 |
| arthursonzogni | 2025-07-15 | [partition_alloc: Resolve C++20 compile errors.](./output/debug/328d516729e7e9edc833244c73cc9013828e5a1a.log) | 🟩 |
| thakis | 2025-07-14 | [Remove remaining __pnacl__ and __native_client__ in...](./output/debug/7b2807165fad397df23f5f749b15e9e43269ccf5.log) | 🟥 |
| tikuta | 2025-07-09 | [base: Remove references to BUILDFLAG(IS_NACL)](./output/debug/a54ac8d0dd78019fb41d2e376726d45b287e856b.log) | 🟥 |
| lizeb | 2025-07-09 | [[PartitionAlloc] Use fewer VMAs by default on Linux...](./output/debug/db340435e8d7e8eb89925d3006ecaf6427e3ab4f.log) | 🟥 |
| mikt | 2025-06-27 | [[PA] Fix pool offset freelist DCHECK with MTE](./output/debug/79b418050876e0c4187a80f668e81ce956b32bf2.log) | 🟥 |
| lizeb | 2025-06-26 | [[base/allocator] Remove launched features](./output/debug/11aaded5a31dc53a08781ca47f146f3795d021c4.log) | 🟥 |
| mikt | 2025-06-25 | [[PA] Add callback for DoubleFreeDetected or Corrupt...](./output/debug/3d6e246fc6014fd3f9f850876eae0fcd8f97921e.log) | 🟥 |
| thiabaud | 2025-06-25 | [[partition_alloc] Add more threading annotations](./output/debug/983d556a9aed36814954a4463bb0b508d2af133a.log) | 🟥 |
| tikuta | 2025-06-24 | [partition_alloc: Add a missing include for std::ignore](./output/debug/f8a48647751d44a0497a76633f6dc22ab28f51ad.log) | 🟥 |
| tasak | 2025-06-23 | [[PA] Make PartitionAllocMemoryAllocationPerfTest hu...](./output/debug/85594a8469649294d3b365e0637256a87dc74602.log) | 🟥 |
| dcheng | 2025-06-20 | [base: remove NaCl from BUILD.gn, as well as NaCl-on...](./output/debug/9b8de412d87c20117d2d04836bc5fa85866eaa08.log) | 🟥 |
| mikt | 2025-06-18 | [[PA] Add option not to crash on Double-Free or Corr...](./output/debug/ffa6d285560e810ab57e9a026b58f0a722658a6a.log) | 🟥 |
| bikineev | 2025-06-18 | [PA: Fix an include to be relative to PA source dir](./output/debug/a28c3c3d01412a17ebf145bfe2d73c8071c686e3.log) | 🟥 |
| rop | 2025-06-17 | [LSC Add 'Update Mechanism:' to README.chromium](./output/debug/49c08e7ea1746f671ce75b96f6ca444f6d6065ab.log) | 🟥 |
| avi | 2025-06-12 | [Update MacOSVersion() for macOS 26](./output/debug/73de62811794a78ccb95ed3e197180ec8fb666c2.log) | 🟥 |
| thiabaud | 2025-06-09 | [[partition_alloc] Add threading annotations](./output/debug/50a84f34499cdfdc040a9d2c8fc1f031d31bbc78.log) | 🟥 |
| fdoray | 2025-06-06 | [[partition_alloc] Add mechanism to terminate a proc...](./output/debug/a585fc502ffa23ddce3412973eba2fe677325f02.log) | 🟥 |
| kdlee | 2025-06-05 | [PA: Remove seam code for 4S](./output/debug/76e5e3ac91101d2976805205fb51585c266e548f.log) | 🟥 |
| thestig | 2025-06-05 | [[PA] Use PA_LOG() instead of LOG()](./output/debug/37c90018cca427ce66d7f2fc3f43fca9d6ee9b6b.log) | 🟥 |
| mikt | 2025-06-03 | [[PA] Optimize Purging mechanism for Scheduler-Loop ...](./output/debug/e3668842ccb3173913161900ec731508f0655604.log) | 🟥 |
| mikt | 2025-06-03 | [[PA] Replace usable_size with slot_size in Schedule...](./output/debug/b1a4a44e2310b4661acf418a3524778969943919.log) | 🟥 |
| mikt | 2025-06-03 | [[PA] Do Scheduler-Loop Quarantine after BRP Quarant...](./output/debug/b95054240369556471d5c438217480a23089aa4a.log) | 🟥 |
| mikt | 2025-06-03 | [[PA/E-LUD] Refactor: Fork LightweightQuarantine](./output/debug/ffb614650932ce01003b1f1cbf26c1709f68c364.log) | 🟥 |
| hans | 2025-05-30 | [Mark pointer in PartitionAllocPageAllocatorTest.Dec...](./output/debug/d617778ed253822ee4c1bb9d03826f01e5f09e32.log) | 🟥 |
| avi | 2025-05-29 | [Remove the macOS 11 malloc size hack from Partition...](./output/debug/3ae30e4cf9d6f59ba825dcc96af9940ab35bf27b.log) | 🟥 |
| nuskos | 2025-05-29 | [Use std::array instead of a c style array in PurgeP...](./output/debug/a160ae6759caac1e19e3bf51b3660b649a9aba2e.log) | 🟥 |
| mikt | 2025-05-28 | [Reland "[PA] Cache ReservationOffsetTable instead o...](./output/debug/964c6996d56bd2167f4f6fdb2d88acfeba32c5d8.log) | 🟥 |
| caseq | 2025-05-28 | [Remove redundant std::max(x, x)](./output/debug/e85940b94442a391f6b528d9202e8c66eaca87be.log) | 🟥 |
| mpdenton | 2025-05-27 | [GWP-ASan: raise kMaxMetadata and kMaxRequestedSlots](./output/debug/f44457d2f971ec0a45c271e093b6aa56044d0ec1.log) | 🟥 |
| jonross | 2025-05-21 | [Revert "[PA] Cache ReservationOffsetTable instead o...](./output/debug/c858ce950cf900f168772e5e7c8f7cfa3e66ce96.log) | 🟥 |
| mikt | 2025-05-20 | [[PA] Cache ReservationOffsetTable instead of lookup...](./output/debug/29111157f1454c5a52fe83c7da9f57cb07a35b82.log) | 🟥 |
| mikt | 2025-05-18 | [[PA/shim] Fix shim test failure on mac component build](./output/debug/57f3d1311ce54e7c528608f2df77951920903451.log) | 🟥 |
| tikuta | 2025-05-15 | [base: Disable libc++ modules build in partition all...](./output/debug/1d9d02e434059dbdb74e10e28ad42fd97c25a85c.log) | 🟥 |
| tasak | 2025-05-14 | [[PA] Remove libc++ string object dependency from al...](./output/debug/269b4081447bcef3f64ad87116d9c6d8cfcf4645.log) | 🟥 |
| thestig | 2025-05-14 | [Clean up PA's instance_tracer.h](./output/debug/299f793686af3b7ea3facf647464a15622c27466.log) | 🟥 |
| mikt | 2025-05-14 | [[PA] Fix PoolOffsetLookup for Configurable Pool](./output/debug/fc79edffac58c4d59925412bf378eaf0f454688e.log) | 🟥 |
| mikt | 2025-05-12 | [[PA] Cache PoolInfo instead of lookup by address](./output/debug/f0e2e7a786cda3a52feaff9c7894ebcf68b13fb3.log) | 🟥 |
| thestig | 2025-05-07 | [Remove <ostream> from PA's safe_conversions.h](./output/debug/2b1d9301c925673637b3ff6e6412686ecfe66d02.log) | 🟥 |
| antoniosartori | 2025-05-07 | [Revert "gardening: Disable PartitionAllocPageAlloca...](./output/debug/60903e2555a42eeac93dc7c91eedbca746943842.log) | 🟥 |
| yukishiino | 2025-05-06 | [gardening: Disable PartitionAllocPageAllocatorTest....](./output/debug/988f84a803953c0874cffadcb0ded36ba174582c.log) | 🟥 |
| mikt | 2025-05-06 | [[PA/docs] Update buckets.md](./output/debug/5c18e6e9b5fc4cb6748df24c2f63003e8ad3b81e.log) | 🟥 |
| dloehr | 2025-05-06 | [Exported things should always be visible](./output/debug/843601306bff485f15960ef0c7b23dd34e2d7ee5.log) | 🟥 |
| mikt | 2025-05-02 | [[PA] Remove Freelist Dispatcher](./output/debug/196ca28d1e516424ab24d9a798e13473895f8b71.log) | 🟥 |
| mikt | 2025-05-02 | [[PA] Remove free slot bitmap](./output/debug/93234db35d91c7af0ff75025fc4be90cc99dfcb9.log) | 🟥 |
| tasak | 2025-05-02 | [[PA] Replace std::unordered_map with base::flat_map](./output/debug/3a86115ff7330669c596355e7d7786703d4f2082.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Remove unused free functions](./output/debug/971c92b116187e9f5ebe2e3c84cf84b04161edbe.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Remove unchecked freelist iteration](./output/debug/2686355087336647c1d9aa5579eed6836dd71617.log) | 🟥 |
| nuskos | 2025-05-01 | [Reland "spanification: remove `#pragma allow_unsafe...](./output/debug/84e59bb4cda4ba071548ede290d44fcfa44f1a42.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Simplify bucket lookup](./output/debug/1397a7c24bc0e506cb7bfa2b5eaac48c144f7540.log) | 🟥 |
| luci-bisection | 2025-05-01 | [Revert "spanification: remove `#pragma allow_unsafe...](./output/debug/afa6432ee9ba7108018c52f8f8e68cc84d2f3370.log) | 🟥 |
| nuskos | 2025-05-01 | [spanification: remove `#pragma allow_unsafe_buffers...](./output/debug/46f7b646565a2f60129a68806b8615347556a08b.log) | 🟥 |
| mikt | 2025-05-01 | [[PA] Remove ZERO_RANDOMLY_ON_FREE](./output/debug/a0068b7420952f0093c6149796d81039284e888c.log) | 🟥 |
| wangqing-hf | 2025-04-29 | [[PA] Add stack scan supported for loongarch64.](./output/debug/b6a1dfdeb69381c36187ce9e7a4e9f24ec1a9065.log) | 🟥 |
| mikt | 2025-04-29 | [[PA] Check ThreadCache validity in DoubleFreeOrCorr...](./output/debug/5ce629459a2c3b6ef5f56490805cd26169ac6969.log) | 🟥 |
| tasak | 2025-04-29 | [[PA] Copy base/containers/flat_{map,tree}.h to part...](./output/debug/4170769c13d02df7bcff9a90112f36ed552dcf3b.log) | 🟥 |
| mikt | 2025-04-28 | [[PA] Scoped Scheduler-Loop Quarantine opt-out](./output/debug/2d19fedeb02734e543c21c46b966835ce217ceea.log) | 🟥 |
| abhijeet | 2025-04-24 | [[tvOS][base_unittests] Replace host_info with sysct...](./output/debug/862506deb382f3f8a8fa9689c8d5136a48e9b778.log) | 🟥 |
| mikt | 2025-04-24 | [[PA] Remove ghost of alternate bucket distribution](./output/debug/b6040b2b33d28d064c2167c878deed3b49e4aeb2.log) | 🟥 |
| smaier | 2025-04-23 | [Roll Android NDK to r28](./output/debug/a9ae8c0fd665f61acca4633d828a1061fbd461cc.log) | 🟥 |
| mikt | 2025-04-23 | [[PA/shim] Support sized-delete](./output/debug/d691f607f29e8ca39c37917be7a69629f80a0dbd.log) | 🟥 |
| tasak | 2025-04-22 | [[PA] Fix wrong includes.](./output/debug/a5083e082d03f4f7d3b0ee35df7cfa3e2ccf8680.log) | 🟥 |
| tasak | 2025-04-20 | [[PA] Fix PartitionAlloc windows component build](./output/debug/471d99073bd4a042dd17aed9fb7604a6c3277ad9.log) | 🟥 |
| anandrv | 2025-04-17 | [[PartitionAlloc] Enable priority inheritance in Spi...](./output/debug/21fe3be95a6c4372f6b3e467c05be49f8cd5279f.log) | 🟥 |
| mikt | 2025-04-16 | [[PA] Refactor: move Scheduler-Loop Quarantine relat...](./output/debug/94efd06f8629f3ee91888150d16d2c2fafd898a5.log) | 🟥 |
| thestig | 2025-04-14 | [Forward declare base::NoDestructor in headers when ...](./output/debug/4b0f19307639826f8fca1a41882781540ff2fb50.log) | 🟥 |
| lizeb | 2025-04-09 | [[base/allocator] Add aligned_alloc to shims on Android](./output/debug/932177a9b8f06e7f478fcb22ac7b7184908738a8.log) | 🟥 |
| lizeb | 2025-04-09 | [[PartitionAlloc] Make ENOMEM issues have a separate...](./output/debug/5144c01d94d24360ec0cecb91319bde84e9acec7.log) | 🟥 |
| dloehr | 2025-04-08 | [Change expected message in nocompile test](./output/debug/2041003ba674f918c33b1afaaad74e652f34bcea.log) | 🟥 |
| lizeb | 2025-04-08 | [[PartitionAlloc] Crash in AddressPoolManager when d...](./output/debug/836a8ac2ba51ad26527eee243edda043586f7390.log) | 🟥 |
| mikt | 2025-04-07 | [Reland "[PA] Disable BRP zapping on iOS"](./output/debug/799310f3bf7d3cdbee28a086035eefc38732b548.log) | 🟥 |
| dtapuska | 2025-04-04 | [[ios blink] Add support for arm64e target](./output/debug/4cc11b45843b513ee6cd469c21dde9c607624865.log) | 🟥 |
| ginnyhuang | 2025-04-04 | [Revert "[PA] Disable BRP zapping on iOS"](./output/debug/20e84b3ed75698f1fb19149a640573f2bd420195.log) | 🟥 |
| mikt | 2025-04-04 | [[PA] Disable BRP zapping on iOS](./output/debug/5a43d8f11eeef195a27b6f0d4373e1a4f1a53581.log) | 🟥 |
| ritownsend | 2025-04-03 | [chore: migrate ritownsend OWNERS/TODOs](./output/debug/3ef26d8c8a8886277a41d4ae1e9d1801320eb274.log) | 🟥 |
| mikt | 2025-04-02 | [Reland "[PA] Add base::CheckHeapIntegrity to invest...](./output/debug/53e916ce2c2835fbe66f639a1c4a8a010efa0514.log) | 🟥 |
| tasak | 2025-03-31 | [[PA] Split DoubleFreeOrCorruptionDetected into Doub...](./output/debug/a9e3cecf8ea5c8da254d98bab323142e17229b0c.log) | 🟥 |
| dloehr | 2025-03-28 | [Export things to prevent accidental duplication](./output/debug/ab56923a27b2793f21994589b0c39bc3324ff49f.log) | 🟥 |
| wcwang | 2025-03-25 | [Revert "[PA] Add base::CheckHeapIntegrity to invest...](./output/debug/01d2444accdc1f985d3cfd0c512222de507eb3a4.log) | 🟥 |
| wcwang | 2025-03-25 | [Revert "[PA] Fix compile failure in PartitionRoot::...](./output/debug/771d9b82c8daa8f1ae68cb33c5a1c3c8cfaf1267.log) | 🟥 |
| mikt | 2025-03-24 | [[PA] Fix compile failure in PartitionRoot::CheckMet...](./output/debug/13a351f4d27353ed972aa4fc37104d872ed576dd.log) | 🟥 |
| mikt | 2025-03-24 | [[PA] Add base::CheckHeapIntegrity to investigate co...](./output/debug/c381bec7b1db2e8aec822a8a6217736f4d70cc9c.log) | 🟥 |
| justincohen | 2025-03-21 | [ios: Correct gwp_asan_unittests out of memory](./output/debug/0abfd4c40e8124de0d14f0d95f5bfe9a4ddd8a8b.log) | 🟥 |
| pmeuleman | 2025-03-20 | [Deactivate MTE in HWASan builds](./output/debug/df5d4c1b2bdc8d18253cec8a3be4e0fa9194a2bb.log) | 🟥 |
| lokokung | 2025-03-18 | [[wasm] Adds rudimentary support for WASM/Emscripten...](./output/debug/fb60666cb1896901bb14a5feb10001d20c8833c3.log) | 🟩 |
| mikt | 2025-03-07 | [[PA] Add EnsureThreadCache() for blocking thread ca...](./output/debug/d3191727ef81ba9daefb0bd3b90d9e4043a4bfa1.log) | 🟩 |
| mikt | 2025-02-27 | [[PA] Add unittest to verify extra extras protecting...](./output/debug/46d880ff62f340854a5a70142b0abf604c7af221.log) | 🟩 |
| jbroman | 2025-02-24 | [Remove an unused include of <unistd.h>](./output/debug/bd46928f4b41532c457fa8834ab56d729f4c6c67.log) | 🟩 |
| arthursonzogni | 2025-02-20 | [PA: Fix compilation error about `LiftThreadIsolatio...](./output/debug/f32541744d6a7305af151078470f0cb07bc3ea4f.log) | 🟩 |
| kdlee | 2025-02-20 | [PA: Remove pool offset freelists feature](./output/debug/98d198364f616abebfbcec16edf45e640fe00ca4.log) | 🟩 |
| arthursonzogni | 2025-02-17 | [partition_alloc: fix missing `basic_common_referenc...](./output/debug/879c3028e66ee96ba147c583315b2fd58c99b43d.log) | 🟩 |
| arthursonzogni | 2025-02-17 | [PartitionAlloc: realloc growth factor mitigation fo...](./output/debug/09ea5ed6c63f10582a6e67cd0db5549597bf25d5.log) | 🟩 |
| marshall | 2025-02-13 | [Fix extra qualification on member 'basic_common_ref...](./output/debug/2e370e26c52803f2524c51c3c7a3d2c21ebabcd8.log) | 🟩 |
| dtapuska | 2025-02-13 | [[ios blink] Set MAP_JIT pages to RWX by default](./output/debug/5ce79ef9d981e6e60ee9a1f5bd905b1ee076965c.log) | 🟩 |
| mikt | 2025-02-13 | [[PA] Add a test for backup_ref_ptr_extra_extras_size](./output/debug/0ebfead86460d7744f604f31717fbcf9ea348def.log) | 🟩 |
| mikt | 2025-02-12 | [[PA] Fix backup_ref_ptr_extra_extras_size not being...](./output/debug/3005f069de69d77fcb06b9184d25c1f54ed8717c.log) | 🟩 |
| hans | 2025-02-11 | [Roll libc++ from 12150825ca73 to 492ff432ef34 (56 r...](./output/debug/f3153d2c69cfaae76414e3e3a7fa15408ffba479.log) | 🟩 |
| dtapuska | 2025-02-07 | [Reland "[ios blink] Enable MAP_JIT unconditionally"](./output/debug/4b9edec2ee9cfdcf63edc195622fd66a8506d65f.log) | 🟩 |
| asamidoi | 2025-02-07 | [Revert "[ios blink] Enable MAP_JIT unconditionally"](./output/debug/21e5eb503a278ed29bf9b88fd383f2c94d8da612.log) | 🟩 |
| dtapuska | 2025-02-05 | [[ios blink] Enable MAP_JIT unconditionally](./output/debug/2c0dac296b692fee8a92f47a7237823d6cbde44f.log) | 🟩 |
| neis | 2025-02-05 | [Remove Lacros leftovers from base/](./output/debug/66a65af8596ab076424176fbbad0f02ac4fcae0f.log) | 🟩 |
| dsanders11 | 2025-02-03 | [Remove some unused includes of <tuple>](./output/debug/185644689122812d475d0507e3bc1aa0c0156782.log) | 🟩 |
| arthursonzogni | 2025-02-03 | [PA: Remove 'NDEBUG' and make is_debug configurable.](./output/debug/85d14cbcf203ad6b4059683b1700f00cc677b29c.log) | 🟩 |
| mikt | 2025-01-28 | [[PA] Unify FreeFlags::kZap with kSchedulerLoopQuara...](./output/debug/6944ecdfe98cc0f76f02d0ec6643ff78c8d5c191.log) | 🟩 |
| tasak | 2025-01-21 | [[PA, MTE] Fix PartitionAllocTest.FewerMemoryRegions...](./output/debug/a004bba90aa8ac07a7071dbf1a09d0e4e99513bc.log) | 🟩 |
| yukishiino | 2025-01-16 | [ELUD: Reduce the usage of machine stack](./output/debug/088f9a5921a6fc929fdffb27577dddc5a01f4a71.log) | 🟩 |
| pkasting | 2025-01-10 | [Manually fix remaining clang-tidy errors in base/.](./output/debug/bad4d8a87337475db378ebb64706a4fdebb641a2.log) | 🟩 |
| lizeb | 2025-01-09 | [[PartitionAlloc] Add feature to use fewer memory re...](./output/debug/ba505b4478daf573942664233c75a23d706607dd.log) | 🟩 |
| lizeb | 2025-01-09 | [[PartitionAlloc] Document apple lock options](./output/debug/a77103c1816d48a72e528c58d78993d45a9c0343.log) | 🟩 |
| pkasting | 2025-01-08 | [Apply clang-tidy autofixes to base/.](./output/debug/5430b75fd1cc5429fc41b18561c0439b2ae16670.log) | 🟩 |
| mikt | 2025-01-08 | [Reland "[PA/AC] UI thread specific capacity configu...](./output/debug/51b0fb5b1c36366f7e174b2637407ad964a9bcf7.log) | 🟩 |
| pkasting | 2025-01-08 | [Mark raw_ptr<T> and T* as having a common reference...](./output/debug/33fbaf834c7673bd75b829b775775ac42e418c09.log) | 🟩 |
| yyanagisawa | 2025-01-07 | [Revert "[PA/AC] UI thread specific capacity configu...](./output/debug/dc027d58406d26da0786910c51720935ebd3b3fc.log) | 🟩 |
| mikt | 2025-01-07 | [[PA/AC] UI thread specific capacity configuration f...](./output/debug/6cdc138f18001b0ba6dbe12a7c95530052b6ac32.log) | 🟩 |
| lizeb | 2025-01-07 | [[PartitionAlloc] Name anonymous VMAs on Linux and C...](./output/debug/6548aa3fdc79179a5b558892afad7e71fa473757.log) | 🟩 |
| verwaest | 2025-01-06 | [[pa] Use adaptive-spin and data-sync on macos](./output/debug/934bddc37b89df34cf8adeb6dd3d12246143df89.log) | 🟩 |
| pkasting | 2024-12-27 | [[cleanup] clang-format base.](./output/debug/9cab8b0d103998c4552b3ac14ef8429b7fe652c4.log) | 🟩 |
| tasak | 2024-12-20 | [[PA] Copy //base/files/platform_file.h to Partition...](./output/debug/165d75a6241b0c43e2c3e1404b22500bada3b5cc.log) | 🟩 |
| edechamps | 2024-12-19 | [Don't build partition_alloc if it is not needed](./output/debug/616b272794c79c5c19f87508ce86448e18afde6c.log) | 🟩 |
| mikt | 2024-12-17 | [[BRP] Allow extras size to be controlled via Finch](./output/debug/847c1e77f386c103aeef42ecee6529d625d045ec.log) | 🟩 |
| pkasting | 2024-12-17 | [Don't use base::internal:: APIs outside base/.](./output/debug/f240d41100751bac9a2528caea233da8d7d3750b.log) | 🟩 |
| fdoray | 2024-12-13 | [[perfcombined2024] Enable PartitionAlloc parameter ...](./output/debug/b15cea87c55341ede2956f7e2bf09eb0332b33d1.log) | 🟩 |
| tikuta | 2024-12-09 | [base: add missing includes for the build with use_l...](./output/debug/e8eba702d878a8cad8d97963f838f2ccee0e7f8a.log) | 🟩 |
| ivan.murashov | 2024-12-09 | [partition_alloc: Remove duplicated includes of buil...](./output/debug/89c828e21c494b6220723c04997a8639633cc7f9.log) | 🟩 |
| tasak | 2024-12-09 | [[PA] Fix flaky test failure of memory reclaimer uni...](./output/debug/3faa9b05d6777335f964cbf901c8ea1b23de07ea.log) | 🟩 |
| kdlee | 2024-12-06 | [PA: Remove *Scan config from `PartitionOptions`](./output/debug/155df0f49332dbf69aec0614d7a89c6a09c0bc3e.log) | 🟩 |
| kdlee | 2024-12-06 | [PA: Remove *Scan references in unit tests](./output/debug/394945644da7df29c4262a0b69c79e0b0c91944c.log) | 🟩 |
| arthursonzogni | 2024-12-04 | [Style: Fix array initializations with size mismatch...](./output/debug/f96b908c9a5edb49a61287aa7fe4e9a311f44766.log) | 🟩 |
| pkasting | 2024-12-03 | [Introduce a "same as any" template and use it to si...](./output/debug/b7a17328404dac7bfc9be2a07190aaf6bbd2c36a.log) | 🟩 |
| tasak | 2024-11-20 | [[PA] Make EnableShadowMetadata() and PartitionDirec...](./output/debug/c551156ef8ccc090e52941d58c22647326066ff3.log) | 🟩 |
| rop | 2024-11-18 | [LSC Updating README.chromium license names to use s...](./output/debug/7b91772e38c3d928d2170cd5cbcef81b8b2dbf5d.log) | 🟩 |
| arthursonzogni | 2024-11-14 | [DanglingPtr: Improve error message.](./output/debug/6a3eb3e3cff5b3f6a0938992c921fd534520af9f.log) | 🟩 |
| pbos | 2024-11-14 | [Replace CHECK(false) in base/](./output/debug/fff6771d53cfd6b9bb8d53180090b2679670c2fc.log) | 🟩 |
| glazunov | 2024-11-08 | [[BRP] Make sure all quarantined allocations are zapped](./output/debug/bd0c0ab0f94f8b9c21e4e9207f66a4832477e96e.log) | 🟩 |
| tikuta | 2024-11-08 | [base: include stdlib.h for malloc/realloc](./output/debug/972d0c921eeba6ee2ecc49762eb6e0676e8ea84f.log) | 🟩 |
| yukishiino | 2024-11-07 | [PA: Narrow the critical section of LightweightQuara...](./output/debug/5720e2701e416a4e8e9b423413659e925ab4dbbb.log) | 🟩 |
| lizeb | 2024-10-30 | [[PartitionAlloc] Add option to eventually memset() ...](./output/debug/72ae2afeb4d373b900683a82919e8d4a0d139f82.log) | 🟩 |
| yukishiino | 2024-10-28 | [ELUD: Do not quarantine direct-mapped allocations](./output/debug/2bc4745c33b44da415fad88ccfdf2900ed835dce.log) | 🟩 |
| lauren | 2024-10-24 | [PA: check for <sys/ifunc.h> to enable MTE/BTI](./output/debug/e11fdbafa549101c04b028e940bf59963229569f.log) | 🟩 |
| lizeb | 2024-10-23 | [[PartitionAlloc] Don't memset() direct-mapped alloo...](./output/debug/914c30a91ad47f1f60de28bc10cfeef910dec161.log) | 🟩 |
| arthursonzogni | 2024-10-22 | [PA: check readability-static-accessed-through-instance](./output/debug/dbaab7e744c75e9c5411397d6a61e8217053ce22.log) | 🟩 |
| yukishiino | 2024-10-21 | [PA: Remove runtime conditional branches from Lightw...](./output/debug/ce13777cb731e0a60c606d1741091fd11a0574d7.log) | 🟩 |
| arthursonzogni | 2024-10-14 | [PA: link against winmm.lib.](./output/debug/49e7d5b5b0bd7342e469b6ff8a6266a2cfe3c489.log) | 🟩 |
| mikt | 2024-10-11 | [[PA] Add configuration for iOS binary experiment](./output/debug/1d1d7753cd2489252833ab2398ff7b94230aa9ca.log) | 🟩 |
| mikt | 2024-10-11 | [[PA] Put some debug data on stack on cookie corruption](./output/debug/67d020b3b9c6e0674b863786ccbdcb2dde2fea4a.log) | 🟩 |
| mikt | 2024-10-10 | [[PA] Clean-up assuming core pools are glued everywhere](./output/debug/325b94b1de054e716ebe86f796acb8e90fc84b29.log) | 🟩 |
| tasak | 2024-10-10 | [[PA] UnmapShadowMetadata() must be invoked before U...](./output/debug/ece815bd85c86702e994cde9ccd79c02335aa4d5.log) | 🟩 |
| pkasting | 2024-10-10 | [Use three-way comparison when available in Partitio...](./output/debug/4f1c8275f78acb2eabcb441f9f09d17e4c129448.log) | 🟩 |
| mikt | 2024-10-10 | [[PA] Glue core pools on iOS](./output/debug/ce32b10a09cfe6be075b586e2a25959d76a6b647.log) | 🟩 |
| mikt | 2024-10-10 | [[PA] Fix PartitionAddressSpace::RegularPoolSize() i...](./output/debug/6034b95817c2a5d4df72f5772c23fcd59bdb8261.log) | 🟩 |
| pkasting | 2024-10-09 | [Remove bartekn@ as OWNER.](./output/debug/4ac2023e4f7fca06b496a85447a12d53ef5ffaf8.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Add FORCE_DISABLE_BACKUP_REF_PTR_FEATURE build...](./output/debug/5eb3834d17db690156ea257d6cad9452b3dd4b92.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Fix enable_partition_lock_reentrancy_check wit...](./output/debug/cfded4a9ba2fd07e08ed66a8b4a1e3d01db52384.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Add "smaller" partition cookie build option](./output/debug/f4b2dd0e30f90470d5400606d72581d9d910937b.log) | 🟩 |
| mikt | 2024-10-09 | [[PA] Add partition cookie check build option](./output/debug/242f8277ece89fecca2c9561c0d6c7d681fc9a99.log) | 🟩 |
| sorin | 2024-10-09 | [base: eliminate empty parameter list in lambdas whe...](./output/debug/524cf957f0260f857928401ec3502c9ec663c6fa.log) | 🟩 |
| sorin | 2024-10-08 | [base: eliminate empty parameter list in lambdas whe...](./output/debug/1ced11f214ead902b40019f031852137f84827c2.log) | 🟩 |
| mikt | 2024-10-04 | [[PA] Add lock reentrancy check build option](./output/debug/7939e34ad2e5c769f8856957cc7f8166c20bd954.log) | 🟩 |
| mikt | 2024-10-03 | [[MO] Enable Partition Alloc with Advanced Checks su...](./output/debug/b986110c534670f28e49969325ee2ab7eca8b114.log) | 🟩 |
| mikt | 2024-10-02 | [[PA-E] Use FreeFlags::kNoHooks consistently](./output/debug/3c7d09f6032e951cbf837608a3d18396c71dbee9.log) | 🟩 |
| mikt | 2024-10-02 | [[MO] Support more functions in PA with Advanced Checks](./output/debug/9011cae703eb8ee0a1ac431a4ffb10f945458e81.log) | 🟩 |
| danakj | 2024-10-01 | [Disable PA-based features in the Rust host tools to...](./output/debug/2850bbe7e393f36419d1df3c0dbbfcda4403092d.log) | 🟩 |
| jdapena | 2024-10-01 | [GCC: do not add redundant template spec in constructor](./output/debug/ccc8b69a92a8f5472b6359190c17e86c91ce0775.log) | 🟩 |
| arthursonzogni | 2024-09-30 | [PA: check readability-redundant-smartptr-get](./output/debug/d3a666931363ad6ea6ff9e633948a26fe4639530.log) | 🟩 |
| pbos | 2024-09-27 | [Mark TerminateBecauseOutOfMemory [[noreturn]]](./output/debug/eb4c8ad8053e37bc0ca11f19cad1405bc0912676.log) | 🟩 |
| arthursonzogni | 2024-09-27 | [PA: Fix #include for memcpy/memset.](./output/debug/2409a3774b4f25a09c3232af60aa717b2d67aee4.log) | 🟩 |
| marshall | 2024-09-26 | [win: Add missing <limits> include](./output/debug/672834421883ed82745701ef948e27175b0a21cf.log) | 🟥 |
| fdoray | 2024-09-25 | [[partition alloc] Add PA_NOT_TAIL_CALLED to out of ...](./output/debug/6d508e4ef47ae3b932648cef6ccb65f1ce931341.log) | 🟥 |
| fdoray | 2024-09-25 | [[partition alloc] Allow foreground/background empty...](./output/debug/85b0685f68760491b20e634f8370be55bba04795.log) | 🟥 |
| arthursonzogni | 2024-09-24 | [partition_alloc: Stop using anonymous namespace in ...](./output/debug/c97fac45ba2b636db5a7505b656c324a48dd4578.log) | 🟥 |
| tasak | 2024-09-20 | [[PA] Add PartitionAllocShadowMetadata feature](./output/debug/c0fe75b0b5e1bfb65aaf60a5abb8a568da3a5590.log) | 🟥 |
| sergionso | 2024-09-19 | [base: Improve CurrentWallclockMicroseconds() on Win...](./output/debug/7605153ca556d38d81429fcebf53b85fb9fe044e.log) | 🟩 |
| pkasting | 2024-09-18 | [Attempt to improve comments in compiler_specific.h.](./output/debug/fb47d3dad7415dfb71a50c76d38a65085c7105c2.log) | 🟩 |
| pkasting | 2024-09-17 | [More consistent macro definitions in base/compiler_...](./output/debug/ee6bf744537f90293b9e21c9be52b5aa32d2b50e.log) | 🟩 |
| rsworktech | 2024-09-17 | [[PA] Use kPartitionCachelineSize instead of hardcod...](./output/debug/c146ea4f65525c50a0a26eeac8a773e886dbe38c.log) | 🟩 |
| fdoray | 2024-09-16 | [[oom] Add commit limit/available to OOM exception a...](./output/debug/ea476c2c12d824c1c89c36b78903276c5c645bf5.log) | 🟩 |
| pkasting | 2024-09-13 | [Prerequisites for changing macro definitions in com...](./output/debug/ca4487e127c2e071da5d4a36a9f71fd7b65b1434.log) | 🟩 |
| kdlee | 2024-09-13 | [PA: Make `SlotStart` methods const](./output/debug/719c912ed6faac0547b91bd5485ba37e516eb978.log) | 🟩 |
| arthursonzogni | 2024-09-12 | [Reland "PA: Invert MiraclePtr Platform Enablement L...](./output/debug/5576de467696ec80ac16be5daaa9e0ec86eb7564.log) | 🟩 |
| sroettger | 2024-09-10 | [[cfi] Implement PageAllocator::SealPages on Linux](./output/debug/1ae169f5bd37d782c885821ed4e60fe39e711cc8.log) | 🟩 |
| mikt | 2024-09-10 | [[PA] Use dispatch with advanced checks when feature...](./output/debug/9b58a78cc026d3088bf954daadfeec7b294b11d4.log) | 🟩 |
| keishi | 2024-09-10 | [Update apple_apsl/README.chromium](./output/debug/65d4191fc0703d5c3b98d002091c93746be24e9a.log) | 🟩 |
| arthursonzogni | 2024-09-09 | [PA: Stop using `constinit`.](./output/debug/69b922bdaae80e2dfe65b1ca5c5583446e3a582c.log) | 🟩 |
| arthursonzogni | 2024-09-09 | [Revert "PA: Invert MiraclePtr Platform Enablement L...](./output/debug/81ff602c377ade97134a29b681068ee4a2f132f2.log) | 🟩 |
| arthursonzogni | 2024-09-09 | [PA: Invert MiraclePtr Platform Enablement Logic](./output/debug/d81b3b062e4b40432a65225a16a5bb2d1590a8ef.log) | 🟩 |
| arthursonzogni | 2024-09-08 | [PA: Revert "Allow std::hardware_destructive_interfe...](./output/debug/b69741434d0a8a8c6a089255866d1cef7ed48778.log) | 🟩 |
| tasak | 2024-09-06 | [[PA] Fix ShadowMetadata issues](./output/debug/51001c0d0378ce34b34d3d6ce0f9899b4d832bab.log) | 🟩 |
| yzshen | 2024-09-06 | [Remove the old gpu::Scheduler.](./output/debug/cff0048aa56a0ac7bf4da8009679b877500af6fa.log) | 🟩 |
| pkasting | 2024-09-04 | [Allow (and use) std::hardware_destructive_interfere...](./output/debug/dbd5fd7ca188b19955dd6fd221a44f79efc39998.log) | 🟩 |
| yukishiino | 2024-09-04 | [PA: Minor tweaks on LightweightQuarantine](./output/debug/18e11e59adc3bf1407bc8433b7cf9cc8c3503867.log) | 🟩 |
| arthursonzogni | 2024-09-04 | [PartitionAlloc: stop depending on "defined(ANDROID)"](./output/debug/21f94456b3ec9d432075dc1d0aeba26d955871a9.log) | 🟩 |
| tasak | 2024-09-02 | [[PA] Split SlotSpanMetadata into read-only one and ...](./output/debug/d0b9630d2515effb20b939cb5e526f8e0b5fd5f1.log) | 🟩 |
| arthursonzogni | 2024-09-02 | [PA: Fix compile error encountered on Skia.](./output/debug/a2ce75ec98d94852baada5d6d98e6b1050099e38.log) | 🟩 |
| kdlee | 2024-08-30 | [PA: Upgrade `DCheckIsValidSlotSpan()`](./output/debug/774e27628835d8580f58b420a6b2b608f22db3c2.log) | 🟩 |
| pkasting | 2024-08-29 | [Switch from `ALIGNAS()` to `alignas()`.](./output/debug/4419c7daa9cc1e08af8769d0bb2314f9c7dfca27.log) | 🟩 |
| tasak | 2024-08-27 | [[PA,shim] Fix compile error of allocator_shim_..._w...](./output/debug/60162d5aab8ebd147e04889e2d56a2f33e0b0adb.log) | 🟩 |
| keishi | 2024-08-23 | [[MTE] Fix tagging after r1344621](./output/debug/9513f560d7de3d8afb6c742e0641c32e56bd22cc.log) | 🟩 |
| pkasting | 2024-08-22 | [Move arch-specific feature macros to build_config.h.](./output/debug/1ca611f5fd7838eae38927063b5e30f35e0b20f3.log) | 🟩 |
| bwwilliams | 2024-08-22 | [Strengthen Warning Enforcement for Assignments in C...](./output/debug/995176567d7c95dfdfa5862cb743bb811d942b41.log) | 🟩 |
| tasak | 2024-08-22 | [[PA,shim] Support allocator_shim on Windows debug b...](./output/debug/bcebe831fd166b7540502cbc3d4a2ba763047c78.log) | 🟩 |
| pkasting | 2024-08-22 | [Remove [UN]LIKELY().](./output/debug/97be0f3c5b04f1d2fda3d4e3e3d585868eb77efd.log) | 🟩 |
| keishi | 2024-08-21 | [[MTE] Do retagging right before RawFreeWithThreadCa...](./output/debug/81cccdaee388163b04970911891f5a6349e19bbc.log) | 🟩 |
| tasak | 2024-08-21 | [[PA] Split PartitionPageMetadata into read-only one...](./output/debug/a07ce06347ac8ac1540b6d08e86194c3e8c37a6a.log) | 🟩 |
| keishi | 2024-08-15 | [Remove *Scan settings related code](./output/debug/cf28c12c0a65f752691ba60583dcfeb84dc84518.log) | 🟩 |
| sky | 2024-08-15 | [pa: puts buildflags in public_deps](./output/debug/8b28072c61a1152b0b7eb0c506d00b24535a47bb.log) | 🟩 |
| tasak | 2024-08-09 | [[shim] Move kPartitionAllocDispatch into another he...](./output/debug/1515d142bda42bc4f6364e2fa11cb79f9014c3cd.log) | 🟩 |
| yukishiino | 2024-08-08 | [PA: Remove the self pointer from shim functions](./output/debug/091b58c775288e29d03ba6776bfa0e444c0b27c7.log) | 🟩 |
| pkasting | 2024-08-07 | [Switch to [[(un)likely]]: .../partition_alloc/](./output/debug/d374cbc2685c6354f1eda1bdd1be0c3ee45f009d.log) | 🟩 |
| tasak | 2024-08-07 | [[PA] Support PartitionAlloc-Everywhere on Windows c...](./output/debug/c362d7a79a023b0693f872527b9d7c1077eb2fd4.log) | 🟩 |
| pkasting | 2024-08-06 | [Switch to [[(un)likely]]: .../partition_alloc_base/](./output/debug/a5626351a84e33d5fee2a5906be9dc85a242aa8e.log) | 🟩 |
| tasak | 2024-08-06 | [[PA] Split PartitionSuperPageExtentEntry into read-...](./output/debug/54cdf4e94899d81db9dd367228300754301f5fd0.log) | 🟩 |
| olivierrobin | 2024-08-02 | [Mark TimeTicks::UnixEpoch deprecated](./output/debug/be025bf066fd720e53fed43ad7906e4b278e85ef.log) | 🟩 |
| derinel | 2024-08-02 | [Add IWYU statement for base::raw_ptr](./output/debug/813f717135e29158905bff102e6261499bb93106.log) | 🟩 |
| mikt | 2024-08-01 | [[PA/shim] Add a new dispatch to switch malloc backe...](./output/debug/be977e0d870ad3d6db2dd92d6076cfe4908db7eb.log) | 🟩 |
| yukishiino | 2024-08-01 | [PA: Fix ineffective PA_UNLIKELY applied to do ... w...](./output/debug/e41031670a9c4a93549ba0f672d2ed3367d9fcac.log) | 🟩 |
| keishi | 2024-07-31 | [[MTE] Use a random value to update a tag](./output/debug/581d48913faf389f935ecb0be5a75fa5f789a4b2.log) | 🟩 |
| dloehr | 2024-07-30 | [Remove uses of variable-length arrays](./output/debug/9930a27ceca75a0d831b0bd1098add097d352aa1.log) | 🟩 |
| tasak | 2024-07-30 | [[PA] Remove unused kCookie from PartitionAllocDeath...](./output/debug/6eb5e6cf980ae8ceee135e5ccd0638a01a9948e9.log) | 🟩 |
| tasak | 2024-07-30 | [[PA] Split DirectMapExtentMetadata into read-only o...](./output/debug/0627742f7ee966d5ab4547963941a2224911083f.log) | 🟩 |
| tasak | 2024-07-26 | [[PA] Deflake PartitionAlloctest.CheckeReservationTy...](./output/debug/540ef1d89bfb64f8078919854dfed17b0ca9deaa.log) | 🟩 |
| arthursonzogni | 2024-07-25 | [partition_alloc: Cleanup never called functions.](./output/debug/6a94c13fbac1e24eaa64161f58e9f566cc965d54.log) | 🟩 |
| tasak | 2024-07-25 | [[MTE] Fix flaky BackupRefPtrTest.GetDeltaElems fail...](./output/debug/bd54734c0467af9fb4ff3610578718d6869f5a38.log) | 🟩 |
| arthursonzogni | 2024-07-24 | [partition_alloc: Disable MTE for benchmark use to a...](./output/debug/561c0d214fe68a31a0fed180ccc8e5bf090b6bbe.log) | 🟩 |
| mikt | 2024-07-24 | [[PA] Optimize IsManagedByPartitionAlloc()](./output/debug/91610144c44e3e96f33b7acd72609d84744a4de1.log) | 🟩 |
| tasak | 2024-07-24 | [PA: Fix EncodedPoolOffset::Encode().](./output/debug/877eaedbfd0c5e851d4f63ff2cbf659bdf036446.log) | 🟩 |
| keishi | 2024-07-23 | [[MTE] Disable MTE during StackCopier::CopyStackCont...](./output/debug/0abdba1e1048de44c4d9d112d48afaf96a14f441.log) | 🟩 |
| mikt | 2024-07-12 | [[PA/*Scan] Remove StarScan](./output/debug/b0cb752ab120cb7c5b46e6612eb7597f7b4153e8.log) | 🟩 |
| arthursonzogni | 2024-07-11 | [partition_alloc: remove cpu_features:ndk_compat dep...](./output/debug/f085b61ade6a84bc24bedcc2d381a4a558431e9c.log) | 🟩 |
| yukishiino | 2024-07-11 | [PA: Add PA_UNLIKELY to allocation failure handlers](./output/debug/29179883f32e3ea25f199238befdd1a09d488f37.log) | 🟩 |
| yukishiino | 2024-07-11 | [PA: Let LightweightQuarantineBranch.Quarantine() ta...](./output/debug/0c714aaffcedd7a77562578e51ef3e2e427a1f4b.log) | 🟩 |
| kdlee | 2024-07-11 | [PA: Precalculate Mac alignment kludge](./output/debug/4188dcd78c5267eacb3c0364f8e580898972c9cb.log) | 🟩 |
| arthursonzogni | 2024-07-10 | [partition_alloc: Use PA_CONSTEXPR_DTOR](./output/debug/2e6b2efb6f435aa3dd400cb3bdcead2a601f8f9a.log) | 🟩 |
| mikt | 2024-07-09 | [[PA/shim] Guarantee tail call optimization](./output/debug/575f1a0af46e358b4cdd6b3769caa754bf720bcb.log) | 🟩 |
| arthursonzogni | 2024-07-09 | [partition_alloc: Follow-up moving tests.](./output/debug/f83b78cb7dc3363149149725b62876efcc995f89.log) | 🟩 |
| arthursonzogni | 2024-07-08 | [partition_alloc: Check support for C++17](./output/debug/880ba2b2e2121f4c37c87b61cd7bd4659fa7690d.log) | 🟩 |
| jdapena | 2024-07-08 | [IWYU: add again required missing include for Histog...](./output/debug/fd1ad7b90ad02af8d2993c2e757b7615dcc1cff7.log) | 🟩 |
| arthursonzogni | 2024-07-08 | [partition_alloc: support cpp17](./output/debug/0ab14762072efc3c894aeebdd1b8578a74b99cda.log) | 🟩 |
| arthursonzogni | 2024-07-05 | [Reland #2 "partition_alloc: Move pa tests into pa.""](./output/debug/36601cb520f4749418d0737cc65ecfda7ddb7500.log) | 🟩 |
| danakj | 2024-07-05 | [Make all allocation routines from Rust fallible whe...](./output/debug/824fb852dc756ae4347d37779d0a7e8e67c04199.log) | 🟩 |
| arthursonzogni | 2024-07-05 | [partition_alloc Fix violations of the PRESUBMIT](./output/debug/c0d55ba698b669900208466f858a9eee93d5ec0f.log) | 🟩 |
| arthursonzogni | 2024-07-05 | [Revert "Reland "partition_alloc: Move pa tests into...](./output/debug/3508fb8a67265256667e6e0586f9b2dcce7ecda9.log) | 🟩 |
| arthursonzogni | 2024-07-04 | [Reland "partition_alloc: Move pa tests into pa."](./output/debug/feb5861c7ee60df986d446ee84ff8b00c90924f3.log) | 🟩 |
| titouan | 2024-07-04 | [Revert "partition_alloc: Move pa tests into pa."](./output/debug/f1888f8b851999367d99c83277527bddfbeef1d0.log) | 🟩 |
| arthursonzogni | 2024-07-04 | [partition_alloc: Move pa tests into pa.](./output/debug/0abbaa1cc0759915e1234da4956ca8b4b231445c.log) | 🟩 |
| tpearson | 2024-07-03 | [partition_alloc: Use 64k pages for ppc64 partition ...](./output/debug/22ca21545058c5fbef24f54c1b1c16ac7ed82590.log) | 🟩 |
| danakj | 2024-07-03 | [Reland "Reland "Reland "Reland "Add toolchains with...](./output/debug/69258b7057b6cf183695ba8e2d6160edcd03d50e.log) | 🟩 |
| mjwilson | 2024-07-02 | [Revert "Reland "Reland "Reland "Add toolchains with...](./output/debug/dc397419b98dc37a18c55a4bcefc43eb30189097.log) | 🟩 |
| danakj | 2024-07-02 | [Reland "Reland "Reland "Add toolchains without Part...](./output/debug/37fa7c1ca9b94e63dc969a69668bcd53d89657e8.log) | 🟩 |
| tpearson | 2024-07-02 | [partition_alloc: Autodetect page size on ppc64 systems](./output/debug/12d49fbf174022a0e5275d87ef9e3c71c3f05547.log) | 🟩 |
| tpearson | 2024-07-02 | [partition_alloc: Allow variable page sizes on ppc64...](./output/debug/24f50b3bd0e30b804855b24c0125e93f7a197d20.log) | 🟩 |
| casey.smalley | 2024-07-01 | [Add support for 64K pages on Linux/AArch64](./output/debug/43ae3905f7007916c04d92fb92fc8167dc2e469f.log) | 🟩 |
| bartekn | 2024-07-01 | [[PA] Enable glue_core_pools](./output/debug/7ac10c8f375123fd71ace5038c27b8fa77b69ed8.log) | 🟩 |
| kdlee | 2024-07-01 | [PA: Untag pool offset freelist entries](./output/debug/0eb0d6bfeba06d4adbae9d82512acc7b565454b2.log) | 🟩 |
| danakj | 2024-06-28 | [Test realloc in the realloc test](./output/debug/89101f0456b29a762c3d4c4e2e85491dd989d225.log) | 🟩 |
| tpearson | 2024-06-28 | [partition_alloc: Prioritize non-constant POSIX page...](./output/debug/773457d3f3772c646a07e59a23758039bcc50089.log) | 🟩 |
| tarcisio.fischer | 2024-06-26 | [Enable MTE by default on ConfigurePartitionsForTesting](./output/debug/45a05505a83e303d704fe088dc01e568bf33e038.log) | 🟩 |
| lizeb | 2024-06-26 | [[PartitionAlloc] Purge more buckets from time to ti...](./output/debug/be8e0bd57d74a7031a7b1e0decd782d3601dd623.log) | 🟩 |
| arthursonzogni | 2024-06-26 | [partition_alloc: merge buildflags.h #cleanup](./output/debug/2d3ec4ceaf5fce669fde51e187f3559a30832f0a.log) | 🟩 |
| wyeager | 2024-06-26 | [Revert "Reland "Reland "Add toolchains without Part...](./output/debug/c29d2bc0167380bd0b0cef6274cd3e7cd02dd9b9.log) | 🟩 |
| arthursonzogni | 2024-06-25 | [PA: Minimize DEPS for tests.](./output/debug/c718a2c1cc43cf34ea6422d64ad14d3d24595635.log) | 🟩 |
| arthursonzogni | 2024-06-25 | [partition_alloc: Fix and simplify SpinningMutex.](./output/debug/c1d59d0456ffb430742563e18f461e8065e40cad.log) | 🟩 |
| danakj | 2024-06-24 | [Reland "Reland "Add toolchains without PartitionAll...](./output/debug/8cdb01ad13cef64377e510814dafa2ca32eea2f7.log) | 🟩 |
| lukasza | 2024-06-24 | [s/ `std::unique_ptr<char[]>` / std::vector<char> / ...](./output/debug/770d1a5a8a4a16f24a002cc51a4f2af4f68152c5.log) | 🟩 |
| bartekn | 2024-06-21 | [[BRP] Test raw_ptr::operator=(T* ptr) when assigned...](./output/debug/efb545e8823213f553fdcb3b0c6af5b8ca5aefa2.log) | 🟩 |
| arthursonzogni | 2024-06-19 | [partition_alloc: #cleanup unnecessary PA_ prefix](./output/debug/26b47cb849db9fbb0a89f1691efd0659f2d832ba.log) | 🟩 |
| bartekn | 2024-06-18 | [[BRP] Handle case where raw_ptr::operator=(T* p) ge...](./output/debug/3c8b6517c927396a3c9767d488aa8af73d4467e9.log) | 🟩 |
| lizeb | 2024-06-18 | [[base/allocator] Add documentation about discard vs...](./output/debug/f7d9f07348e454ed3e7ec3d6e8acf24388750e18.log) | 🟩 |
| kdlee | 2024-06-17 | [PA: Add `SlotStart` death test](./output/debug/16c47e1a56f460b190083a114d39871e917c8492.log) | 🟩 |
| bartekn | 2024-06-17 | [[PA] Fix BUILDFLAG->PA_BUILDFLAG under #if](./output/debug/b7d5ab0f5fa14c0981c6ffe5afbcfb5adc728d6b.log) | 🟩 |
| kdlee | 2024-06-13 | [PA: Enable freelist dispatcher](./output/debug/7864cdced1d6ee0aae78768a808dd798480d76f0.log) | 🟩 |
| bartekn | 2024-06-13 | [Remove USE_ASAN_UNOWNED_PTR](./output/debug/35643f54fd6309713d96266a17543e1e04dcc846.log) | 🟩 |
| kdlee | 2024-06-13 | [PA: Adjust corruption test](./output/debug/2d4fa48c99b41f38c6df296b87954be94c8ee2f6.log) | 🟩 |
| kdlee | 2024-06-13 | [PA: Hide GN arg](./output/debug/db10b18b633a65ea10d649b533d6848dbe7e4224.log) | 🟩 |
| bartekn | 2024-06-12 | [[PA] Work around Adreno-GSL mmap address conflict](./output/debug/4b46ebdc43523f7f6ec2e8e6dbc151293ad115c5.log) | 🟩 |
| kdlee | 2024-06-12 | [PA: Remove `TaggedSlotStart`](./output/debug/a1a8f60c590447fd1f9a93235c6e3552c462c549.log) | 🟩 |
| kdlee | 2024-06-12 | [PA: Add `SlotStart::{From,To}Object()`](./output/debug/d5c2aacddbf420bc6385d4b3bc2b2afdcdbda1bd.log) | 🟩 |
| kdlee | 2024-06-10 | [PA: Adjust bucketing comment](./output/debug/402d95788326f22ba4d06846d983bcb44da0fa07.log) | 🟩 |
| kdlee | 2024-06-07 | [PA: Return slot size from `MaybePutInCache()`](./output/debug/ebfce4880cbffeea184c5b8e1ab0c7227878b7f3.log) | 🟩 |
| kdlee | 2024-06-04 | [PA: Introduce `SlotStart` type](./output/debug/596919c38e416762842d3dabfeca9795de390f43.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [partition_alloc: Remove unused files.](./output/debug/4bc9d0c84a830f8883ad6558e54b2b3c3072583b.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [partition_alloc: Remove temporary exception for bui...](./output/debug/7013d1fbc8ae4a63addb2d8b3809290649469f20.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [Partition Alloc: Cutting the Cord!](./output/debug/ae870b571ec44a11de1bb2eba3376ad41779b5d1.log) | 🟩 |
| arthursonzogni | 2024-06-04 | [partition_alloc: Check no external dependencies in GN.](./output/debug/195dd3d1a28e04dfe8a50d9911414a7f75fa0038.log) | 🟥 |
| kdlee | 2024-06-04 | [PA: Introduce `ObjectToSlotStartUnchecked()`](./output/debug/b06c973eedc38f49bdfc18c3f594dd4f0e9cea77.log) | 🟥 |
| arthursonzogni | 2024-06-03 | [partition_alloc: Stop using chromium's build_config...](./output/debug/8d08a407ab68da324863ebc274f20fefc4713e78.log) | 🟥 |
| arthursonzogni | 2024-06-03 | [PA: Stop depending on `IS_CHROMEOS`.](./output/debug/77aad2ab99d3b15766dac04552911da4d892a08a.log) | 🟥 |
| arthursonzogni | 2024-06-03 | [partition_alloc: provide build_config.h](./output/debug/b99a401f457eb03adae9c873c835a5ab736d126a.log) | 🟥 |
| kdlee | 2024-06-03 | [PA: Adjust `PA_USE_DEATH_TESTS()`](./output/debug/89029ef39983240e0d9834340c5bf56c3f219868.log) | 🟥 |
| lizeb | 2024-05-31 | [[PartitionAlloc] Do less work in fast MemoryReclaim...](./output/debug/4e54cefb1472e8fa0e4e120266c57b716c7f4cbc.log) | 🟥 |
| arthursonzogni | 2024-05-30 | [partition_alloc: remove -Wl,--start-group, --end-group](./output/debug/f941becc7efa75971aa4e83d0cd3217f4f1ef57f.log) | 🟥 |
| lizeb | 2024-05-30 | [[PartitionAlloc] Add a feature capping memory recla...](./output/debug/e9b1e467c32d80a904df8efddb8ed542aaf8171d.log) | 🟥 |
| arthursonzogni | 2024-05-30 | [Define partition_alloc standalone GN config.](./output/debug/087911ce77bce70f277fda09e10db56fe577ed53.log) | 🟥 |

</details>

