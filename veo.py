#!/usr/bin/env python3
"""CLI tool for generating videos with Gemini's Veo models.

Designed for agent use: JSON output on stdout, progress on stderr.

Usage:
    veo generate "A cat riding a skateboard" -o cat.mp4
    veo generate "Ocean waves at sunset" --model veo-3.1-fast-generate-preview --aspect-ratio 9:16
    veo generate "A dialogue between two robots" --duration 8 --resolution 1080p
    veo extend cat.mp4 "The cat does a kickflip" -o cat_extended.mp4
"""

import argparse
import json
import os
import pathlib
import sys
import time
import urllib.request


def log(msg):
    print(msg, file=sys.stderr)


def get_client():
    try:
        from google import genai
    except ImportError:
        log("Error: google-genai not installed. Run: pip install google-genai")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        log("Error: GEMINI_API_KEY environment variable not set")
        sys.exit(1)

    return genai.Client(api_key=api_key)


def wait_for_operation(client, operation, poll_interval=10):
    elapsed = 0
    while not operation.done:
        log(f"  Generating video... ({elapsed}s elapsed)")
        time.sleep(poll_interval)
        elapsed += poll_interval
        operation = client.operations.get(operation)
    return operation


def download_video(client, generated_video, output_path):
    """Download a generated video to disk.

    Tries the SDK download first, falls back to direct URI download
    if the result is suspiciously small (<500KB for a video).
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    video_uri = generated_video.video.uri if generated_video.video else None

    log(f"  Downloading video to {output_path}...")
    if video_uri:
        log(f"  Video URI: {video_uri}")

    # Try SDK download first
    data = client.files.download(file=generated_video)
    size_kb = len(data) / 1024

    if size_kb >= 500:
        log(f"  SDK download: {size_kb:.0f}KB")
        pathlib.Path(output_path).write_bytes(data)
        return

    # SDK returned suspiciously small data, try direct URI download
    log(f"  SDK download too small ({size_kb:.0f}KB), trying direct URI download...")
    if not video_uri or not api_key:
        log(f"  Warning: No URI or API key for fallback, using SDK result ({size_kb:.0f}KB)")
        pathlib.Path(output_path).write_bytes(data)
        return

    req = urllib.request.Request(video_uri)
    req.add_header("x-goog-api-key", api_key)
    with urllib.request.urlopen(req) as resp:
        direct_data = resp.read()

    direct_size_kb = len(direct_data) / 1024
    log(f"  Direct download: {direct_size_kb:.0f}KB")

    # Use whichever is larger
    if len(direct_data) > len(data):
        pathlib.Path(output_path).write_bytes(direct_data)
    else:
        pathlib.Path(output_path).write_bytes(data)


def cmd_generate(args):
    from google.genai import types

    client = get_client()

    config_kwargs = {}
    if args.aspect_ratio:
        config_kwargs["aspect_ratio"] = args.aspect_ratio
    if args.resolution:
        config_kwargs["resolution"] = args.resolution
    if args.duration:
        config_kwargs["duration_seconds"] = args.duration
    if args.negative_prompt:
        config_kwargs["negative_prompt"] = args.negative_prompt

    generate_kwargs = {
        "model": args.model,
        "prompt": args.prompt,
    }

    if args.image:
        from google.genai.types import Image
        log(f"  Loading reference image: {args.image}")
        img = Image.from_file(args.image)
        generate_kwargs["image"] = img

    if config_kwargs:
        generate_kwargs["config"] = types.GenerateVideosConfig(**config_kwargs)

    log(f"  Model: {args.model}")
    log(f"  Prompt: {args.prompt}")
    if config_kwargs:
        log(f"  Config: {json.dumps({k: str(v) for k, v in config_kwargs.items()})}")

    log("  Submitting video generation request...")
    operation = client.models.generate_videos(**generate_kwargs)

    operation = wait_for_operation(client, operation)

    if not operation.response or not operation.response.generated_videos:
        result = {"success": False, "error": "No video generated"}
        print(json.dumps(result))
        sys.exit(1)

    video = operation.response.generated_videos[0]
    output_path = args.output or "output.mp4"

    download_video(client, video, output_path)

    result = {
        "success": True,
        "output": os.path.abspath(output_path),
        "model": args.model,
        "prompt": args.prompt,
    }
    print(json.dumps(result))


def cmd_extend(args):
    from google.genai import types

    client = get_client()

    if not os.path.exists(args.video):
        log(f"Error: Video file not found: {args.video}")
        sys.exit(1)

    log(f"  Uploading video: {args.video}")
    uploaded = client.files.upload(file=args.video)

    log(f"  Model: {args.model}")
    log(f"  Prompt: {args.prompt}")
    log("  Submitting video extension request...")

    operation = client.models.generate_videos(
        model=args.model,
        prompt=args.prompt,
        video=uploaded,
        config=types.GenerateVideosConfig(resolution="720p"),
    )

    operation = wait_for_operation(client, operation)

    if not operation.response or not operation.response.generated_videos:
        result = {"success": False, "error": "No video generated"}
        print(json.dumps(result))
        sys.exit(1)

    video = operation.response.generated_videos[0]
    output_path = args.output or "extended.mp4"

    download_video(client, video, output_path)

    result = {
        "success": True,
        "output": os.path.abspath(output_path),
        "model": args.model,
        "prompt": args.prompt,
        "source_video": os.path.abspath(args.video),
    }
    print(json.dumps(result))


def cmd_models(args):
    models = [
        {
            "id": "veo-3.1-generate-preview",
            "description": "Latest Veo model, highest quality",
            "features": ["text-to-video", "image-to-video", "video-extension", "reference-images"],
        },
        {
            "id": "veo-3.1-fast-generate-preview",
            "description": "Speed-optimized Veo 3.1",
            "features": ["text-to-video", "image-to-video"],
        },
        {
            "id": "veo-2.0-generate-001",
            "description": "Stable Veo 2.0",
            "features": ["text-to-video", "image-to-video"],
        },
    ]
    print(json.dumps(models, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Generate videos with Gemini Veo models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Set GEMINI_API_KEY environment variable before use.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate
    gen = subparsers.add_parser("generate", help="Generate a video from a text prompt")
    gen.add_argument("prompt", help="Text description of the video to generate")
    gen.add_argument("-o", "--output", help="Output file path (default: output.mp4)")
    gen.add_argument(
        "--model",
        default="veo-3.1-generate-preview",
        help="Model ID (default: veo-3.1-generate-preview)",
    )
    gen.add_argument(
        "--aspect-ratio",
        choices=["16:9", "9:16"],
        help="Aspect ratio (default: 16:9)",
    )
    gen.add_argument(
        "--resolution",
        choices=["720p", "1080p", "4k"],
        help="Resolution (default: 720p). 1080p/4k require --duration 8",
    )
    gen.add_argument(
        "--duration",
        type=int,
        choices=[4, 6, 8],
        help="Duration in seconds (default: model decides)",
    )
    gen.add_argument("--negative-prompt", help="Describe what to exclude from the video")
    gen.add_argument("--image", help="Path to a reference image for image-to-video generation")
    gen.set_defaults(func=cmd_generate)

    # extend
    ext = subparsers.add_parser("extend", help="Extend a previously generated Veo video")
    ext.add_argument("video", help="Path to the Veo-generated video to extend")
    ext.add_argument("prompt", help="Text description for the continuation")
    ext.add_argument("-o", "--output", help="Output file path (default: extended.mp4)")
    ext.add_argument(
        "--model",
        default="veo-3.1-generate-preview",
        help="Model ID (default: veo-3.1-generate-preview)",
    )
    ext.set_defaults(func=cmd_extend)

    # models
    mdl = subparsers.add_parser("models", help="List available Veo models")
    mdl.set_defaults(func=cmd_models)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
