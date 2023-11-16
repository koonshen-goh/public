// Compiled with g++, c++17
#include <string>
#include <cassert>

std::string reverse_words(const std::string &str)
{
    // TODO: Implement this function
    return "???";
}

void test_empty() {
    std::string test_str = "";
    assert(reverse_words(test_str) == "");
}

void test_simple() {
    std::string test_str = "reversed";
    assert(reverse_words(test_str) == "desrever");
}

void test_multiple() {
    std::string test_str = "String to be reversed";
    assert(reverse_words(test_str) == "gnirtS ot eb desrever");
}

void test_alphanumeric() {
    std::string test_str = "fe80::1ff:fe23:4567:890a";
    assert(reverse_words(test_str) == "08ef::ff1:32ef:7654:a098");
}

void test_complex() {
    std::string test_str = "String; 2be reversed...";
    assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
}

void test_all() {
    test_empty();
    test_simple();
    test_multiple();
    test_alphanumeric();
    test_complex();
}

int main()
{
    test_all();
    // std::string test_str = "String; 2be reversed...";
    // assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
    return 0;
}
