import asyncio
import tornado.web

data = dict()

from handlers import (
  HelloWorld
)

def make_app():
  return tornado.web.Application([
    (r"/data", HelloWorld, dict(data = data)),
    (r"/data/([^/]+)?", HelloWorld, dict(data = data)),
  ])

async def main():
  app = make_app()
  app.listen(8888)
  await asyncio.Event().wait()

if __name__ == "__main__":
  print('server has started.')
  asyncio.run(main())