from socket import *

host = '127.0.0.1'
port = 12345

client_socket = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
client_socket.connect((host, port))  # 서버에 연결


# 클라이언트 소켓 대기:
client_socket, client_address = server_socket.accept() # 클라이언트 접속 대기 및 연결 수락

print(str(client_address) + '에서 접속이 확인되었습니다.')

data = client_socket.recv(1024) # 클라이언트로부터 데이터 수신
print('받은 데이터: ' + data.decode('utf-8'))

client_socket.sendall('안녕하세요, 서버에서 알려드립니다'.encode('utf-8')) # 클라이언트에게 데이터 송신

server_socket.close() # 소켓 닫기 -> 서버 소켓 생성 완료

# 데이터 송신
client_socket.sendall('안녕하세요, 클라이언트에서 보냅니다.'.encode('utf-8'))

# 데이터 수신
data = client_socket.recv(1024)
print('서버로부터 받은 데이터:', data.decode('utf-8'))

client_socket.close()  # 소켓 닫기
