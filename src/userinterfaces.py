import discord
import datahandling, helper

class PagesInterface(discord.ui.View):
    """
    Interface used for implementing UIs that have multiple pages.
    """
    pages = [] # List that contains information for each of the pages

    def __init__(self, *, timeout = 180, index = 0):
        super().__init__(timeout = timeout)
        self.index = index
    
    def get_page_embed(self, index):
        """
        Returns discord embed given a page index
        """
        pass

    @discord.ui.button(label = "<-", style = discord.ButtonStyle.blurple)
    async def left_button(self, ctx: discord.Interaction, button: discord.ui.button):
        """
        Increases the index of the page being viewed and edits the current message with an embed of the current page
        """
        pass

    @discord.ui.button(label = "->", style = discord.ButtonStyle.blurple)
    async def right_button(self, ctx: discord.Interaction, button: discord.ui.button):
        """
        Decreases the index of the page being viewed and edits the current message with an embed of the current page
        """
        pass


class HelpMenu(PagesInterface):
    pages = [
        {"name": "Fun Commands", "value": "- copypasta\n- fumo\n- echo"},
        {"name": "Utility Commands", "value": "- server-enable\n- server-disable\n- channel-enable\n- channel-disable\n- help\n- ping"},
        {"name": "Auto Features", "value": "- all\n- sus\n- morbius\n- sad\n- trade\n- mom"}
    ]

    item_descriptions = {
        "copypasta": "Returns a copypasta from a list of copypastas added by the bot host.",
        "fumo": "Returns an image of a fumo (plush dolls of characters from the series \"Touhou\").",
        "echo": "Echos specified text from a user. This works similarly to echo in a command prompt.",
        "server-enable": "Enables an auto feature throughout the entire server. This does not affect features enabled in specific channels.",
        "server-disable": "Disables an auto features throughout the entire server. This will only work on features that have previously been enabled throughout the server and does not keep a feature from being enabled.",
        "channel-enable": "Enables an auto feature in the specific channel this command is used in.",
        "channel-disable": "Disables an auto feature in the specific channel this command is used in. This will only work on features that have previously been enabled throughout the server and does not keep a feature from being enabled.",
        "ping": "A classic among discord bots. Returns Pong! upon recieving the command and client latency.",
        "help": "Returns the very menu you're using! Can be used to browse commands, features, and read up on specific features the bot has to offer.",
        "all": "Every auto feature in one. This can be useful when attempting to enable or disable every automatic feature at once.",
        "sus": "When a message contains the string 'sus', responds with the original message with 'sus' bolded and italicized.",
        "morbius": "When a message contains the string 'morb', responds with a morbius quote.",
        "sad": "When a message contains the string 'sad', responds with a sad image of Spongebob.",
        "trade": "When a message contains the string 'trade', responds with 'Yeah, I trade :smile:'",
        "mom": "When a message ends with the word 'do', 'doing', 'done', etc… responds with the message 'Your Mom' with a 20% chance of saying 'Your Dad :sunglasses:'"
    }

    def __init__(self, *, timeout = 180, index = 0):
        super().__init__(timeout = timeout, index = index)

    def get_page_embed(self, index):
        """
        Returns an embed of a page given an index.
        """
        self.index = (index) % len(HelpMenu.pages)
        embed = discord.Embed(title = "Help Menu", description = f"Page {self.index + 1}/{len(HelpMenu.pages)}", color = 0xffab00)
        embed.add_field(name = HelpMenu.pages[self.index]["name"], value = HelpMenu.pages[self.index]["value"], inline=False)
        return embed

    @discord.ui.button(label="<-", style = discord.ButtonStyle.blurple)
    async def left_button(self, ctx: discord.Interaction, button: discord.ui.Button):
        self.index = (self.index - 1) % len(HelpMenu.pages)
        await ctx.response.edit_message(embed = self.get_page_embed(self.index), view = self)

    @discord.ui.button(label="->", style = discord.ButtonStyle.blurple)
    async def right_button(self, ctx: discord.Interaction, button: discord.ui.Button):
        self.index = (self.index + 1) % len(HelpMenu.pages)
        await ctx.response.edit_message(embed = self.get_page_embed(self.index), view = self)
        