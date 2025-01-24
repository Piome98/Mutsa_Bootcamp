# 소켓 서버 프로그래밍:

from socket import *

# 서버 소켓 생성:
host = '127.0.0.1' # 자기 자신의 로컬 아이피
port = 12345 # 포트 번호 -> 프로그램 식별 번호

server_socket = socket(AF_INET, SOCK_STREAM) # 소켓 생성
server_socket.bind((host, port)) # 소켓에 주소 할당 -> 소켓과 포트의 연결
server_socket.listen(100) # 대기열을 100개로 제한, 매핑된 소켓을 클라이언트의 연결을 기다리는 상태로 전환

print('서버 소켓 생성 및 바인딩 완료')

# 클라이언트 소켓 대기:
client_socket, client_address = server_socket.accept() # 클라이언트 접속 대기 및 연결 수락

print(str(client_address) + '에서 접속이 확인되었습니다.')

data = client_socket.recv(1024) # 클라이언트로부터 데이터 수신
print('받은 데이터: ' + data.decode('utf-8'))

client_socket.sendall('안녕하세요, 서버에서 알려드립니다'.encode('utf-8')) # 클라이언트에게 데이터 송신

server_socket.close() # 소켓 닫기 -> 서버 소켓 생성 완료