# credits to the respective owner xD
# imported by @heyworld
import requests
import re
import random
import asyncio
import urllib
import os

from telethon.tl import functions
from userbot.utils import toni_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd

COLLECTION_STRING = [
    "epic-fantasy-wallpaper",
    "castle-in-the-sky-wallpaper",
    "fantasy-forest-wallpaper",
    "fantasy-wallpaper-1080p",
    "toothless-wallpaper-hd",
    "japanese-art-wallpaper",
    "star-wars-landscape-wallpaper",
    "4k-sci-fi-wallpaper",
    "minion-screensavers-wallpaper",
    "zootopia-hd-wallpaper",
    "gravity-falls-hd-wallpaper",
    "cool-cartoon-wallpaper",
    "disney-movie-wallpaper",
    "cute-pokemon-wallpapers",
    "4k-anime-wallpaper",
    "balance-druid-wallpaper",
    "harry-potter-wallpaper",
    "funny-meme-wallpaper",
    "minimalist-hd-wallpaper",
    "cute-animal-wallpaper-backgrounds",
    "3840-x-1080-wallpaper",
    "wallpaper-outer-space",
    "best-wallpapers-in-the-world",
    "funny-desktop-backgrounds",
    "funny-cats-wallpapers",
    "cool-cat-wallpaper",
    "doge-wallpaper-hd",
    "ice-cream-cone-wallpaper",
    "food-wallpaper-background",
    "snowy-christmas-scenes-wallpaper",
    "life-quotes-wallpaper"
]


async def animepp():

    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r'/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)

    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf", "f.ttf")
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@toni_cmd(pattern="pprandom(?: |$)(.*)")
async def main(event):
    await event.edit("`Sedang Mengubah Photo Profile Anda...`")

    while True:
        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(3600)  # Edit this to your required needs

CMD_HELP.update({
    "randompp": f"\n\n✨𝘾𝙈𝘿✨: `{cmd}pprandom`"
    "\n↳ : Mengubah Photo Profile Anda Secara Random."})
