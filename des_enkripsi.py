{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5e5c7a2d-c6e1-4050-ae03-2cb061787631",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Encrypted: 78fdfd083678960292e9d3355b8ec293806d67d064c8a4bdc6a2d91c30ef8a8c\n",
      "Decrypted: Mataram, mata air kehidupan\n"
     ]
    }
   ],
   "source": [
    "from Crypto.Cipher import DES\n",
    "from Crypto.Random import get_random_bytes\n",
    "from Crypto.Util.Padding import pad, unpad\n",
    "\n",
    "# Buat kunci DES (harus 8 byte)\n",
    "key = b'12345678'  # 8 bytes\n",
    "\n",
    "# Bikin cipher object\n",
    "cipher = DES.new(key, DES.MODE_ECB)\n",
    "\n",
    "# Pesan yang mau dienkripsi\n",
    "data = b'Mataram, mata air kehidupan'\n",
    "padded_data = pad(data, DES.block_size)  # padding biar kelipatan 8\n",
    "\n",
    "# Enkripsi\n",
    "encrypted = cipher.encrypt(padded_data)\n",
    "print(\"Encrypted:\", encrypted.hex())\n",
    "\n",
    "# Dekripsi\n",
    "cipher2 = DES.new(key, DES.MODE_ECB)\n",
    "decrypted_padded = cipher2.decrypt(encrypted)\n",
    "decrypted = unpad(decrypted_padded, DES.block_size)\n",
    "print(\"Decrypted:\", decrypted.decode())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e52448f9-0673-4360-a368-157b21d3427e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
