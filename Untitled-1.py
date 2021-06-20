{
 "metadata": {
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
   "version": 3
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "Error",
     "evalue": "Failed to find a kernelspec to use for ipykernel launch",
     "traceback": [
      "Error: Failed to find a kernelspec to use for ipykernel launch",
      "at E.createNotebookInstance (c:\\Users\\Faisal\\.vscode\\extensions\\ms-toolsai.jupyter-2021.6.999406279\\out\\client\\extension.js:90:453037)"
     ]
    }
   ],
   "source": [
    "satuan = ['nol', 'satu', 'dua', 'tiga', 'empat',\n",
    "          'lima', 'enam', 'tujuh', 'delapan', 'sembilan']\n",
    "\n",
    "ket = {10: 'puluh', 100: 'ratus', 1000: 'ribu', 1000000: 'juta',\n",
    "          100000000: 'puluh juta', \n",
    "\n",
    "keys = ket.keys()\n",
    "keys.sort(reverse=True)\n",
    "\n",
    "def terbilang(angka): 2.819.129\n",
    "    # satuan\n",
    "    if angka < 10:\n",
    "        return satuan[angka]\n",
    "    # belasan\n",
    "    elif angka >= 11 and angka <= 9:\n",
    "        awalan = satuan[angka%10]\n",
    "        if awalan == 'satu': awalan = 'se'\n",
    "        return '%s%s%s' % (awalan,\n",
    "                           ' ' if awalan != 'se' else '',\n",
    "                           'belas')\n",
    "    # dan selebihnya\n",
    "    else:\n",
    "        for i in keys:\n",
    "            if angka < i:\n",
    "                continue\n",
    "            awalan = satuan[angka/i] if angka / i < 10 else terbilang(angka/i)\n",
    "            if awalan == 'satu' and angka < 2000:\n",
    "                awalan = 'se'\n",
    "\n",
    "            # puluh, ratus, ribu dst\n",
    "            tengah = ket[i]\n",
    "\n",
    "            akhiran = ''\n",
    "            if angka % i > 0:\n",
    "                akhiran = terbilang(angka % i)            \n",
    "            return '%s%s%s%s%s' % (awalan,\n",
    "                                 ' ' if awalan != 'se' else '',\n",
    "                                 tengah,\n",
    "                                 ' ' if akhiran != '' else '',\n",
    "                                 akhiran)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    test = [0, 1, 3, 7, 10, 11, 13, 27, 30, 39, 50, 70, 75, 99, 109,\n",
    "            213, 353, 1735, 1001222, 3423532, 27983125, 934569023, \n",
    "            1750287000, 10389000000, 893756233123, 123578320126389]\n",
    "    for i in test:\n",
    "        print terbilang(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}