# Awesome iOS AI

Curated iOS on-device and Apple AI resources. Status is checked weekly.

## Core AI

- [apple/coreai-models](https://github.com/apple/coreai-models) - Apple's official Core AI export recipes, Python primitives and Swift runtime utilities. Requires iOS/macOS 27 and Xcode 27. Not accepting PRs at launch.
- [john-rocky/coreai-model-zoo](https://github.com/john-rocky/coreai-model-zoo) - Swift-focused model zoo converting open LLMs (e.g., Qwen3.5, Gemma 4) to Core AI. The most active community zoo found.
- [CYBRTRK2/coreai-model-zoo](https://github.com/CYBRTRK2/coreai-model-zoo) - Community zoo listing 66 Core AI models across LLM, VLM, OCR, ASR, TTS and image/video. Newer and low adoption; verify model quality before use.

## Core ML

- [apple/coremltools](https://github.com/apple/coremltools) - Apple's Python tools to convert, edit and validate Core ML models from PyTorch and TensorFlow. Start here for any conversion.
- [john-rocky/CoreML-Models](https://github.com/john-rocky/CoreML-Models) - Model zoo of PyTorch models converted to ready-to-use .mlpackage files for iOS/macOS, with conversion notes per model. Updated this week.
- [apple-aiml-research/ml-stable-diffusion](https://github.com/apple-aiml-research/ml-stable-diffusion) - Apple's reference for running Stable Diffusion with Core ML on Apple silicon, including a Swift package.
- [apple-aiml-research/ml-ane-transformers](https://github.com/apple-aiml-research/ml-ane-transformers) - Reference Transformer implementation optimized for the Apple Neural Engine. Use when latency or battery matters for a Core ML model.
- [huggingface/swift-coreml-diffusers](https://github.com/huggingface/swift-coreml-diffusers) - Swift app demonstrating Core ML Stable Diffusion. Archived, so use Apple's ml-stable-diffusion for current code. _(stale)_
- [likedan/Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) - Large curated index of Core ML models. Last pushed June 2025; many links may be dead. _(stale)_

## Curated lists

- [tucan9389/awesome-ml-demos-with-ios](https://github.com/tucan9389/awesome-ml-demos-with-ios) - Sample projects running ML models on iOS. Last pushed 2021; useful for patterns, not current APIs. _(stale)_
- [onmyway133/awesome-machine-learning](https://github.com/onmyway133/awesome-machine-learning) - Curated ML resources with a Core ML focus. Active.

## Evals and benchmarks

- [dromerosm/fm-smishing-bench](https://github.com/dromerosm/fm-smishing-bench) - Reproducible benchmark of Foundation Models on SMS scam detection. One of the few public evals for on-device LLM output. Low adoption.

## Foundation Models

- [huggingface/AnyLanguageModel](https://github.com/huggingface/AnyLanguageModel) - Drop-in, API-compatible replacement for Apple's Foundation Models framework that adds other backends. Use it to test or ship beyond Apple Intelligence devices.
- [AppStorage/FoundationChat](https://github.com/AppStorage/FoundationChat) - SwiftUI chat app on Foundation Models (MIT). Requires iOS/macOS 26 and Xcode 26. Last pushed June 2025, so check it still builds. _(stale)_
- [artemnovichkov/HotdogApp](https://github.com/artemnovichkov/HotdogApp) - Small sample app built with Foundation Models ("Hotdog or Not Hotdog"). Good minimal reference for guided prompting.
- [AddikiPraveenKumar/foundation-models-ios-guide](https://github.com/AddikiPraveenKumar/foundation-models-ios-guide) - Written guide to the Foundation Models framework on iOS 26, focused on privacy-first features. Low adoption; check content against Apple's docs. _(stale)_
- [GijungKim/expo-local-llm](https://github.com/GijungKim/expo-local-llm) - Expo module running on-device LLMs via Foundation Models on iOS and Gemini Nano on Android. Use for cross-platform React Native apps.

## MLX

- [ml-explore/mlx-swift](https://github.com/ml-explore/mlx-swift) - Swift API for Apple's MLX array framework on Apple silicon. Base layer for the LLM packages below.
- [ml-explore/mlx-swift-lm](https://github.com/ml-explore/mlx-swift-lm) - Run and fine-tune LLMs and VLMs in Swift. iOS 17+. Includes an MLXFoundationModels bridge for Apple's LanguageModelSession.
- [ml-explore/mlx-swift-examples](https://github.com/ml-explore/mlx-swift-examples) - Runnable iOS and macOS sample apps: MLXChatExample, LLMEval, StableDiffusionExample.

## Runtimes

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ LLM inference for GGUF models; the most widely used local runtime. Build for iOS and call from Swift via C interop.
- [mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm) - Compiled LLM deployment engine that targets iOS and other platforms. Use when you need one compiled model across devices.
- [huggingface/swift-transformers](https://github.com/huggingface/swift-transformers) - Swift package for tokenizers and Hugging Face Hub access. Needed for most Swift LLM apps that load models from the Hub.

## Speech

- [argmaxinc/argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) - On-device speech AI for Apple silicon (formerly WhisperKit). Strongest Swift-native option for transcription on iPhone.
- [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) - C/C++ port of OpenAI's Whisper. Widely used on mobile; usable from Swift via C interop.

## Contributing

Not sure which to use? See [COMPARISON.md](COMPARISON.md).

See [CONTRIBUTING.md](CONTRIBUTING.md).
