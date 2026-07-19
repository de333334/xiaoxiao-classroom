# -*- coding: utf-8 -*-
"""创建笔记并加入 ima 知识库 imao"""
import subprocess, json, os, sys

NODE = r"C:\Users\90630\.workbuddy\binaries\node\versions\22.22.2\node.exe"
CJS  = r"C:\Users\90630\.workbuddy\skills\ima-skills__skillhub\ima_api.cjs"
KB_ID = "pm8-1404_EPGkcfBKDri-wPiUpjUHUjqokpiC7NvFo8="
MD = os.path.join(os.path.dirname(__file__), "据理力争_参考答案_imao.md")
TITLE = "据理力争小课堂 · 第8课费曼参考答案（被拒绝后如何再争取·听缓换据求再）"

def call(apipath, body):
    p = subprocess.run([NODE, CJS, apipath, json.dumps(body, ensure_ascii=False)],
                       capture_output=True, text=True, encoding="utf-8")
    if p.returncode != 0:
        print("ERR stderr:", p.stderr[:500]); sys.exit(1)
    return json.loads(p.stdout)

content = open(MD, encoding="utf-8").read()
# 1) 新建笔记
r1 = call("openapi/note/v1/import_doc", {"content_format": 1, "content": content})
print("import_doc:", r1.get("code"), r1.get("msg"))
if r1.get("code") != 0:
    sys.exit(1)
note_id = r1["data"]["note_id"]
print("note_id:", note_id)

# 2) 加入知识库 imao
r2 = call("openapi/wiki/v1/add_knowledge", {
    "media_type": 11,
    "note_info": {"content_id": note_id},
    "title": TITLE,
    "knowledge_base_id": KB_ID,
})
print("add_knowledge:", r2.get("code"), r2.get("msg"))
print(json.dumps(r2.get("data", {}), ensure_ascii=False)[:400])
