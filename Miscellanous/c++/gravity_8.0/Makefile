CXX      = g++
CXXFLAGS = -Wall -std=c++17
LIBNAME  = ./lib/libgravity.a

# The final program depends on the LIBRARY, not the .cpp
gravity_static.exe: main.o $(LIBNAME)
	$(CXX) main.o -o gravity.exe -L./lib -lgravity

# Rule to create the static library
$(LIBNAME): gravity.o
	ar rcs $(LIBNAME) gravity.o

# Individual object files
main.o: main.cpp gravity.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

gravity.o: gravity.cpp gravity.hpp
	$(CXX) $(CXXFLAGS) -c gravity.cpp

clean:
	rm -f *.o *.a gravity.exe
