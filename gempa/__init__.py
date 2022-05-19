"""
Package Gempa
"""
import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    tanggal: 19 Mei 2022
    waktu: 04:12:08 WIB
    magnitudo: 2.9
    kedalaman: 10 km
    koordinat: ls: 3.63, bt: 128.17
    lokasi: Pusat gempa berada di darat 7 km Utara Ambon
    dirasakan: Dirasakan (Skala MMI): III Ambon
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        tanggal = soup.find("span", {"class": "waktu"}).text.split(", ")
        magnitudo = soup.find("span", {"class": "ic magnitude"}).text

        hasil = dict()
        hasil["tanggal"] = tanggal[0]
        hasil["waktu"] = tanggal[1]
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = 10
        hasil["koordinat"] = {"ls": 3.63, "bt": 128.17}
        hasil["lokasi"] = "Pusat gempa berada di darat 7 km Utara Ambon"
        hasil["dirasakan"] = "Dirasakan (Skala MMI): III Ambon"

        return hasil


def tampilkan_data(result):
    if result is None:
        print("Data gempa tidak ditemukan.")
        return
    print("Gempa Terkini berdasarkan informasi dari BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']} km")
    print(f"Koordinat {result['koordinat']['ls']} LS, {result['koordinat']['bt']} BT")
    print(f"{result['lokasi']}")
    print(f"{result['dirasakan']}")