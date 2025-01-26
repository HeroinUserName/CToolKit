#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <openssl/err.h>
#include <iostream>

void encrypt_message(const std::string& message) {
    RSA *rsa = RSA_generate_key(2048, RSA_F4, nullptr, nullptr);
    unsigned char encrypted[256];
    int result = RSA_public_encrypt(message.length(), (unsigned char*)message.c_str(), encrypted, rsa, RSA_PKCS1_OAEP_PADDING);
    if(result == -1) {
        std::cout << "Encryption failed!" << std::endl;
    } else {
        std::cout << "Encrypted Message: ";
        for(int i = 0; i < result; i++) {
            printf("%02x", encrypted[i]);
        }
        std::cout << std::endl;
    }
}

int main() {
    encrypt_message("This is a secret message.");
    return 0;
}
