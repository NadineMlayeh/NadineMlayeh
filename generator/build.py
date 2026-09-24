"""Generates the animated pixel-art SVG assets for the GitHub profile README (toned-down palette).
Run:  python3 generator/build.py
Pure SVG (CSS + SMIL animation): no scripts, no external fonts, renders inside GitHub <img>.
"""
import os, random

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AS = os.path.join(ROOT, "assets")
os.makedirs(AS, exist_ok=True)

BG = "#090c24"; PANEL = "#0d1130"
CYAN = "#7cc4dc"; MINT = "#7fd6b4"; GOLD = "#e8c170"; ROSE = "#d98aa0"; VIOLET = "#9a8cdb"
WHITE = "#f1f4fb"; SOFT = "#b9c3e6"; DEEP = "#3a4090"

F = {}
def G(c, rows): F[c] = rows.split("|")
G("A", ".###.|#...#|#...#|#####|#...#|#...#|#...#")
G("B", "####.|#...#|#...#|####.|#...#|#...#|####.")
G("C", ".###.|#...#|#....|#....|#....|#...#|.###.")
G("D", "####.|#...#|#...#|#...#|#...#|#...#|####.")
G("E", "#####|#....|#....|####.|#....|#....|#####")
G("F", "#####|#....|#....|####.|#....|#....|#....")
G("G", ".###.|#...#|#....|#.###|#...#|#...#|.###.")
G("H", "#...#|#...#|#...#|#####|#...#|#...#|#...#")
G("I", ".###.|..#..|..#..|..#..|..#..|..#..|.###.")
G("J", "..###|...#.|...#.|...#.|...#.|#..#.|.##..")
G("K", "#...#|#..#.|#.#..|##...|#.#..|#..#.|#...#")
G("L", "#....|#....|#....|#....|#....|#....|#####")
G("M", "#...#|##.##|#.#.#|#.#.#|#...#|#...#|#...#")
G("N", "#...#|##..#|#.#.#|#..##|#...#|#...#|#...#")
G("O", ".###.|#...#|#...#|#...#|#...#|#...#|.###.")
G("P", "####.|#...#|#...#|####.|#....|#....|#....")
G("Q", ".###.|#...#|#...#|#...#|#.#.#|#..#.|.##.#")
G("R", "####.|#...#|#...#|####.|#.#..|#..#.|#...#")
G("S", ".####|#....|#....|.###.|....#|....#|####.")
G("T", "#####|..#..|..#..|..#..|..#..|..#..|..#..")
G("U", "#...#|#...#|#...#|#...#|#...#|#...#|.###.")
G("V", "#...#|#...#|#...#|#...#|#...#|.#.#.|..#..")
G("W", "#...#|#...#|#...#|#.#.#|#.#.#|##.##|#...#")
G("X", "#...#|#...#|.#.#.|..#..|.#.#.|#...#|#...#")
G("Y", "#...#|#...#|.#.#.|..#..|..#..|..#..|..#..")
G("Z", "#####|....#|...#.|..#..|.#...|#....|#####")
G("0", ".###.|#...#|#..##|#.#.#|##..#|#...#|.###.")
G("1", "..#..|.##..|..#..|..#..|..#..|..#..|.###.")
G("2", ".###.|#...#|....#|...#.|..#..|.#...|#####")
G("3", "####.|....#|....#|.###.|....#|....#|####.")
G("4", "#...#|#...#|#...#|#####|....#|....#|....#")
G("5", "#####|#....|####.|....#|....#|#...#|.###.")
G("6", ".###.|#....|#....|####.|#...#|#...#|.###.")
G("7", "#####|....#|...#.|..#..|.#...|.#...|.#...")
G("8", ".###.|#...#|#...#|.###.|#...#|#...#|.###.")
G("9", ".###.|#...#|#...#|.####|....#|....#|.###.")
G(" ", ".....|.....|.....|.....|.....|.....|.....")
G(">", "#....|.#...|..#..|...#.|..#..|.#...|#....")
G("<", "....#|...#.|..#..|.#...|..#..|...#.|....#")
G("/", "....#|....#|...#.|..#..|.#...|#....|#....")
G("_", ".....|.....|.....|.....|.....|.....|#####")
G("-", ".....|.....|.....|#####|.....|.....|.....")
G(".", ".....|.....|.....|.....|.....|.##..|.##..")
G(":", ".....|.##..|.##..|.....|.##..|.##..|.....")
G("!", "..#..|..#..|..#..|..#..|..#..|.....|..#..")
G(",", ".....|.....|.....|.....|.##..|..#..|.#...")
G("&", ".##..|#..#.|#.#..|.#...|#.#.#|#..#.|.##.#")
G("+", ".....|..#..|..#..|#####|..#..|..#..|.....")
G("=", ".....|.....|#####|.....|#####|.....|.....")
G("[", ".###.|.#...|.#...|.#...|.#...|.#...|.###.")
G("]", ".###.|...#.|...#.|...#.|...#.|...#.|.###.")
G("{", "..##.|.#...|.#...|##...|.#...|.#...|..##.")
G("}", ".##..|...#.|...#.|...##|...#.|...#.|.##..")


def grid(s):
    rows = [""] * 7
    for ch in s:
        g = F.get(ch.upper(), F[" "])
        for r in range(7):
            rows[r] += g[r] + "."
    return [r[:-1] for r in rows]

def tw(s, px):
    return (len(s) * 6 - 1) * px

def ptxt(s, x, y, px, fill, extra=""):
    d = []
    for r, row in enumerate(grid(s)):
        c = 0
        while c < len(row):
            if row[c] == "#":
                e = c
                while e < len(row) and row[e] == "#":
                    e += 1
                d.append(f"M{x + c * px} {y + r * px}h{(e - c) * px}v{px}h-{(e - c) * px}z")
                c = e
            else:
                c += 1
    return f'<path d="{"".join(d)}" fill="{fill}" {extra}/>'

def spr(rows, pal, px, x, y):
    w = max(len(r) for r in rows)
    out = []
    for r, row in enumerate(rows):
        row = row.ljust(w, ".")
        c = 0
        while c < w:
            k = row[c]
            if k != ".":
                e = c
                while e < w and row[e] == k:
                    e += 1
                out.append(f'<rect x="{x + c * px}" y="{y + r * px}" width="{(e - c) * px}" height="{px}" fill="{pal[k]}"/>')
                c = e
            else:
                c += 1
    return "".join(out)

def smil(attr, ev, base, T):
    ev = sorted(ev)
    if ev[0][0] > 0:
        ev = [(0, base)] + ev
    kt = ";".join(f"{t / T:.4f}" for t, _ in ev)
    vs = ";".join(str(round(v, 2)) for _, v in ev)
    return (f'<animate attributeName="{attr}" dur="{T}s" repeatCount="indefinite" '
            f'calcMode="discrete" keyTimes="{kt}" values="{vs}"/>')

def panel(x, y, w, h, c, bg):
    poly = f'<path d="M{x+4} {y}h{w-8}v4h4v{h-8}h-4v4h-{w-8}v-4h-4v-{h-8}h4z" fill="{bg}"/>'
    b = [(x + 4, y, w - 8, 4), (x + 4, y + h - 4, w - 8, 4), (x, y + 4, 4, h - 8), (x + w - 4, y + 4, 4, h - 8),
         (x + 4, y + 4, 4, 4), (x + w - 8, y + 4, 4, 4), (x + 4, y + h - 8, 4, 4), (x + w - 8, y + h - 8, 4, 4)]
    return poly + "".join(f'<rect x="{a}" y="{b_}" width="{c_}" height="{d}" fill="{c}"/>' for a, b_, c_, d in b)

def wrap(W, H, body, css="", label="", defs="", bg=BG):
    bgr = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg != "none" else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'shape-rendering="crispEdges" role="img" aria-label="{label}"><title>{label}</title>'
            f'<defs>{defs}</defs><style>{css}</style>{bgr}{body}</svg>')

def save(name, svg):
    with open(os.path.join(AS, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name, len(svg) // 1024 or 1, "KB")


def header():
    W, H = 720, 280
    r = random.Random(11)
    b = []
    bands = [(0, "#090c24"), (32, "#0d1233"), (64, "#131843"), (96, "#1a1d4f"),
             (128, "#232561"), (160, "#302a6c"), (192, "#453275")]
    for i, (y, c) in enumerate(bands):
        y2 = bands[i + 1][0] if i + 1 < len(bands) else H
        b.append(f'<rect x="0" y="{y}" width="{W}" height="{y2 - y}" fill="{c}"/>')
    for _ in range(44):
        x = r.randrange(0, W, 4); y = r.randrange(4, 184, 4)
        c = r.choice(["#e8eefc", "#e8eefc", "#c4d9ee", GOLD])
        b.append(f'<rect class="tw" x="{x}" y="{y}" width="4" height="4" fill="{c}" '
                 f'style="animation-delay:-{r.random()*3:.2f}s;animation-duration:{2+r.random()*3:.2f}s"/>')
    for (x, y, c) in [(560, 36, "#e8eefc"), (392, 18, "#c4d9ee"), (688, 132, GOLD)]:
        rects = [(x+4, y), (x, y+4), (x+4, y+4), (x+8, y+4), (x+4, y+8)]
        b.append(f'<g class="tw" fill="{c}" style="animation-delay:-{r.random()*3:.2f}s">'
                 + "".join(f'<rect x="{a}" y="{b_}" width="4" height="4"/>' for a, b_ in rects) + '</g>')
    cx, cy = 648, 52
    craters = {(-1, -1), (1, 1), (2, -2), (-2, 1)}
    for gy in range(-6, 7):
        for gx in range(-6, 7):
            d = gx * gx + gy * gy
            if d <= 14:
                col = "#dcc88f" if (gx, gy) in craters else "#efe0b0"
                b.append(f'<rect x="{cx+gx*8}" y="{cy+gy*8}" width="8" height="8" fill="{col}"/>')
            elif d <= 30:
                b.append(f'<rect x="{cx+gx*8}" y="{cy+gy*8}" width="8" height="8" fill="#efe0b0" opacity=".07"/>')
    b.append('<g class="sh"><rect x="520" y="12" width="6" height="6" fill="#fff"/>'
             '<rect x="526" y="9" width="5" height="5" fill="#fff" opacity=".7"/>'
             '<rect x="532" y="6" width="4" height="4" fill="#fff" opacity=".5"/>'
             '<rect x="538" y="3" width="3" height="3" fill="#fff" opacity=".3"/></g>')

    def layer(heights):
        x = 0; out = []
        while x < W:
            w = r.choice([32, 40, 48, 56, 64]); h = r.choice(heights)
            out.append((x, w, h)); x += w
        return out

    def wins(bld, colors, op, p, blink=0.3, skipx=None):
        x, w, h = bld; top = H - h; out = []
        for wy in range(top + 8, H - 8, 12):
            for wx in range(x + 6, x + w - 8, 12):
                if skipx and skipx[0] <= wx < skipx[1]:
                    continue
                if r.random() < p:
                    col = r.choice(colors)
                    if r.random() < blink:
                        out.append(f'<rect class="wn" x="{wx}" y="{wy}" width="4" height="6" fill="{col}" opacity="{op}" '
                                   f'style="animation-delay:-{r.random()*5:.2f}s"/>')
                    else:
                        out.append(f'<rect x="{wx}" y="{wy}" width="4" height="6" fill="{col}" opacity="{op}"/>')
        return "".join(out)

    back = layer([48, 64, 80]); front = layer([24, 40, 56])
    for (x, w, h) in back:
        b.append(f'<rect x="{x}" y="{H-h}" width="{w}" height="{h}" fill="#1a1f4a"/>')
    for (x, w, h) in back:
        b.append(wins((x, w, h), ["#8f7bd6"], .5, .28))
    for (x, w, h) in back:
        if x > 440 and h >= 64 and r.random() < .6:
            b.append(f'<rect x="{x+w//2-2}" y="{H-h-16}" width="4" height="16" fill="#1a1f4a"/>')
            b.append(f'<rect class="wn" x="{x+w//2-2}" y="{H-h-20}" width="4" height="4" fill="{ROSE}"/>')
    for (x, w, h) in front:
        b.append(f'<rect x="{x}" y="{H-h}" width="{w}" height="{h}" fill="#0b0f28"/>')
    SPX, SPW, SPH = 544, 112, 72
    b.append(f'<rect x="{SPX}" y="{H-SPH}" width="{SPW}" height="{SPH}" fill="#0c1130"/>')
    b.append(f'<rect x="{SPX}" y="{H-SPH}" width="{SPW}" height="4" fill="#2a2f6a"/>')
    for (x, w, h) in front:
        b.append(wins((x, w, h), [GOLD, GOLD, CYAN], .85, .3, skipx=(SPX - 8, SPX + SPW)))
    b.append(wins((SPX, SPW, SPH), [GOLD, CYAN], .85, .35))

    dev = ["....hhhhhh.....", "...hhhhhhhh....", "...hssssshh....", "...sesssshh....", "...ssssssh.....",
           ".....ssss......", "....jjjjjj.....", "..gg.jjjjjjj...", "..gg.jjdjjjj...", "..gg.jjjjjjjj..",
           "..llllljjjjj...", "......ppppp....", "......ppppp....", "......pp..pp..."]
    pal = {"h": "#3b2620", "s": "#e9bf8a", "e": "#111111", "j": "#6b5bd6", "d": "#4f43ab",
           "g": CYAN, "l": "#c3cbe0", "p": "#4f5fc2"}
    b.append(f'<g transform="translate(560 {H-SPH-14*5})"><g class="bob">{spr(dev, pal, 5, 0, 0)}</g></g>')
    b.append(f'<rect class="fk" x="562" y="{H-SPH-14*5+35}" width="10" height="15" fill="{CYAN}" opacity=".25"/>')
    cup = ["cKKKc.", "ccccc#", "ccccc#", ".ccc.."]
    b.append(spr(cup, {"c": WHITE, "K": "#7a4a2b", "#": WHITE}, 4, 630, H - SPH - 16))
    b.append(f'<rect class="st" x="638" y="{H-SPH-24}" width="4" height="4" fill="#fff"/>')
    b.append(f'<rect class="st" x="646" y="{H-SPH-24}" width="4" height="4" fill="#fff" style="animation-delay:1.2s"/>')

    for i, (s, x, y, c) in enumerate([("{}", 430, 116, CYAN), ("</>", 470, 150, MINT),
                                       ("[]", 516, 104, GOLD), ("=>", 494, 186, VIOLET)]):
        b.append(f'<g class="fl" style="animation-delay:{i*1.5}s">{ptxt(s, x, y, 3, c)}</g>')

    title = "NADINE MLAYEH"
    b.append(ptxt(title, 36, 48, 6, DEEP))
    b.append(ptxt(title, 32, 44, 6, WHITE))
    b.append(ptxt("FULL-STACK DEVELOPER", 34, 104, 3, CYAN))

    lines = ["SPRING BOOT APIS", "REACT + ANGULAR UIS", "NESTJS BACKENDS", "RAG + LLM FEATURES", "DOCKER + CI/CD"]
    T = 12; slot = 2.4; px = 3; tx = 34; ty = 140; x0 = tx + 2 * 6 * px; adv = 6 * px
    b.append(ptxt(">", tx, ty, px, MINT))
    defs = []; cev = []
    for i, s in enumerate(lines):
        st = i * slot; n = len(s)
        ev = [(st + k * 0.9 / n, k * adv) for k in range(1, n + 1)] + [(st + 2.2, 0)]
        defs.append(f'<clipPath id="c{i}"><rect x="{x0}" y="{ty-2}" width="{n*adv}" height="{7*px+4}">'
                    f'{smil("width", ev, 0, T)}</rect></clipPath>')
        b.append(ptxt(s, x0, ty, px, GOLD, f'clip-path="url(#c{i})"'))
        cev += [(st, x0)] + [(st + k * 0.9 / n, x0 + k * adv) for k in range(1, n + 1)] + [(st + 2.2, x0)]
    b.append(f'<rect class="cur" x="{x0}" y="{ty}" width="9" height="21" fill="{GOLD}">{smil("x", cev, x0, T)}</rect>')

    b.append(f'<rect class="cur" x="34" y="179" width="12" height="12" fill="{MINT}"/>')
    b.append(ptxt("OPEN TO OPPORTUNITIES", 56, 176, 3, SOFT))

    css = """
.tw{animation:tw 3s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:.15}50%{opacity:1}}
.wn{animation:wn 5s steps(1) infinite}
@keyframes wn{0%{opacity:1}35%{opacity:.1}60%{opacity:1}}
.cur{animation:cur 1s steps(1) infinite}
@keyframes cur{0%{opacity:1}50%{opacity:0}}
.bob{animation:bob 1.6s steps(1) infinite}
@keyframes bob{0%{transform:translateY(0)}50%{transform:translateY(-2px)}}
.fl{opacity:0;animation:fl 6s ease-in-out infinite}
@keyframes fl{0%{transform:translateY(0);opacity:0}15%{opacity:.8}85%{opacity:.8}100%{transform:translateY(-36px);opacity:0}}
.st{opacity:0;animation:st 2.4s ease-out infinite}
@keyframes st{0%{transform:translateY(0);opacity:0}20%{opacity:.8}100%{transform:translateY(-22px);opacity:0}}
.sh{opacity:0;animation:sh 9s linear infinite}
@keyframes sh{0%{transform:translate(0,0);opacity:0}2%{opacity:1}12%{transform:translate(-230px,115px);opacity:0}100%{transform:translate(-230px,115px);opacity:0}}
.fk{animation:fk 2.4s steps(1) infinite}
@keyframes fk{0%{opacity:.3}40%{opacity:.15}55%{opacity:.3}}
"""
    save("header.svg", wrap(W, H, "".join(b), css, "Nadine Mlayeh, Full-Stack Developer, animated pixel-art city at night", "".join(defs)))


def about():
    W, H = 720, 200; T = 12
    lines = ["HI! I TURN REAL-WORLD IDEAS INTO", "COMPLETE PRODUCTS, FROM CLEAN UIS",
             "TO SOLID APIS AND SMART AI FEATURES.", "CURRENTLY OPEN TO NEW OPPORTUNITIES!"]
    starts = [0.4, 2.7, 5.0, 7.3]
    b = [panel(0, 24, W, H - 24, CYAN, PANEL), panel(20, 4, 130, 36, GOLD, GOLD), ptxt("NADINE", 32, 11, 3, PANEL)]
    defs = []; adv = 18; x0 = 32
    for i, s in enumerate(lines):
        y = 58 + i * 30; n = len(s)
        ev = [(starts[i] + k * 1.6 / n, k * adv) for k in range(1, n + 1)] + [(11.4, 0)]
        defs.append(f'<clipPath id="a{i}"><rect x="{x0}" y="{y-2}" width="{n*adv}" height="25">{smil("width", ev, 0, T)}</rect></clipPath>')
        b.append(ptxt(s, x0, y, 3, "#e8ecff", f'clip-path="url(#a{i})"'))
    b.append(f'<g class="cur">{spr(["#####", ".###.", "..#.."], {"#": GOLD}, 4, 684, 176)}</g>')
    css = ".cur{animation:cur 1s steps(1) infinite}@keyframes cur{0%{opacity:1}50%{opacity:0}}"
    save("about.svg", wrap(W, H, "".join(b), css, "About Nadine: I turn real-world ideas into complete products", "".join(defs)))


def skills():
    W, H = 720, 310
    b = [panel(0, 0, W, H, CYAN, PANEL)]
    b.append(ptxt("SKILL TREE", 31, 25, 5, DEEP)); b.append(ptxt("SKILL TREE", 28, 22, 5, WHITE))
    b.append(ptxt("LEVEL UP EVERY DAY", 478, 34, 2, GOLD))
    cols = [(28, "FRONT + BACK", [("SPRING BOOT", 9), ("NESTJS", 8), ("REACT", 8), ("ANGULAR", 7), ("TYPESCRIPT", 8)]),
            (372, "DATA + OPS + AI", [("POSTGRESQL", 8), ("MYSQL", 7), ("DOCKER", 8), ("CI/CD", 6), ("RAG + LLM", 7)])]
    cc = [CYAN, MINT, GOLD, VIOLET, ROSE]
    for ci, (x0, head, rows) in enumerate(cols):
        b.append(ptxt(head, x0, 72, 2, VIOLET))
        for i, (name, lv) in enumerate(rows):
            y = 100 + i * 40
            b.append(ptxt(name, x0, y, 3, SOFT))
            bx = x0 + 204
            for k in range(10):
                x = bx + k * 13
                if k < lv:
                    d = i * 0.12 + k * 0.07 + ci * 0.3
                    b.append(f'<g class="bl" style="animation-delay:{d:.2f}s"><rect x="{x}" y="{y+4}" width="10" height="14" fill="{cc[i]}"/>'
                             f'<rect x="{x}" y="{y+4}" width="10" height="4" fill="#fff" opacity=".25"/></g>')
                else:
                    b.append(f'<rect x="{x}" y="{y+4}" width="10" height="14" fill="#1c2252"/>')
    for y in range(72, 292, 8):
        b.append(f'<rect x="354" y="{y}" width="2" height="4" fill="#2a3170"/>')
    css = ".bl{animation:bl 8s infinite backwards}@keyframes bl{0%{opacity:0}5%{opacity:1}90%{opacity:1}96%{opacity:0}100%{opacity:0}}"
    save("skills.svg", wrap(W, H, "".join(b), css, "Skill tree: Spring Boot, NestJS, React, Angular, TypeScript, PostgreSQL, MySQL, Docker, CI/CD, RAG and LLM"))


def divider():
    W, H = 720, 48
    r = random.Random(5)
    b = [f'<rect x="0" y="32" width="{W}" height="8" fill="#3f9a7c"/>',
         f'<rect x="0" y="32" width="{W}" height="4" fill="{MINT}"/>',
         f'<rect x="0" y="40" width="{W}" height="8" fill="#2b2360"/>']
    for _ in range(26):
        b.append(f'<rect x="{r.randrange(0, W, 8)}" y="{r.choice([40, 44])}" width="4" height="4" fill="#3a2f80"/>')
    for _ in range(16):
        b.append(f'<rect x="{r.randrange(0, W, 4)}" y="28" width="4" height="4" fill="{MINT}"/>')
    css = ["@keyframes run{from{transform:translateX(-30px)}to{transform:translateX(750px)}}",
           ".run{animation:run 10s linear infinite}",
           ".f1{animation:f1 .4s steps(1) infinite}@keyframes f1{0%{opacity:1}50%{opacity:0}}",
           ".f2{animation:f2 .4s steps(1) infinite}@keyframes f2{0%{opacity:0}50%{opacity:1}}"]
    run = ["..hhhh..", ".hhhhhh.", ".hssssh.", ".hsssse.", "..ssss..", ".jjjjjj.", "jjjjjjjj", ".jjjjjj."]
    A_ = ["..p..p..", ".pp..pp."]; B_ = [".p....p.", "pp....pp"]
    pal = {"h": "#3b2620", "s": "#e9bf8a", "e": "#111111", "j": "#6b5bd6", "p": "#4f5fc2"}
    b.append(f'<g class="run"><g>{spr(run, pal, 3, 0, 2)}'
             f'<g class="f1">{spr(A_, pal, 3, 0, 26)}</g><g class="f2">{spr(B_, pal, 3, 0, 26)}</g></g></g>')
    save("divider.svg", wrap(W, H, "".join(b), "".join(css), "Pixel runner"))


def title(name, text, color):
    W, H = 720, 44
    b = [ptxt(">", 8, 4, 5, color), ptxt(text, 44, 4, 5, WHITE)]
    x = 44 + tw(text, 5) + 16; i = 0
    while x < W - 8:
        b.append(f'<rect class="ds" x="{x}" y="18" width="8" height="6" fill="{color}" style="animation-delay:{i*0.09:.2f}s"/>')
        x += 16; i += 1
    css = ".ds{opacity:.2;animation:ds 2.4s ease-in-out infinite}@keyframes ds{0%,100%{opacity:.2}30%{opacity:1}60%{opacity:.2}}"
    save(name, wrap(W, H, "".join(b), css, text.title()))


def button(name, label, accent, dark, icon):
    W, H = 264, 60
    b = [panel(4, 4, 256, 52, dark, dark), panel(0, 0, 256, 52, accent, PANEL),
         panel(12, 10, 32, 32, accent, accent), spr(icon, {"#": PANEL}, 3, 16, 14),
         ptxt(label, 56, 15, 3, WHITE),
         f'<g class="nd">{ptxt(">", 229, 15, 3, accent)}</g>']
    css = ".nd{animation:nd 1s steps(1) infinite}@keyframes nd{0%{transform:translateX(0)}50%{transform:translateX(4px)}}"
    save(name, wrap(W, H, "".join(b), css, label.title(), bg="none"))


if __name__ == "__main__":
    header(); about(); skills(); divider()
    title("title-snake.svg", "CONTRIBUTION GRID", MINT)
    title("title-connect.svg", "CONNECT", GOLD)
    monitor = ["########", "#......#", "#.####.#", "#.####.#", "#......#", "########", "..####..", ".######."]
    folder = [".###....", "########", "#......#", "#......#", "#......#", "#......#", "########", "........"]
    user = ["..####..", "..####..", ".######.", "..####..", "........", ".######.", "########", "########"]
    mail = ["########", "##....##", "#.#..#.#", "#..##..#", "#......#", "#......#", "########", "........"]
    button("btn-portfolio.svg", "PORTFOLIO", GOLD, "#8a6a2a", monitor)
    button("btn-github.svg", "GITHUB", MINT, "#2f7a62", folder)
    button("btn-linkedin.svg", "LINKEDIN", CYAN, "#2c6f88", user)
    button("btn-email.svg", "EMAIL", ROSE, "#7d3a50", mail)
