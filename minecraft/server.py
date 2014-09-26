import subprocess
import asyncio

			
class EchoServer(asyncio.Protocol):		
	def connection_made(self, transport):
		peername = transport.get_extra_info('peername')
		print('connection from {}'.format(peername))
		self.transport = transport
	
	def connection_lost(self, transport):
		self.transport.close()
	
	def data_received(self, data):
		data = data.decode()
		print('data received: {}'.format(data))
		process.stdin.write((data + '\n').encode())
		process.stdin.flush()

	
if __name__ == "__main__":
	mc = "java -jar minecraft_server.jar nogui"
	process = subprocess.Popen(mc, stdin = subprocess.PIPE)
	
	loop = asyncio.get_event_loop()
	coro = loop.create_server(EchoServer, '', 9090)
	server = loop.run_until_complete(coro)
	
	print('serving on {}'.format(server.sockets[0].getsockname()))
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		print("exit")
	finally:
		process.kill()
		server.close()
		loop.close()
