# Step 1: Link the object files into the final program
gravity.exe: main.o gravity.o
	g++ main.o gravity.o -o gravity.exe

# Step 2: Compile the driver
main.o: main.cpp gravity.hpp
	g++ -c main.cpp

# Step 3: Compile the math
gravity.o: gravity.cpp gravity.hpp
	g++ -c gravity.cpp

# Step 4: Add a way to reset
clean:
	rm -f *.o gravity.exe

