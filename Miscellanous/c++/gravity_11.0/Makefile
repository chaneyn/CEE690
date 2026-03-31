CXX      = g++
# 1. ADDED -fPIC to the flags
CXXFLAGS = -Wall -std=c++17 -fPIC
# 2. CHANGED extension to .so
LIBNAME  = libgravity.so
LIB_DIR  = ./lib
INC_DIR  = ./include

# The final program depends on the LIBRARY, not the .cpp
# 3. ADDED the -Wl,-rpath flag for runtime searching
gravity_dynamic.exe: main.o $(LIB_DIR)/$(LIBNAME)
	$(CXX) main.o -o gravity.exe -I$(INC_DIR) -L$(LIB_DIR) -lgravity -Wl,-rpath,$(LIB_DIR)

# Rule to create the dynamic library
# 4. REPLACED 'ar' with 'g++ -shared'
$(LIB_DIR)/$(LIBNAME): gravity.o
	$(CXX) -shared -o $(LIB_DIR)/$(LIBNAME) gravity.o

# Individual object files
main.o: main.cpp $(INC_DIR)/gravity.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp -I$(INC_DIR)

gravity.o: gravity.cpp $(INC_DIR)/gravity.hpp
	$(CXX) $(CXXFLAGS) -c gravity.cpp -I$(INC_DIR)

clean:
	# 5. UPDATED clean to target .so and the new exe name
	rm -f *.o $(LIB_DIR)/*.so gravity_dynamic.exe


