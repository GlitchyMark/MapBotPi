CC = g++ -std=c++11 -Wall

all: mapbot_pi

mapbot_pi: main.o Message.o SerialPortCommunicator.o SerialPortEnumerator.o MessageCodec.o GameDirector.o UDPServer.o serial/serial.o serial/impl/unix.o
	$(CC) -o gamelogic main.o Message.o SerialPortCommunicator.o SerialPortEnumerator.o MessageCodec.o GameDirector.o UDPServer.o serial/serial.o serial/impl/unix.o

main.o:
	$(CC) -c -o main.o main.cpp

robot.o:
	$(CC) -c -o robot.o robot.cpp

serial/serial.o:
	$(CC) -c -o serial/serial.o serial/serial.cc

serial/impl/unix.o:
	$(CC) -c -o serial/impl/unix.o serial/impl/unix.cc

clean:
	rm -f *.o serial/*.o serial/impl/*.o mapbot_pi
