

g++ "-IF:\\Drive\\System Files\\SFML-2.5.1\\include" -O0 -g3 -Wall -c -fmessage-length=0 -o Bubble.o "..\\Bubble.cpp" 
g++ "-IF:\\Drive\\System Files\\SFML-2.5.1\\include" -O0 -g3 -Wall -c -fmessage-length=0 -o main.o "..\\main.cpp" 
g++ "-LF:\\Drive\\System Files\\SFML-2.5.1\\lib" -o "Set8 Code.exe" Bubble.o main.o -lsfml-graphics -lsfml-window -lsfml-system 