import json

with open("prueba3.json", "r", encoding="utf-8") as f:
    cookies = json.load(f)

cookie_string = "; ".join(
    f"{c['name']}={c['value']}"
    for c in cookies
    if "name" in c and "value" in c
)

with open("fbchat_v2.json", "w", encoding="utf-8") as f:
    json.dump(
        {"cookies": cookie_string},
        f,
        ensure_ascii=False,
        indent=2
    )

print("✅ Cookies convertidas a fbchat_v2.json")
print("Cantidad de cookies:", len(cookies))
