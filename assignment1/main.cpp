// Compiled with g++, c++17
#include <string>
#include <cassert>

bool is_alphanumeric(char character) {
    // Assumes ASCII encoding
    return ('a' <= character && character <= 'z')
        || ('A' <= character && character <= 'Z') 
        || ('0' <= character && character <= '9');
}
// Use a unordered set for a more general use case, checking if character is in set

std::string reverse_words(const std::string &str)
{
    std::string result;
    uint strLen = str.length();
    uint wordStart = strLen;
    result.reserve(strLen);
    for (uint i = 0; i < strLen; ++i) {
        if (is_alphanumeric(str[i])) {
            if (wordStart == strLen) {
                // Start of new word, keep track of start position
                wordStart = i;
            }
            // Continue iterating until end of word
            continue;
        } else if (wordStart != strLen) {
            // End of word, append reversed substring to result
            const std::string substring = str.substr(wordStart, i - wordStart);
            result.append(substring.rbegin(), substring.rend());
            wordStart = strLen;
        }
        // Non alphanumeric character, append character to result
        result.push_back(str[i]);
    }
    // Special case, check if last word was not processed
    if (wordStart != strLen) {
        const std::string substring = str.substr(wordStart, strLen - wordStart);
        result.append(substring.rbegin(), substring.rend());
    }

    return result;
}

void test_empty() {
    std::string test_str = "";
    assert(reverse_words(test_str) == "");
}

void test_simple() {
    std::string test_str = "reversed";
    assert(reverse_words(test_str) == "desrever");
}

void test_specials() {
    std::string test_str = "?.[]^&#";
    assert(reverse_words(test_str) == "?.[]^&#");
}

void test_alphanumeric() {
    std::string test_str = "fe80:0000:01ff:fe23:4567:890a";
    assert(reverse_words(test_str) == "08ef:0000:ff10:32ef:7654:a098");
}

void test_single_sequences() {
    std::string test_str = "a.b[1].x+a.b[2].y";
    assert(reverse_words(test_str) == "a.b[1].x+a.b[2].y");
}

void test_multiple() {
    std::string test_str = "String to be reversed";
    assert(reverse_words(test_str) == "gnirtS ot eb desrever");
}

void test_multiple_specials() {
    std::string test_str = "[.:@(&\")]a(*&%(*&'))b_+(";
    assert(reverse_words(test_str) == "[.:@(&\")]a(*&%(*&'))b_+(");
}

void test_complex() {
    std::string test_str = "String; 2be reversed...";
    assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
}

void test_all() {
    test_empty();
    test_simple();
    test_specials();
    test_alphanumeric();
    test_single_sequences();
    test_multiple();
    test_multiple_specials();
    test_complex();
}

int main()
{
    // test_all();
    std::string test_str = "String; 2be reversed...";
    assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
    return 0;
}
