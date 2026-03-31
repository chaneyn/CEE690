CXX      = g++
CXXFLAGS = -Wall -std=c++17
LIBNAME  = libgravity.a
LIB_DIR =  ./lib
INC_DIR  = ./include

# The final program depends on the LIBRARY, not the .cpp
gravity.exe: main.o $(LIB_DIR)/$(LIBNAME)
	$(CXX) main.o -o gravity.exe -I$(INC_DIR) -L$(LIB_DIR) -lgravity

# Rule to create the static library
$(LIB_DIR)/$(LIBNAME): gravity.o
	ar rcs $(LIB_DIR)/$(LIBNAME) gravity.o

# Individual object files
main.o: main.cpp $(INC_DIR)/gravity.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp -I$(INC_DIR)

gravity.o: gravity.cpp $(INC_DIR)/gravity.hpp
	$(CXX) $(CXXFLAGS) -c gravity.cpp -I$(INC_DIR)

clean:
	rm -f *.o *.a gravity.exe


