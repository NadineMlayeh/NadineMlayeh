"""Generates the animated SVG assets for the GitHub profile README (calm, modern look).
Run:  python3 generator/build.py
Pure SVG + CSS animation: no scripts, no external fonts, renders inside GitHub <img>.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AS = os.path.join(ROOT, "assets")
os.makedirs(AS, exist_ok=True)

FONT = "Inter,'Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif"
TEAL = "#5eead4"; SKY = "#7dd3fc"; INDIGO = "#a5b4fc"; VIOLET = "#c4b5fd"
INK = "#f1f5f9"; MUTED = "#94a3b8"; PANEL = "#0d1526"; LINE = "#1e2b4a"


def save(name, svg):
    with open(os.path.join(AS, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name, len(svg) // 1024 or 1, "KB")


def header():
    W, H = 720, 260
    cols = []
    for c in range(51):
        x = 8 + c * 14
        d = "".join(f"M{x} {y}h3v3h-3z" for y in range(8, 252, 14))
        cols.append(f'<path class="cl" d="{d}" fill="url(#dg)" style="animation-delay:-{c*0.16:.2f}s"/>')
    taglines = ["Spring Boot &amp; NestJS backends", "React &amp; Angular interfaces",
                "AI, LLMs &amp; RAG", "Docker &amp; CI/CD"]
    tg = "".join(
        f'<text class="tg" x="48" y="162" font-size="15" fill="{MUTED}" style="animation-delay:{i*3}s">{t}</text>'
        for i, t in enumerate(taglines))
    css = f"""
text{{font-family:{FONT}}}
.cl{{opacity:.08;animation:wv 7s ease-in-out infinite}}
@keyframes wv{{0%,100%{{opacity:.08}}50%{{opacity:.6}}}}
.o1{{animation:d1 16s ease-in-out infinite alternate}}
@keyframes d1{{from{{transform:translate(0,0)}}to{{transform:translate(-40px,30px)}}}}
.o2{{animation:d2 19s ease-in-out infinite alternate}}
@keyframes d2{{from{{transform:translate(0,0)}}to{{transform:translate(50px,-30px)}}}}
.tg{{opacity:0;animation:tg 12s ease-in-out infinite}}
@keyframes tg{{0%{{opacity:0;transform:translateY(6px)}}5%{{opacity:1;transform:translateY(0)}}22%{{opacity:1;transform:translateY(0)}}27%{{opacity:0;transform:translateY(-6px)}}100%{{opacity:0;transform:translateY(-6px)}}}}
.pl{{transform-box:fill-box;transform-origin:center;animation:pl 2.4s ease-out infinite}}
@keyframes pl{{0%{{transform:scale(1);opacity:.6}}100%{{transform:scale(3.2);opacity:0}}}}
"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Nadine Mlayeh, Full-Stack Developer">
<title>Nadine Mlayeh, Full-Stack Developer</title>
<defs>
<style>{css}</style>
<clipPath id="r"><rect width="{W}" height="{H}" rx="16"/></clipPath>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset=".55" stop-color="#101c33"/><stop offset="1" stop-color="#0c1425"/></linearGradient>
<linearGradient id="dg" x1="0" x2="{W}" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{MUTED}"/><stop offset="1" stop-color="{SKY}"/></linearGradient>
<linearGradient id="fd" x1="0" x2="1"><stop offset=".3" stop-color="#000"/><stop offset=".85" stop-color="#fff"/></linearGradient>
<mask id="mk"><rect width="{W}" height="{H}" fill="url(#fd)"/></mask>
<linearGradient id="sub" x1="48" x2="260" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{SKY}"/></linearGradient>
<linearGradient id="hl" x1="0" x2="1"><stop offset="0" stop-color="{TEAL}" stop-opacity=".9"/><stop offset=".6" stop-color="#818cf8" stop-opacity=".6"/><stop offset="1" stop-color="#818cf8" stop-opacity="0"/></linearGradient>
<filter id="bl" filterUnits="userSpaceOnUse" x="-150" y="-150" width="1020" height="560"><feGaussianBlur stdDeviation="42"/></filter>
</defs>
<g clip-path="url(#r)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<g filter="url(#bl)"><circle class="o1" cx="600" cy="70" r="110" fill="#6366f1" opacity=".38"/><circle class="o2" cx="140" cy="250" r="90" fill="#14b8a6" opacity=".26"/></g>
<g mask="url(#mk)">{"".join(cols)}</g>
<text x="48" y="96" font-size="44" font-weight="700" fill="{INK}" letter-spacing="-0.5">Nadine Mlayeh</text>
<text x="48" y="130" font-size="20" font-weight="500" fill="url(#sub)">Full-Stack Developer</text>
{tg}
<rect x="48" y="184" width="196" height="30" rx="15" fill="{TEAL}" fill-opacity=".08" stroke="{TEAL}" stroke-opacity=".35"/>
<circle class="pl" cx="67" cy="199" r="4" fill="{TEAL}"/>
<circle cx="67" cy="199" r="4" fill="{TEAL}"/>
<text x="82" y="204" font-size="13" fill="#99f6e4">Open to opportunities</text>
<rect y="{H-2}" width="{W}" height="2" fill="url(#hl)"/>
</g>
</svg>'''
    save("header.svg", svg)


def skills():
    W = 720
    groups = [
        ("FRONTEND", SKY, ["React", "Angular", "TypeScript", "JavaScript", "HTML/CSS"]),
        ("BACKEND", TEAL, ["Spring Boot", "NestJS", "Node.js", "REST APIs"]),
        ("DATA", INDIGO, ["PostgreSQL", "MySQL", "MongoDB", "Prisma"]),
        ("DEVOPS &amp; AI", VIOLET, ["Docker", "CI/CD", "GitHub Actions", "RAG", "LLMs"]),
    ]
    H = 210
    out = []; n = 0
    for i, (label, col, items) in enumerate(groups):
        y = 26 + i * 46
        out.append(f'<text x="32" y="{y+19}" font-size="11" font-weight="600" letter-spacing="1.6" fill="{col}">{label}</text>')
        x = 176
        for it in items:
            w = round(len(it) * 7.4 + 26)
            out.append(f'<g class="ch" style="animation-delay:{n*0.06:.2f}s"><rect x="{x}" y="{y}" width="{w}" height="30" rx="8" '
                       f'fill="{col}" fill-opacity=".08" stroke="{col}" stroke-opacity=".35"/>'
                       f'<text x="{x+w/2}" y="{y+20}" font-size="13" text-anchor="middle" fill="#e2e8f0">{it}</text></g>')
            x += w + 8; n += 1
    css = (f"text{{font-family:{FONT}}}"
           ".ch{animation:in .7s ease-out both}"
           "@keyframes in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="Tech stack: React, Angular, TypeScript, Spring Boot, NestJS, PostgreSQL, MySQL, Docker, CI/CD, RAG, LLMs">'
           f'<style>{css}</style><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="{PANEL}" stroke="{LINE}"/>'
           + "".join(out) + "</svg>")
    save("skills.svg", svg)


def button(name, label, w, primary=False):
    H = 44
    css = f"text{{font-family:{FONT}}}"
    if primary:
        css += f".sh{{animation:sh 5s ease-in-out infinite}}@keyframes sh{{0%,55%{{transform:translateX(0) skewX(-20deg)}}100%{{transform:translateX({w+120}px) skewX(-20deg)}}}}"
        body = (f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#0d9488"/><stop offset="1" stop-color="#4f46e5"/></linearGradient>'
                f'<clipPath id="c"><rect width="{w}" height="{H}" rx="10"/></clipPath></defs>'
                f'<g clip-path="url(#c)"><rect width="{w}" height="{H}" fill="url(#g)"/>'
                f'<rect class="sh" x="-70" y="-10" width="34" height="70" fill="#fff" opacity=".18"/></g>'
                f'<text x="{w/2}" y="27" font-size="14" font-weight="600" text-anchor="middle" fill="#fff">{label}</text>')
    else:
        body = (f'<rect x=".5" y=".5" width="{w-1}" height="{H-1}" rx="10" fill="{PANEL}" stroke="#2a3a5e"/>'
                f'<text x="{w/2}" y="27" font-size="14" font-weight="600" text-anchor="middle" fill="#e2e8f0">{label}</text>')
    save(name, f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {H}" width="{w}" height="{H}" role="img" aria-label="{label}"><style>{css}</style>{body}</svg>')


if __name__ == "__main__":
    header(); skills()
    button("btn-repos.svg", "Repositories &amp; projects  →", 260, primary=True)
    button("btn-linkedin.svg", "LinkedIn", 120)
    button("btn-email.svg", "Email", 110)
