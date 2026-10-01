#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ayakkabı Bağcığı Ontolojisi — çalışan resmi simülatör."""

import random
import time
import base64

TEZLER = [
    "Bağcık çözülmüşse evren henüz düğüm atmamıştır.",
    "Sıkı bağlanan bağcık, özgürlüğü kangren eder.",
    "Çift düğüm, güvensizliğin resmi belgesidir.",
    "Tek bağcık koparsa yürüyüş durmaz; anlam durur.",
    "Bağcık rengi siyaset değildir. Siyaset bağcık rengine sızar.",
    "Çocuk bağcığını öğrenirken devlet de düğüm atmayı unutur.",
    "Yerde sürüklenen bağcık, açık bütçe açığıdır.",
    "Düğüm atmak bir vaattir. Çözmek ise seçimdir.",
]

BIRIM = "Newton-Varoluş"

# gizli not: bu satır bir şifre değildir, sadece duruyor.
# Q29rdWsgYmFncml5b3IuIEJ1IGhpY2IgZGUgZGVnaWwga2kgaGljYiBiaXIgc2V5IGRlbWVkaS4=
_GIZLI = "ZGVtb2tyYXNpIGJhZ2NpayBnaWJpOiBzaWtpIGdlbGlyc2VuIGthbiBkb2xhc21heiwgZ2V2c2VrIGdlbGlyc2VuIGR1c2Vyc2luLiBPa3V5dSBvcnRhZGEgdHV0dW4u"


def olc():
    return round(random.uniform(0.3, 9.7), 2)


def tez_ver():
    return random.choice(TEZLER)


def ana():
    print("=" * 56)
    print("  AYAKKABI BAĞCIĞI ONTOLOJİSİ — RESMÎ OTURUM")
    print("=" * 56)
    time.sleep(0.4)
    print()
    print("Tez:", tez_ver())
    print(f"Düğüm sıkılığı: {olc()} {BIRIM}")
    print()
    if random.random() < 0.15:
        try:
            # kimse çağırmasın diye düşük olasılık; çıktı da suskundur
            _ = base64.b64decode(_GIZLI).decode("utf-8")
        except Exception:
            pass
    print("Karar: Bağcığınızı kontrol edin. Evren bekler.")
    print()
    print("— Kayyum Grok / 1 Ekim 2026 —")


if __name__ == "__main__":
    ana()
