# Behin-behineko irudiak sortzeko gidoia (matplotlib xkcd estiloa + Purisa letra).
# Exekutatu latex/ karpetatik: python3 ../01_idazketa_oharrak/irudiak_behin_behinekoak.py
# Irudi bakoitza eskuz berriro marraztu behar da Xournal-en (Pictures/NN/*.xoj) argitaratu aurretik.
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np, warnings
warnings.filterwarnings("ignore")
plt.rcParams["pdf.fonttype"] = 42
INK = "#111111"; RED = "#c0392b"; GREEN = "#1e8449"; BLUE = "#1f4e79"

def box(ax, x, y, w, h, text="", fc="white", ec=INK, fs=13, lw=2, rounded=True, color=INK):
    style = "round,pad=0.02,rounding_size=0.25" if rounded else "square,pad=0.02"
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw))
    if text: ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs, color=color)

def arrow(ax, p, q, lw=2, color=INK, rad=0.0, style="->"):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle=style, lw=lw, color=color, connectionstyle=f"arc3,rad={rad}"))

def start():
    plt.rcParams["font.family"] = "Purisa"; plt.rcParams["font.size"] = 13

# ---------- 1. Botila-lepoa lekuz aldatu da ----------
with plt.xkcd(scale=1.1, length=120, randomness=2):
    start()
    fig, ax = plt.subplots(figsize=(10, 4.4)); ax.set_xlim(0, 100); ax.set_ylim(0, 10); ax.axis("off")
    rows = [("Lehen", 6.6, [("erabaki", 9), ("banatu", 9), ("kodea idatzi", 44), ("egiaztatu", 12), ("integratu", 12)], 2),
            ("Orain", 2.0, [("erabaki", 22), ("banatu", 20), ("kodea idatzi", 6), ("egiaztatu", 20), ("integratu", 18)], 2)]
    for name, y, segs, bn in rows:
        ax.text(1, y + 0.9, name, fontsize=17, va="center", color=INK)
        x = 12
        for i, (lab, w) in enumerate(segs):
            hot = (i == bn)
            box(ax, x, y, w, 1.8, "", fc=("#f9d5d0" if hot else "white"), ec=(RED if hot else INK), rounded=False)
            if w >= 16: ax.text(x + w/2, y + 0.9, lab, ha="center", va="center", fontsize=12, color=(RED if hot else INK))
            else: ax.text(x + w/2, y - 0.55, lab, ha="center", va="top", fontsize=10, color=(RED if hot else INK))
            x += w
    ax.text(62, 9.3, "lanik astunena", color=RED, fontsize=12, ha="center")
    arrow(ax, (62, 9.0), (53, 8.5), color=RED)
    ax.text(78, 5.0, "lan astunak lekuz aldatu dira", color=RED, fontsize=12, ha="center")
    arrow(ax, (66, 4.8), (36, 3.9), color=RED, rad=0.25)
    arrow(ax, (84, 4.7), (92, 3.9), color=RED, rad=-0.3)
    fig.savefig("Pictures/01/1.lan_astunak.pdf", bbox_inches="tight"); plt.close(fig)

# ---------- 4. Git vs GitHub ----------
with plt.xkcd(scale=1.1, length=120, randomness=2):
    start()
    fig, ax = plt.subplots(figsize=(10, 6.2)); ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis("off")
    box(ax, 14, 31, 84, 27, "", fc="#eef6fb", ec=BLUE, lw=2)
    ax.text(18, 55, "GitHub: plataforma (geruza soziala eta kudeaketakoa)", fontsize=12, color=BLUE, va="center")
    box(ax, 14, 2, 84, 27, "", fc="#f7f7f7", ec=INK, lw=2)
    ax.text(33, 26, "Git: teknologia (konfirmazioen grafoa eta sinkronizazioa)", fontsize=11, color=INK, va="center")
    rows = [(44.5, ["issue-ak", "pull request-ak", "berrikuspenak"]), (34.5, ["proiektu-taula", "Actions", "baimenak"])]
    for y, items in rows:
        x = 20
        for it in items:
            box(ax, x, y, 24, 7.5, it, fc="white", ec=BLUE, fs=11, color=BLUE); x += 26
    box(ax, 20, 9, 16, 11, "garatzailea", fs=12)
    box(ax, 74, 9, 16, 11, "agentea", fs=12)
    box(ax, 47, 8, 16, 13, "origin", fs=14)
    ax.text(55, 5.8, "urruneko helbidea", fontsize=10, ha="center", color=INK)
    arrow(ax, (36, 14.5), (47, 14.5), style="<->"); ax.text(41.5, 16.5, "push / pull", fontsize=10, ha="center")
    arrow(ax, (74, 14.5), (63, 14.5), style="<->"); ax.text(68.5, 16.5, "push / pull", fontsize=10, ha="center")
    arrow(ax, (28, 20), (28, 33), color=BLUE, style="<->"); ax.text(26.5, 26.5, "koordinatu", fontsize=10, color=BLUE, rotation=90, va="center", ha="center")
    arrow(ax, (82, 20), (82, 33), color=BLUE, style="<->"); ax.text(83.8, 26.5, "koordinatu", fontsize=10, color=BLUE, rotation=90, va="center", ha="center")
    ax.text(3, 44.5, "GitHub", fontsize=15, color=BLUE, va="center", rotation=90)
    ax.text(3, 15.5, "Git", fontsize=15, color=INK, va="center", rotation=90)
    fig.savefig("Pictures/04/4.git_vs_github.pdf", bbox_inches="tight"); plt.close(fig)

# ---------- 7. Bi begiztak ----------
with plt.xkcd(scale=1.1, length=120, randomness=2):
    start()
    fig, ax = plt.subplots(figsize=(9, 8)); ax.set_xlim(-5.5, 5.5); ax.set_ylim(-4.8, 5.1); ax.set_aspect("equal"); ax.axis("off")
    def loop(r, labels, color, lw):
        ax.add_patch(Circle((0, 0), r, fill=False, ec=color, lw=lw))
        for ang in (60, 150, 240, 330):   # arrowheads, clockwise
            a1, a2 = np.radians(ang + 9), np.radians(ang - 9)
            arrow(ax, (r*np.cos(a1), r*np.sin(a1)), (r*np.cos(a2), r*np.sin(a2)), color=color, lw=lw, rad=-0.25)
        for (lab, ang) in labels:
            a = np.radians(ang); x, y = r*np.cos(a), r*np.sin(a)
            bw = 2.1 if r > 2 else 1.6
            box(ax, x - bw/2, y - 0.36, bw, 0.72, lab, fc="white", ec=color, fs=11 if r > 2 else 10, lw=1.8, color=color)
    loop(3.6, [("Sprint-planifikazioa", 90), ("Lana", 0), ("Sprint-berrikuspena", 270), ("Atzera-begirakoa", 180)], INK, 2.2)
    loop(1.35, [("Egiteko", 90), ("Egiten", 0), ("Berrikusteko", 270), ("Eginda", 180)], GREEN, 2.0)
    ax.text(0, 0.25, "agenteak", ha="center", fontsize=13, color=GREEN)
    ax.text(0, -0.35, "minutuak / orduak", ha="center", fontsize=10, color=GREEN)
    ax.text(-5.3, 4.7, "gizakiak: egunak / asteak", fontsize=13, color=INK)
    arrow(ax, (-3.9, 4.4), (-2.8, 2.8), color=INK, rad=0.2)
    fig.savefig("Pictures/07/7.bi_begiztak.pdf", bbox_inches="tight"); plt.close(fig)
print("figures done")
