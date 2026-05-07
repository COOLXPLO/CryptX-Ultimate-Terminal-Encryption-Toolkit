#!/usr/bin/env python3
# ============================================================
#   ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗  ██╗
#  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝╚██╗██╔╝
#  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║    ╚███╔╝ 
#  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║    ██╔██╗ 
#  ╚██████╗██║  ██║   ██║   ██║        ██║   ██╔╝ ██╗
#   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝  ╚═╝
# ============================================================
#  Advanced Encryption Toolkit  |  Kali Linux / Terminal
#  Author  : iamunknown77
#  Version : 2.0.0
#  Based on: caesar_cipher by iamunknown77
# ============================================================

import os, sys, base64, hashlib, string, math, argparse, binascii, random, re
from itertools import cycle

# ─── ANSI COLORS ──────────────────────────────────────────
R  = "\033[1;31m"   # Red
G  = "\033[1;32m"   # Green
Y  = "\033[1;33m"   # Yellow
B  = "\033[1;34m"   # Blue
M  = "\033[1;35m"   # Magenta
C  = "\033[1;36m"   # Cyan
W  = "\033[1;37m"   # White
DIM= "\033[2;37m"
RST= "\033[0m"

def clear(): os.system("clear" if os.name != "nt" else "cls")

BANNER = f"""
{C}╔══════════════════════════════════════════════════════════╗
║  {R}██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗  ██╗{C}      ║
║  {R}██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝╚██╗██╔╝{C}     ║
║  {R}██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║    ╚███╔╝{C}      ║
║  {R}██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║    ██╔██╗{C}      ║
║  {R}╚██████╗██║  ██║   ██║   ██║        ██║   ██╔╝ ██╗{C}     ║
║  {R} ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝  ╚═╝{C}    ║
╠══════════════════════════════════════════════════════════╣
║  {Y}Advanced Encryption Toolkit   v2.0.0                  {C}║
║  {G}Author: iamunknown77  |  Kali Linux / Terminal Ready  {C}║
╚══════════════════════════════════════════════════════════╝{RST}
"""

MENU = f"""
{C}╔══════════════════╡ {W}CIPHER MENU{C} ╞══════════════════╗{RST}
{C}║{RST}                                                    {C}║{RST}
{C}║  {Y}── CLASSICAL CIPHERS ──────────────────────────{C}  ║{RST}
{C}║{RST}  {G}[1]{RST}  Caesar / ROT-N                            {C}║{RST}
{C}║{RST}  {G}[2]{RST}  ROT13 (Quick)                             {C}║{RST}
{C}║{RST}  {G}[3]{RST}  Vigenère Cipher                           {C}║{RST}
{C}║{RST}  {G}[4]{RST}  Atbash Cipher                             {C}║{RST}
{C}║{RST}  {G}[5]{RST}  Affine Cipher                             {C}║{RST}
{C}║{RST}  {G}[6]{RST}  Rail Fence (Zigzag) Cipher               {C}║{RST}
{C}║{RST}  {G}[7]{RST}  Playfair Cipher                           {C}║{RST}
{C}║{RST}  {G}[8]{RST}  Beaufort Cipher                           {C}║{RST}
{C}║{RST}  {G}[9]{RST}  Running Key Cipher                        {C}║{RST}
{C}║{RST}                                                    {C}║{RST}
{C}║  {Y}── ENCODING / BINARY ───────────────────────────{C}  ║{RST}
{C}║{RST}  {G}[10]{RST} Base64 Encode / Decode                    {C}║{RST}
{C}║{RST}  {G}[11]{RST} Base32 Encode / Decode                    {C}║{RST}
{C}║{RST}  {G}[12]{RST} Base58 Encode / Decode                    {C}║{RST}
{C}║{RST}  {G}[13]{RST} Hex Encode / Decode                       {C}║{RST}
{C}║{RST}  {G}[14]{RST} Binary Encode / Decode                    {C}║{RST}
{C}║{RST}  {G}[15]{RST} Morse Code Encode / Decode                {C}║{RST}
{C}║{RST}                                                    {C}║{RST}
{C}║  {Y}── MODERN SYMMETRIC ────────────────────────────{C}  ║{RST}
{C}║{RST}  {G}[16]{RST} XOR Cipher                                {C}║{RST}
{C}║{RST}  {G}[17]{RST} OTP – One-Time Pad Generator              {C}║{RST}
{C}║{RST}                                                    {C}║{RST}
{C}║  {Y}── HASH / DIGEST ───────────────────────────────{C}  ║{RST}
{C}║{RST}  {G}[18]{RST} Hash Text  (MD5 / SHA-1/256/512 / …)      {C}║{RST}
{C}║{RST}  {G}[19]{RST} Hash File                                  {C}║{RST}
{C}║{RST}                                                    {C}║{RST}
{C}║  {Y}── UTILS ──────────────────────────────────────{C}   ║{RST}
{C}║{RST}  {G}[20]{RST} Brute-Force Caesar                         {C}║{RST}
{C}║{RST}  {G}[21]{RST} Frequency Analysis                         {C}║{RST}
{C}║{RST}  {G}[22]{RST} String Reverse                             {C}║{RST}
{C}║{RST}  {G}[23]{RST} URL Encode / Decode                        {C}║{RST}
{C}║{RST}  {G}[0]{RST}  Exit                                       {C}║{RST}
{C}║                                                    ║{RST}
{C}╚════════════════════════════════════════════════════╝{RST}
"""

# ──────────────────────────────────────────────────────────
#  HELPERS
# ──────────────────────────────────────────────────────────
def hdr(title):
    print(f"\n{C}{'─'*54}{RST}")
    print(f"{C} ⚙  {W}{title}{RST}")
    print(f"{C}{'─'*54}{RST}\n")

def result(label, value):
    print(f"\n{G}  ╔═══ {label} ═══╗{RST}")
    print(f"{Y}  ║  {W}{value}{RST}")
    print(f"{G}  ╚{'═'*(len(label)+9)}╝{RST}\n")

def ask(prompt):
    return input(f"{B}  ▶ {W}{prompt}: {RST}").strip()

def ask_mode():
    m = ask("Mode [E]ncrypt / [D]ecrypt").lower()
    return "encrypt" if m in ("e","encrypt","enc","1") else "decrypt"

def pause():
    input(f"\n{DIM}  Press Enter to continue…{RST}")

# ──────────────────────────────────────────────────────────
#  1. CAESAR / ROT-N
# ──────────────────────────────────────────────────────────
ALPHA_L = string.ascii_lowercase
ALPHA_U = string.ascii_uppercase

def caesar(text: str, shift: int, mode="encrypt") -> str:
    if mode == "decrypt":
        shift = -shift
    out = []
    for ch in text:
        if ch in ALPHA_L:
            out.append(ALPHA_L[(ALPHA_L.index(ch) + shift) % 26])
        elif ch in ALPHA_U:
            out.append(ALPHA_U[(ALPHA_U.index(ch) + shift) % 26])
        else:
            out.append(ch)
    return "".join(out)

def menu_caesar():
    hdr("Caesar / ROT-N Cipher")
    text  = ask("Enter text")
    shift = int(ask("Shift (1-25)"))
    mode  = ask_mode()
    out   = caesar(text, shift, mode)
    result(f"ROT{shift} {mode.upper()}", out)
    pause()

# ──────────────────────────────────────────────────────────
#  2. ROT13
# ──────────────────────────────────────────────────────────
def rot13(text): return caesar(text, 13)

def menu_rot13():
    hdr("ROT13")
    text = ask("Enter text")
    result("ROT13", rot13(text))
    pause()

# ──────────────────────────────────────────────────────────
#  3. VIGENÈRE
# ──────────────────────────────────────────────────────────
def vigenere(text: str, key: str, mode="encrypt") -> str:
    key  = key.lower()
    ki   = 0
    out  = []
    for ch in text:
        if ch.isalpha():
            ks   = ord(key[ki % len(key)]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            if mode == "encrypt":
                out.append(chr((ord(ch) - base + ks) % 26 + base))
            else:
                out.append(chr((ord(ch) - base - ks) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    return "".join(out)

def menu_vigenere():
    hdr("Vigenère Cipher")
    text = ask("Enter text")
    key  = ask("Keyword")
    mode = ask_mode()
    result(f"Vigenère {mode.upper()}", vigenere(text, key, mode))
    pause()

# ──────────────────────────────────────────────────────────
#  4. ATBASH
# ──────────────────────────────────────────────────────────
def atbash(text: str) -> str:
    out = []
    for ch in text:
        if ch in ALPHA_L:
            out.append(ALPHA_L[25 - ALPHA_L.index(ch)])
        elif ch in ALPHA_U:
            out.append(ALPHA_U[25 - ALPHA_U.index(ch)])
        else:
            out.append(ch)
    return "".join(out)

def menu_atbash():
    hdr("Atbash Cipher (self-inverse)")
    text = ask("Enter text")
    result("Atbash", atbash(text))
    pause()

# ──────────────────────────────────────────────────────────
#  5. AFFINE
# ──────────────────────────────────────────────────────────
def _modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a={a}, m={m}")

def affine(text: str, a: int, b: int, mode="encrypt") -> str:
    valid_a = [1,3,5,7,9,11,15,17,19,21,23,25]
    if a not in valid_a:
        raise ValueError(f"'a' must be coprime with 26: {valid_a}")
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            x = ord(ch.lower()) - ord('a')
            if mode == "encrypt":
                y = (a * x + b) % 26
            else:
                inv = _modinv(a, 26)
                y = (inv * (x - b)) % 26
            result_ch = chr(y + ord('a'))
            out.append(result_ch if ch.islower() else result_ch.upper())
        else:
            out.append(ch)
    return "".join(out)

def menu_affine():
    hdr("Affine Cipher")
    print(f"{DIM}  Formula: E(x) = (a·x + b) mod 26{RST}")
    print(f"{DIM}  Valid a values: 1,3,5,7,9,11,15,17,19,21,23,25{RST}\n")
    text = ask("Enter text")
    a    = int(ask("Value of a (must be coprime with 26)"))
    b    = int(ask("Value of b (0-25)"))
    mode = ask_mode()
    try:
        result(f"Affine {mode.upper()}", affine(text, a, b, mode))
    except ValueError as e:
        print(f"{R}  ✗ Error: {e}{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  6. RAIL FENCE (ZIGZAG)
# ──────────────────────────────────────────────────────────
def rail_fence_encrypt(text: str, rails: int) -> str:
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for ch in text:
        fence[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return "".join("".join(r) for r in fence)

def rail_fence_decrypt(cipher: str, rails: int) -> str:
    n      = len(cipher)
    pattern= []
    rail, direction = 0, 1
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    idx    = sorted(range(n), key=lambda i: pattern[i])
    result_ = [''] * n
    for i, c in zip(idx, cipher):
        result_[i] = c
    return "".join(result_)

def menu_rail_fence():
    hdr("Rail Fence (Zigzag) Cipher")
    text  = ask("Enter text")
    rails = int(ask("Number of rails"))
    mode  = ask_mode()
    if mode == "encrypt":
        out = rail_fence_encrypt(text, rails)
    else:
        out = rail_fence_decrypt(text, rails)
    result(f"Rail Fence {mode.upper()}", out)
    pause()

# ──────────────────────────────────────────────────────────
#  7. PLAYFAIR
# ──────────────────────────────────────────────────────────
def _playfair_matrix(key: str):
    key  = key.upper().replace("J","I")
    seen = []
    for ch in key + string.ascii_uppercase:
        if ch not in seen and ch != 'J':
            seen.append(ch)
    return [seen[i*5:(i+1)*5] for i in range(5)]

def _pf_pos(matrix, ch):
    for r, row in enumerate(matrix):
        if ch in row:
            return r, row.index(ch)

def _pf_pairs(text: str):
    text = text.upper().replace("J","I")
    text = re.sub(r'[^A-Z]', '', text)
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append((a,'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def playfair(text: str, key: str, mode="encrypt") -> str:
    m   = _playfair_matrix(key)
    pairs = _pf_pairs(text)
    d   = 1 if mode == "encrypt" else -1
    out = []
    for a, b in pairs:
        ra, ca = _pf_pos(m, a)
        rb, cb = _pf_pos(m, b)
        if ra == rb:
            out += [m[ra][(ca+d)%5], m[rb][(cb+d)%5]]
        elif ca == cb:
            out += [m[(ra+d)%5][ca], m[(rb+d)%5][cb]]
        else:
            out += [m[ra][cb], m[rb][ca]]
    return "".join(out)

def menu_playfair():
    hdr("Playfair Cipher")
    text = ask("Enter text")
    key  = ask("Keyword")
    mode = ask_mode()
    result(f"Playfair {mode.upper()}", playfair(text, key, mode))
    pause()

# ──────────────────────────────────────────────────────────
#  8. BEAUFORT
# ──────────────────────────────────────────────────────────
def beaufort(text: str, key: str) -> str:
    # Beaufort is self-inverse: same operation for encrypt & decrypt
    key = key.lower()
    out, ki = [], 0
    for ch in text:
        if ch.isalpha():
            ks = ord(key[ki % len(key)]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            y = (ks - (ord(ch) - base)) % 26
            out.append(chr(y + base))
            ki += 1
        else:
            out.append(ch)
    return "".join(out)

def menu_beaufort():
    hdr("Beaufort Cipher (self-inverse)")
    text = ask("Enter text")
    key  = ask("Keyword")
    result("Beaufort", beaufort(text, key))
    pause()

# ──────────────────────────────────────────────────────────
#  9. RUNNING KEY
# ──────────────────────────────────────────────────────────
def running_key(text: str, key: str, mode="encrypt") -> str:
    key = key.lower()
    out, ki = [], 0
    for ch in text:
        if ch.isalpha():
            ks   = ord(key[ki % len(key)]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            if mode == "encrypt":
                y = (ord(ch) - base + ks) % 26
            else:
                y = (ord(ch) - base - ks) % 26
            out.append(chr(y + base))
            ki += 1
        else:
            out.append(ch)
    return "".join(out)

def menu_running_key():
    hdr("Running Key Cipher")
    print(f"{DIM}  Key should be a long text (same length or longer than message){RST}\n")
    text = ask("Enter text")
    key  = ask("Running key (long text)")
    mode = ask_mode()
    result(f"RunKey {mode.upper()}", running_key(text, key, mode))
    pause()

# ──────────────────────────────────────────────────────────
#  10. BASE64
# ──────────────────────────────────────────────────────────
def menu_base64():
    hdr("Base64 Encode / Decode")
    mode = ask_mode()
    text = ask("Enter text")
    try:
        if mode == "encrypt":
            out = base64.b64encode(text.encode()).decode()
        else:
            out = base64.b64decode(text).decode()
        result(f"Base64 {mode.upper()}", out)
    except Exception as e:
        print(f"{R}  ✗ {e}{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  11. BASE32
# ──────────────────────────────────────────────────────────
def menu_base32():
    hdr("Base32 Encode / Decode")
    mode = ask_mode()
    text = ask("Enter text")
    try:
        if mode == "encrypt":
            out = base64.b32encode(text.encode()).decode()
        else:
            out = base64.b32decode(text).decode()
        result(f"Base32 {mode.upper()}", out)
    except Exception as e:
        print(f"{R}  ✗ {e}{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  12. BASE58
# ──────────────────────────────────────────────────────────
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(data: bytes) -> str:
    n = int.from_bytes(data, "big")
    s = ""
    while n:
        n, r = divmod(n, 58)
        s = BASE58_ALPHABET[r] + s
    pad = len(data) - len(data.lstrip(b'\x00'))
    return BASE58_ALPHABET[0] * pad + s

def base58_decode(s: str) -> bytes:
    n = 0
    for ch in s:
        n = n * 58 + BASE58_ALPHABET.index(ch)
    result_bytes = []
    while n:
        n, r = divmod(n, 256)
        result_bytes.insert(0, r)
    pad = len(s) - len(s.lstrip(BASE58_ALPHABET[0]))
    return b'\x00' * pad + bytes(result_bytes)

def menu_base58():
    hdr("Base58 Encode / Decode (Bitcoin-style)")
    mode = ask_mode()
    text = ask("Enter text")
    try:
        if mode == "encrypt":
            out = base58_encode(text.encode())
        else:
            out = base58_decode(text).decode()
        result(f"Base58 {mode.upper()}", out)
    except Exception as e:
        print(f"{R}  ✗ {e}{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  13. HEX
# ──────────────────────────────────────────────────────────
def menu_hex():
    hdr("Hex Encode / Decode")
    mode = ask_mode()
    text = ask("Enter text")
    try:
        if mode == "encrypt":
            out = text.encode().hex()
        else:
            out = bytes.fromhex(text).decode()
        result(f"Hex {mode.upper()}", out)
    except Exception as e:
        print(f"{R}  ✗ {e}{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  14. BINARY
# ──────────────────────────────────────────────────────────
def menu_binary():
    hdr("Binary Encode / Decode")
    mode = ask_mode()
    text = ask("Enter text")
    try:
        if mode == "encrypt":
            out = " ".join(format(ord(c), "08b") for c in text)
        else:
            parts = text.split()
            out   = "".join(chr(int(p, 2)) for p in parts)
        result(f"Binary {mode.upper()}", out)
    except Exception as e:
        print(f"{R}  ✗ {e}{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  15. MORSE CODE
# ──────────────────────────────────────────────────────────
MORSE = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
    'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
    'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
    ' ':'/'
}
MORSE_INV = {v: k for k, v in MORSE.items()}

def morse_encode(text: str) -> str:
    return " ".join(MORSE.get(c.upper(), "?") for c in text)

def morse_decode(text: str) -> str:
    return "".join(MORSE_INV.get(token, "?") for token in text.split(" "))

def menu_morse():
    hdr("Morse Code")
    mode = ask_mode()
    text = ask("Enter text")
    out  = morse_encode(text) if mode == "encrypt" else morse_decode(text)
    result(f"Morse {mode.upper()}", out)
    pause()

# ──────────────────────────────────────────────────────────
#  16. XOR CIPHER
# ──────────────────────────────────────────────────────────
def xor_cipher(text: str, key: str) -> str:
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, cycle(key)))

def xor_to_hex(text: str, key: str) -> str:
    raw = bytes(b ^ ord(k) for b, k in zip(text.encode(), cycle(key)))
    return raw.hex()

def hex_xor_decrypt(hex_str: str, key: str) -> str:
    raw = bytes.fromhex(hex_str)
    return "".join(chr(b ^ ord(k)) for b, k in zip(raw, cycle(key)))

def menu_xor():
    hdr("XOR Cipher")
    mode = ask_mode()
    key  = ask("XOR Key")
    if mode == "encrypt":
        text = ask("Plaintext")
        out  = xor_to_hex(text, key)
        result("XOR Encrypted (hex)", out)
    else:
        text = ask("Ciphertext (hex)")
        out  = hex_xor_decrypt(text, key)
        result("XOR Decrypted", out)
    pause()

# ──────────────────────────────────────────────────────────
#  17. ONE-TIME PAD
# ──────────────────────────────────────────────────────────
def otp_generate(length: int) -> str:
    return "".join(chr(random.randint(32, 126)) for _ in range(length))

def otp_encrypt(text: str, pad: str) -> str:
    return xor_to_hex(text, pad)

def otp_decrypt(hex_str: str, pad: str) -> str:
    return hex_xor_decrypt(hex_str, pad)

def menu_otp():
    hdr("One-Time Pad (OTP)")
    mode = ask_mode()
    if mode == "encrypt":
        text = ask("Plaintext")
        pad  = otp_generate(len(text))
        ct   = otp_encrypt(text, pad)
        print(f"\n{G}  ╔═══ OTP Generated Pad ═══╗{RST}")
        print(f"{Y}  ║  {W}{pad}{RST}")
        print(f"{G}  ╚{'═'*27}╝{RST}")
        result("OTP Ciphertext (hex)", ct)
        print(f"{R}  ⚠  Save the pad! Without it decryption is impossible.{RST}")
    else:
        ct  = ask("Ciphertext (hex)")
        pad = ask("OTP Pad")
        result("OTP Decrypted", otp_decrypt(ct, pad))
    pause()

# ──────────────────────────────────────────────────────────
#  18. HASH TEXT
# ──────────────────────────────────────────────────────────
HASH_MAP = {
    "1": ("MD5",      "md5"),
    "2": ("SHA-1",    "sha1"),
    "3": ("SHA-224",  "sha224"),
    "4": ("SHA-256",  "sha256"),
    "5": ("SHA-384",  "sha384"),
    "6": ("SHA-512",  "sha512"),
    "7": ("SHA3-256", "sha3_256"),
    "8": ("SHA3-512", "sha3_512"),
    "9": ("BLAKE2b",  "blake2b"),
}

def menu_hash_text():
    hdr("Hash Text")
    print(f"{C}  Algorithms:{RST}")
    for k, (name, _) in HASH_MAP.items():
        print(f"    {G}[{k}]{RST} {name}")
    choice = ask("\n  Choose algorithm")
    if choice not in HASH_MAP:
        print(f"{R}  Invalid choice{RST}")
        pause(); return
    name, algo = HASH_MAP[choice]
    text  = ask("Enter text to hash")
    h     = hashlib.new(algo, text.encode()).hexdigest()
    result(f"{name} Hash", h)
    pause()

# ──────────────────────────────────────────────────────────
#  19. HASH FILE
# ──────────────────────────────────────────────────────────
def menu_hash_file():
    hdr("Hash File")
    print(f"{C}  Algorithms:{RST}")
    for k, (name, _) in HASH_MAP.items():
        print(f"    {G}[{k}]{RST} {name}")
    choice = ask("\n  Choose algorithm")
    if choice not in HASH_MAP:
        print(f"{R}  Invalid choice{RST}"); pause(); return
    name, algo = HASH_MAP[choice]
    path  = ask("File path")
    try:
        h = hashlib.new(algo)
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        result(f"{name} ({os.path.basename(path)})", h.hexdigest())
    except FileNotFoundError:
        print(f"{R}  ✗ File not found{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  20. BRUTE FORCE CAESAR
# ──────────────────────────────────────────────────────────
def menu_brute_caesar():
    hdr("Brute-Force Caesar (All 25 Shifts)")
    text = ask("Enter ciphertext")
    print(f"\n{C}  {'Shift':<8}{'Result'}{RST}")
    print(f"  {'─'*50}")
    for n in range(1, 26):
        dec = caesar(text, n, "decrypt")
        print(f"  {G}ROT{n:<5}{RST}{dec}")
    pause()

# ──────────────────────────────────────────────────────────
#  21. FREQUENCY ANALYSIS
# ──────────────────────────────────────────────────────────
def menu_freq():
    hdr("Frequency Analysis")
    text   = ask("Enter ciphertext")
    counts = {}
    total  = 0
    for ch in text.upper():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
            total += 1
    if total == 0:
        print(f"{R}  No alphabetic characters found.{RST}"); pause(); return
    print(f"\n{C}  {'Char':<6}{'Count':<8}{'Freq':<8}Bar{RST}")
    print(f"  {'─'*50}")
    for ch, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        freq = cnt / total * 100
        bar  = "█" * int(freq / 2)
        print(f"  {Y}{ch:<6}{W}{cnt:<8}{G}{freq:<6.1f}%{C}  {bar}{RST}")
    print(f"\n{DIM}  English frequency order: E T A O I N S H R D L C U M W F G Y P B V K J X Q Z{RST}")
    pause()

# ──────────────────────────────────────────────────────────
#  22. STRING REVERSE
# ──────────────────────────────────────────────────────────
def menu_reverse():
    hdr("String Reverse")
    text = ask("Enter text")
    result("Reversed", text[::-1])
    pause()

# ──────────────────────────────────────────────────────────
#  23. URL ENCODE / DECODE
# ──────────────────────────────────────────────────────────
try:
    from urllib.parse import quote, unquote
except ImportError:
    quote = unquote = lambda x: x

def menu_url():
    hdr("URL Encode / Decode")
    mode = ask_mode()
    text = ask("Enter text")
    out  = quote(text, safe="") if mode == "encrypt" else unquote(text)
    result(f"URL {mode.upper()}", out)
    pause()

# ──────────────────────────────────────────────────────────
#  DISPATCH TABLE
# ──────────────────────────────────────────────────────────
MENU_MAP = {
    "1": menu_caesar,    "2": menu_rot13,     "3": menu_vigenere,
    "4": menu_atbash,    "5": menu_affine,    "6": menu_rail_fence,
    "7": menu_playfair,  "8": menu_beaufort,  "9": menu_running_key,
    "10": menu_base64,   "11": menu_base32,   "12": menu_base58,
    "13": menu_hex,      "14": menu_binary,   "15": menu_morse,
    "16": menu_xor,      "17": menu_otp,
    "18": menu_hash_text,"19": menu_hash_file,
    "20": menu_brute_caesar,"21": menu_freq,
    "22": menu_reverse,  "23": menu_url,
}

# ──────────────────────────────────────────────────────────
#  CLI ARGUMENT MODE  (non-interactive)
# ──────────────────────────────────────────────────────────
def cli_mode():
    parser = argparse.ArgumentParser(
        prog="cryptx",
        description="CryptX – Advanced Encryption Toolkit by iamunknown77",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-c", "--cipher",  required=True,
        choices=["caesar","rot13","vigenere","atbash","affine","rail","playfair",
                 "beaufort","runkey","base64","base32","base58","hex","binary",
                 "morse","xor","hash","b-caesar","freq","reverse","url"],
        help="Cipher / operation to use")
    parser.add_argument("-t","--text",  help="Input text")
    parser.add_argument("-m","--mode",  default="encrypt",
        choices=["encrypt","decrypt"], help="Mode (default: encrypt)")
    parser.add_argument("-k","--key",   help="Key / keyword / shift")
    parser.add_argument("--algo", default="sha256",
        help="Hash algorithm (default: sha256)")
    args = parser.parse_args()

    text = args.text or input("Enter text: ")
    out  = None

    try:
        if args.cipher == "caesar":
            out = caesar(text, int(args.key or 3), args.mode)
        elif args.cipher == "rot13":
            out = rot13(text)
        elif args.cipher == "vigenere":
            out = vigenere(text, args.key or "key", args.mode)
        elif args.cipher == "atbash":
            out = atbash(text)
        elif args.cipher == "affine":
            a, b = map(int, (args.key or "5,8").split(","))
            out  = affine(text, a, b, args.mode)
        elif args.cipher == "rail":
            out  = rail_fence_encrypt(text, int(args.key or 3)) if args.mode == "encrypt" \
                   else rail_fence_decrypt(text, int(args.key or 3))
        elif args.cipher == "playfair":
            out  = playfair(text, args.key or "keyword", args.mode)
        elif args.cipher == "beaufort":
            out  = beaufort(text, args.key or "key")
        elif args.cipher == "runkey":
            out  = running_key(text, args.key or "thequickbrownfox", args.mode)
        elif args.cipher == "base64":
            out  = base64.b64encode(text.encode()).decode() if args.mode == "encrypt" \
                   else base64.b64decode(text).decode()
        elif args.cipher == "base32":
            out  = base64.b32encode(text.encode()).decode() if args.mode == "encrypt" \
                   else base64.b32decode(text).decode()
        elif args.cipher == "base58":
            out  = base58_encode(text.encode()) if args.mode == "encrypt" \
                   else base58_decode(text).decode()
        elif args.cipher == "hex":
            out  = text.encode().hex() if args.mode == "encrypt" \
                   else bytes.fromhex(text).decode()
        elif args.cipher == "binary":
            out  = " ".join(format(ord(c),"08b") for c in text) if args.mode == "encrypt" \
                   else "".join(chr(int(p,2)) for p in text.split())
        elif args.cipher == "morse":
            out  = morse_encode(text) if args.mode == "encrypt" \
                   else morse_decode(text)
        elif args.cipher == "xor":
            out  = xor_to_hex(text, args.key or "secret") if args.mode == "encrypt" \
                   else hex_xor_decrypt(text, args.key or "secret")
        elif args.cipher == "hash":
            out  = hashlib.new(args.algo, text.encode()).hexdigest()
        elif args.cipher == "b-caesar":
            out  = "\n".join(f"ROT{n}: {caesar(text,n,'decrypt')}" for n in range(1,26))
        elif args.cipher == "freq":
            counts = {}
            for ch in text.upper():
                if ch.isalpha(): counts[ch] = counts.get(ch,0)+1
            total = sum(counts.values())
            out   = "\n".join(f"{ch}: {cnt} ({cnt/total*100:.1f}%)"
                              for ch,cnt in sorted(counts.items(),key=lambda x:-x[1]))
        elif args.cipher == "reverse":
            out  = text[::-1]
        elif args.cipher == "url":
            out  = quote(text,safe="") if args.mode == "encrypt" else unquote(text)

        print(out)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

# ──────────────────────────────────────────────────────────
#  MAIN
# ──────────────────────────────────────────────────────────
def main():
    if len(sys.argv) > 1:
        cli_mode()
        return

    while True:
        clear()
        print(BANNER)
        print(MENU)
        choice = ask("Select option").strip()
        if choice == "0":
            print(f"\n{G}  Goodbye! – iamunknown77{RST}\n")
            sys.exit(0)
        fn = MENU_MAP.get(choice)
        if fn:
            clear()
            print(BANNER)
            fn()
        else:
            print(f"{R}  Invalid option. Try again.{RST}")
            import time; time.sleep(1)

if __name__ == "__main__":
    main()
