#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сортировка и объединение PDF файлов в один из указанной папки"""

import glob
import sh
from tkinter import Tcl
from PyPDF2 import PdfMerger

folder = input('Enter path about folder: ')
name_file = input('Enter the name of the target file (your_filename.pdf): ')
sh.cd(folder)

"""Сортировка и запись имен файлов в список list_dir """
files = sorted(glob.glob(r"*.pdf"))

list_dir = []
for key, myfile in enumerate(files):
    list_dir.append(myfile)

"""Возвращает сортированный список в виде кортежа"""
sort_tuple = Tcl().call('lsort', '-dict', files)
sort_list = list(sort_tuple)

"""Объединяем pdf файлы"""
merger = PdfMerger()

for pdf in sort_list:
    merger.append(pdf)

merger.write(name_file)
merger.close()



