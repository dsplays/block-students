import os as q1z
import sys as p8k

r3d = "/etc/hosts"
m7y = "/etc/hosts.backup"

a9x = [
    "roblox.com","www.roblox.com","minecraft.net","education.minecraft.net",
    "epicgames.com","innersloth.com","steampowered.com","playvalorant.com",
    "leagueoflegends.com","riotgames.com","store.steampowered.com",
    "ea.com","origin.com","callofduty.com","battle.net","rockstargames.com",
    "socialclub.rockstargames.com","geoguessr.com","agar.io","slither.io",
    "krunker.io","shellshock.io","coolmathgames.com","abcya.com","sporcle.com",
    "gimkit.com","kahoot.com","quizlet.com","quizizz.com","blooket.com",
    "poptropica.com","nealfun.org","freerice.com","beanbeanbean.com",
    "cityguesser.com","diep.io","paper-io.com","hole-io.com","surviv.io",
    "zombsroyale.io","itch.io","newgrounds.com"
]

h2s = [
    "block drop out quick on en0 to 128.116.0.0/16",
    "block drop out quick on en0 to 162.254.192.0/18",
    "block drop out quick on en0 to 69.174.160.0/20",
    "block drop out quick on en0 to 34.120.0.0/16",
    "block drop out quick on en0 to 24.105.30.0/23"
]

def v0l():
    q1z.system("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder")

def f3g():
    if not q1z.path.exists(m7y):
        q1z.system(f"sudo cp {r3d} {m7y}")
    with open("t1p", "w") as j0n:
        with open(r3d, "r") as g6q:
            for k9u in g6q:
                if not any(x5c in k9u for x5c in a9x):
                    j0n.write(k9u)
        j0n.write("\n")
        for x5c in a9x:
            j0n.write(f"127.0.0.1 {x5c}\n")
    q1z.system(f"sudo cp t1p {r3d}")
    q1z.remove("t1p")
    v0l()

def u8m():
    if not q1z.path.exists(m7y):
        return
    q1z.system(f"sudo cp {m7y} {r3d}")
    v0l()

def w4n():
    d2f = "/etc/pf.conf"
    y7k = "/etc/pf.conf.backup"
    if not q1z.path.exists(y7k):
        q1z.system(f"sudo cp {d2f} {y7k}")
    with open("o3b", "w") as j0n:
        with open(d2f, "r") as g6q:
            j0n.write(g6q.read())
        j0n.write("\n")
        for n6p in h2s:
            j0n.write(n6p + "\n")
    q1z.system("sudo cp o3b /etc/pf.conf")
    q1z.remove("o3b")
    q1z.system("sudo pfctl -f /etc/pf.conf; sudo pfctl -e")

def k5r():
    d2f = "/etc/pf.conf"
    y7k = "/etc/pf.conf.backup"
    if not q1z.path.exists(y7k):
        return
    q1z.system(f"sudo cp {y7k} {d2f}")
    q1z.system("sudo pfctl -f /etc/pf.conf")

def n2d():
    f3g()
    w4n()

def l8x():
    u8m()
    k5r()

if __name__ == "__main__":
    if len(p8k.argv) != 2 or p8k.argv[1] not in ["block", "unblock"]:
        p8k.exit(1)
    if p8k.argv[1] == "block":
        n2d()
    else:
        l8x()
