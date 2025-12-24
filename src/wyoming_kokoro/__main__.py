import asyncio


async def main() -> None:
    print("Wyoming Kokoro is running...")


def run():
    asyncio.run(main())


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        pass