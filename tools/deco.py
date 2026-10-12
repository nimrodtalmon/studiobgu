# Generates subtle line illustrations (orange on dark/light slides, dark on orange slides).
import sys, os
out = sys.argv[1]
O, D = "#F7941D", "#26282C"

def svg(body, stroke, fill):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" fill="none" '
            f'stroke="{stroke}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
            + body.replace("FILL", fill) + '</svg>\n')

designs = {}
# network of people/ideas
pts = [(80,300),(160,200),(260,250),(320,130),(200,90),(110,110),(330,320)]
edges = [(0,1),(1,2),(2,3),(3,4),(4,1),(1,5),(5,4),(2,6),(0,2)]
b = "".join(f'<line x1="{pts[a][0]}" y1="{pts[a][1]}" x2="{pts[c][0]}" y2="{pts[c][1]}" opacity=".55"/>' for a,c in edges)
b += "".join(f'<circle cx="{x}" cy="{y}" r="16"/>' for i,(x,y) in enumerate(pts) if i != 2)
b += f'<circle cx="{pts[2][0]}" cy="{pts[2][1]}" r="20" fill="FILL" stroke="none"/>'
designs["network"] = b
# paper sheet
designs["paper"] = ('<path d="M110 40 H250 L310 100 V360 H110 Z"/><path d="M250 40 V100 H310"/>'
    '<line x1="140" y1="130" x2="240" y2="130" stroke-width="9"/>'
    + "".join(f'<line x1="140" y1="{y}" x2="{280 if i%3 else 250}" y2="{y}" opacity=".6"/>' for i,y in enumerate(range(175,340,30))))
# stacked floors
designs["stack"] = ('<rect x="60" y="300" width="280" height="50" rx="8"/>'
    '<rect x="90" y="240" width="220" height="50" rx="8"/>'
    '<rect x="120" y="180" width="160" height="50" rx="8"/>'
    '<rect x="150" y="110" width="100" height="60" rx="8" fill="FILL" stroke="none"/>')
# magnifier over text
designs["magnifier"] = ('<circle cx="170" cy="170" r="100"/><line x1="242" y1="242" x2="340" y2="340" stroke-width="16"/>'
    '<line x1="115" y1="140" x2="225" y2="140" opacity=".6"/><line x1="115" y1="170" x2="210" y2="170" opacity=".6"/>'
    '<line x1="115" y1="200" x2="190" y2="200" fill="FILL" stroke="FILL" stroke-width="9"/>')
# two speech bubbles
designs["bubbles"] = ('<path d="M50 80 H230 a20 20 0 0 1 20 20 V190 a20 20 0 0 1 -20 20 H120 L80 250 V210 H70 a20 20 0 0 1 -20 -20 V100 a20 20 0 0 1 20 -20 Z"/>'
    '<path d="M170 230 H330 a20 20 0 0 1 20 20 V320 a20 20 0 0 1 -20 20 H320 V375 L285 340 H190 a20 20 0 0 1 -20 -20 Z" fill="FILL" stroke="none"/>')
# light bulb
designs["bulb"] = ('<path d="M200 50 a105 105 0 0 1 60 191 V280 H140 V241 A105 105 0 0 1 200 50 Z"/>'
    '<line x1="150" y1="315" x2="250" y2="315"/><line x1="165" y1="350" x2="235" y2="350"/>'
    '<circle cx="200" cy="140" r="0" />'
    '<line x1="40" y1="160" x2="70" y2="160" stroke="FILL"/><line x1="330" y1="160" x2="360" y2="160" stroke="FILL"/>'
    '<line x1="75" y1="60" x2="97" y2="82" stroke="FILL"/><line x1="325" y1="60" x2="303" y2="82" stroke="FILL"/>')

for name, body in designs.items():
    open(os.path.join(out, f"deco-{name}.svg"), "w").write(svg(body, O, O))
    open(os.path.join(out, f"deco-{name}-dark.svg"), "w").write(svg(body, D, D))
print(sorted(designs))
