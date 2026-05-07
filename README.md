# CryptX – Advanced Encryption Toolkit
> **Author:** iamunknown77 | Based on the original `caesar_cipher` project

A feature-rich, terminal-ready encryption toolkit for **Kali Linux**, Ubuntu, macOS, and Windows. Runs interactively or via CLI flags — perfect for CTFs, security learning, and CyberChef-style quick operations directly in your terminal.

---

## Quick Start

### Kali Linux / Bash
```bash
chmod +x cryptx.sh
./cryptx.sh                  # interactive menu
./cryptx.sh -c caesar -t "hello world" -k 13 -m encrypt
```

### Windows (CMD / PowerShell)
```bat
cryptx.bat                   :: interactive menu
cryptx.bat -c rot13 -t "hello world"
```

### Direct Python
```bash
python3 cryptx.py            # interactive menu
python3 cryptx.py -c sha256 --algo sha256 -t "password123"
```

---

## Ciphers & Tools

### Classical Ciphers
| # | Cipher | Description |
|---|--------|-------------|
| 1 | Caesar / ROT-N | Shift alphabet by N positions |
| 2 | ROT13 | Fixed 13-shift (self-inverse) |
| 3 | Vigenère | Polyalphabetic substitution with keyword |
| 4 | Atbash | Reverse-alphabet substitution (self-inverse) |
| 5 | Affine | E(x) = (ax + b) mod 26 |
| 6 | Rail Fence | Zigzag transposition cipher |
| 7 | Playfair | 5×5 digraph substitution cipher |
| 8 | Beaufort | Variant of Vigenère (self-inverse) |
| 9 | Running Key | Long-key variant of Vigenère |

### Encoding / Binary
| # | Method | Description |
|---|--------|-------------|
| 10 | Base64 | Standard Base64 encode/decode |
| 11 | Base32 | Base32 encode/decode |
| 12 | Base58 | Bitcoin-style Base58 encode/decode |
| 13 | Hex | Hex encode/decode |
| 14 | Binary | 8-bit binary encode/decode |
| 15 | Morse Code | International Morse encode/decode |

### Modern / Symmetric
| # | Method | Description |
|---|--------|-------------|
| 16 | XOR Cipher | Key-streamed XOR (output as hex) |
| 17 | One-Time Pad | Cryptographically random OTP generator |

### Hash / Digest
| # | Method | Algorithms |
|---|--------|------------|
| 18 | Hash Text | MD5, SHA-1, SHA-224/256/384/512, SHA3-256/512, BLAKE2b |
| 19 | Hash File | Same algorithms — hashes any file on disk |

### Utilities
| # | Tool | Description |
|---|------|-------------|
| 20 | Brute-Force Caesar | Tries all 25 shifts at once |
| 21 | Frequency Analysis | Letter frequency chart with bar graph |
| 22 | String Reverse | Simple string reversal |
| 23 | URL Encode/Decode | Percent-encoding for URLs |

---

## CLI Usage (Non-Interactive)

```bash
# Caesar encrypt
python3 cryptx.py -c caesar -t "attack at dawn" -k 7 -m encrypt

# Vigenère decrypt
python3 cryptx.py -c vigenere -t "LXFOPVEFRNHR" -k "lemon" -m decrypt

# SHA-256 hash
python3 cryptx.py -c hash -t "password" --algo sha256

# Brute-force all Caesar shifts
python3 cryptx.py -c b-caesar -t "khoor"

# XOR encrypt
python3 cryptx.py -c xor -t "secret message" -k "mykey" -m encrypt

# Base64 encode
python3 cryptx.py -c base64 -t "hello world" -m encrypt

# Morse encode
python3 cryptx.py -c morse -t "SOS" -m encrypt

# Frequency analysis
python3 cryptx.py -c freq -t "KHOOR ZRUOG"
```

---

## Requirements
- Python 3.6+ (no external libraries needed — stdlib only)

---

## Credits
Original Caesar Cipher project by **iamunknown77**  
Enhanced CryptX Toolkit by **iamunknown77**
