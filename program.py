import time
import numpy as np
import matplotlib.pyplot as plt
import csv
from typing import List, Tuple

def input_matriks(rows: int, cols: int) -> List[List[int]]:
    """Input matriks interaktif dari user."""
    mat = []
    print(f"Masukkan {rows}x{cols} matriks (baris per baris, spasi dipisah):")
    for i in range(rows):
        row = list(map(int, input(f"Baris {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Baris {i+1} harus punya {cols} elemen!")
        mat.append(row)
    return mat

def input_array() -> List[int]:
    """Input array interaktif dari user."""
    arr_str = input("Masukkan array (spasi dipisah): ")
    return list(map(int, arr_str.split()))

def tambah_matriks_np(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    """Tambah matriks pakai NumPy (efisien)."""
    if mat1.shape != mat2.shape:
        raise ValueError("Ukuran matriks tidak cocok untuk penjumlahan!")
    return mat1 + mat2

def kali_matriks_np(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    """Kali matriks pakai NumPy (asumsi 'mengalihkan' = multiply)."""
    if mat1.shape[1] != mat2.shape[0]:
        raise ValueError("Ukuran matriks tidak cocok untuk perkalian!")
    return np.dot(mat1, mat2)

def selection_sort(arr: List[int]) -> Tuple[List[int], List[List[int]]]:
    """Selection Sort dengan tracking steps untuk visualisasi."""
    steps = [arr.copy()]  # Track setiap perubahan
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return arr, steps

def bubble_sort(arr: List[int]) -> Tuple[List[int], List[List[int]]]:
    """Bubble Sort dengan tracking steps."""
    steps = [arr.copy()]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        steps.append(arr.copy())
    return arr, steps

def sequential_search(arr: List[int], target: int) -> int:
    """Sequential Search sederhana."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def measure_time(func, *args, **kwargs) -> float:
    """Ukur waktu eksekusi fungsi."""
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end - start

def visualize_sorting(steps: List[List[int]], sort_name: str):
    """Visualisasi steps sorting pakai Matplotlib (bar chart)."""
    fig, axs = plt.subplots(len(steps), 1, figsize=(10, 2*len(steps)))
    if len(steps) == 1:
        axs = [axs]
    for i, step in enumerate(steps):
        axs[i].bar(range(len(step)), step)
        axs[i].set_title(f"{sort_name} - Step {i+1}")
        axs[i].set_xlabel("Index")
        axs[i].set_ylabel("Value")
    plt.tight_layout()
    plt.show()

def save_to_csv(filename: str, data: List[List[int]], headers: List[str]):
    """Simpan data ke CSV."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

def print_complexity(algo_name: str):
    """Tampilkan Big O complexity."""
    complexities = {
        "Selection Sort": "O(n²) waktu, O(1) space",
        "Bubble Sort": "O(n²) waktu, O(1) space",
        "Sequential Search": "O(n) waktu, O(1) space",
        "Matrix Add/Mult": "O(m*n) waktu untuk ukuran m x n"
    }
    print(f"\nKompleksitas {algo_name}: {complexities.get(algo_name, 'N/A')}")

def main():
    while True:
        print("\n=== PROGRAM  ===")
        print("1. Operasi Matriks (Tambah/Kali)")
        print("2. Selection Sort + Visualisasi")
        print("3. Bubble Sort + Visualisasi")
        print("4. Sequential Search")
        print("5. Keluar")
        
        choice = input("Pilih menu (1-5): ").strip()
        
        if choice == '1':
            try:
                rows1, cols1 = map(int, input("Ukuran matriks 1 (rows cols): ").split())
                mat1 = np.array(input_matriks(rows1, cols1))
                rows2, cols2 = map(int, input("Ukuran matriks 2 (rows cols): ").split())
                mat2 = np.array(input_matriks(rows2, cols2))
                
                op = input("Pilih: tambah (t) atau kali (k)? ").strip().lower()
                start = time.time()
                if op == 't':
                    result = tambah_matriks_np(mat1, mat2)
                else:
                    result = kali_matriks_np(mat1, mat2)
                exec_time = time.time() - start
                
                print(f"Hasil:\n{result}")
                print(f"Waktu eksekusi: {exec_time:.4f} detik")
                print_complexity("Matrix Add/Mult")
                
                save_to_csv('hasil_matriks.csv', result.tolist(), ['Kolom'])
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            arr = input_array()
            if not arr:
                print("Array kosong!")
                continue
            start = time.time()
            sorted_arr, steps = selection_sort(arr.copy())
            exec_time = time.time() - start
            print(f"Array asli: {arr}")
            print(f"Array terurut: {sorted_arr}")
            print(f"Waktu eksekusi: {exec_time:.4f} detik")
            print_complexity("Selection Sort")
            vis = input("Visualisasi? (y/n): ").strip().lower()
            if vis == 'y':
                visualize_sorting(steps, "Selection Sort")
            save_to_csv('hasil_selection.csv', [arr, sorted_arr], ['Asli', 'Terurut'])
        
        elif choice == '3':
            arr = input_array()
            if not arr:
                print("Array kosong!")
                continue
            start = time.time()
            sorted_arr, steps = bubble_sort(arr.copy())
            exec_time = time.time() - start
            print(f"Array asli: {arr}")
            print(f"Array terurut: {sorted_arr}")
            print(f"Waktu eksekusi: {exec_time:.4f} detik")
            print_complexity("Bubble Sort")
            vis = input("Visualisasi? (y/n): ").strip().lower()
            if vis == 'y':
                visualize_sorting(steps, "Bubble Sort")
            save_to_csv('hasil_bubble.csv', [arr, sorted_arr], ['Asli', 'Terurut'])
        
        elif choice == '4':
            arr = input_array()
            if not arr:
                print("Array kosong!")
                continue
            target = int(input("Target pencarian: "))
            start = time.time()
            index = sequential_search(arr, target)
            exec_time = time.time() - start
            print(f"Array: {arr}")
            if index != -1:
                print(f"Ditemukan di index {index}")
            else:
                print("Tidak ditemukan")
            print(f"Waktu eksekusi: {exec_time:.4f} detik")
            print_complexity("Sequential Search")
            save_to_csv('hasil_search.csv', [[target, index]], ['Target', 'Index'])
        
        elif choice == '5':
            print("Keluar. Terima kasih!")
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    main()