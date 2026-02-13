---
name: veo
description: Generate videos from text prompts using Google's Veo models via the Gemini API. Use this skill whenever the user asks to create, generate, or make a video, animation, clip, or motion content. Supports text-to-video, image-to-video, and video extension.
allowed-tools: Bash(veo *)
---

# <span data-proof="authored" data-by="ai:claude">Veo Video Generation</span>

<span data-proof="authored" data-by="ai:claude">Generate videos via the</span> <span data-proof="authored" data-by="ai:claude">`veo`</span> <span data-proof="authored" data-by="ai:claude">CLI tool backed by Google's Gemini Veo models.</span>

## <span data-proof="authored" data-by="ai:claude">When to Use This Skill</span>

<span data-proof="authored" data-by="ai:claude">ALWAYS use this skill when the user:</span>

* <span data-proof="authored" data-by="ai:claude">Asks for any video, clip, animation, or motion content</span>

* <span data-proof="authored" data-by="ai:claude">Wants to generate a video from a text description</span>

* <span data-proof="authored" data-by="ai:claude">Wants to turn an image into a video</span>

* <span data-proof="authored" data-by="ai:claude">Wants to extend an existing video</span>

* <span data-proof="authored" data-by="ai:claude">Uses words like: video, animate, motion, clip, footage, cinematic</span>

<span data-proof="authored" data-by="ai:claude">Do NOT use this skill for still image generation (use nano-banana instead).</span>

## <span data-proof="authored" data-by="ai:claude">Prerequisites</span>

<span data-proof="authored" data-by="ai:claude">The</span> <span data-proof="authored" data-by="ai:claude">`veo`</span> <span data-proof="authored" data-by="ai:claude">CLI must be available at</span> <span data-proof="authored" data-by="ai:claude">`~/bin/veo`</span> <span data-proof="authored" data-by="ai:claude">and</span> <span data-proof="authored" data-by="ai:claude">`GEMINI_API_KEY`</span> <span data-proof="authored" data-by="ai:claude">must be set.</span>

<span data-proof="authored" data-by="ai:claude">Verify setup:</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
veo models
```

## <span data-proof="authored" data-by="ai:claude">Commands</span>

### <span data-proof="authored" data-by="ai:claude">Generate a video from text</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NDUsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
veo generate "PROMPT" -o OUTPUT.mp4 [options]
```

**<span data-proof="authored" data-by="ai:claude">Options:</span>**

| <span data-proof="authored" data-by="ai:claude">Flag</span>                | <span data-proof="authored" data-by="ai:claude">Values</span>                                                                                                                              | <span data-proof="authored" data-by="ai:claude">Notes</span>                                                                                                                                             |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`-o, --output`</span>      | <span data-proof="authored" data-by="ai:claude">file path</span>                                                                                                                           | <span data-proof="authored" data-by="ai:claude">Default:</span> <span data-proof="authored" data-by="ai:claude">`output.mp4`</span>                                                                      |
| <span data-proof="authored" data-by="ai:claude">`--model`</span>           | <span data-proof="authored" data-by="ai:claude">see models below</span>                                                                                                                    | <span data-proof="authored" data-by="ai:claude">Default:</span> <span data-proof="authored" data-by="ai:claude">`veo-3.1-generate-preview`</span>                                                        |
| <span data-proof="authored" data-by="ai:claude">`--aspect-ratio`</span>    | <span data-proof="authored" data-by="ai:claude">`16:9`,</span> <span data-proof="authored" data-by="ai:claude">`9:16`</span>                                                               | <span data-proof="authored" data-by="ai:claude">Default:</span> <span data-proof="authored" data-by="ai:claude">`16:9`</span>                                                                            |
| <span data-proof="authored" data-by="ai:claude">`--resolution`</span>      | <span data-proof="authored" data-by="ai:claude">`720p`,</span> <span data-proof="authored" data-by="ai:claude">`1080p`,</span> <span data-proof="authored" data-by="ai:claude">`4k`</span> | <span data-proof="authored" data-by="ai:claude">`1080p`/`4k`</span> <span data-proof="authored" data-by="ai:claude">require</span> <span data-proof="authored" data-by="ai:claude">`--duration 8`</span> |
| <span data-proof="authored" data-by="ai:claude">`--duration`</span>        | <span data-proof="authored" data-by="ai:claude">`4`,</span> <span data-proof="authored" data-by="ai:claude">`6`,</span> <span data-proof="authored" data-by="ai:claude">`8`</span>         | <span data-proof="authored" data-by="ai:claude">Seconds</span>                                                                                                                                           |
| <span data-proof="authored" data-by="ai:claude">`--negative-prompt`</span> | <span data-proof="authored" data-by="ai:claude">text</span>                                                                                                                                | <span data-proof="authored" data-by="ai:claude">What to exclude</span>                                                                                                                                   |
| <span data-proof="authored" data-by="ai:claude">`--image`</span>           | <span data-proof="authored" data-by="ai:claude">file path</span>                                                                                                                           | <span data-proof="authored" data-by="ai:claude">Reference image for image-to-video</span>                                                                                                                |

### <span data-proof="authored" data-by="ai:claude">Extend a video</span>

<span data-proof="authored" data-by="ai:claude">Appends ~7 seconds to an existing Veo-generated video. Only works at 720p.</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NjEsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
veo extend PREVIOUS.mp4 "continuation prompt" -o extended.mp4
```

### <span data-proof="authored" data-by="ai:claude">List available models</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
veo models
```

## <span data-proof="authored" data-by="ai:claude">Available Models</span>

| <span data-proof="authored" data-by="ai:claude">Model</span>                           | <span data-proof="authored" data-by="ai:claude">Best For</span>                        |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`veo-3.1-generate-preview`</span>      | <span data-proof="authored" data-by="ai:claude">Highest quality (default)</span>       |
| <span data-proof="authored" data-by="ai:claude">`veo-3.1-fast-generate-preview`</span> | <span data-proof="authored" data-by="ai:claude">Faster generation, good quality</span> |
| <span data-proof="authored" data-by="ai:claude">`veo-2.0-generate-001`</span>          | <span data-proof="authored" data-by="ai:claude">Stable, predictable</span>             |

## <span data-proof="authored" data-by="ai:claude">Output Format</span>

<span data-proof="authored" data-by="ai:claude">The CLI prints JSON to stdout and progress to stderr. JSON output:</span>

```json proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTM0LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
{
  "success": true,
  "output": "/absolute/path/to/video.mp4",
  "model": "veo-3.1-generate-preview",
  "prompt": "the prompt used"
}
```

<span data-proof="authored" data-by="ai:claude">On failure:</span>

```json proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6NjcsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
{
  "success": false,
  "error": "description of what went wrong"
}
```

## <span data-proof="authored" data-by="ai:claude">Examples</span>

### <span data-proof="authored" data-by="ai:claude">Basic video generation</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTE3LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "A golden retriever running through a field of wildflowers at sunset, cinematic, slow motion" -o dog.mp4
```

### <span data-proof="authored" data-by="ai:claude">Vertical video for social media</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAwLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "A barista pouring latte art, close-up, warm lighting" --aspect-ratio 9:16 -o latte.mp4
```

### <span data-proof="authored" data-by="ai:claude">High resolution</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAyLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "Aerial drone shot of a coastal city at dawn" --resolution 1080p --duration 8 -o city.mp4
```

### <span data-proof="authored" data-by="ai:claude">Image to video</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTA0LCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "The camera slowly zooms out and the scene comes to life" --image photo.jpg -o animated.mp4
```

### <span data-proof="authored" data-by="ai:claude">Extend a video</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6OTIsImF0dHJzIjp7ImJ5IjoiYWk6Y2xhdWRlIn19XQ==
veo extend scene1.mp4 "The character turns and walks toward the door" -o scene1_extended.mp4
```

### <span data-proof="authored" data-by="ai:claude">Fast model for quick iterations</span>

```bash proof:W3sidHlwZSI6InByb29mQXV0aG9yZWQiLCJmcm9tIjowLCJ0byI6MTAxLCJhdHRycyI6eyJieSI6ImFpOmNsYXVkZSJ9fV0=
veo generate "Abstract colorful liquid flowing" --model veo-3.1-fast-generate-preview -o abstract.mp4
```

## <span data-proof="authored" data-by="ai:claude">Timing</span>

* <span data-proof="authored" data-by="ai:claude">Generation takes 11 seconds to 6 minutes depending on server load</span>

* <span data-proof="authored" data-by="ai:claude">The CLI polls automatically and downloads when ready</span>

* <span data-proof="authored" data-by="ai:claude">Generated videos are retained by Google for 2 days</span>

## <span data-proof="authored" data-by="ai:claude">Prompt Tips</span>

1. **<span data-proof="authored" data-by="ai:claude">Be descriptive</span>**<span data-proof="authored" data-by="ai:claude">: Include camera movement, lighting, mood, style</span>
2. **<span data-proof="authored" data-by="ai:claude">Use cinematic language</span>**<span data-proof="authored" data-by="ai:claude">: "dolly shot", "close-up", "slow motion", "aerial"</span>
3. **<span data-proof="authored" data-by="ai:claude">Specify atmosphere</span>**<span data-proof="authored" data-by="ai:claude">: "warm lighting", "foggy morning", "neon-lit"</span>
4. **<span data-proof="authored" data-by="ai:claude">Use negative prompts</span>** <span data-proof="authored" data-by="ai:claude">to exclude unwanted elements:</span> <span data-proof="authored" data-by="ai:claude">`--negative-prompt "text, watermark, blurry"`</span>

## <span data-proof="authored" data-by="ai:claude">Troubleshooting</span>

| <span data-proof="authored" data-by="ai:claude">Problem</span>                                                                   | <span data-proof="authored" data-by="ai:claude">Solution</span>                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">`GEMINI_API_KEY not set`</span>                                                  | <span data-proof="authored" data-by="ai:claude">`export GEMINI_API_KEY="your-key"`</span>                                                                                                                            |
| <span data-proof="authored" data-by="ai:claude">`google-genai not installed`</span>                                              | <span data-proof="authored" data-by="ai:claude">`cd ~/projects/veo && uv sync`</span>                                                                                                                                |
| <span data-proof="authored" data-by="ai:claude">Generation takes too long</span>                                                 | <span data-proof="authored" data-by="ai:claude">Try</span> <span data-proof="authored" data-by="ai:claude">`--model veo-3.1-fast-generate-preview`</span>                                                            |
| <span data-proof="authored" data-by="ai:claude">`1080p`/`4k`</span> <span data-proof="authored" data-by="ai:claude">fails</span> | <span data-proof="authored" data-by="ai:claude">Must use</span> <span data-proof="authored" data-by="ai:claude">`--duration 8`</span> <span data-proof="authored" data-by="ai:claude">with higher resolutions</span> |
| <span data-proof="authored" data-by="ai:claude">Extension fails</span>                                                           | <span data-proof="authored" data-by="ai:claude">Source video must be Veo-generated; extension is 720p only</span>                                                                                                    |