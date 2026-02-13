# <span data-proof="authored" data-by="ai:claude">Veo - Gemini Video Generation CLI</span>

## <span data-proof="authored" data-by="ai:claude">Quick Start</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6OTYsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
export GEMINI_API_KEY="your-key-here"
uv run veo generate "A cat riding a skateboard" -o cat.mp4
```

## <span data-proof="authored" data-by="ai:claude">Commands</span>

### <span data-proof="authored" data-by="ai:claude">Generate video from text</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NTIsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
uv run veo generate "prompt" -o output.mp4 [options]
```

<span data-proof="authored" data-by="ai:claude">Options:</span> <span data-proof="authored" data-by="ai:claude">`--model`,</span> <span data-proof="authored" data-by="ai:claude">`--aspect-ratio 16:9|9:16`,</span> <span data-proof="authored" data-by="ai:claude">`--resolution 720p|1080p|4k`,</span> <span data-proof="authored" data-by="ai:claude">`--duration 4|6|8`,</span> <span data-proof="authored" data-by="ai:claude">`--negative-prompt`,</span> <span data-proof="authored" data-by="ai:claude">`--image path`</span>

### <span data-proof="authored" data-by="ai:claude">Generate video from image + text</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NzgsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
uv run veo generate "prompt describing motion" --image photo.jpg -o output.mp4
```

### <span data-proof="authored" data-by="ai:claude">Extend a video</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NjgsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
uv run veo extend previous.mp4 "continuation prompt" -o extended.mp4
```

### <span data-proof="authored" data-by="ai:claude">List models</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTcsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
uv run veo models
```

## <span data-proof="authored" data-by="ai:claude">Agent Usage Notes</span>

* <span data-proof="authored" data-by="ai:claude">All output is JSON on stdout, progress/errors on stderr</span>

* <span data-proof="authored" data-by="ai:claude">Exit code 0 = success, 1 = failure</span>

* <span data-proof="authored" data-by="ai:claude">JSON output includes</span> <span data-proof="authored" data-by="ai:claude">`success`,</span> <span data-proof="authored" data-by="ai:claude">`output`</span> <span data-proof="authored" data-by="ai:claude">(absolute path),</span> <span data-proof="authored" data-by="ai:claude">`model`,</span> <span data-proof="authored" data-by="ai:claude">`prompt`</span>

* <span data-proof="authored" data-by="ai:claude">Video generation takes 11s-6min depending on load</span>

* <span data-proof="authored" data-by="ai:claude">Generated videos are retained by Google for 2 days</span>

* <span data-proof="authored" data-by="ai:claude">1080p/4k require</span> <span data-proof="authored" data-by="ai:claude">`--duration 8`</span>

* <span data-proof="authored" data-by="ai:claude">Video extension only works at 720p</span>