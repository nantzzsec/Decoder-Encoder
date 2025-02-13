# Create By Nantzzsec

import base64
import hashlib
import webbrowser
from colorama import Fore, Style, init

init()

LEBAR_MENU = 45

github = "https://github.com/nantzzsec"
linkedin = "https://id.linkedin.com/in/gede-ananda-960699309"
tiktok = "https://www.tiktok.com/@accessdenied_error"

def encode_base64(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def encrypt_sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def encrypt_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def encrypt_md4(text):
    return hashlib.new('md4', text.encode()).hexdigest()

def view_history():
    print(Fore.YELLOW + "\nHistory:" + Style.RESET_ALL)
    for item in history:
        print(Fore.CYAN + item + Style.RESET_ALL)

def menu_base64():
    while True:
        print(Fore.GREEN + "\n" + "=" * LEBAR_MENU)
        print("Nantzz Base64".center(LEBAR_MENU))
        print("=" * LEBAR_MENU + Style.RESET_ALL)
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. History")
        print("4. Kembali")
        choice = input("Masukkan pilihan: ")
        
        if choice == "1":
            print(Fore.GREEN + "\n" + "=" * LEBAR_MENU)
            print("Input Text".center(LEBAR_MENU))
            print("=" * LEBAR_MENU + Style.RESET_ALL)
            text = input("Masukkan text: ")
            result = encode_base64(text)
            history.append(f"Base64 Encrypt: {text} -> {result}")
            print(Fore.BLUE + "\n" + "=" * LEBAR_MENU)
            print("Hasil Encrypt".center(LEBAR_MENU))
            print(result)
            print("=" * LEBAR_MENU + Style.RESET_ALL)

        elif choice == "2":
            print(Fore.GREEN + "\n" + "=" * LEBAR_MENU)
            print("Input Text".center(LEBAR_MENU))
            print("=" * LEBAR_MENU + Style.RESET_ALL)
            text = input("Masukkan encoded text: ")
            result = decode_base64(text)
            history.append(f"Base64 Decrypt: {text} -> {result}")
            print(Fore.BLUE + "\n" + "=" * LEBAR_MENU)
            print("Hasil Decrypt".center(LEBAR_MENU))
            print(result)
            print("=" * LEBAR_MENU + Style.RESET_ALL)
        elif choice == "3":
            view_history()
        elif choice == "4":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Coba lagi." + Style.RESET_ALL)
            break

def menu_hash(encrypt_function, hash_name):
    while True:
        print(Fore.GREEN + "\n" + "=" * LEBAR_MENU)
        print(f"Nantzz {hash_name}".center(LEBAR_MENU))
        print("=" * LEBAR_MENU + Style.RESET_ALL)
        print("1. Encrypt Text")
        print("2. History")
        print("3. Kembali")
        choice = input("Masukkan pilihan: ")
        
        if choice == "1":
            text = input("Masukkan text: ")
            result = encrypt_function(text)
            history.append(f"{hash_name} Encrypt: {text} -> {result}")
            print(Fore.BLUE + "\n" + "=" * LEBAR_MENU)
            print("Hasil Encrypt".center(LEBAR_MENU))
            print(result)
            print("=" * LEBAR_MENU + Style.RESET_ALL)
        elif choice == "2":
            view_history()
        elif choice == "3":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Coba lagi." + Style.RESET_ALL)
            break

def menu_sosmed():
    while True:
        print(Fore.GREEN + "\n" + "=" * LEBAR_MENU)
        print("Follow Me".center(LEBAR_MENU))
        print("=" * LEBAR_MENU + Style.RESET_ALL)
        print("1. Github")
        print("2. Linkedin")
        print("3. Tiktok")
        print("4. Kembali")
        choice = input("Masukkan pilihan: ")
        
        if choice == "1":
            webbrowser.open(github)
        elif choice == "2":
            webbrowser.open(linkedin)
        elif choice == "3":
            webbrowser.open(tiktok)
        elif choice == "4":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Coba lagi." + Style.RESET_ALL)
            break

def main():
    global history
    history = []
    while True:
        print(Fore.GREEN + "\n" + "=" * LEBAR_MENU)
        print("Nantzz Encryp Decript".center(LEBAR_MENU))
        print("=" * LEBAR_MENU + Style.RESET_ALL)
        print("1. Base 64")
        print("2. SHA")
        print("3. MD5")
        print("4. MD4")
        print("5. Follow me")
        print("6. Keluar")
        print("=" * LEBAR_MENU)
        choice = input("Masukkan pilihan: ")
        
        if choice == "1":
            menu_base64()
        elif choice == "2":
            menu_hash(encrypt_sha, "SHA")
        elif choice == "3":
            menu_hash(encrypt_md5, "MD5")
        elif choice == "4":
            menu_hash(encrypt_md4, "MD4")
        elif choice == "5":
            menu_sosmed()
        elif choice == "6":
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Coba lagi." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
