import asyncio
import argparse
import logging

from . import __version__


async def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--voice",
        required=True,
        help="Default Kokoro voice to use (e.g., af_heart)",
    )
    parser.add_argument("--uri", default="stdio://", help="unix:// or tcp://")
    #
    parser.add_argument(
        "--zeroconf",
        nargs="?",
        const="kokoro",
        help="Enable discovery over zeroconf with optional name (default: kokoro)", # noqa
    )
    #
    parser.add_argument(
        "--data-dir",
        required=True,
        action="append",
        help="Data directory to check for downloaded models",
    )
    parser.add_argument(
        "--download-dir",
        help="Directory to download voices into (default: first data dir)",
    )
    #
    parser.add_argument(
        "--speaker", type=str, help="Name or id of speaker for default voice"
    )
    parser.add_argument("--noise-scale", type=float, help="Generator noise")
    parser.add_argument("--length-scale", type=float, help="Phoneme length")
    parser.add_argument(
        "--noise-w-scale", "--noise-w", type=float, help="Phoneme width noise"
    )
    #
    parser.add_argument(
        "--auto-punctuation", 
        default=".?!", 
        help="Automatically add punctuation"
    )
    parser.add_argument("--samples-per-chunk", type=int, default=1024)
    parser.add_argument(
        "--no-streaming",
        action="store_true",
        help="Disable audio streaming on sentence boundaries",
    )
    #
    parser.add_argument(
        "--update-voices",
        action="store_true",
        help="Download latest voices.json during startup",
    )
    #
    parser.add_argument(
        "--use-cuda",
        action="store_true",
        help="Use CUDA if available (requires onnxruntime-gpu)",
    )
    #
    parser.add_argument(
        "--debug", 
        action="store_true", 
        help="Log DEBUG messages"
    )
    parser.add_argument(
        "--log-format", 
        default=logging.BASIC_FORMAT, 
        help="Format for log messages"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Print version and exit",
    )
    args = parser.parse_args()


def run():
    """Run the main entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        pass
