from redbot.core import commands
import discord
import requests
import json
from requests.structures import CaseInsensitiveDict
import random
from datetime import datetime


class Nasa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def nasa(self, ctx):
        """NASA API"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @nasa.command()
    async def apod(self, ctx):
        """NASA Astronomy Picture of the Day"""
        url = "https://api.nasa.gov/planetary/apod?api_key=DKMfp5STY5db4AacbeDlxcFAXjvwatSZvocdVpgT"
        response = requests.get(url)
        data = response.json()
        media = data["media_type"]
        if media == "video":
            embed = discord.Embed(title=data["title"], url=data["url"])
            embed.set_footer(text=f"{data['explanation']}")
            await ctx.send(embed=embed)
            
        else:
            embed = discord.Embed(title=data["title"], url=data["hdurl"], color=0x00ff00)
            embed.set_image(url=data["url"])
            embed.set_footer(text=f"{data['explanation']}")
            await ctx.send(embed=embed)
        
        

    @commands.group()
    async def epic(self, ctx):
        """NASA Earth Polychromatic Imagery Camera photos"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @epic.command()
    async def date(self, ctx, date: str):
        """Get a specific dated EPIC image using the date format YYYY-MM-DD (e.g. 2020-01-01)"""
        ## make sure request is in the correct format
        if len(date) != 10:
            await ctx.send("Please enter a date in the correct format YYYY-MM-DD")
            return
        ## make sure date is not before 2015-06-13
        if date < "2015-06-13":
            await ctx.send("Please enter a date after 2015-06-13")
            return
        url = "https://api.nasa.gov/EPIC/api/natural/date/" + date + "?api_key=DKMfp5STY5db4AacbeDlxcFAXjvwatSZvocdVpgT"
        response = requests.get(url)
        data = response.json()
        ## if data is empty, return error message
        if data == []:
            await ctx.send("No imagery data for that date")
        else:
            ##get random image from list using integers
            chung = data[0]
            random_image = chung.get("image")
            ## get image url
            ## reformat date string to match NASA API for date format
            date = date.replace("-", "/")  
            url = "https://api.nasa.gov/EPIC/archive/natural/" + date + "/png/" + random_image + ".png" + "?api_key=DKMfp5STY5db4AacbeDlxcFAXjvwatSZvocdVpgT"
            embed = discord.Embed(title="Imagery of Earth from NASA's Deep Space Climate Observatory satellite", url=url, color=0x00ff00)
            embed.set_image(url=url)
            embed.set_footer(text="Image courtesy of NASA")
            await ctx.send(embed=embed)

        
    @commands.group()
    async def mars(self, ctx):
        """NASA Mars Rover Photos from the rovers Curiosity, Opportunity, and Spirit"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @mars.command()
    async def curiosity(self, ctx):
        """NASA Mars Rover Photos from Curiosity"""
        ## randomize sol in api reuqest
        sol = random.randint(0, 1000)
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key=DKMfp5STY5db4AacbeDlxcFAXjvwatSZvocdVpgT"
        response = requests.get(url)
        data = response.json()
        photos = data["photos"]
        photo = random.choice(photos)
        embed = discord.Embed(title=photo["camera"]["full_name"], url=photo["img_src"], color=0x00ff00)
        embed.set_image(url=photo["img_src"])
        embed.set_footer(text=f"{photo['earth_date']}")
        await ctx.send(embed=embed)

    @mars.command()
    async def opportunity(self, ctx):
        """NASA Mars Rover Photos from Opportunity"""
        ## randomize sol in api reuqest
        sol = random.randint(0, 1000)
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol={sol}&api_key=DKMfp5STY5db4AacbeDlxcFAXjvwatSZvocdVpgT"
        response = requests.get(url)
        data = response.json()
        photos = data["photos"]
        photo = random.choice(photos)
        embed = discord.Embed(title=photo["camera"]["full_name"], url=photo["img_src"], color=0x00ff00)
        embed.set_image(url=photo["img_src"])
        embed.set_footer(text=f"{photo['earth_date']}")
        await ctx.send(embed=embed)

    @mars.command()
    async def spirit(self, ctx):
        """NASA Mars Rover Photos from Spirit"""
        ## randomize sol in api reuqest
        sol = random.randint(0, 1000)
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol={sol}&api_key=DKMfp5STY5db4AacbeDlxcFAXjvwatSZvocdVpgT"
        response = requests.get(url)
        data = response.json()
        photos = data["photos"]
        photo = random.choice(photos)
        embed = discord.Embed(title=photo["camera"]["full_name"], url=photo["img_src"], color=0x00ff00)
        embed.set_image(url=photo["img_src"])
        embed.set_footer(text=f"{photo['earth_date']}")
        await ctx.send(embed=embed)
