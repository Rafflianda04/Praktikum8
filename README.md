## PERTEMUAN KE 12
# NilaiMahasiswa Class

## Program Class Data_Mahasiswa
* **Diagram Class**
![img](Gambar/1.png)

* **Flowchart**
![img](Gambar/2.png)

## Overview
The `NilaiMahasiswa` class is a simple Python class designed to manage and manipulate student data, specifically their names and corresponding grades. The class provides functionality to add, display, update, and delete student records.

## Class Methods

### `__init__(self) -> None`
- Initializes an instance of the class with an empty dictionary to store student data.

### `tambah(self, nama: str, nilai: int) -> str`
- Adds a new student to the records with the given name (`nama`) and grade (`nilai`).
- Returns a success message if the student is added, or an error message if the student already exists.

### `tampilkan(self) -> str`
- Displays the list of students and their corresponding grades.
- Returns a message indicating that there is no student data if the records are empty.

### `hapus(self, nama: str) -> str`
- Removes a student from the records based on the provided name (`nama`).
- Returns a success message if the student is deleted, or an error message if the student is not found.

### `ubah(self, nama: str, nilai: int) -> str`
- Updates the grade of an existing student with the provided name (`nama`) to the new grade (`nilai`).
- Returns a success message if the update is successful, or an error message if the student is not found.

## Example Usage

```python
# Creating an instance of the NilaiMahasiswa class
nilai_mahasiswa = NilaiMahasiswa()

# Adding students with their grades
print(nilai_mahasiswa.tambah("Rusli", 90))
print(nilai_mahasiswa.tambah("Ramfly", 100))
print(nilai_mahasiswa.tambah("Raffli", 100))

# Displaying the list of students and grades
print(nilai_mahasiswa.tampilkan())

# Updating the grade for an existing student
print(nilai_mahasiswa.ubah("Rusli", 100))

# Deleting a student
print(nilai_mahasiswa.hapus("Ramfly"))

# Displaying the updated list of students and grades
print(nilai_mahasiswa.tampilkan())
```
## Output
![Alt text](Gambar/Hsl.png)
## Notes
- Ensure that the provided name (`nama`) is a string, and the grade (`nilai`) is an integer when using the `tambah`, `hapus`, and `ubah` methods.
- The class provides a basic template for managing student records and can be extended to include additional features based on specific requirements.