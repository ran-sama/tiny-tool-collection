#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio, re

async def handler(reader, writer):
    try:
        while True:
            line = await reader.readline()
            if line:
                line = line.decode('latin1').partition('\r\n')[0]
                if re.match(r"^CONNECT.*|^DELETE.*|^GET.*|^HEAD.*|^OPTIONS.*|^PATCH.*|^POST.*|^PUT.*|^TRACE.*", line):
                    print(line)
            else:
                break
            writer.close()
    except ConnectionResetError:
        pass

async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 7890)
    async with server:
        await server.serve_forever()

asyncio.run(main())
