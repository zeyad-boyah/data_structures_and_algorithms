CC = gcc
CFLAGS = -Wall -Wextra -std=c99

SRC = src/c/linked_lists/linked_list.c
TEST = tests/linked_list_test.c
TARGET = linked_list_test

all: $(TARGET)

$(TARGET): $(SRC) $(TEST)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC) $(TEST)

clean:
	rm -f $(TARGET)
