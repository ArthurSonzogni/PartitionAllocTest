# PartitionAlloc standalone CI

Unofficial CI for the [PartitionAlloc](https://chromium.googlesource.com/chromium/src/base/allocator/partition_allocator.git) **standlone** project, which is a memory allocator used in Chromium, Pdfium, Dawn, V8, Skia (WIP), Angle(Soon), ...

## Build Results

<details>
<summary>✅ Configuration: `debug`</summary>

| Email | Date | Title | ? | Log |
|---|---|---|---|---|
| arthursonzogni | 2025-07-15 | partition_alloc: Resolve C++20 compile errors. | ✅ | [log](./output/debug/328d516729e7e9edc833244c73cc9013828e5a1a.log) |
| thakis | 2025-07-14 | Remove remaining __pnacl__ and __native_client__ in... | ❌ | [log](./output/debug/7b2807165fad397df23f5f749b15e9e43269ccf5.log) |
| tikuta | 2025-07-09 | base: Remove references to BUILDFLAG(IS_NACL) | ❌ | [log](./output/debug/a54ac8d0dd78019fb41d2e376726d45b287e856b.log) |
| lizeb | 2025-07-09 | [PartitionAlloc] Use fewer VMAs by default on Linux... | ❌ | [log](./output/debug/db340435e8d7e8eb89925d3006ecaf6427e3ab4f.log) |
| mikt | 2025-06-27 | [PA] Fix pool offset freelist DCHECK with MTE | ❌ | [log](./output/debug/79b418050876e0c4187a80f668e81ce956b32bf2.log) |
| lizeb | 2025-06-26 | [base/allocator] Remove launched features | ❌ | [log](./output/debug/11aaded5a31dc53a08781ca47f146f3795d021c4.log) |
| mikt | 2025-06-25 | [PA] Add callback for DoubleFreeDetected or Corrupt... | ❌ | [log](./output/debug/3d6e246fc6014fd3f9f850876eae0fcd8f97921e.log) |
| thiabaud | 2025-06-25 | [partition_alloc] Add more threading annotations | ❌ | [log](./output/debug/983d556a9aed36814954a4463bb0b508d2af133a.log) |
| tikuta | 2025-06-24 | partition_alloc: Add a missing include for std::ignore | ❌ | [log](./output/debug/f8a48647751d44a0497a76633f6dc22ab28f51ad.log) |
| tasak | 2025-06-23 | [PA] Make PartitionAllocMemoryAllocationPerfTest hu... | ❌ | [log](./output/debug/85594a8469649294d3b365e0637256a87dc74602.log) |
| dcheng | 2025-06-20 | base: remove NaCl from BUILD.gn, as well as NaCl-on... | ❌ | [log](./output/debug/9b8de412d87c20117d2d04836bc5fa85866eaa08.log) |
| mikt | 2025-06-18 | [PA] Add option not to crash on Double-Free or Corr... | ❌ | [log](./output/debug/ffa6d285560e810ab57e9a026b58f0a722658a6a.log) |
| bikineev | 2025-06-18 | PA: Fix an include to be relative to PA source dir | ❌ | [log](./output/debug/a28c3c3d01412a17ebf145bfe2d73c8071c686e3.log) |
| rop | 2025-06-17 | LSC Add 'Update Mechanism:' to README.chromium | ❌ | [log](./output/debug/49c08e7ea1746f671ce75b96f6ca444f6d6065ab.log) |
| avi | 2025-06-12 | Update MacOSVersion() for macOS 26 | ❌ | [log](./output/debug/73de62811794a78ccb95ed3e197180ec8fb666c2.log) |
| thiabaud | 2025-06-09 | [partition_alloc] Add threading annotations | ❌ | [log](./output/debug/50a84f34499cdfdc040a9d2c8fc1f031d31bbc78.log) |
| fdoray | 2025-06-06 | [partition_alloc] Add mechanism to terminate a proc... | ❌ | [log](./output/debug/a585fc502ffa23ddce3412973eba2fe677325f02.log) |
| kdlee | 2025-06-05 | PA: Remove seam code for 4S | ❌ | [log](./output/debug/76e5e3ac91101d2976805205fb51585c266e548f.log) |
| thestig | 2025-06-05 | [PA] Use PA_LOG() instead of LOG() | ❌ | [log](./output/debug/37c90018cca427ce66d7f2fc3f43fca9d6ee9b6b.log) |
| mikt | 2025-06-03 | [PA] Optimize Purging mechanism for Scheduler-Loop ... | ❌ | [log](./output/debug/e3668842ccb3173913161900ec731508f0655604.log) |
| mikt | 2025-06-03 | [PA] Replace usable_size with slot_size in Schedule... | ❌ | [log](./output/debug/b1a4a44e2310b4661acf418a3524778969943919.log) |
| mikt | 2025-06-03 | [PA] Do Scheduler-Loop Quarantine after BRP Quarant... | ❌ | [log](./output/debug/b95054240369556471d5c438217480a23089aa4a.log) |
| mikt | 2025-06-03 | [PA/E-LUD] Refactor: Fork LightweightQuarantine | ❌ | [log](./output/debug/ffb614650932ce01003b1f1cbf26c1709f68c364.log) |
| hans | 2025-05-30 | Mark pointer in PartitionAllocPageAllocatorTest.Dec... | ❌ | [log](./output/debug/d617778ed253822ee4c1bb9d03826f01e5f09e32.log) |
| avi | 2025-05-29 | Remove the macOS 11 malloc size hack from Partition... | ❌ | [log](./output/debug/3ae30e4cf9d6f59ba825dcc96af9940ab35bf27b.log) |
| nuskos | 2025-05-29 | Use std::array instead of a c style array in PurgeP... | ❌ | [log](./output/debug/a160ae6759caac1e19e3bf51b3660b649a9aba2e.log) |
| mikt | 2025-05-28 | Reland "[PA] Cache ReservationOffsetTable instead o... | ❌ | [log](./output/debug/964c6996d56bd2167f4f6fdb2d88acfeba32c5d8.log) |
| caseq | 2025-05-28 | Remove redundant std::max(x, x) | ❌ | [log](./output/debug/e85940b94442a391f6b528d9202e8c66eaca87be.log) |
| mpdenton | 2025-05-27 | GWP-ASan: raise kMaxMetadata and kMaxRequestedSlots | ❌ | [log](./output/debug/f44457d2f971ec0a45c271e093b6aa56044d0ec1.log) |
| jonross | 2025-05-21 | Revert "[PA] Cache ReservationOffsetTable instead o... | ❌ | [log](./output/debug/c858ce950cf900f168772e5e7c8f7cfa3e66ce96.log) |
| mikt | 2025-05-20 | [PA] Cache ReservationOffsetTable instead of lookup... | ❌ | [log](./output/debug/29111157f1454c5a52fe83c7da9f57cb07a35b82.log) |
| mikt | 2025-05-18 | [PA/shim] Fix shim test failure on mac component build | ❌ | [log](./output/debug/57f3d1311ce54e7c528608f2df77951920903451.log) |
| tikuta | 2025-05-15 | base: Disable libc++ modules build in partition all... | ❌ | [log](./output/debug/1d9d02e434059dbdb74e10e28ad42fd97c25a85c.log) |
| tasak | 2025-05-14 | [PA] Remove libc++ string object dependency from al... | ❌ | [log](./output/debug/269b4081447bcef3f64ad87116d9c6d8cfcf4645.log) |
| thestig | 2025-05-14 | Clean up PA's instance_tracer.h | ❌ | [log](./output/debug/299f793686af3b7ea3facf647464a15622c27466.log) |
| mikt | 2025-05-14 | [PA] Fix PoolOffsetLookup for Configurable Pool | ❌ | [log](./output/debug/fc79edffac58c4d59925412bf378eaf0f454688e.log) |
| mikt | 2025-05-12 | [PA] Cache PoolInfo instead of lookup by address | ❌ | [log](./output/debug/f0e2e7a786cda3a52feaff9c7894ebcf68b13fb3.log) |
| thestig | 2025-05-07 | Remove <ostream> from PA's safe_conversions.h | ❌ | [log](./output/debug/2b1d9301c925673637b3ff6e6412686ecfe66d02.log) |
| antoniosartori | 2025-05-07 | Revert "gardening: Disable PartitionAllocPageAlloca... | ❌ | [log](./output/debug/60903e2555a42eeac93dc7c91eedbca746943842.log) |
| yukishiino | 2025-05-06 | gardening: Disable PartitionAllocPageAllocatorTest.... | ❌ | [log](./output/debug/988f84a803953c0874cffadcb0ded36ba174582c.log) |
| mikt | 2025-05-06 | [PA/docs] Update buckets.md | ❌ | [log](./output/debug/5c18e6e9b5fc4cb6748df24c2f63003e8ad3b81e.log) |
| dloehr | 2025-05-06 | Exported things should always be visible | ❌ | [log](./output/debug/843601306bff485f15960ef0c7b23dd34e2d7ee5.log) |
| mikt | 2025-05-02 | [PA] Remove Freelist Dispatcher | ❌ | [log](./output/debug/196ca28d1e516424ab24d9a798e13473895f8b71.log) |
| mikt | 2025-05-02 | [PA] Remove free slot bitmap | ❌ | [log](./output/debug/93234db35d91c7af0ff75025fc4be90cc99dfcb9.log) |
| tasak | 2025-05-02 | [PA] Replace std::unordered_map with base::flat_map | ❌ | [log](./output/debug/3a86115ff7330669c596355e7d7786703d4f2082.log) |
| mikt | 2025-05-01 | [PA] Remove unused free functions | ❌ | [log](./output/debug/971c92b116187e9f5ebe2e3c84cf84b04161edbe.log) |
| mikt | 2025-05-01 | [PA] Remove unchecked freelist iteration | ❌ | [log](./output/debug/2686355087336647c1d9aa5579eed6836dd71617.log) |
| nuskos | 2025-05-01 | Reland "spanification: remove `#pragma allow_unsafe... | ❌ | [log](./output/debug/84e59bb4cda4ba071548ede290d44fcfa44f1a42.log) |
| mikt | 2025-05-01 | [PA] Simplify bucket lookup | ❌ | [log](./output/debug/1397a7c24bc0e506cb7bfa2b5eaac48c144f7540.log) |
| luci-bisection | 2025-05-01 | Revert "spanification: remove `#pragma allow_unsafe... | ❌ | [log](./output/debug/afa6432ee9ba7108018c52f8f8e68cc84d2f3370.log) |
| nuskos | 2025-05-01 | spanification: remove `#pragma allow_unsafe_buffers... | ❌ | [log](./output/debug/46f7b646565a2f60129a68806b8615347556a08b.log) |
| mikt | 2025-05-01 | [PA] Remove ZERO_RANDOMLY_ON_FREE | ❌ | [log](./output/debug/a0068b7420952f0093c6149796d81039284e888c.log) |
| wangqing-hf | 2025-04-29 | [PA] Add stack scan supported for loongarch64. | ❌ | [log](./output/debug/b6a1dfdeb69381c36187ce9e7a4e9f24ec1a9065.log) |
| mikt | 2025-04-29 | [PA] Check ThreadCache validity in DoubleFreeOrCorr... | ❌ | [log](./output/debug/5ce629459a2c3b6ef5f56490805cd26169ac6969.log) |
| tasak | 2025-04-29 | [PA] Copy base/containers/flat_{map,tree}.h to part... | ❌ | [log](./output/debug/4170769c13d02df7bcff9a90112f36ed552dcf3b.log) |
| mikt | 2025-04-28 | [PA] Scoped Scheduler-Loop Quarantine opt-out | ❌ | [log](./output/debug/2d19fedeb02734e543c21c46b966835ce217ceea.log) |
| abhijeet | 2025-04-24 | [tvOS][base_unittests] Replace host_info with sysct... | ❌ | [log](./output/debug/862506deb382f3f8a8fa9689c8d5136a48e9b778.log) |
| mikt | 2025-04-24 | [PA] Remove ghost of alternate bucket distribution | ❌ | [log](./output/debug/b6040b2b33d28d064c2167c878deed3b49e4aeb2.log) |
| smaier | 2025-04-23 | Roll Android NDK to r28 | ❌ | [log](./output/debug/a9ae8c0fd665f61acca4633d828a1061fbd461cc.log) |
| mikt | 2025-04-23 | [PA/shim] Support sized-delete | ❌ | [log](./output/debug/d691f607f29e8ca39c37917be7a69629f80a0dbd.log) |
| tasak | 2025-04-22 | [PA] Fix wrong includes. | ❌ | [log](./output/debug/a5083e082d03f4f7d3b0ee35df7cfa3e2ccf8680.log) |
| tasak | 2025-04-20 | [PA] Fix PartitionAlloc windows component build | ❌ | [log](./output/debug/471d99073bd4a042dd17aed9fb7604a6c3277ad9.log) |
| anandrv | 2025-04-17 | [PartitionAlloc] Enable priority inheritance in Spi... | ❌ | [log](./output/debug/21fe3be95a6c4372f6b3e467c05be49f8cd5279f.log) |
| mikt | 2025-04-16 | [PA] Refactor: move Scheduler-Loop Quarantine relat... | ❌ | [log](./output/debug/94efd06f8629f3ee91888150d16d2c2fafd898a5.log) |
| thestig | 2025-04-14 | Forward declare base::NoDestructor in headers when ... | ❌ | [log](./output/debug/4b0f19307639826f8fca1a41882781540ff2fb50.log) |
| lizeb | 2025-04-09 | [base/allocator] Add aligned_alloc to shims on Android | ❌ | [log](./output/debug/932177a9b8f06e7f478fcb22ac7b7184908738a8.log) |
| lizeb | 2025-04-09 | [PartitionAlloc] Make ENOMEM issues have a separate... | ❌ | [log](./output/debug/5144c01d94d24360ec0cecb91319bde84e9acec7.log) |
| dloehr | 2025-04-08 | Change expected message in nocompile test | ❌ | [log](./output/debug/2041003ba674f918c33b1afaaad74e652f34bcea.log) |
| lizeb | 2025-04-08 | [PartitionAlloc] Crash in AddressPoolManager when d... | ❌ | [log](./output/debug/836a8ac2ba51ad26527eee243edda043586f7390.log) |
| mikt | 2025-04-07 | Reland "[PA] Disable BRP zapping on iOS" | ❌ | [log](./output/debug/799310f3bf7d3cdbee28a086035eefc38732b548.log) |
| dtapuska | 2025-04-04 | [ios blink] Add support for arm64e target | ❌ | [log](./output/debug/4cc11b45843b513ee6cd469c21dde9c607624865.log) |
| ginnyhuang | 2025-04-04 | Revert "[PA] Disable BRP zapping on iOS" | ❌ | [log](./output/debug/20e84b3ed75698f1fb19149a640573f2bd420195.log) |
| mikt | 2025-04-04 | [PA] Disable BRP zapping on iOS | ❌ | [log](./output/debug/5a43d8f11eeef195a27b6f0d4373e1a4f1a53581.log) |
| ritownsend | 2025-04-03 | chore: migrate ritownsend OWNERS/TODOs | ❌ | [log](./output/debug/3ef26d8c8a8886277a41d4ae1e9d1801320eb274.log) |
| mikt | 2025-04-02 | Reland "[PA] Add base::CheckHeapIntegrity to invest... | ❌ | [log](./output/debug/53e916ce2c2835fbe66f639a1c4a8a010efa0514.log) |
| tasak | 2025-03-31 | [PA] Split DoubleFreeOrCorruptionDetected into Doub... | ❌ | [log](./output/debug/a9e3cecf8ea5c8da254d98bab323142e17229b0c.log) |
| dloehr | 2025-03-28 | Export things to prevent accidental duplication | ❌ | [log](./output/debug/ab56923a27b2793f21994589b0c39bc3324ff49f.log) |
| wcwang | 2025-03-25 | Revert "[PA] Add base::CheckHeapIntegrity to invest... | ❌ | [log](./output/debug/01d2444accdc1f985d3cfd0c512222de507eb3a4.log) |
| wcwang | 2025-03-25 | Revert "[PA] Fix compile failure in PartitionRoot::... | ❌ | [log](./output/debug/771d9b82c8daa8f1ae68cb33c5a1c3c8cfaf1267.log) |
| mikt | 2025-03-24 | [PA] Fix compile failure in PartitionRoot::CheckMet... | ❌ | [log](./output/debug/13a351f4d27353ed972aa4fc37104d872ed576dd.log) |
| mikt | 2025-03-24 | [PA] Add base::CheckHeapIntegrity to investigate co... | ❌ | [log](./output/debug/c381bec7b1db2e8aec822a8a6217736f4d70cc9c.log) |
| justincohen | 2025-03-21 | ios: Correct gwp_asan_unittests out of memory | ❌ | [log](./output/debug/0abfd4c40e8124de0d14f0d95f5bfe9a4ddd8a8b.log) |
| pmeuleman | 2025-03-20 | Deactivate MTE in HWASan builds | ❌ | [log](./output/debug/df5d4c1b2bdc8d18253cec8a3be4e0fa9194a2bb.log) |
| lokokung | 2025-03-18 | [wasm] Adds rudimentary support for WASM/Emscripten... | ✅ | [log](./output/debug/fb60666cb1896901bb14a5feb10001d20c8833c3.log) |
| mikt | 2025-03-07 | [PA] Add EnsureThreadCache() for blocking thread ca... | ✅ | [log](./output/debug/d3191727ef81ba9daefb0bd3b90d9e4043a4bfa1.log) |
| mikt | 2025-02-27 | [PA] Add unittest to verify extra extras protecting... | ✅ | [log](./output/debug/46d880ff62f340854a5a70142b0abf604c7af221.log) |
| jbroman | 2025-02-24 | Remove an unused include of <unistd.h> | ✅ | [log](./output/debug/bd46928f4b41532c457fa8834ab56d729f4c6c67.log) |
| arthursonzogni | 2025-02-20 | PA: Fix compilation error about `LiftThreadIsolatio... | ✅ | [log](./output/debug/f32541744d6a7305af151078470f0cb07bc3ea4f.log) |
| kdlee | 2025-02-20 | PA: Remove pool offset freelists feature | ✅ | [log](./output/debug/98d198364f616abebfbcec16edf45e640fe00ca4.log) |
| arthursonzogni | 2025-02-17 | partition_alloc: fix missing `basic_common_referenc... | ✅ | [log](./output/debug/879c3028e66ee96ba147c583315b2fd58c99b43d.log) |
| arthursonzogni | 2025-02-17 | PartitionAlloc: realloc growth factor mitigation fo... | ✅ | [log](./output/debug/09ea5ed6c63f10582a6e67cd0db5549597bf25d5.log) |
| marshall | 2025-02-13 | Fix extra qualification on member 'basic_common_ref... | ✅ | [log](./output/debug/2e370e26c52803f2524c51c3c7a3d2c21ebabcd8.log) |
| dtapuska | 2025-02-13 | [ios blink] Set MAP_JIT pages to RWX by default | ✅ | [log](./output/debug/5ce79ef9d981e6e60ee9a1f5bd905b1ee076965c.log) |
| mikt | 2025-02-13 | [PA] Add a test for backup_ref_ptr_extra_extras_size | ✅ | [log](./output/debug/0ebfead86460d7744f604f31717fbcf9ea348def.log) |
| mikt | 2025-02-12 | [PA] Fix backup_ref_ptr_extra_extras_size not being... | ✅ | [log](./output/debug/3005f069de69d77fcb06b9184d25c1f54ed8717c.log) |
| hans | 2025-02-11 | Roll libc++ from 12150825ca73 to 492ff432ef34 (56 r... | ✅ | [log](./output/debug/f3153d2c69cfaae76414e3e3a7fa15408ffba479.log) |
| dtapuska | 2025-02-07 | Reland "[ios blink] Enable MAP_JIT unconditionally" | ✅ | [log](./output/debug/4b9edec2ee9cfdcf63edc195622fd66a8506d65f.log) |
| asamidoi | 2025-02-07 | Revert "[ios blink] Enable MAP_JIT unconditionally" | ✅ | [log](./output/debug/21e5eb503a278ed29bf9b88fd383f2c94d8da612.log) |
| dtapuska | 2025-02-05 | [ios blink] Enable MAP_JIT unconditionally | ✅ | [log](./output/debug/2c0dac296b692fee8a92f47a7237823d6cbde44f.log) |
| neis | 2025-02-05 | Remove Lacros leftovers from base/ | ✅ | [log](./output/debug/66a65af8596ab076424176fbbad0f02ac4fcae0f.log) |
| dsanders11 | 2025-02-03 | Remove some unused includes of <tuple> | ✅ | [log](./output/debug/185644689122812d475d0507e3bc1aa0c0156782.log) |
| arthursonzogni | 2025-02-03 | PA: Remove 'NDEBUG' and make is_debug configurable. | ✅ | [log](./output/debug/85d14cbcf203ad6b4059683b1700f00cc677b29c.log) |
| mikt | 2025-01-28 | [PA] Unify FreeFlags::kZap with kSchedulerLoopQuara... | ✅ | [log](./output/debug/6944ecdfe98cc0f76f02d0ec6643ff78c8d5c191.log) |
| tasak | 2025-01-21 | [PA, MTE] Fix PartitionAllocTest.FewerMemoryRegions... | ✅ | [log](./output/debug/a004bba90aa8ac07a7071dbf1a09d0e4e99513bc.log) |
| yukishiino | 2025-01-16 | ELUD: Reduce the usage of machine stack | ✅ | [log](./output/debug/088f9a5921a6fc929fdffb27577dddc5a01f4a71.log) |
| pkasting | 2025-01-10 | Manually fix remaining clang-tidy errors in base/. | ✅ | [log](./output/debug/bad4d8a87337475db378ebb64706a4fdebb641a2.log) |
| lizeb | 2025-01-09 | [PartitionAlloc] Add feature to use fewer memory re... | ✅ | [log](./output/debug/ba505b4478daf573942664233c75a23d706607dd.log) |
| lizeb | 2025-01-09 | [PartitionAlloc] Document apple lock options | ✅ | [log](./output/debug/a77103c1816d48a72e528c58d78993d45a9c0343.log) |
| pkasting | 2025-01-08 | Apply clang-tidy autofixes to base/. | ✅ | [log](./output/debug/5430b75fd1cc5429fc41b18561c0439b2ae16670.log) |
| mikt | 2025-01-08 | Reland "[PA/AC] UI thread specific capacity configu... | ✅ | [log](./output/debug/51b0fb5b1c36366f7e174b2637407ad964a9bcf7.log) |
| pkasting | 2025-01-08 | Mark raw_ptr<T> and T* as having a common reference... | ✅ | [log](./output/debug/33fbaf834c7673bd75b829b775775ac42e418c09.log) |
| yyanagisawa | 2025-01-07 | Revert "[PA/AC] UI thread specific capacity configu... | ✅ | [log](./output/debug/dc027d58406d26da0786910c51720935ebd3b3fc.log) |
| mikt | 2025-01-07 | [PA/AC] UI thread specific capacity configuration f... | ✅ | [log](./output/debug/6cdc138f18001b0ba6dbe12a7c95530052b6ac32.log) |
| lizeb | 2025-01-07 | [PartitionAlloc] Name anonymous VMAs on Linux and C... | ✅ | [log](./output/debug/6548aa3fdc79179a5b558892afad7e71fa473757.log) |
| verwaest | 2025-01-06 | [pa] Use adaptive-spin and data-sync on macos | ✅ | [log](./output/debug/934bddc37b89df34cf8adeb6dd3d12246143df89.log) |
| pkasting | 2024-12-27 | [cleanup] clang-format base. | ✅ | [log](./output/debug/9cab8b0d103998c4552b3ac14ef8429b7fe652c4.log) |
| tasak | 2024-12-20 | [PA] Copy //base/files/platform_file.h to Partition... | ✅ | [log](./output/debug/165d75a6241b0c43e2c3e1404b22500bada3b5cc.log) |
| edechamps | 2024-12-19 | Don't build partition_alloc if it is not needed | ✅ | [log](./output/debug/616b272794c79c5c19f87508ce86448e18afde6c.log) |
| mikt | 2024-12-17 | [BRP] Allow extras size to be controlled via Finch | ✅ | [log](./output/debug/847c1e77f386c103aeef42ecee6529d625d045ec.log) |
| pkasting | 2024-12-17 | Don't use base::internal:: APIs outside base/. | ✅ | [log](./output/debug/f240d41100751bac9a2528caea233da8d7d3750b.log) |
| fdoray | 2024-12-13 | [perfcombined2024] Enable PartitionAlloc parameter ... | ✅ | [log](./output/debug/b15cea87c55341ede2956f7e2bf09eb0332b33d1.log) |
| tikuta | 2024-12-09 | base: add missing includes for the build with use_l... | ✅ | [log](./output/debug/e8eba702d878a8cad8d97963f838f2ccee0e7f8a.log) |
| ivan.murashov | 2024-12-09 | partition_alloc: Remove duplicated includes of buil... | ✅ | [log](./output/debug/89c828e21c494b6220723c04997a8639633cc7f9.log) |
| tasak | 2024-12-09 | [PA] Fix flaky test failure of memory reclaimer uni... | ✅ | [log](./output/debug/3faa9b05d6777335f964cbf901c8ea1b23de07ea.log) |
| kdlee | 2024-12-06 | PA: Remove *Scan config from `PartitionOptions` | ✅ | [log](./output/debug/155df0f49332dbf69aec0614d7a89c6a09c0bc3e.log) |
| kdlee | 2024-12-06 | PA: Remove *Scan references in unit tests | ✅ | [log](./output/debug/394945644da7df29c4262a0b69c79e0b0c91944c.log) |
| arthursonzogni | 2024-12-04 | Style: Fix array initializations with size mismatch... | ✅ | [log](./output/debug/f96b908c9a5edb49a61287aa7fe4e9a311f44766.log) |
| pkasting | 2024-12-03 | Introduce a "same as any" template and use it to si... | ✅ | [log](./output/debug/b7a17328404dac7bfc9be2a07190aaf6bbd2c36a.log) |
| tasak | 2024-11-20 | [PA] Make EnableShadowMetadata() and PartitionDirec... | ✅ | [log](./output/debug/c551156ef8ccc090e52941d58c22647326066ff3.log) |
| rop | 2024-11-18 | LSC Updating README.chromium license names to use s... | ✅ | [log](./output/debug/7b91772e38c3d928d2170cd5cbcef81b8b2dbf5d.log) |
| arthursonzogni | 2024-11-14 | DanglingPtr: Improve error message. | ✅ | [log](./output/debug/6a3eb3e3cff5b3f6a0938992c921fd534520af9f.log) |
| pbos | 2024-11-14 | Replace CHECK(false) in base/ | ✅ | [log](./output/debug/fff6771d53cfd6b9bb8d53180090b2679670c2fc.log) |
| glazunov | 2024-11-08 | [BRP] Make sure all quarantined allocations are zapped | ✅ | [log](./output/debug/bd0c0ab0f94f8b9c21e4e9207f66a4832477e96e.log) |
| tikuta | 2024-11-08 | base: include stdlib.h for malloc/realloc | ✅ | [log](./output/debug/972d0c921eeba6ee2ecc49762eb6e0676e8ea84f.log) |
| yukishiino | 2024-11-07 | PA: Narrow the critical section of LightweightQuara... | ✅ | [log](./output/debug/5720e2701e416a4e8e9b423413659e925ab4dbbb.log) |
| lizeb | 2024-10-30 | [PartitionAlloc] Add option to eventually memset() ... | ✅ | [log](./output/debug/72ae2afeb4d373b900683a82919e8d4a0d139f82.log) |
| yukishiino | 2024-10-28 | ELUD: Do not quarantine direct-mapped allocations | ✅ | [log](./output/debug/2bc4745c33b44da415fad88ccfdf2900ed835dce.log) |
| lauren | 2024-10-24 | PA: check for <sys/ifunc.h> to enable MTE/BTI | ✅ | [log](./output/debug/e11fdbafa549101c04b028e940bf59963229569f.log) |
| lizeb | 2024-10-23 | [PartitionAlloc] Don't memset() direct-mapped alloo... | ✅ | [log](./output/debug/914c30a91ad47f1f60de28bc10cfeef910dec161.log) |
| arthursonzogni | 2024-10-22 | PA: check readability-static-accessed-through-instance | ✅ | [log](./output/debug/dbaab7e744c75e9c5411397d6a61e8217053ce22.log) |
| yukishiino | 2024-10-21 | PA: Remove runtime conditional branches from Lightw... | ✅ | [log](./output/debug/ce13777cb731e0a60c606d1741091fd11a0574d7.log) |
| arthursonzogni | 2024-10-14 | PA: link against winmm.lib. | ✅ | [log](./output/debug/49e7d5b5b0bd7342e469b6ff8a6266a2cfe3c489.log) |
| mikt | 2024-10-11 | [PA] Add configuration for iOS binary experiment | ✅ | [log](./output/debug/1d1d7753cd2489252833ab2398ff7b94230aa9ca.log) |
| mikt | 2024-10-11 | [PA] Put some debug data on stack on cookie corruption | ✅ | [log](./output/debug/67d020b3b9c6e0674b863786ccbdcb2dde2fea4a.log) |
| mikt | 2024-10-10 | [PA] Clean-up assuming core pools are glued everywhere | ✅ | [log](./output/debug/325b94b1de054e716ebe86f796acb8e90fc84b29.log) |
| tasak | 2024-10-10 | [PA] UnmapShadowMetadata() must be invoked before U... | ✅ | [log](./output/debug/ece815bd85c86702e994cde9ccd79c02335aa4d5.log) |
| pkasting | 2024-10-10 | Use three-way comparison when available in Partitio... | ✅ | [log](./output/debug/4f1c8275f78acb2eabcb441f9f09d17e4c129448.log) |
| mikt | 2024-10-10 | [PA] Glue core pools on iOS | ✅ | [log](./output/debug/ce32b10a09cfe6be075b586e2a25959d76a6b647.log) |
| mikt | 2024-10-10 | [PA] Fix PartitionAddressSpace::RegularPoolSize() i... | ✅ | [log](./output/debug/6034b95817c2a5d4df72f5772c23fcd59bdb8261.log) |
| pkasting | 2024-10-09 | Remove bartekn@ as OWNER. | ✅ | [log](./output/debug/4ac2023e4f7fca06b496a85447a12d53ef5ffaf8.log) |
| mikt | 2024-10-09 | [PA] Add FORCE_DISABLE_BACKUP_REF_PTR_FEATURE build... | ✅ | [log](./output/debug/5eb3834d17db690156ea257d6cad9452b3dd4b92.log) |
| mikt | 2024-10-09 | [PA] Fix enable_partition_lock_reentrancy_check wit... | ✅ | [log](./output/debug/cfded4a9ba2fd07e08ed66a8b4a1e3d01db52384.log) |
| mikt | 2024-10-09 | [PA] Add "smaller" partition cookie build option | ✅ | [log](./output/debug/f4b2dd0e30f90470d5400606d72581d9d910937b.log) |
| mikt | 2024-10-09 | [PA] Add partition cookie check build option | ✅ | [log](./output/debug/242f8277ece89fecca2c9561c0d6c7d681fc9a99.log) |
| sorin | 2024-10-09 | base: eliminate empty parameter list in lambdas whe... | ✅ | [log](./output/debug/524cf957f0260f857928401ec3502c9ec663c6fa.log) |
| sorin | 2024-10-08 | base: eliminate empty parameter list in lambdas whe... | ✅ | [log](./output/debug/1ced11f214ead902b40019f031852137f84827c2.log) |
| mikt | 2024-10-04 | [PA] Add lock reentrancy check build option | ✅ | [log](./output/debug/7939e34ad2e5c769f8856957cc7f8166c20bd954.log) |
| mikt | 2024-10-03 | [MO] Enable Partition Alloc with Advanced Checks su... | ✅ | [log](./output/debug/b986110c534670f28e49969325ee2ab7eca8b114.log) |
| mikt | 2024-10-02 | [PA-E] Use FreeFlags::kNoHooks consistently | ✅ | [log](./output/debug/3c7d09f6032e951cbf837608a3d18396c71dbee9.log) |
| mikt | 2024-10-02 | [MO] Support more functions in PA with Advanced Checks | ✅ | [log](./output/debug/9011cae703eb8ee0a1ac431a4ffb10f945458e81.log) |
| danakj | 2024-10-01 | Disable PA-based features in the Rust host tools to... | ✅ | [log](./output/debug/2850bbe7e393f36419d1df3c0dbbfcda4403092d.log) |
| jdapena | 2024-10-01 | GCC: do not add redundant template spec in constructor | ✅ | [log](./output/debug/ccc8b69a92a8f5472b6359190c17e86c91ce0775.log) |
| arthursonzogni | 2024-09-30 | PA: check readability-redundant-smartptr-get | ✅ | [log](./output/debug/d3a666931363ad6ea6ff9e633948a26fe4639530.log) |
| pbos | 2024-09-27 | Mark TerminateBecauseOutOfMemory [[noreturn]] | ✅ | [log](./output/debug/eb4c8ad8053e37bc0ca11f19cad1405bc0912676.log) |
| arthursonzogni | 2024-09-27 | PA: Fix #include for memcpy/memset. | ✅ | [log](./output/debug/2409a3774b4f25a09c3232af60aa717b2d67aee4.log) |
| marshall | 2024-09-26 | win: Add missing <limits> include | ❌ | [log](./output/debug/672834421883ed82745701ef948e27175b0a21cf.log) |
| fdoray | 2024-09-25 | [partition alloc] Add PA_NOT_TAIL_CALLED to out of ... | ❌ | [log](./output/debug/6d508e4ef47ae3b932648cef6ccb65f1ce931341.log) |
| fdoray | 2024-09-25 | [partition alloc] Allow foreground/background empty... | ❌ | [log](./output/debug/85b0685f68760491b20e634f8370be55bba04795.log) |
| arthursonzogni | 2024-09-24 | partition_alloc: Stop using anonymous namespace in ... | ❌ | [log](./output/debug/c97fac45ba2b636db5a7505b656c324a48dd4578.log) |
| tasak | 2024-09-20 | [PA] Add PartitionAllocShadowMetadata feature | ❌ | [log](./output/debug/c0fe75b0b5e1bfb65aaf60a5abb8a568da3a5590.log) |
| sergionso | 2024-09-19 | base: Improve CurrentWallclockMicroseconds() on Win... | ✅ | [log](./output/debug/7605153ca556d38d81429fcebf53b85fb9fe044e.log) |
| pkasting | 2024-09-18 | Attempt to improve comments in compiler_specific.h. | ✅ | [log](./output/debug/fb47d3dad7415dfb71a50c76d38a65085c7105c2.log) |
| pkasting | 2024-09-17 | More consistent macro definitions in base/compiler_... | ✅ | [log](./output/debug/ee6bf744537f90293b9e21c9be52b5aa32d2b50e.log) |
| rsworktech | 2024-09-17 | [PA] Use kPartitionCachelineSize instead of hardcod... | ✅ | [log](./output/debug/c146ea4f65525c50a0a26eeac8a773e886dbe38c.log) |
| fdoray | 2024-09-16 | [oom] Add commit limit/available to OOM exception a... | ✅ | [log](./output/debug/ea476c2c12d824c1c89c36b78903276c5c645bf5.log) |
| pkasting | 2024-09-13 | Prerequisites for changing macro definitions in com... | ✅ | [log](./output/debug/ca4487e127c2e071da5d4a36a9f71fd7b65b1434.log) |
| kdlee | 2024-09-13 | PA: Make `SlotStart` methods const | ✅ | [log](./output/debug/719c912ed6faac0547b91bd5485ba37e516eb978.log) |
| arthursonzogni | 2024-09-12 | Reland "PA: Invert MiraclePtr Platform Enablement L... | ✅ | [log](./output/debug/5576de467696ec80ac16be5daaa9e0ec86eb7564.log) |
| sroettger | 2024-09-10 | [cfi] Implement PageAllocator::SealPages on Linux | ✅ | [log](./output/debug/1ae169f5bd37d782c885821ed4e60fe39e711cc8.log) |
| mikt | 2024-09-10 | [PA] Use dispatch with advanced checks when feature... | ✅ | [log](./output/debug/9b58a78cc026d3088bf954daadfeec7b294b11d4.log) |
| keishi | 2024-09-10 | Update apple_apsl/README.chromium | ✅ | [log](./output/debug/65d4191fc0703d5c3b98d002091c93746be24e9a.log) |
| arthursonzogni | 2024-09-09 | PA: Stop using `constinit`. | ✅ | [log](./output/debug/69b922bdaae80e2dfe65b1ca5c5583446e3a582c.log) |
| arthursonzogni | 2024-09-09 | Revert "PA: Invert MiraclePtr Platform Enablement L... | ✅ | [log](./output/debug/81ff602c377ade97134a29b681068ee4a2f132f2.log) |
| arthursonzogni | 2024-09-09 | PA: Invert MiraclePtr Platform Enablement Logic | ✅ | [log](./output/debug/d81b3b062e4b40432a65225a16a5bb2d1590a8ef.log) |
| arthursonzogni | 2024-09-08 | PA: Revert "Allow std::hardware_destructive_interfe... | ✅ | [log](./output/debug/b69741434d0a8a8c6a089255866d1cef7ed48778.log) |
| tasak | 2024-09-06 | [PA] Fix ShadowMetadata issues | ✅ | [log](./output/debug/51001c0d0378ce34b34d3d6ce0f9899b4d832bab.log) |
| yzshen | 2024-09-06 | Remove the old gpu::Scheduler. | ✅ | [log](./output/debug/cff0048aa56a0ac7bf4da8009679b877500af6fa.log) |
| pkasting | 2024-09-04 | Allow (and use) std::hardware_destructive_interfere... | ✅ | [log](./output/debug/dbd5fd7ca188b19955dd6fd221a44f79efc39998.log) |
| yukishiino | 2024-09-04 | PA: Minor tweaks on LightweightQuarantine | ✅ | [log](./output/debug/18e11e59adc3bf1407bc8433b7cf9cc8c3503867.log) |
| arthursonzogni | 2024-09-04 | PartitionAlloc: stop depending on "defined(ANDROID)" | ✅ | [log](./output/debug/21f94456b3ec9d432075dc1d0aeba26d955871a9.log) |
| tasak | 2024-09-02 | [PA] Split SlotSpanMetadata into read-only one and ... | ✅ | [log](./output/debug/d0b9630d2515effb20b939cb5e526f8e0b5fd5f1.log) |
| arthursonzogni | 2024-09-02 | PA: Fix compile error encountered on Skia. | ✅ | [log](./output/debug/a2ce75ec98d94852baada5d6d98e6b1050099e38.log) |
| kdlee | 2024-08-30 | PA: Upgrade `DCheckIsValidSlotSpan()` | ✅ | [log](./output/debug/774e27628835d8580f58b420a6b2b608f22db3c2.log) |
| pkasting | 2024-08-29 | Switch from `ALIGNAS()` to `alignas()`. | ✅ | [log](./output/debug/4419c7daa9cc1e08af8769d0bb2314f9c7dfca27.log) |
| tasak | 2024-08-27 | [PA,shim] Fix compile error of allocator_shim_..._w... | ✅ | [log](./output/debug/60162d5aab8ebd147e04889e2d56a2f33e0b0adb.log) |
| keishi | 2024-08-23 | [MTE] Fix tagging after r1344621 | ✅ | [log](./output/debug/9513f560d7de3d8afb6c742e0641c32e56bd22cc.log) |
| pkasting | 2024-08-22 | Move arch-specific feature macros to build_config.h. | ✅ | [log](./output/debug/1ca611f5fd7838eae38927063b5e30f35e0b20f3.log) |
| bwwilliams | 2024-08-22 | Strengthen Warning Enforcement for Assignments in C... | ✅ | [log](./output/debug/995176567d7c95dfdfa5862cb743bb811d942b41.log) |
| tasak | 2024-08-22 | [PA,shim] Support allocator_shim on Windows debug b... | ✅ | [log](./output/debug/bcebe831fd166b7540502cbc3d4a2ba763047c78.log) |
| pkasting | 2024-08-22 | Remove [UN]LIKELY(). | ✅ | [log](./output/debug/97be0f3c5b04f1d2fda3d4e3e3d585868eb77efd.log) |
| keishi | 2024-08-21 | [MTE] Do retagging right before RawFreeWithThreadCa... | ✅ | [log](./output/debug/81cccdaee388163b04970911891f5a6349e19bbc.log) |
| tasak | 2024-08-21 | [PA] Split PartitionPageMetadata into read-only one... | ✅ | [log](./output/debug/a07ce06347ac8ac1540b6d08e86194c3e8c37a6a.log) |
| keishi | 2024-08-15 | Remove *Scan settings related code | ✅ | [log](./output/debug/cf28c12c0a65f752691ba60583dcfeb84dc84518.log) |
| sky | 2024-08-15 | pa: puts buildflags in public_deps | ✅ | [log](./output/debug/8b28072c61a1152b0b7eb0c506d00b24535a47bb.log) |
| tasak | 2024-08-09 | [shim] Move kPartitionAllocDispatch into another he... | ✅ | [log](./output/debug/1515d142bda42bc4f6364e2fa11cb79f9014c3cd.log) |
| yukishiino | 2024-08-08 | PA: Remove the self pointer from shim functions | ✅ | [log](./output/debug/091b58c775288e29d03ba6776bfa0e444c0b27c7.log) |
| pkasting | 2024-08-07 | Switch to [[(un)likely]]: .../partition_alloc/ | ✅ | [log](./output/debug/d374cbc2685c6354f1eda1bdd1be0c3ee45f009d.log) |
| tasak | 2024-08-07 | [PA] Support PartitionAlloc-Everywhere on Windows c... | ✅ | [log](./output/debug/c362d7a79a023b0693f872527b9d7c1077eb2fd4.log) |
| pkasting | 2024-08-06 | Switch to [[(un)likely]]: .../partition_alloc_base/ | ✅ | [log](./output/debug/a5626351a84e33d5fee2a5906be9dc85a242aa8e.log) |
| tasak | 2024-08-06 | [PA] Split PartitionSuperPageExtentEntry into read-... | ✅ | [log](./output/debug/54cdf4e94899d81db9dd367228300754301f5fd0.log) |
| olivierrobin | 2024-08-02 | Mark TimeTicks::UnixEpoch deprecated | ✅ | [log](./output/debug/be025bf066fd720e53fed43ad7906e4b278e85ef.log) |
| derinel | 2024-08-02 | Add IWYU statement for base::raw_ptr | ✅ | [log](./output/debug/813f717135e29158905bff102e6261499bb93106.log) |
| mikt | 2024-08-01 | [PA/shim] Add a new dispatch to switch malloc backe... | ✅ | [log](./output/debug/be977e0d870ad3d6db2dd92d6076cfe4908db7eb.log) |
| yukishiino | 2024-08-01 | PA: Fix ineffective PA_UNLIKELY applied to do ... w... | ✅ | [log](./output/debug/e41031670a9c4a93549ba0f672d2ed3367d9fcac.log) |
| keishi | 2024-07-31 | [MTE] Use a random value to update a tag | ✅ | [log](./output/debug/581d48913faf389f935ecb0be5a75fa5f789a4b2.log) |
| dloehr | 2024-07-30 | Remove uses of variable-length arrays | ✅ | [log](./output/debug/9930a27ceca75a0d831b0bd1098add097d352aa1.log) |
| tasak | 2024-07-30 | [PA] Remove unused kCookie from PartitionAllocDeath... | ✅ | [log](./output/debug/6eb5e6cf980ae8ceee135e5ccd0638a01a9948e9.log) |
| tasak | 2024-07-30 | [PA] Split DirectMapExtentMetadata into read-only o... | ✅ | [log](./output/debug/0627742f7ee966d5ab4547963941a2224911083f.log) |
| tasak | 2024-07-26 | [PA] Deflake PartitionAlloctest.CheckeReservationTy... | ✅ | [log](./output/debug/540ef1d89bfb64f8078919854dfed17b0ca9deaa.log) |
| arthursonzogni | 2024-07-25 | partition_alloc: Cleanup never called functions. | ✅ | [log](./output/debug/6a94c13fbac1e24eaa64161f58e9f566cc965d54.log) |
| tasak | 2024-07-25 | [MTE] Fix flaky BackupRefPtrTest.GetDeltaElems fail... | ✅ | [log](./output/debug/bd54734c0467af9fb4ff3610578718d6869f5a38.log) |
| arthursonzogni | 2024-07-24 | partition_alloc: Disable MTE for benchmark use to a... | ✅ | [log](./output/debug/561c0d214fe68a31a0fed180ccc8e5bf090b6bbe.log) |
| mikt | 2024-07-24 | [PA] Optimize IsManagedByPartitionAlloc() | ✅ | [log](./output/debug/91610144c44e3e96f33b7acd72609d84744a4de1.log) |
| tasak | 2024-07-24 | PA: Fix EncodedPoolOffset::Encode(). | ✅ | [log](./output/debug/877eaedbfd0c5e851d4f63ff2cbf659bdf036446.log) |
| keishi | 2024-07-23 | [MTE] Disable MTE during StackCopier::CopyStackCont... | ✅ | [log](./output/debug/0abdba1e1048de44c4d9d112d48afaf96a14f441.log) |
| mikt | 2024-07-12 | [PA/*Scan] Remove StarScan | ✅ | [log](./output/debug/b0cb752ab120cb7c5b46e6612eb7597f7b4153e8.log) |
| arthursonzogni | 2024-07-11 | partition_alloc: remove cpu_features:ndk_compat dep... | ✅ | [log](./output/debug/f085b61ade6a84bc24bedcc2d381a4a558431e9c.log) |
| yukishiino | 2024-07-11 | PA: Add PA_UNLIKELY to allocation failure handlers | ✅ | [log](./output/debug/29179883f32e3ea25f199238befdd1a09d488f37.log) |
| yukishiino | 2024-07-11 | PA: Let LightweightQuarantineBranch.Quarantine() ta... | ✅ | [log](./output/debug/0c714aaffcedd7a77562578e51ef3e2e427a1f4b.log) |
| kdlee | 2024-07-11 | PA: Precalculate Mac alignment kludge | ✅ | [log](./output/debug/4188dcd78c5267eacb3c0364f8e580898972c9cb.log) |
| arthursonzogni | 2024-07-10 | partition_alloc: Use PA_CONSTEXPR_DTOR | ✅ | [log](./output/debug/2e6b2efb6f435aa3dd400cb3bdcead2a601f8f9a.log) |
| mikt | 2024-07-09 | [PA/shim] Guarantee tail call optimization | ✅ | [log](./output/debug/575f1a0af46e358b4cdd6b3769caa754bf720bcb.log) |
| arthursonzogni | 2024-07-09 | partition_alloc: Follow-up moving tests. | ✅ | [log](./output/debug/f83b78cb7dc3363149149725b62876efcc995f89.log) |
| arthursonzogni | 2024-07-08 | partition_alloc: Check support for C++17 | ✅ | [log](./output/debug/880ba2b2e2121f4c37c87b61cd7bd4659fa7690d.log) |
| jdapena | 2024-07-08 | IWYU: add again required missing include for Histog... | ✅ | [log](./output/debug/fd1ad7b90ad02af8d2993c2e757b7615dcc1cff7.log) |
| arthursonzogni | 2024-07-08 | partition_alloc: support cpp17 | ✅ | [log](./output/debug/0ab14762072efc3c894aeebdd1b8578a74b99cda.log) |
| arthursonzogni | 2024-07-05 | Reland #2 "partition_alloc: Move pa tests into pa."" | ✅ | [log](./output/debug/36601cb520f4749418d0737cc65ecfda7ddb7500.log) |
| danakj | 2024-07-05 | Make all allocation routines from Rust fallible whe... | ✅ | [log](./output/debug/824fb852dc756ae4347d37779d0a7e8e67c04199.log) |
| arthursonzogni | 2024-07-05 | partition_alloc Fix violations of the PRESUBMIT | ✅ | [log](./output/debug/c0d55ba698b669900208466f858a9eee93d5ec0f.log) |
| arthursonzogni | 2024-07-05 | Revert "Reland "partition_alloc: Move pa tests into... | ✅ | [log](./output/debug/3508fb8a67265256667e6e0586f9b2dcce7ecda9.log) |
| arthursonzogni | 2024-07-04 | Reland "partition_alloc: Move pa tests into pa." | ✅ | [log](./output/debug/feb5861c7ee60df986d446ee84ff8b00c90924f3.log) |
| titouan | 2024-07-04 | Revert "partition_alloc: Move pa tests into pa." | ✅ | [log](./output/debug/f1888f8b851999367d99c83277527bddfbeef1d0.log) |
| arthursonzogni | 2024-07-04 | partition_alloc: Move pa tests into pa. | ✅ | [log](./output/debug/0abbaa1cc0759915e1234da4956ca8b4b231445c.log) |
| tpearson | 2024-07-03 | partition_alloc: Use 64k pages for ppc64 partition ... | ✅ | [log](./output/debug/22ca21545058c5fbef24f54c1b1c16ac7ed82590.log) |
| danakj | 2024-07-03 | Reland "Reland "Reland "Reland "Add toolchains with... | ✅ | [log](./output/debug/69258b7057b6cf183695ba8e2d6160edcd03d50e.log) |
| mjwilson | 2024-07-02 | Revert "Reland "Reland "Reland "Add toolchains with... | ✅ | [log](./output/debug/dc397419b98dc37a18c55a4bcefc43eb30189097.log) |
| danakj | 2024-07-02 | Reland "Reland "Reland "Add toolchains without Part... | ✅ | [log](./output/debug/37fa7c1ca9b94e63dc969a69668bcd53d89657e8.log) |
| tpearson | 2024-07-02 | partition_alloc: Autodetect page size on ppc64 systems | ✅ | [log](./output/debug/12d49fbf174022a0e5275d87ef9e3c71c3f05547.log) |
| tpearson | 2024-07-02 | partition_alloc: Allow variable page sizes on ppc64... | ✅ | [log](./output/debug/24f50b3bd0e30b804855b24c0125e93f7a197d20.log) |
| casey.smalley | 2024-07-01 | Add support for 64K pages on Linux/AArch64 | ✅ | [log](./output/debug/43ae3905f7007916c04d92fb92fc8167dc2e469f.log) |
| bartekn | 2024-07-01 | [PA] Enable glue_core_pools | ✅ | [log](./output/debug/7ac10c8f375123fd71ace5038c27b8fa77b69ed8.log) |
| kdlee | 2024-07-01 | PA: Untag pool offset freelist entries | ✅ | [log](./output/debug/0eb0d6bfeba06d4adbae9d82512acc7b565454b2.log) |
| danakj | 2024-06-28 | Test realloc in the realloc test | ✅ | [log](./output/debug/89101f0456b29a762c3d4c4e2e85491dd989d225.log) |
| tpearson | 2024-06-28 | partition_alloc: Prioritize non-constant POSIX page... | ✅ | [log](./output/debug/773457d3f3772c646a07e59a23758039bcc50089.log) |
| tarcisio.fischer | 2024-06-26 | Enable MTE by default on ConfigurePartitionsForTesting | ✅ | [log](./output/debug/45a05505a83e303d704fe088dc01e568bf33e038.log) |
| lizeb | 2024-06-26 | [PartitionAlloc] Purge more buckets from time to ti... | ✅ | [log](./output/debug/be8e0bd57d74a7031a7b1e0decd782d3601dd623.log) |
| arthursonzogni | 2024-06-26 | partition_alloc: merge buildflags.h #cleanup | ✅ | [log](./output/debug/2d3ec4ceaf5fce669fde51e187f3559a30832f0a.log) |
| wyeager | 2024-06-26 | Revert "Reland "Reland "Add toolchains without Part... | ✅ | [log](./output/debug/c29d2bc0167380bd0b0cef6274cd3e7cd02dd9b9.log) |
| arthursonzogni | 2024-06-25 | PA: Minimize DEPS for tests. | ✅ | [log](./output/debug/c718a2c1cc43cf34ea6422d64ad14d3d24595635.log) |
| arthursonzogni | 2024-06-25 | partition_alloc: Fix and simplify SpinningMutex. | ✅ | [log](./output/debug/c1d59d0456ffb430742563e18f461e8065e40cad.log) |
| danakj | 2024-06-24 | Reland "Reland "Add toolchains without PartitionAll... | ✅ | [log](./output/debug/8cdb01ad13cef64377e510814dafa2ca32eea2f7.log) |
| lukasza | 2024-06-24 | s/ `std::unique_ptr<char[]>` / std::vector<char> / ... | ✅ | [log](./output/debug/770d1a5a8a4a16f24a002cc51a4f2af4f68152c5.log) |
| bartekn | 2024-06-21 | [BRP] Test raw_ptr::operator=(T* ptr) when assigned... | ✅ | [log](./output/debug/efb545e8823213f553fdcb3b0c6af5b8ca5aefa2.log) |
| arthursonzogni | 2024-06-19 | partition_alloc: #cleanup unnecessary PA_ prefix | ✅ | [log](./output/debug/26b47cb849db9fbb0a89f1691efd0659f2d832ba.log) |
| bartekn | 2024-06-18 | [BRP] Handle case where raw_ptr::operator=(T* p) ge... | ✅ | [log](./output/debug/3c8b6517c927396a3c9767d488aa8af73d4467e9.log) |
| lizeb | 2024-06-18 | [base/allocator] Add documentation about discard vs... | ✅ | [log](./output/debug/f7d9f07348e454ed3e7ec3d6e8acf24388750e18.log) |
| kdlee | 2024-06-17 | PA: Add `SlotStart` death test | ✅ | [log](./output/debug/16c47e1a56f460b190083a114d39871e917c8492.log) |
| bartekn | 2024-06-17 | [PA] Fix BUILDFLAG->PA_BUILDFLAG under #if | ✅ | [log](./output/debug/b7d5ab0f5fa14c0981c6ffe5afbcfb5adc728d6b.log) |
| kdlee | 2024-06-13 | PA: Enable freelist dispatcher | ✅ | [log](./output/debug/7864cdced1d6ee0aae78768a808dd798480d76f0.log) |
| bartekn | 2024-06-13 | Remove USE_ASAN_UNOWNED_PTR | ✅ | [log](./output/debug/35643f54fd6309713d96266a17543e1e04dcc846.log) |
| kdlee | 2024-06-13 | PA: Adjust corruption test | ✅ | [log](./output/debug/2d4fa48c99b41f38c6df296b87954be94c8ee2f6.log) |
| kdlee | 2024-06-13 | PA: Hide GN arg | ✅ | [log](./output/debug/db10b18b633a65ea10d649b533d6848dbe7e4224.log) |
| bartekn | 2024-06-12 | [PA] Work around Adreno-GSL mmap address conflict | ✅ | [log](./output/debug/4b46ebdc43523f7f6ec2e8e6dbc151293ad115c5.log) |
| kdlee | 2024-06-12 | PA: Remove `TaggedSlotStart` | ✅ | [log](./output/debug/a1a8f60c590447fd1f9a93235c6e3552c462c549.log) |
| kdlee | 2024-06-12 | PA: Add `SlotStart::{From,To}Object()` | ✅ | [log](./output/debug/d5c2aacddbf420bc6385d4b3bc2b2afdcdbda1bd.log) |
| kdlee | 2024-06-10 | PA: Adjust bucketing comment | ✅ | [log](./output/debug/402d95788326f22ba4d06846d983bcb44da0fa07.log) |
| kdlee | 2024-06-07 | PA: Return slot size from `MaybePutInCache()` | ✅ | [log](./output/debug/ebfce4880cbffeea184c5b8e1ab0c7227878b7f3.log) |
| kdlee | 2024-06-04 | PA: Introduce `SlotStart` type | ✅ | [log](./output/debug/596919c38e416762842d3dabfeca9795de390f43.log) |
| arthursonzogni | 2024-06-04 | partition_alloc: Remove unused files. | ✅ | [log](./output/debug/4bc9d0c84a830f8883ad6558e54b2b3c3072583b.log) |
| arthursonzogni | 2024-06-04 | partition_alloc: Remove temporary exception for bui... | ✅ | [log](./output/debug/7013d1fbc8ae4a63addb2d8b3809290649469f20.log) |
| arthursonzogni | 2024-06-04 | Partition Alloc: Cutting the Cord! | ✅ | [log](./output/debug/ae870b571ec44a11de1bb2eba3376ad41779b5d1.log) |
| arthursonzogni | 2024-06-04 | partition_alloc: Check no external dependencies in GN. | ❌ | [log](./output/debug/195dd3d1a28e04dfe8a50d9911414a7f75fa0038.log) |
| kdlee | 2024-06-04 | PA: Introduce `ObjectToSlotStartUnchecked()` | ❌ | [log](./output/debug/b06c973eedc38f49bdfc18c3f594dd4f0e9cea77.log) |
| arthursonzogni | 2024-06-03 | partition_alloc: Stop using chromium's build_config... | ❌ | [log](./output/debug/8d08a407ab68da324863ebc274f20fefc4713e78.log) |
| arthursonzogni | 2024-06-03 | PA: Stop depending on `IS_CHROMEOS`. | ❌ | [log](./output/debug/77aad2ab99d3b15766dac04552911da4d892a08a.log) |
| arthursonzogni | 2024-06-03 | partition_alloc: provide build_config.h | ❌ | [log](./output/debug/b99a401f457eb03adae9c873c835a5ab736d126a.log) |
| kdlee | 2024-06-03 | PA: Adjust `PA_USE_DEATH_TESTS()` | ❌ | [log](./output/debug/89029ef39983240e0d9834340c5bf56c3f219868.log) |
| lizeb | 2024-05-31 | [PartitionAlloc] Do less work in fast MemoryReclaim... | ❌ | [log](./output/debug/4e54cefb1472e8fa0e4e120266c57b716c7f4cbc.log) |
| arthursonzogni | 2024-05-30 | partition_alloc: remove -Wl,--start-group, --end-group | ❌ | [log](./output/debug/f941becc7efa75971aa4e83d0cd3217f4f1ef57f.log) |
| lizeb | 2024-05-30 | [PartitionAlloc] Add a feature capping memory recla... | ❌ | [log](./output/debug/e9b1e467c32d80a904df8efddb8ed542aaf8171d.log) |

</details>

<details>
<summary>✅ Configuration: `release`</summary>

| Email | Date | Title | ? | Log |
|---|---|---|---|---|
| arthursonzogni | 2025-07-15 | partition_alloc: Resolve C++20 compile errors. | ✅ | [log](./output/release/328d516729e7e9edc833244c73cc9013828e5a1a.log) |
| thakis | 2025-07-14 | Remove remaining __pnacl__ and __native_client__ in... | ❌ | [log](./output/release/7b2807165fad397df23f5f749b15e9e43269ccf5.log) |
| tikuta | 2025-07-09 | base: Remove references to BUILDFLAG(IS_NACL) | ❌ | [log](./output/release/a54ac8d0dd78019fb41d2e376726d45b287e856b.log) |
| lizeb | 2025-07-09 | [PartitionAlloc] Use fewer VMAs by default on Linux... | ❌ | [log](./output/release/db340435e8d7e8eb89925d3006ecaf6427e3ab4f.log) |
| mikt | 2025-06-27 | [PA] Fix pool offset freelist DCHECK with MTE | ❌ | [log](./output/release/79b418050876e0c4187a80f668e81ce956b32bf2.log) |
| lizeb | 2025-06-26 | [base/allocator] Remove launched features | ❌ | [log](./output/release/11aaded5a31dc53a08781ca47f146f3795d021c4.log) |
| mikt | 2025-06-25 | [PA] Add callback for DoubleFreeDetected or Corrupt... | ❌ | [log](./output/release/3d6e246fc6014fd3f9f850876eae0fcd8f97921e.log) |
| thiabaud | 2025-06-25 | [partition_alloc] Add more threading annotations | ❌ | [log](./output/release/983d556a9aed36814954a4463bb0b508d2af133a.log) |
| tikuta | 2025-06-24 | partition_alloc: Add a missing include for std::ignore | ❌ | [log](./output/release/f8a48647751d44a0497a76633f6dc22ab28f51ad.log) |
| tasak | 2025-06-23 | [PA] Make PartitionAllocMemoryAllocationPerfTest hu... | ❌ | [log](./output/release/85594a8469649294d3b365e0637256a87dc74602.log) |
| dcheng | 2025-06-20 | base: remove NaCl from BUILD.gn, as well as NaCl-on... | ❌ | [log](./output/release/9b8de412d87c20117d2d04836bc5fa85866eaa08.log) |
| mikt | 2025-06-18 | [PA] Add option not to crash on Double-Free or Corr... | ❌ | [log](./output/release/ffa6d285560e810ab57e9a026b58f0a722658a6a.log) |
| bikineev | 2025-06-18 | PA: Fix an include to be relative to PA source dir | ❌ | [log](./output/release/a28c3c3d01412a17ebf145bfe2d73c8071c686e3.log) |
| rop | 2025-06-17 | LSC Add 'Update Mechanism:' to README.chromium | ❌ | [log](./output/release/49c08e7ea1746f671ce75b96f6ca444f6d6065ab.log) |
| avi | 2025-06-12 | Update MacOSVersion() for macOS 26 | ❌ | [log](./output/release/73de62811794a78ccb95ed3e197180ec8fb666c2.log) |
| thiabaud | 2025-06-09 | [partition_alloc] Add threading annotations | ❌ | [log](./output/release/50a84f34499cdfdc040a9d2c8fc1f031d31bbc78.log) |
| fdoray | 2025-06-06 | [partition_alloc] Add mechanism to terminate a proc... | ❌ | [log](./output/release/a585fc502ffa23ddce3412973eba2fe677325f02.log) |
| kdlee | 2025-06-05 | PA: Remove seam code for 4S | ❌ | [log](./output/release/76e5e3ac91101d2976805205fb51585c266e548f.log) |
| thestig | 2025-06-05 | [PA] Use PA_LOG() instead of LOG() | ❌ | [log](./output/release/37c90018cca427ce66d7f2fc3f43fca9d6ee9b6b.log) |
| mikt | 2025-06-03 | [PA] Optimize Purging mechanism for Scheduler-Loop ... | ❌ | [log](./output/release/e3668842ccb3173913161900ec731508f0655604.log) |
| mikt | 2025-06-03 | [PA] Replace usable_size with slot_size in Schedule... | ❌ | [log](./output/release/b1a4a44e2310b4661acf418a3524778969943919.log) |
| mikt | 2025-06-03 | [PA] Do Scheduler-Loop Quarantine after BRP Quarant... | ❌ | [log](./output/release/b95054240369556471d5c438217480a23089aa4a.log) |
| mikt | 2025-06-03 | [PA/E-LUD] Refactor: Fork LightweightQuarantine | ❌ | [log](./output/release/ffb614650932ce01003b1f1cbf26c1709f68c364.log) |
| hans | 2025-05-30 | Mark pointer in PartitionAllocPageAllocatorTest.Dec... | ❌ | [log](./output/release/d617778ed253822ee4c1bb9d03826f01e5f09e32.log) |
| avi | 2025-05-29 | Remove the macOS 11 malloc size hack from Partition... | ❌ | [log](./output/release/3ae30e4cf9d6f59ba825dcc96af9940ab35bf27b.log) |
| nuskos | 2025-05-29 | Use std::array instead of a c style array in PurgeP... | ❌ | [log](./output/release/a160ae6759caac1e19e3bf51b3660b649a9aba2e.log) |
| mikt | 2025-05-28 | Reland "[PA] Cache ReservationOffsetTable instead o... | ❌ | [log](./output/release/964c6996d56bd2167f4f6fdb2d88acfeba32c5d8.log) |
| caseq | 2025-05-28 | Remove redundant std::max(x, x) | ❌ | [log](./output/release/e85940b94442a391f6b528d9202e8c66eaca87be.log) |
| mpdenton | 2025-05-27 | GWP-ASan: raise kMaxMetadata and kMaxRequestedSlots | ❌ | [log](./output/release/f44457d2f971ec0a45c271e093b6aa56044d0ec1.log) |
| jonross | 2025-05-21 | Revert "[PA] Cache ReservationOffsetTable instead o... | ❌ | [log](./output/release/c858ce950cf900f168772e5e7c8f7cfa3e66ce96.log) |
| mikt | 2025-05-20 | [PA] Cache ReservationOffsetTable instead of lookup... | ❌ | [log](./output/release/29111157f1454c5a52fe83c7da9f57cb07a35b82.log) |
| mikt | 2025-05-18 | [PA/shim] Fix shim test failure on mac component build | ❌ | [log](./output/release/57f3d1311ce54e7c528608f2df77951920903451.log) |
| tikuta | 2025-05-15 | base: Disable libc++ modules build in partition all... | ❌ | [log](./output/release/1d9d02e434059dbdb74e10e28ad42fd97c25a85c.log) |
| tasak | 2025-05-14 | [PA] Remove libc++ string object dependency from al... | ❌ | [log](./output/release/269b4081447bcef3f64ad87116d9c6d8cfcf4645.log) |
| thestig | 2025-05-14 | Clean up PA's instance_tracer.h | ❌ | [log](./output/release/299f793686af3b7ea3facf647464a15622c27466.log) |
| mikt | 2025-05-14 | [PA] Fix PoolOffsetLookup for Configurable Pool | ❌ | [log](./output/release/fc79edffac58c4d59925412bf378eaf0f454688e.log) |
| mikt | 2025-05-12 | [PA] Cache PoolInfo instead of lookup by address | ❌ | [log](./output/release/f0e2e7a786cda3a52feaff9c7894ebcf68b13fb3.log) |
| thestig | 2025-05-07 | Remove <ostream> from PA's safe_conversions.h | ❌ | [log](./output/release/2b1d9301c925673637b3ff6e6412686ecfe66d02.log) |
| antoniosartori | 2025-05-07 | Revert "gardening: Disable PartitionAllocPageAlloca... | ❌ | [log](./output/release/60903e2555a42eeac93dc7c91eedbca746943842.log) |
| yukishiino | 2025-05-06 | gardening: Disable PartitionAllocPageAllocatorTest.... | ❌ | [log](./output/release/988f84a803953c0874cffadcb0ded36ba174582c.log) |
| mikt | 2025-05-06 | [PA/docs] Update buckets.md | ❌ | [log](./output/release/5c18e6e9b5fc4cb6748df24c2f63003e8ad3b81e.log) |
| dloehr | 2025-05-06 | Exported things should always be visible | ❌ | [log](./output/release/843601306bff485f15960ef0c7b23dd34e2d7ee5.log) |
| mikt | 2025-05-02 | [PA] Remove Freelist Dispatcher | ❌ | [log](./output/release/196ca28d1e516424ab24d9a798e13473895f8b71.log) |
| mikt | 2025-05-02 | [PA] Remove free slot bitmap | ❌ | [log](./output/release/93234db35d91c7af0ff75025fc4be90cc99dfcb9.log) |
| tasak | 2025-05-02 | [PA] Replace std::unordered_map with base::flat_map | ❌ | [log](./output/release/3a86115ff7330669c596355e7d7786703d4f2082.log) |
| mikt | 2025-05-01 | [PA] Remove unused free functions | ❌ | [log](./output/release/971c92b116187e9f5ebe2e3c84cf84b04161edbe.log) |
| mikt | 2025-05-01 | [PA] Remove unchecked freelist iteration | ❌ | [log](./output/release/2686355087336647c1d9aa5579eed6836dd71617.log) |
| nuskos | 2025-05-01 | Reland "spanification: remove `#pragma allow_unsafe... | ❌ | [log](./output/release/84e59bb4cda4ba071548ede290d44fcfa44f1a42.log) |
| mikt | 2025-05-01 | [PA] Simplify bucket lookup | ❌ | [log](./output/release/1397a7c24bc0e506cb7bfa2b5eaac48c144f7540.log) |
| luci-bisection | 2025-05-01 | Revert "spanification: remove `#pragma allow_unsafe... | ❌ | [log](./output/release/afa6432ee9ba7108018c52f8f8e68cc84d2f3370.log) |
| nuskos | 2025-05-01 | spanification: remove `#pragma allow_unsafe_buffers... | ❌ | [log](./output/release/46f7b646565a2f60129a68806b8615347556a08b.log) |
| mikt | 2025-05-01 | [PA] Remove ZERO_RANDOMLY_ON_FREE | ❌ | [log](./output/release/a0068b7420952f0093c6149796d81039284e888c.log) |
| wangqing-hf | 2025-04-29 | [PA] Add stack scan supported for loongarch64. | ❌ | [log](./output/release/b6a1dfdeb69381c36187ce9e7a4e9f24ec1a9065.log) |
| mikt | 2025-04-29 | [PA] Check ThreadCache validity in DoubleFreeOrCorr... | ❌ | [log](./output/release/5ce629459a2c3b6ef5f56490805cd26169ac6969.log) |
| tasak | 2025-04-29 | [PA] Copy base/containers/flat_{map,tree}.h to part... | ❌ | [log](./output/release/4170769c13d02df7bcff9a90112f36ed552dcf3b.log) |
| mikt | 2025-04-28 | [PA] Scoped Scheduler-Loop Quarantine opt-out | ❌ | [log](./output/release/2d19fedeb02734e543c21c46b966835ce217ceea.log) |
| abhijeet | 2025-04-24 | [tvOS][base_unittests] Replace host_info with sysct... | ❌ | [log](./output/release/862506deb382f3f8a8fa9689c8d5136a48e9b778.log) |
| mikt | 2025-04-24 | [PA] Remove ghost of alternate bucket distribution | ❌ | [log](./output/release/b6040b2b33d28d064c2167c878deed3b49e4aeb2.log) |
| smaier | 2025-04-23 | Roll Android NDK to r28 | ❌ | [log](./output/release/a9ae8c0fd665f61acca4633d828a1061fbd461cc.log) |
| mikt | 2025-04-23 | [PA/shim] Support sized-delete | ❌ | [log](./output/release/d691f607f29e8ca39c37917be7a69629f80a0dbd.log) |
| tasak | 2025-04-22 | [PA] Fix wrong includes. | ❌ | [log](./output/release/a5083e082d03f4f7d3b0ee35df7cfa3e2ccf8680.log) |
| tasak | 2025-04-20 | [PA] Fix PartitionAlloc windows component build | ❌ | [log](./output/release/471d99073bd4a042dd17aed9fb7604a6c3277ad9.log) |
| anandrv | 2025-04-17 | [PartitionAlloc] Enable priority inheritance in Spi... | ❌ | [log](./output/release/21fe3be95a6c4372f6b3e467c05be49f8cd5279f.log) |
| mikt | 2025-04-16 | [PA] Refactor: move Scheduler-Loop Quarantine relat... | ❌ | [log](./output/release/94efd06f8629f3ee91888150d16d2c2fafd898a5.log) |
| thestig | 2025-04-14 | Forward declare base::NoDestructor in headers when ... | ❌ | [log](./output/release/4b0f19307639826f8fca1a41882781540ff2fb50.log) |
| lizeb | 2025-04-09 | [base/allocator] Add aligned_alloc to shims on Android | ❌ | [log](./output/release/932177a9b8f06e7f478fcb22ac7b7184908738a8.log) |
| lizeb | 2025-04-09 | [PartitionAlloc] Make ENOMEM issues have a separate... | ❌ | [log](./output/release/5144c01d94d24360ec0cecb91319bde84e9acec7.log) |
| dloehr | 2025-04-08 | Change expected message in nocompile test | ❌ | [log](./output/release/2041003ba674f918c33b1afaaad74e652f34bcea.log) |
| lizeb | 2025-04-08 | [PartitionAlloc] Crash in AddressPoolManager when d... | ❌ | [log](./output/release/836a8ac2ba51ad26527eee243edda043586f7390.log) |
| mikt | 2025-04-07 | Reland "[PA] Disable BRP zapping on iOS" | ❌ | [log](./output/release/799310f3bf7d3cdbee28a086035eefc38732b548.log) |
| dtapuska | 2025-04-04 | [ios blink] Add support for arm64e target | ❌ | [log](./output/release/4cc11b45843b513ee6cd469c21dde9c607624865.log) |
| ginnyhuang | 2025-04-04 | Revert "[PA] Disable BRP zapping on iOS" | ❌ | [log](./output/release/20e84b3ed75698f1fb19149a640573f2bd420195.log) |
| mikt | 2025-04-04 | [PA] Disable BRP zapping on iOS | ❌ | [log](./output/release/5a43d8f11eeef195a27b6f0d4373e1a4f1a53581.log) |
| ritownsend | 2025-04-03 | chore: migrate ritownsend OWNERS/TODOs | ❌ | [log](./output/release/3ef26d8c8a8886277a41d4ae1e9d1801320eb274.log) |
| mikt | 2025-04-02 | Reland "[PA] Add base::CheckHeapIntegrity to invest... | ❌ | [log](./output/release/53e916ce2c2835fbe66f639a1c4a8a010efa0514.log) |
| tasak | 2025-03-31 | [PA] Split DoubleFreeOrCorruptionDetected into Doub... | ❌ | [log](./output/release/a9e3cecf8ea5c8da254d98bab323142e17229b0c.log) |
| dloehr | 2025-03-28 | Export things to prevent accidental duplication | ❌ | [log](./output/release/ab56923a27b2793f21994589b0c39bc3324ff49f.log) |
| wcwang | 2025-03-25 | Revert "[PA] Add base::CheckHeapIntegrity to invest... | ❌ | [log](./output/release/01d2444accdc1f985d3cfd0c512222de507eb3a4.log) |
| wcwang | 2025-03-25 | Revert "[PA] Fix compile failure in PartitionRoot::... | ❌ | [log](./output/release/771d9b82c8daa8f1ae68cb33c5a1c3c8cfaf1267.log) |
| mikt | 2025-03-24 | [PA] Fix compile failure in PartitionRoot::CheckMet... | ❌ | [log](./output/release/13a351f4d27353ed972aa4fc37104d872ed576dd.log) |
| mikt | 2025-03-24 | [PA] Add base::CheckHeapIntegrity to investigate co... | ❌ | [log](./output/release/c381bec7b1db2e8aec822a8a6217736f4d70cc9c.log) |
| justincohen | 2025-03-21 | ios: Correct gwp_asan_unittests out of memory | ❌ | [log](./output/release/0abfd4c40e8124de0d14f0d95f5bfe9a4ddd8a8b.log) |
| pmeuleman | 2025-03-20 | Deactivate MTE in HWASan builds | ❌ | [log](./output/release/df5d4c1b2bdc8d18253cec8a3be4e0fa9194a2bb.log) |
| lokokung | 2025-03-18 | [wasm] Adds rudimentary support for WASM/Emscripten... | ✅ | [log](./output/release/fb60666cb1896901bb14a5feb10001d20c8833c3.log) |
| mikt | 2025-03-07 | [PA] Add EnsureThreadCache() for blocking thread ca... | ✅ | [log](./output/release/d3191727ef81ba9daefb0bd3b90d9e4043a4bfa1.log) |
| mikt | 2025-02-27 | [PA] Add unittest to verify extra extras protecting... | ✅ | [log](./output/release/46d880ff62f340854a5a70142b0abf604c7af221.log) |
| jbroman | 2025-02-24 | Remove an unused include of <unistd.h> | ✅ | [log](./output/release/bd46928f4b41532c457fa8834ab56d729f4c6c67.log) |
| arthursonzogni | 2025-02-20 | PA: Fix compilation error about `LiftThreadIsolatio... | ✅ | [log](./output/release/f32541744d6a7305af151078470f0cb07bc3ea4f.log) |
| kdlee | 2025-02-20 | PA: Remove pool offset freelists feature | ✅ | [log](./output/release/98d198364f616abebfbcec16edf45e640fe00ca4.log) |
| arthursonzogni | 2025-02-17 | partition_alloc: fix missing `basic_common_referenc... | ✅ | [log](./output/release/879c3028e66ee96ba147c583315b2fd58c99b43d.log) |
| arthursonzogni | 2025-02-17 | PartitionAlloc: realloc growth factor mitigation fo... | ✅ | [log](./output/release/09ea5ed6c63f10582a6e67cd0db5549597bf25d5.log) |
| marshall | 2025-02-13 | Fix extra qualification on member 'basic_common_ref... | ✅ | [log](./output/release/2e370e26c52803f2524c51c3c7a3d2c21ebabcd8.log) |
| dtapuska | 2025-02-13 | [ios blink] Set MAP_JIT pages to RWX by default | ✅ | [log](./output/release/5ce79ef9d981e6e60ee9a1f5bd905b1ee076965c.log) |
| mikt | 2025-02-13 | [PA] Add a test for backup_ref_ptr_extra_extras_size | ✅ | [log](./output/release/0ebfead86460d7744f604f31717fbcf9ea348def.log) |
| mikt | 2025-02-12 | [PA] Fix backup_ref_ptr_extra_extras_size not being... | ✅ | [log](./output/release/3005f069de69d77fcb06b9184d25c1f54ed8717c.log) |
| hans | 2025-02-11 | Roll libc++ from 12150825ca73 to 492ff432ef34 (56 r... | ✅ | [log](./output/release/f3153d2c69cfaae76414e3e3a7fa15408ffba479.log) |
| dtapuska | 2025-02-07 | Reland "[ios blink] Enable MAP_JIT unconditionally" | ✅ | [log](./output/release/4b9edec2ee9cfdcf63edc195622fd66a8506d65f.log) |
| asamidoi | 2025-02-07 | Revert "[ios blink] Enable MAP_JIT unconditionally" | ✅ | [log](./output/release/21e5eb503a278ed29bf9b88fd383f2c94d8da612.log) |
| dtapuska | 2025-02-05 | [ios blink] Enable MAP_JIT unconditionally | ✅ | [log](./output/release/2c0dac296b692fee8a92f47a7237823d6cbde44f.log) |
| neis | 2025-02-05 | Remove Lacros leftovers from base/ | ✅ | [log](./output/release/66a65af8596ab076424176fbbad0f02ac4fcae0f.log) |
| dsanders11 | 2025-02-03 | Remove some unused includes of <tuple> | ✅ | [log](./output/release/185644689122812d475d0507e3bc1aa0c0156782.log) |
| arthursonzogni | 2025-02-03 | PA: Remove 'NDEBUG' and make is_debug configurable. | ✅ | [log](./output/release/85d14cbcf203ad6b4059683b1700f00cc677b29c.log) |
| mikt | 2025-01-28 | [PA] Unify FreeFlags::kZap with kSchedulerLoopQuara... | ✅ | [log](./output/release/6944ecdfe98cc0f76f02d0ec6643ff78c8d5c191.log) |
| tasak | 2025-01-21 | [PA, MTE] Fix PartitionAllocTest.FewerMemoryRegions... | ✅ | [log](./output/release/a004bba90aa8ac07a7071dbf1a09d0e4e99513bc.log) |
| yukishiino | 2025-01-16 | ELUD: Reduce the usage of machine stack | ✅ | [log](./output/release/088f9a5921a6fc929fdffb27577dddc5a01f4a71.log) |
| pkasting | 2025-01-10 | Manually fix remaining clang-tidy errors in base/. | ✅ | [log](./output/release/bad4d8a87337475db378ebb64706a4fdebb641a2.log) |
| lizeb | 2025-01-09 | [PartitionAlloc] Add feature to use fewer memory re... | ✅ | [log](./output/release/ba505b4478daf573942664233c75a23d706607dd.log) |
| lizeb | 2025-01-09 | [PartitionAlloc] Document apple lock options | ✅ | [log](./output/release/a77103c1816d48a72e528c58d78993d45a9c0343.log) |
| pkasting | 2025-01-08 | Apply clang-tidy autofixes to base/. | ✅ | [log](./output/release/5430b75fd1cc5429fc41b18561c0439b2ae16670.log) |
| mikt | 2025-01-08 | Reland "[PA/AC] UI thread specific capacity configu... | ✅ | [log](./output/release/51b0fb5b1c36366f7e174b2637407ad964a9bcf7.log) |
| pkasting | 2025-01-08 | Mark raw_ptr<T> and T* as having a common reference... | ✅ | [log](./output/release/33fbaf834c7673bd75b829b775775ac42e418c09.log) |
| yyanagisawa | 2025-01-07 | Revert "[PA/AC] UI thread specific capacity configu... | ✅ | [log](./output/release/dc027d58406d26da0786910c51720935ebd3b3fc.log) |
| mikt | 2025-01-07 | [PA/AC] UI thread specific capacity configuration f... | ✅ | [log](./output/release/6cdc138f18001b0ba6dbe12a7c95530052b6ac32.log) |
| lizeb | 2025-01-07 | [PartitionAlloc] Name anonymous VMAs on Linux and C... | ✅ | [log](./output/release/6548aa3fdc79179a5b558892afad7e71fa473757.log) |
| verwaest | 2025-01-06 | [pa] Use adaptive-spin and data-sync on macos | ✅ | [log](./output/release/934bddc37b89df34cf8adeb6dd3d12246143df89.log) |
| pkasting | 2024-12-27 | [cleanup] clang-format base. | ✅ | [log](./output/release/9cab8b0d103998c4552b3ac14ef8429b7fe652c4.log) |
| tasak | 2024-12-20 | [PA] Copy //base/files/platform_file.h to Partition... | ✅ | [log](./output/release/165d75a6241b0c43e2c3e1404b22500bada3b5cc.log) |
| edechamps | 2024-12-19 | Don't build partition_alloc if it is not needed | ✅ | [log](./output/release/616b272794c79c5c19f87508ce86448e18afde6c.log) |
| mikt | 2024-12-17 | [BRP] Allow extras size to be controlled via Finch | ✅ | [log](./output/release/847c1e77f386c103aeef42ecee6529d625d045ec.log) |
| pkasting | 2024-12-17 | Don't use base::internal:: APIs outside base/. | ✅ | [log](./output/release/f240d41100751bac9a2528caea233da8d7d3750b.log) |
| fdoray | 2024-12-13 | [perfcombined2024] Enable PartitionAlloc parameter ... | ✅ | [log](./output/release/b15cea87c55341ede2956f7e2bf09eb0332b33d1.log) |
| tikuta | 2024-12-09 | base: add missing includes for the build with use_l... | ✅ | [log](./output/release/e8eba702d878a8cad8d97963f838f2ccee0e7f8a.log) |
| ivan.murashov | 2024-12-09 | partition_alloc: Remove duplicated includes of buil... | ✅ | [log](./output/release/89c828e21c494b6220723c04997a8639633cc7f9.log) |
| tasak | 2024-12-09 | [PA] Fix flaky test failure of memory reclaimer uni... | ✅ | [log](./output/release/3faa9b05d6777335f964cbf901c8ea1b23de07ea.log) |
| kdlee | 2024-12-06 | PA: Remove *Scan config from `PartitionOptions` | ✅ | [log](./output/release/155df0f49332dbf69aec0614d7a89c6a09c0bc3e.log) |
| kdlee | 2024-12-06 | PA: Remove *Scan references in unit tests | ✅ | [log](./output/release/394945644da7df29c4262a0b69c79e0b0c91944c.log) |
| arthursonzogni | 2024-12-04 | Style: Fix array initializations with size mismatch... | ✅ | [log](./output/release/f96b908c9a5edb49a61287aa7fe4e9a311f44766.log) |
| pkasting | 2024-12-03 | Introduce a "same as any" template and use it to si... | ✅ | [log](./output/release/b7a17328404dac7bfc9be2a07190aaf6bbd2c36a.log) |
| tasak | 2024-11-20 | [PA] Make EnableShadowMetadata() and PartitionDirec... | ✅ | [log](./output/release/c551156ef8ccc090e52941d58c22647326066ff3.log) |
| rop | 2024-11-18 | LSC Updating README.chromium license names to use s... | ✅ | [log](./output/release/7b91772e38c3d928d2170cd5cbcef81b8b2dbf5d.log) |
| arthursonzogni | 2024-11-14 | DanglingPtr: Improve error message. | ✅ | [log](./output/release/6a3eb3e3cff5b3f6a0938992c921fd534520af9f.log) |
| pbos | 2024-11-14 | Replace CHECK(false) in base/ | ✅ | [log](./output/release/fff6771d53cfd6b9bb8d53180090b2679670c2fc.log) |
| glazunov | 2024-11-08 | [BRP] Make sure all quarantined allocations are zapped | ✅ | [log](./output/release/bd0c0ab0f94f8b9c21e4e9207f66a4832477e96e.log) |
| tikuta | 2024-11-08 | base: include stdlib.h for malloc/realloc | ✅ | [log](./output/release/972d0c921eeba6ee2ecc49762eb6e0676e8ea84f.log) |
| yukishiino | 2024-11-07 | PA: Narrow the critical section of LightweightQuara... | ✅ | [log](./output/release/5720e2701e416a4e8e9b423413659e925ab4dbbb.log) |
| lizeb | 2024-10-30 | [PartitionAlloc] Add option to eventually memset() ... | ✅ | [log](./output/release/72ae2afeb4d373b900683a82919e8d4a0d139f82.log) |
| yukishiino | 2024-10-28 | ELUD: Do not quarantine direct-mapped allocations | ✅ | [log](./output/release/2bc4745c33b44da415fad88ccfdf2900ed835dce.log) |
| lauren | 2024-10-24 | PA: check for <sys/ifunc.h> to enable MTE/BTI | ✅ | [log](./output/release/e11fdbafa549101c04b028e940bf59963229569f.log) |
| lizeb | 2024-10-23 | [PartitionAlloc] Don't memset() direct-mapped alloo... | ✅ | [log](./output/release/914c30a91ad47f1f60de28bc10cfeef910dec161.log) |
| arthursonzogni | 2024-10-22 | PA: check readability-static-accessed-through-instance | ✅ | [log](./output/release/dbaab7e744c75e9c5411397d6a61e8217053ce22.log) |
| yukishiino | 2024-10-21 | PA: Remove runtime conditional branches from Lightw... | ✅ | [log](./output/release/ce13777cb731e0a60c606d1741091fd11a0574d7.log) |
| arthursonzogni | 2024-10-14 | PA: link against winmm.lib. | ✅ | [log](./output/release/49e7d5b5b0bd7342e469b6ff8a6266a2cfe3c489.log) |
| mikt | 2024-10-11 | [PA] Add configuration for iOS binary experiment | ✅ | [log](./output/release/1d1d7753cd2489252833ab2398ff7b94230aa9ca.log) |
| mikt | 2024-10-11 | [PA] Put some debug data on stack on cookie corruption | ✅ | [log](./output/release/67d020b3b9c6e0674b863786ccbdcb2dde2fea4a.log) |
| mikt | 2024-10-10 | [PA] Clean-up assuming core pools are glued everywhere | ✅ | [log](./output/release/325b94b1de054e716ebe86f796acb8e90fc84b29.log) |
| tasak | 2024-10-10 | [PA] UnmapShadowMetadata() must be invoked before U... | ✅ | [log](./output/release/ece815bd85c86702e994cde9ccd79c02335aa4d5.log) |
| pkasting | 2024-10-10 | Use three-way comparison when available in Partitio... | ✅ | [log](./output/release/4f1c8275f78acb2eabcb441f9f09d17e4c129448.log) |
| mikt | 2024-10-10 | [PA] Glue core pools on iOS | ✅ | [log](./output/release/ce32b10a09cfe6be075b586e2a25959d76a6b647.log) |
| mikt | 2024-10-10 | [PA] Fix PartitionAddressSpace::RegularPoolSize() i... | ✅ | [log](./output/release/6034b95817c2a5d4df72f5772c23fcd59bdb8261.log) |
| pkasting | 2024-10-09 | Remove bartekn@ as OWNER. | ✅ | [log](./output/release/4ac2023e4f7fca06b496a85447a12d53ef5ffaf8.log) |
| mikt | 2024-10-09 | [PA] Add FORCE_DISABLE_BACKUP_REF_PTR_FEATURE build... | ✅ | [log](./output/release/5eb3834d17db690156ea257d6cad9452b3dd4b92.log) |
| mikt | 2024-10-09 | [PA] Fix enable_partition_lock_reentrancy_check wit... | ✅ | [log](./output/release/cfded4a9ba2fd07e08ed66a8b4a1e3d01db52384.log) |
| mikt | 2024-10-09 | [PA] Add "smaller" partition cookie build option | ✅ | [log](./output/release/f4b2dd0e30f90470d5400606d72581d9d910937b.log) |
| mikt | 2024-10-09 | [PA] Add partition cookie check build option | ✅ | [log](./output/release/242f8277ece89fecca2c9561c0d6c7d681fc9a99.log) |
| sorin | 2024-10-09 | base: eliminate empty parameter list in lambdas whe... | ✅ | [log](./output/release/524cf957f0260f857928401ec3502c9ec663c6fa.log) |
| sorin | 2024-10-08 | base: eliminate empty parameter list in lambdas whe... | ✅ | [log](./output/release/1ced11f214ead902b40019f031852137f84827c2.log) |
| mikt | 2024-10-04 | [PA] Add lock reentrancy check build option | ✅ | [log](./output/release/7939e34ad2e5c769f8856957cc7f8166c20bd954.log) |
| mikt | 2024-10-03 | [MO] Enable Partition Alloc with Advanced Checks su... | ✅ | [log](./output/release/b986110c534670f28e49969325ee2ab7eca8b114.log) |
| mikt | 2024-10-02 | [PA-E] Use FreeFlags::kNoHooks consistently | ✅ | [log](./output/release/3c7d09f6032e951cbf837608a3d18396c71dbee9.log) |
| mikt | 2024-10-02 | [MO] Support more functions in PA with Advanced Checks | ✅ | [log](./output/release/9011cae703eb8ee0a1ac431a4ffb10f945458e81.log) |
| danakj | 2024-10-01 | Disable PA-based features in the Rust host tools to... | ✅ | [log](./output/release/2850bbe7e393f36419d1df3c0dbbfcda4403092d.log) |
| jdapena | 2024-10-01 | GCC: do not add redundant template spec in constructor | ✅ | [log](./output/release/ccc8b69a92a8f5472b6359190c17e86c91ce0775.log) |
| arthursonzogni | 2024-09-30 | PA: check readability-redundant-smartptr-get | ✅ | [log](./output/release/d3a666931363ad6ea6ff9e633948a26fe4639530.log) |
| pbos | 2024-09-27 | Mark TerminateBecauseOutOfMemory [[noreturn]] | ✅ | [log](./output/release/eb4c8ad8053e37bc0ca11f19cad1405bc0912676.log) |
| arthursonzogni | 2024-09-27 | PA: Fix #include for memcpy/memset. | ✅ | [log](./output/release/2409a3774b4f25a09c3232af60aa717b2d67aee4.log) |
| marshall | 2024-09-26 | win: Add missing <limits> include | ❌ | [log](./output/release/672834421883ed82745701ef948e27175b0a21cf.log) |
| fdoray | 2024-09-25 | [partition alloc] Add PA_NOT_TAIL_CALLED to out of ... | ❌ | [log](./output/release/6d508e4ef47ae3b932648cef6ccb65f1ce931341.log) |
| fdoray | 2024-09-25 | [partition alloc] Allow foreground/background empty... | ❌ | [log](./output/release/85b0685f68760491b20e634f8370be55bba04795.log) |
| arthursonzogni | 2024-09-24 | partition_alloc: Stop using anonymous namespace in ... | ❌ | [log](./output/release/c97fac45ba2b636db5a7505b656c324a48dd4578.log) |
| tasak | 2024-09-20 | [PA] Add PartitionAllocShadowMetadata feature | ❌ | [log](./output/release/c0fe75b0b5e1bfb65aaf60a5abb8a568da3a5590.log) |
| sergionso | 2024-09-19 | base: Improve CurrentWallclockMicroseconds() on Win... | ✅ | [log](./output/release/7605153ca556d38d81429fcebf53b85fb9fe044e.log) |
| pkasting | 2024-09-18 | Attempt to improve comments in compiler_specific.h. | ✅ | [log](./output/release/fb47d3dad7415dfb71a50c76d38a65085c7105c2.log) |
| pkasting | 2024-09-17 | More consistent macro definitions in base/compiler_... | ✅ | [log](./output/release/ee6bf744537f90293b9e21c9be52b5aa32d2b50e.log) |
| rsworktech | 2024-09-17 | [PA] Use kPartitionCachelineSize instead of hardcod... | ✅ | [log](./output/release/c146ea4f65525c50a0a26eeac8a773e886dbe38c.log) |
| fdoray | 2024-09-16 | [oom] Add commit limit/available to OOM exception a... | ✅ | [log](./output/release/ea476c2c12d824c1c89c36b78903276c5c645bf5.log) |
| pkasting | 2024-09-13 | Prerequisites for changing macro definitions in com... | ✅ | [log](./output/release/ca4487e127c2e071da5d4a36a9f71fd7b65b1434.log) |
| kdlee | 2024-09-13 | PA: Make `SlotStart` methods const | ✅ | [log](./output/release/719c912ed6faac0547b91bd5485ba37e516eb978.log) |
| arthursonzogni | 2024-09-12 | Reland "PA: Invert MiraclePtr Platform Enablement L... | ✅ | [log](./output/release/5576de467696ec80ac16be5daaa9e0ec86eb7564.log) |
| sroettger | 2024-09-10 | [cfi] Implement PageAllocator::SealPages on Linux | ✅ | [log](./output/release/1ae169f5bd37d782c885821ed4e60fe39e711cc8.log) |
| mikt | 2024-09-10 | [PA] Use dispatch with advanced checks when feature... | ✅ | [log](./output/release/9b58a78cc026d3088bf954daadfeec7b294b11d4.log) |
| keishi | 2024-09-10 | Update apple_apsl/README.chromium | ✅ | [log](./output/release/65d4191fc0703d5c3b98d002091c93746be24e9a.log) |
| arthursonzogni | 2024-09-09 | PA: Stop using `constinit`. | ✅ | [log](./output/release/69b922bdaae80e2dfe65b1ca5c5583446e3a582c.log) |
| arthursonzogni | 2024-09-09 | Revert "PA: Invert MiraclePtr Platform Enablement L... | ✅ | [log](./output/release/81ff602c377ade97134a29b681068ee4a2f132f2.log) |
| arthursonzogni | 2024-09-09 | PA: Invert MiraclePtr Platform Enablement Logic | ✅ | [log](./output/release/d81b3b062e4b40432a65225a16a5bb2d1590a8ef.log) |
| arthursonzogni | 2024-09-08 | PA: Revert "Allow std::hardware_destructive_interfe... | ✅ | [log](./output/release/b69741434d0a8a8c6a089255866d1cef7ed48778.log) |
| tasak | 2024-09-06 | [PA] Fix ShadowMetadata issues | ✅ | [log](./output/release/51001c0d0378ce34b34d3d6ce0f9899b4d832bab.log) |
| yzshen | 2024-09-06 | Remove the old gpu::Scheduler. | ✅ | [log](./output/release/cff0048aa56a0ac7bf4da8009679b877500af6fa.log) |
| pkasting | 2024-09-04 | Allow (and use) std::hardware_destructive_interfere... | ✅ | [log](./output/release/dbd5fd7ca188b19955dd6fd221a44f79efc39998.log) |
| yukishiino | 2024-09-04 | PA: Minor tweaks on LightweightQuarantine | ✅ | [log](./output/release/18e11e59adc3bf1407bc8433b7cf9cc8c3503867.log) |
| arthursonzogni | 2024-09-04 | PartitionAlloc: stop depending on "defined(ANDROID)" | ✅ | [log](./output/release/21f94456b3ec9d432075dc1d0aeba26d955871a9.log) |
| tasak | 2024-09-02 | [PA] Split SlotSpanMetadata into read-only one and ... | ✅ | [log](./output/release/d0b9630d2515effb20b939cb5e526f8e0b5fd5f1.log) |
| arthursonzogni | 2024-09-02 | PA: Fix compile error encountered on Skia. | ✅ | [log](./output/release/a2ce75ec98d94852baada5d6d98e6b1050099e38.log) |
| kdlee | 2024-08-30 | PA: Upgrade `DCheckIsValidSlotSpan()` | ✅ | [log](./output/release/774e27628835d8580f58b420a6b2b608f22db3c2.log) |
| pkasting | 2024-08-29 | Switch from `ALIGNAS()` to `alignas()`. | ✅ | [log](./output/release/4419c7daa9cc1e08af8769d0bb2314f9c7dfca27.log) |
| tasak | 2024-08-27 | [PA,shim] Fix compile error of allocator_shim_..._w... | ✅ | [log](./output/release/60162d5aab8ebd147e04889e2d56a2f33e0b0adb.log) |
| keishi | 2024-08-23 | [MTE] Fix tagging after r1344621 | ✅ | [log](./output/release/9513f560d7de3d8afb6c742e0641c32e56bd22cc.log) |
| pkasting | 2024-08-22 | Move arch-specific feature macros to build_config.h. | ✅ | [log](./output/release/1ca611f5fd7838eae38927063b5e30f35e0b20f3.log) |
| bwwilliams | 2024-08-22 | Strengthen Warning Enforcement for Assignments in C... | ✅ | [log](./output/release/995176567d7c95dfdfa5862cb743bb811d942b41.log) |
| tasak | 2024-08-22 | [PA,shim] Support allocator_shim on Windows debug b... | ✅ | [log](./output/release/bcebe831fd166b7540502cbc3d4a2ba763047c78.log) |
| pkasting | 2024-08-22 | Remove [UN]LIKELY(). | ✅ | [log](./output/release/97be0f3c5b04f1d2fda3d4e3e3d585868eb77efd.log) |
| keishi | 2024-08-21 | [MTE] Do retagging right before RawFreeWithThreadCa... | ✅ | [log](./output/release/81cccdaee388163b04970911891f5a6349e19bbc.log) |
| tasak | 2024-08-21 | [PA] Split PartitionPageMetadata into read-only one... | ✅ | [log](./output/release/a07ce06347ac8ac1540b6d08e86194c3e8c37a6a.log) |
| keishi | 2024-08-15 | Remove *Scan settings related code | ✅ | [log](./output/release/cf28c12c0a65f752691ba60583dcfeb84dc84518.log) |
| sky | 2024-08-15 | pa: puts buildflags in public_deps | ✅ | [log](./output/release/8b28072c61a1152b0b7eb0c506d00b24535a47bb.log) |
| tasak | 2024-08-09 | [shim] Move kPartitionAllocDispatch into another he... | ✅ | [log](./output/release/1515d142bda42bc4f6364e2fa11cb79f9014c3cd.log) |
| yukishiino | 2024-08-08 | PA: Remove the self pointer from shim functions | ✅ | [log](./output/release/091b58c775288e29d03ba6776bfa0e444c0b27c7.log) |
| pkasting | 2024-08-07 | Switch to [[(un)likely]]: .../partition_alloc/ | ✅ | [log](./output/release/d374cbc2685c6354f1eda1bdd1be0c3ee45f009d.log) |
| tasak | 2024-08-07 | [PA] Support PartitionAlloc-Everywhere on Windows c... | ✅ | [log](./output/release/c362d7a79a023b0693f872527b9d7c1077eb2fd4.log) |
| pkasting | 2024-08-06 | Switch to [[(un)likely]]: .../partition_alloc_base/ | ✅ | [log](./output/release/a5626351a84e33d5fee2a5906be9dc85a242aa8e.log) |
| tasak | 2024-08-06 | [PA] Split PartitionSuperPageExtentEntry into read-... | ✅ | [log](./output/release/54cdf4e94899d81db9dd367228300754301f5fd0.log) |
| olivierrobin | 2024-08-02 | Mark TimeTicks::UnixEpoch deprecated | ✅ | [log](./output/release/be025bf066fd720e53fed43ad7906e4b278e85ef.log) |
| derinel | 2024-08-02 | Add IWYU statement for base::raw_ptr | ✅ | [log](./output/release/813f717135e29158905bff102e6261499bb93106.log) |
| mikt | 2024-08-01 | [PA/shim] Add a new dispatch to switch malloc backe... | ✅ | [log](./output/release/be977e0d870ad3d6db2dd92d6076cfe4908db7eb.log) |
| yukishiino | 2024-08-01 | PA: Fix ineffective PA_UNLIKELY applied to do ... w... | ✅ | [log](./output/release/e41031670a9c4a93549ba0f672d2ed3367d9fcac.log) |
| keishi | 2024-07-31 | [MTE] Use a random value to update a tag | ✅ | [log](./output/release/581d48913faf389f935ecb0be5a75fa5f789a4b2.log) |
| dloehr | 2024-07-30 | Remove uses of variable-length arrays | ✅ | [log](./output/release/9930a27ceca75a0d831b0bd1098add097d352aa1.log) |
| tasak | 2024-07-30 | [PA] Remove unused kCookie from PartitionAllocDeath... | ✅ | [log](./output/release/6eb5e6cf980ae8ceee135e5ccd0638a01a9948e9.log) |
| tasak | 2024-07-30 | [PA] Split DirectMapExtentMetadata into read-only o... | ✅ | [log](./output/release/0627742f7ee966d5ab4547963941a2224911083f.log) |
| tasak | 2024-07-26 | [PA] Deflake PartitionAlloctest.CheckeReservationTy... | ✅ | [log](./output/release/540ef1d89bfb64f8078919854dfed17b0ca9deaa.log) |
| arthursonzogni | 2024-07-25 | partition_alloc: Cleanup never called functions. | ✅ | [log](./output/release/6a94c13fbac1e24eaa64161f58e9f566cc965d54.log) |
| tasak | 2024-07-25 | [MTE] Fix flaky BackupRefPtrTest.GetDeltaElems fail... | ✅ | [log](./output/release/bd54734c0467af9fb4ff3610578718d6869f5a38.log) |
| arthursonzogni | 2024-07-24 | partition_alloc: Disable MTE for benchmark use to a... | ✅ | [log](./output/release/561c0d214fe68a31a0fed180ccc8e5bf090b6bbe.log) |
| mikt | 2024-07-24 | [PA] Optimize IsManagedByPartitionAlloc() | ✅ | [log](./output/release/91610144c44e3e96f33b7acd72609d84744a4de1.log) |
| tasak | 2024-07-24 | PA: Fix EncodedPoolOffset::Encode(). | ✅ | [log](./output/release/877eaedbfd0c5e851d4f63ff2cbf659bdf036446.log) |
| keishi | 2024-07-23 | [MTE] Disable MTE during StackCopier::CopyStackCont... | ✅ | [log](./output/release/0abdba1e1048de44c4d9d112d48afaf96a14f441.log) |
| mikt | 2024-07-12 | [PA/*Scan] Remove StarScan | ✅ | [log](./output/release/b0cb752ab120cb7c5b46e6612eb7597f7b4153e8.log) |
| arthursonzogni | 2024-07-11 | partition_alloc: remove cpu_features:ndk_compat dep... | ✅ | [log](./output/release/f085b61ade6a84bc24bedcc2d381a4a558431e9c.log) |
| yukishiino | 2024-07-11 | PA: Add PA_UNLIKELY to allocation failure handlers | ✅ | [log](./output/release/29179883f32e3ea25f199238befdd1a09d488f37.log) |
| yukishiino | 2024-07-11 | PA: Let LightweightQuarantineBranch.Quarantine() ta... | ✅ | [log](./output/release/0c714aaffcedd7a77562578e51ef3e2e427a1f4b.log) |
| kdlee | 2024-07-11 | PA: Precalculate Mac alignment kludge | ✅ | [log](./output/release/4188dcd78c5267eacb3c0364f8e580898972c9cb.log) |
| arthursonzogni | 2024-07-10 | partition_alloc: Use PA_CONSTEXPR_DTOR | ✅ | [log](./output/release/2e6b2efb6f435aa3dd400cb3bdcead2a601f8f9a.log) |
| mikt | 2024-07-09 | [PA/shim] Guarantee tail call optimization | ✅ | [log](./output/release/575f1a0af46e358b4cdd6b3769caa754bf720bcb.log) |
| arthursonzogni | 2024-07-09 | partition_alloc: Follow-up moving tests. | ✅ | [log](./output/release/f83b78cb7dc3363149149725b62876efcc995f89.log) |
| arthursonzogni | 2024-07-08 | partition_alloc: Check support for C++17 | ✅ | [log](./output/release/880ba2b2e2121f4c37c87b61cd7bd4659fa7690d.log) |
| jdapena | 2024-07-08 | IWYU: add again required missing include for Histog... | ✅ | [log](./output/release/fd1ad7b90ad02af8d2993c2e757b7615dcc1cff7.log) |
| arthursonzogni | 2024-07-08 | partition_alloc: support cpp17 | ✅ | [log](./output/release/0ab14762072efc3c894aeebdd1b8578a74b99cda.log) |
| arthursonzogni | 2024-07-05 | Reland #2 "partition_alloc: Move pa tests into pa."" | ✅ | [log](./output/release/36601cb520f4749418d0737cc65ecfda7ddb7500.log) |
| danakj | 2024-07-05 | Make all allocation routines from Rust fallible whe... | ✅ | [log](./output/release/824fb852dc756ae4347d37779d0a7e8e67c04199.log) |
| arthursonzogni | 2024-07-05 | partition_alloc Fix violations of the PRESUBMIT | ✅ | [log](./output/release/c0d55ba698b669900208466f858a9eee93d5ec0f.log) |
| arthursonzogni | 2024-07-05 | Revert "Reland "partition_alloc: Move pa tests into... | ✅ | [log](./output/release/3508fb8a67265256667e6e0586f9b2dcce7ecda9.log) |
| arthursonzogni | 2024-07-04 | Reland "partition_alloc: Move pa tests into pa." | ✅ | [log](./output/release/feb5861c7ee60df986d446ee84ff8b00c90924f3.log) |
| titouan | 2024-07-04 | Revert "partition_alloc: Move pa tests into pa." | ✅ | [log](./output/release/f1888f8b851999367d99c83277527bddfbeef1d0.log) |
| arthursonzogni | 2024-07-04 | partition_alloc: Move pa tests into pa. | ✅ | [log](./output/release/0abbaa1cc0759915e1234da4956ca8b4b231445c.log) |
| tpearson | 2024-07-03 | partition_alloc: Use 64k pages for ppc64 partition ... | ✅ | [log](./output/release/22ca21545058c5fbef24f54c1b1c16ac7ed82590.log) |
| danakj | 2024-07-03 | Reland "Reland "Reland "Reland "Add toolchains with... | ✅ | [log](./output/release/69258b7057b6cf183695ba8e2d6160edcd03d50e.log) |
| mjwilson | 2024-07-02 | Revert "Reland "Reland "Reland "Add toolchains with... | ✅ | [log](./output/release/dc397419b98dc37a18c55a4bcefc43eb30189097.log) |
| danakj | 2024-07-02 | Reland "Reland "Reland "Add toolchains without Part... | ✅ | [log](./output/release/37fa7c1ca9b94e63dc969a69668bcd53d89657e8.log) |
| tpearson | 2024-07-02 | partition_alloc: Autodetect page size on ppc64 systems | ✅ | [log](./output/release/12d49fbf174022a0e5275d87ef9e3c71c3f05547.log) |
| tpearson | 2024-07-02 | partition_alloc: Allow variable page sizes on ppc64... | ✅ | [log](./output/release/24f50b3bd0e30b804855b24c0125e93f7a197d20.log) |
| casey.smalley | 2024-07-01 | Add support for 64K pages on Linux/AArch64 | ✅ | [log](./output/release/43ae3905f7007916c04d92fb92fc8167dc2e469f.log) |
| bartekn | 2024-07-01 | [PA] Enable glue_core_pools | ✅ | [log](./output/release/7ac10c8f375123fd71ace5038c27b8fa77b69ed8.log) |
| kdlee | 2024-07-01 | PA: Untag pool offset freelist entries | ✅ | [log](./output/release/0eb0d6bfeba06d4adbae9d82512acc7b565454b2.log) |
| danakj | 2024-06-28 | Test realloc in the realloc test | ✅ | [log](./output/release/89101f0456b29a762c3d4c4e2e85491dd989d225.log) |
| tpearson | 2024-06-28 | partition_alloc: Prioritize non-constant POSIX page... | ✅ | [log](./output/release/773457d3f3772c646a07e59a23758039bcc50089.log) |
| tarcisio.fischer | 2024-06-26 | Enable MTE by default on ConfigurePartitionsForTesting | ✅ | [log](./output/release/45a05505a83e303d704fe088dc01e568bf33e038.log) |
| lizeb | 2024-06-26 | [PartitionAlloc] Purge more buckets from time to ti... | ✅ | [log](./output/release/be8e0bd57d74a7031a7b1e0decd782d3601dd623.log) |
| arthursonzogni | 2024-06-26 | partition_alloc: merge buildflags.h #cleanup | ✅ | [log](./output/release/2d3ec4ceaf5fce669fde51e187f3559a30832f0a.log) |
| wyeager | 2024-06-26 | Revert "Reland "Reland "Add toolchains without Part... | ✅ | [log](./output/release/c29d2bc0167380bd0b0cef6274cd3e7cd02dd9b9.log) |
| arthursonzogni | 2024-06-25 | PA: Minimize DEPS for tests. | ✅ | [log](./output/release/c718a2c1cc43cf34ea6422d64ad14d3d24595635.log) |
| arthursonzogni | 2024-06-25 | partition_alloc: Fix and simplify SpinningMutex. | ✅ | [log](./output/release/c1d59d0456ffb430742563e18f461e8065e40cad.log) |
| danakj | 2024-06-24 | Reland "Reland "Add toolchains without PartitionAll... | ✅ | [log](./output/release/8cdb01ad13cef64377e510814dafa2ca32eea2f7.log) |
| lukasza | 2024-06-24 | s/ `std::unique_ptr<char[]>` / std::vector<char> / ... | ✅ | [log](./output/release/770d1a5a8a4a16f24a002cc51a4f2af4f68152c5.log) |
| bartekn | 2024-06-21 | [BRP] Test raw_ptr::operator=(T* ptr) when assigned... | ✅ | [log](./output/release/efb545e8823213f553fdcb3b0c6af5b8ca5aefa2.log) |
| arthursonzogni | 2024-06-19 | partition_alloc: #cleanup unnecessary PA_ prefix | ✅ | [log](./output/release/26b47cb849db9fbb0a89f1691efd0659f2d832ba.log) |
| bartekn | 2024-06-18 | [BRP] Handle case where raw_ptr::operator=(T* p) ge... | ✅ | [log](./output/release/3c8b6517c927396a3c9767d488aa8af73d4467e9.log) |
| lizeb | 2024-06-18 | [base/allocator] Add documentation about discard vs... | ✅ | [log](./output/release/f7d9f07348e454ed3e7ec3d6e8acf24388750e18.log) |
| kdlee | 2024-06-17 | PA: Add `SlotStart` death test | ✅ | [log](./output/release/16c47e1a56f460b190083a114d39871e917c8492.log) |
| bartekn | 2024-06-17 | [PA] Fix BUILDFLAG->PA_BUILDFLAG under #if | ✅ | [log](./output/release/b7d5ab0f5fa14c0981c6ffe5afbcfb5adc728d6b.log) |
| kdlee | 2024-06-13 | PA: Enable freelist dispatcher | ✅ | [log](./output/release/7864cdced1d6ee0aae78768a808dd798480d76f0.log) |
| bartekn | 2024-06-13 | Remove USE_ASAN_UNOWNED_PTR | ✅ | [log](./output/release/35643f54fd6309713d96266a17543e1e04dcc846.log) |
| kdlee | 2024-06-13 | PA: Adjust corruption test | ✅ | [log](./output/release/2d4fa48c99b41f38c6df296b87954be94c8ee2f6.log) |
| kdlee | 2024-06-13 | PA: Hide GN arg | ✅ | [log](./output/release/db10b18b633a65ea10d649b533d6848dbe7e4224.log) |
| bartekn | 2024-06-12 | [PA] Work around Adreno-GSL mmap address conflict | ✅ | [log](./output/release/4b46ebdc43523f7f6ec2e8e6dbc151293ad115c5.log) |
| kdlee | 2024-06-12 | PA: Remove `TaggedSlotStart` | ✅ | [log](./output/release/a1a8f60c590447fd1f9a93235c6e3552c462c549.log) |
| kdlee | 2024-06-12 | PA: Add `SlotStart::{From,To}Object()` | ✅ | [log](./output/release/d5c2aacddbf420bc6385d4b3bc2b2afdcdbda1bd.log) |
| kdlee | 2024-06-10 | PA: Adjust bucketing comment | ✅ | [log](./output/release/402d95788326f22ba4d06846d983bcb44da0fa07.log) |
| kdlee | 2024-06-07 | PA: Return slot size from `MaybePutInCache()` | ✅ | [log](./output/release/ebfce4880cbffeea184c5b8e1ab0c7227878b7f3.log) |
| kdlee | 2024-06-04 | PA: Introduce `SlotStart` type | ✅ | [log](./output/release/596919c38e416762842d3dabfeca9795de390f43.log) |
| arthursonzogni | 2024-06-04 | partition_alloc: Remove unused files. | ✅ | [log](./output/release/4bc9d0c84a830f8883ad6558e54b2b3c3072583b.log) |
| arthursonzogni | 2024-06-04 | partition_alloc: Remove temporary exception for bui... | ✅ | [log](./output/release/7013d1fbc8ae4a63addb2d8b3809290649469f20.log) |
| arthursonzogni | 2024-06-04 | Partition Alloc: Cutting the Cord! | ✅ | [log](./output/release/ae870b571ec44a11de1bb2eba3376ad41779b5d1.log) |
| arthursonzogni | 2024-06-04 | partition_alloc: Check no external dependencies in GN. | ❌ | [log](./output/release/195dd3d1a28e04dfe8a50d9911414a7f75fa0038.log) |
| kdlee | 2024-06-04 | PA: Introduce `ObjectToSlotStartUnchecked()` | ❌ | [log](./output/release/b06c973eedc38f49bdfc18c3f594dd4f0e9cea77.log) |
| arthursonzogni | 2024-06-03 | partition_alloc: Stop using chromium's build_config... | ❌ | [log](./output/release/8d08a407ab68da324863ebc274f20fefc4713e78.log) |
| arthursonzogni | 2024-06-03 | PA: Stop depending on `IS_CHROMEOS`. | ❌ | [log](./output/release/77aad2ab99d3b15766dac04552911da4d892a08a.log) |
| arthursonzogni | 2024-06-03 | partition_alloc: provide build_config.h | ❌ | [log](./output/release/b99a401f457eb03adae9c873c835a5ab736d126a.log) |
| kdlee | 2024-06-03 | PA: Adjust `PA_USE_DEATH_TESTS()` | ❌ | [log](./output/release/89029ef39983240e0d9834340c5bf56c3f219868.log) |
| lizeb | 2024-05-31 | [PartitionAlloc] Do less work in fast MemoryReclaim... | ❌ | [log](./output/release/4e54cefb1472e8fa0e4e120266c57b716c7f4cbc.log) |
| arthursonzogni | 2024-05-30 | partition_alloc: remove -Wl,--start-group, --end-group | ❌ | [log](./output/release/f941becc7efa75971aa4e83d0cd3217f4f1ef57f.log) |
| lizeb | 2024-05-30 | [PartitionAlloc] Add a feature capping memory recla... | ❌ | [log](./output/release/e9b1e467c32d80a904df8efddb8ed542aaf8171d.log) |

</details>

