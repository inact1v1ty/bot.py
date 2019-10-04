import sys
import asyncio

sys.path.append('../')

from bot import Bot, types  # noqa: E420


async def run():
    async with Bot('') as b:
        b: Bot
        user = await b.get_me()

        print(user)

        @b.inline_query_handler()
        async def query(inline_query):
            try:
                r = types.InlineQueryResultArticle(
                    '1',
                    'Test',
                    types.InputTextMessageContent('Some text')
                )

                await b.answer_inline_query(
                    inline_query.id,
                    [r])

            except Exception as e:
                print(e)

        await b.polling()


asyncio.get_event_loop().run_until_complete(run())
