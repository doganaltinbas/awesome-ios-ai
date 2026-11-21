# Awesome iOS AI

Curated iOS on-device and Apple AI resources. Build results are from Xcode 27.1; status is refreshed weekly.

## Core AI

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [apple/coreai-models](https://github.com/apple/coreai-models) | Apple's official Core AI export recipes, Python primitives and Swift runtime utilities. Requires iOS/macOS 27 and Xcode 27. Not accepting PRs at launch. _Built for generic iOS (device SDK); the simulator SDK lacks CoreAI_ | iOS 27 | passed (Xcode 27.1, 2026-11-21) | BSD-3-Clause | active | 2,368 |
| [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) | Swift-focused model zoo converting open LLMs (e.g., Qwen3.5, Gemma 4) to Core AI. The most active community zoo found. | iOS 27 | not tested | — | active | 467 |
| [CYBRTRK2/coreai-model-zoo](https://github.com/CYBRTRK2/coreai-model-zoo) | Community zoo with 66 Core AI models across LLM, VLM, OCR, ASR, TTS and image/video. Newer project. | iOS 27 | not tested | — | active | 0 |

## Foundation Models

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [huggingface/AnyLanguageModel](https://github.com/huggingface/AnyLanguageModel) | Drop-in, API-compatible replacement for Apple's Foundation Models framework that adds other backends. Use it to test or ship beyond Apple Intelligence devices. | — | passed (Xcode 27.1, 2026-11-21) | Apache-2.0 | active | 990 |
| [GijungKim/expo-local-llm](https://github.com/GijungKim/expo-local-llm) | Expo module running on-device LLMs via Foundation Models on iOS and Gemini Nano on Android. Use for cross-platform React Native apps. | iOS 26 | not tested | MIT | active | 15 |
| [artemnovichkov/HotdogApp](https://github.com/artemnovichkov/HotdogApp) | Minimal Foundation Models sample app for guided prompting. Builds on Xcode 27.1. _iOS Simulator_ | — | passed (Xcode 27.1, 2026-11-21) | — | active | 5 |
| [AddikiPraveenKumar/foundation-models-ios-guide](https://github.com/AddikiPraveenKumar/foundation-models-ios-guide) _(stale)_ | Written guide to Foundation Models on iOS 26, focused on privacy-first features. | iOS 26 | not tested | — | stale | 0 |
| [AppStorage/FoundationChat](https://github.com/AppStorage/FoundationChat) _(stale)_ | SwiftUI chat app on Foundation Models (MIT). Written for Xcode 26; needs updates to build on Xcode 27. _ConversationDetailView API mismatch_ | iOS 26 | failed (Xcode 27.1, 2026-11-21) | MIT | stale | 0 |

## Core ML

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [apple-aiml-research/ml-stable-diffusion](https://github.com/apple-aiml-research/ml-stable-diffusion) | Apple's reference for running Stable Diffusion with Core ML on Apple silicon, including a Swift package. _CLI target imports Cocoa; library not isolated_ | — | not tested | MIT | active | 17,962 |
| [likedan/Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) _(stale)_ | Large curated index of Core ML models. Last pushed June 2025; many links may be dead. | — | — | MIT | stale | 7,078 |
| [apple/coremltools](https://github.com/apple/coremltools) | Apple's Python tools to convert, edit and validate Core ML models from PyTorch and TensorFlow. Start here for any conversion. | — | not tested | BSD-3-Clause | active | 5,456 |
| [apple-aiml-research/ml-ane-transformers](https://github.com/apple-aiml-research/ml-ane-transformers) | Reference Transformer implementation optimized for the Apple Neural Engine. Use when latency or battery matters for a Core ML model. | — | not tested | — | active | 2,750 |
| [huggingface/swift-coreml-diffusers](https://github.com/huggingface/swift-coreml-diffusers) _(stale)_ | Swift app demonstrating Core ML Stable Diffusion. Archived, so use Apple's ml-stable-diffusion for current code. | — | not tested | Apache-2.0 | stale | 2,748 |
| [john-rocky/CoreML-Models](https://github.com/john-rocky/CoreML-Models) | Model zoo of PyTorch models converted to ready-to-use .mlpackage files for iOS/macOS, with conversion notes per model. Updated this week. | — | not tested | Apache-2.0 | active | 1,902 |

## MLX

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [ml-explore/mlx-swift-examples](https://github.com/ml-explore/mlx-swift-examples) | Sample apps for iOS and macOS: MLXChatExample, LLMEval, StableDiffusionExample. MLXChatExample builds on Xcode 27.1. _iOS Simulator; MLXChatExample needs Xcode's macro trust prompt accepted_ | iOS 17 | passed (Xcode 27.1, 2026-11-21) | MIT | active | 2,702 |
| [ml-explore/mlx-swift](https://github.com/ml-explore/mlx-swift) | Swift API for Apple's MLX array framework on Apple silicon. Base layer for the LLM packages below. | — | not tested | MIT | active | 2,095 |
| [ml-explore/mlx-swift-lm](https://github.com/ml-explore/mlx-swift-lm) | Run and fine-tune LLMs and VLMs in Swift. iOS 17+. Includes an MLXFoundationModels bridge for Apple's LanguageModelSession. _Built as a dependency of mlx-swift-examples_ | iOS 17 | passed (Xcode 27.1, 2026-11-21) | MIT | active | 878 |

## Runtimes

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | C/C++ LLM inference for GGUF models; the most widely used local runtime. Build for iOS and call from Swift via C interop. | — | not tested | MIT | active | 135,900 |
| [mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm) | Compiled LLM deployment engine that targets iOS and other platforms. Use when you need one compiled model across devices. | — | not tested | Apache-2.0 | active | 23,405 |
| [huggingface/swift-transformers](https://github.com/huggingface/swift-transformers) | Swift package for tokenizers and Hugging Face Hub access. Needed for most Swift LLM apps that load models from the Hub. _Hub scheme_ | — | passed (Xcode 27.1, 2026-11-21) | Apache-2.0 | active | 1,366 |

## Speech

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | C/C++ port of OpenAI's Whisper. Widely used on mobile; usable from Swift via C interop. | — | not tested | MIT | active | 55,383 |
| [argmaxinc/argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) | On-device speech AI for Apple silicon (formerly WhisperKit). WhisperAX example builds on Xcode 27.1. Swift-native option for on-device transcription. _WhisperAX example, iOS Simulator_ | — | passed (Xcode 27.1, 2026-11-21) | MIT | active | 6,469 |

## Evals and benchmarks

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [dromerosm/fm-smishing-bench](https://github.com/dromerosm/fm-smishing-bench) | Reproducible benchmark of Foundation Models on SMS scam detection. A public eval for on-device LLM output. | iOS 27 | not tested | MIT | active | 1 |

## Curated lists

| Project | What it does | Min iOS | Build | License | Status | Stars |
|---|---|---|---|---|---|---|
| [tucan9389/awesome-ml-demos-with-ios](https://github.com/tucan9389/awesome-ml-demos-with-ios) _(stale)_ | Sample projects running ML models on iOS. Last pushed 2021; useful for patterns, not current APIs. | — | not tested | MIT | stale | 1,293 |
| [onmyway133/awesome-machine-learning](https://github.com/onmyway133/awesome-machine-learning) | Curated ML resources with a Core ML focus. Active. | — | — | MIT | active | 814 |

## Contributing

Not sure which option to use? See [COMPARISON.md](COMPARISON.md).

Adding a project? See [CONTRIBUTING.md](CONTRIBUTING.md).
