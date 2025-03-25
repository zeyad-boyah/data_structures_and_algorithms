CC = gcc

# Compiler flags:
# -Wall enables all warnings,
# -Wextra enables extra warnings,
# -std=c99 tells the compiler to use the C99 standard.
CFLAGS = -Wall -Wextra -std=c99

# Name of the executable target
TARGET = hash_tables

# Default target: compile the target executable
all: $(TARGET)

# Rule to build the executable from object file(s)
$(TARGET): hash_tables.o
	$(CC) $(CFLAGS) -o $(TARGET) hash_tables.o

# Rule to compile hash_tables.c into an object file
hash_tables.o: hash_tables.c
	$(CC) $(CFLAGS) -c hash_tables.c

# Clean up build artifacts (object files and executable)
clean:
	rm -f $(TARGET) *.o
