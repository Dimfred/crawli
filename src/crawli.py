import asyncio

import typer
from crawl4ai import AsyncWebCrawler

app = typer.Typer()


@app.command()
def crawl(url: str):
    async def main(url: str):
        async with AsyncWebCrawler(verbose=False) as crawler:
            result = await crawler.arun(url=url)
        print(result.markdown_v2.raw_markdown)

    asyncio.run(main(url))


if __name__ == "__main__":
    app()
