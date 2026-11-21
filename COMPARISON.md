# Which on-device AI option for iOS?

Quick comparison of Apple's and open-source options. Rows marked _(verify)_ come from iOS 27 material that may change before release.

| | Foundation Models | Core AI _(verify)_ | Core ML | MLX Swift |
|---|---|---|---|---|
| Introduced | iOS 26 | iOS 27 | iOS 11 (2017) | Open source, Apple silicon |
| Minimum OS | iOS 26 | iOS 27 | iOS 11 | iOS 17 (mlx-swift-lm) |
| Model source | Apple's built-in on-device LLM only | Your own, exported to `.aimodel` | Your own, converted with coremltools | Your own, usually from Hugging Face |
| Runs on | Devices with Apple Intelligence | CPU, GPU, Neural Engine | CPU, GPU, Neural Engine | GPU via Metal |
| Cloud option | Private Cloud Compute: 32K context, needs a managed entitlement, daily per-user limit | No | No | No |
| On-device context | About 4K tokens | Model-dependent | Model-dependent | Model-dependent |
| Structured output and tools | Yes (guided generation, tool calling) | Model-dependent | No built-in support | Grammar-constrained generation via MLXGuidedGeneration |
| Fine-tuning | No | No | Limited | Yes (LoRA and full fine-tuning) |
| Cost | No per-token fee on-device | No per-token fee | No per-token fee | No per-token fee |
| Best for | Adding AI features to apps on Apple Intelligence devices | Custom models on the newest OS | Shipping existing models to older iOS | Experimenting with and fine-tuning LLMs and VLMs |

## Choosing

- Need a built-in model with no setup: **Foundation Models**.
- Need a specific open model on iOS 27+: **Core AI**.
- Need to support iOS 17 to 25, or a model you already converted: **Core ML**.
- Need fine-tuning or the latest open LLM architectures: **MLX Swift**.

## Sources

- [Foundation Models framework](https://developer.apple.com/documentation/foundationmodels)
- [Core AI Models repo](https://github.com/apple/coreai-models)
- [mlx-swift-lm](https://github.com/ml-explore/mlx-swift-lm)
- [mlx-swift](https://github.com/ml-explore/mlx-swift)
