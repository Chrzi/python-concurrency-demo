import asyncio
from asyncio import StreamWriter, StreamReader


async def handle_client(reader: StreamReader, writer: StreamWriter):
    received = await reader.readline()
    print(f"S: {received}")
    writer.write(received)
    await writer.drain()

    #close connection
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, host="localhost", port=1234)

    # client code
    c_reader, c_writer = await asyncio.open_connection(host="localhost", port=1234)
    text = input("What do you want to send? ") + "\n"

    c_writer.write(text.encode())
    await c_writer.drain()
    print(f"C: {await c_reader.readline()}")
    c_writer.close()
    await c_writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
