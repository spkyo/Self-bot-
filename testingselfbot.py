import requests
import random
from telethon import TelegramClient, events, functions
import logging
import asyncio
from asyncio import sleep
from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
import random
import re
from collections import defaultdict

# Replace with your API credentials
api_id = 29451852  # Your API ID
api_hash = 'd61e68206f2b18610f6d75d311c4ecfc'  # Your API Hash

# Your Telegram User ID (replace with your own user ID)
owner_id = 7672348593  # Your Owner ID
media_chat_id = 'bostpluger'
media_message_id = 6

# Alpha Vantage API key (replace with your own API key)
alpha_vantage_api_key = 'V4O4APVY9KTCR740'  # Your Alpha Vantage API key
GENIUS_API_KEY = 'tRp8cpZov87C9sIyoQy66wHXqIZaAvIi_YJS1gmSSfXJXlEM6x0RtB_2_5O1LSND'  # Replace with your Genius API key

client = TelegramClient('selfmybot', api_id, api_hash)

# Global sets to track muted users, banned users, and locked groups
muted_users = set()
banned_users = set()
locked_groups = set()
can_speak = set()
welcome_users = {}

def is_owner(event):
    """Check if the command is sent by the owner."""
    return event.sender_id == owner_id
    
@client.on(events.NewMessage(pattern=r'\.mute'))
async def mute_handler(event):
    """Mute the current user in DM (Owner only)."""
    if not await is_owner(event):
        return  

    if event.is_private:
        muted_users.add(event.chat_id)

        # Final 100% progress and send the result
        await event.edit(f"🔇 This Chat Has been Muted Successfully.")
        
@client.on(events.NewMessage(pattern=r'\.unmute'))
async def unmute_handler(event):
    """Unmute the current user in DM (Owner only)."""
    if not await is_owner(event):  # Awaiting is_owner
        return  

    if event.is_private:
        # Remove the user from muted users list
        muted_users.discard(event.chat_id)

        # Final 100% progress and send the result
        await event.edit(f"🔊 The Chat Has Been Unmuted Again ♡")

@client.on(events.NewMessage())
async def mute_checker(event):
    """Automatically delete messages from muted users."""
    if event.chat_id in muted_users and event.is_private:
        if not await is_owner(event):  # Allow owner to send messages
            await event.delete()
            
@client.on(events.NewMessage(pattern=r'\.mid'))
async def upload_picture_handler(event):
    """Fetch a picture from a Telegram channel by message ID, add a caption, and send an edited message."""
    if not await is_owner(event):
        return

    try:
        # Extract the message ID from the command
        message_id = 2
        source_channel = "@bostpluger"

        # Fetch the message by ID
        message = await client.get_messages(source_channel, ids=message_id)
        if message and message.photo:
            # Download the photo
            photo = await client.download_media(message.photo)
            await event.edit("Getting The Bost's Telegram ID Info.")
            await asyncio.sleep(2)
            await event.delete()
            # Send the photo with a caption
            sent_message = await client.send_file(event.chat_id, photo, caption="========================\n**Name :** **[𝐁𝐨𝐬𝐭~ ]**(tg://openmessage?user_id=6066188248)\n**Username :** **@ogbost**\n**Bost's Tg ID :** `6066188248`\n**Joined Tg :** **27 Dec 2024**\n**Status :** **Single💍**\n========================")
            __import__('os').remove(photo)
        else:
            await event.edit("No photo found for the given message ID in the specified channel.")

    except Exception as e:
        await event.edit(f"An error occurred: {str(e)}")

@client.on(events.NewMessage(pattern=r'\.upi'))
async def upload_picture_handler(event):
    """Fetch a picture from a Telegram channel by message ID, add a caption, and send an edited message."""
    if not await is_owner(event):
        return

    try:
        # Extract the message ID from the command
        message_id = 5
        source_channel = "@"

        # Fetch the message by ID
        message = await client.get_messages(source_channel, ids=message_id)
        if message and message.photo:
            # Download the photo
            photo = await client.download_media(message.photo)
            await event.edit("**Getting The 𝐁𝐨𝐬𝐭's Upi ID**.")
            await asyncio.sleep(2)
            await event.delete()
            # Send the photo with a caption
            sent_message = await client.send_file(event.chat_id, photo, caption="💸**UPI ID :** `unknrohit@fam`")
            __import__('os').remove(photo)
        else:
            await event.edit("No photo found for the given message ID in the specified channel.")

    except Exception as e:
        await event.edit(f"An error occurred: {str(e)}")

@client.on(events.NewMessage(pattern=r'\.shop'))
async def shop_handler(event):
    """Display shop link."""
    if not is_owner(event):
        return  # Only the owner can use this command
    
    shop_link = "https://t.me/bostpluger"
    await event.edit(f"🛒 Shop Link: [Click Here]({shop_link})")
    
@client.on(events.NewMessage(pattern=r'\.selfbot'))
async def shop_handler(event):
    """Display shop link."""
    if not is_owner(event):
        return  # Only the owner can use this command
    
    shop_link = "https://t.me/m/2A8ZHnsEMzc9"
    await event.edit(f"🧑🏻‍💻 **I've bought this selfbot script by @ogbost / @spkyo**\n•360rs/week\n•1200rs/month\n•Script in just 5k inr\n•You can get some discount by tapping here ~ **[Discount]**({shop_link})")   
    
@client.on(events.NewMessage(pattern=r'\.ban'))
async def ban_handler(event):
    """Ban the current user in DM (Owner only)."""
    if not await is_owner(event):  # Await is_owner
        return  

    if event.is_private:
        # Ban the user
        banned_users.add(event.chat_id)
        await client(functions.contacts.BlockRequest(event.chat_id))

        # Final 100% loading and send result
        await event.edit(f"🚫 User banned: {event.chat_id}.\nThey have been blocked.\n😮‍💨 ")

@client.on(events.NewMessage(pattern=r'\.unban'))
async def unban_handler(event):
    """Unban the current user in DM (Owner only)."""
    if not await is_owner(event):  # Await is_owner
        return  

    if event.is_private:
 
        # Unban the user
        banned_users.discard(event.chat_id)
        await client(functions.contacts.UnblockRequest(event.chat_id))

        # Final 100% loading and send result
        await event.edit(f"✅ User unbanned: {event.chat_id}.\nThey can now contact you again.\n😉🥰")
    
# ========== Block Command ==========
@client.on(events.NewMessage(pattern=r'\.block (.+)'))
async def block_user_handler(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return
    
    # Extract the username from the command
    username = event.pattern_match.group(1).strip()

    try:
        # Resolve the username to get the user entity
        user_to_block = await client.get_entity(username)
        
        # Block the user
        await client(functions.contacts.BlockRequest(user_to_block.id))
        
        # Confirm the action
        await event.respond(f"🚫 Successfully blocked the user: {username}")
    except Exception as e:
        # Handle errors and inform the user
        await event.respond(f"❌ Failed to block {username}. Error: {str(e)}")
        
# ========== Unblock Command ==========
@client.on(events.NewMessage(pattern=r'\.unblock (.+)'))
async def unblock_user_handler(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return
    
    # Extract the username from the command
    username = event.pattern_match.group(1).strip()

    try:
        # Resolve the username to get the user entity
        user_to_unblock = await client.get_entity(username)
        
        # Unblock the user
        await client(functions.contacts.UnblockRequest(user_to_unblock.id))
        
        # Confirm the action
        await event.respond(f"✅ Successfully unblocked the user: {username}")
    except Exception as e:
        # Handle errors and inform the user
        await event.respond(f"❌ Failed to unblock {username}. Error: {str(e)}")    
user_email_requests = {}  

@client.on(events.NewMessage(pattern=r'\.reset (\S+)$'))
async def reset_command_handler(event):
    """Handle the `.reset <username/email>` command for owner only."""
    
    if event.sender_id != owner_id:
        return  # अगर Owner नहीं है तो कोई रिस्पॉन्स नहीं देगा
    
    username_or_email = event.pattern_match.group(1)

    # स्टार्टिंग मैसेज भेजो (बाद में इसे एडिट करेंगे)
    msg = await event.edit(f"🔄 Attempting to reset password for `{username_or_email}`... Wait a secs...")

    # Instagram Password Reset Function
    def send_password_reset(username):
        """Send a password reset request to Instagram."""
        url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'eng',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'csrftoken=vEG96oJnlEsyUWNS53bHLkVTMFYQKCBV; ig_did=5D80D38A-797B-482D-A407-4B51217E09E7; ig_nrcb=1; mid=ZEqtPgALAAE-IVt6zG-ZazKzI4qN; datr=jrJKZGOaV4gHwa-Znj2QCVyB',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/password/reset/?next=%2Faccounts%2Flogout%2F',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-csrftoken': 'vEG96oJnlEsyUWNS53bHLkVTMFYQKCBV',
            'x-ig-app-id': '936619743392459',
            'x-instagram-ajax': '1007389883',
        }
        data = {"user_email": username}
        
        try:
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                return f"✅ Password reset link has been successfully sent to `{username}` BY **𝐁 𝐎 𝐒 𝐓~** | @ogbost"
            else:
                return None  # अगर कुछ गड़बड़ हुई तो None रिटर्न करेगा
        except:
            return None

    # Instagram API Call
    result = send_password_reset(username_or_email)

    # 2 सेकंड का वेट फिर उसी मैसेज को एडिट करो
    await asyncio.sleep(2)

    if result:
        await msg.edit(f"💞 Here's the result you are looking for...\n\n{result}")
    else:
        await msg.edit(f"🥲Oops!! I tried my best to reset password for `{username_or_email}`...\n\n❌ But Unable to reset password. The acc could be disband, deactivate or might be of other error mails.")
        
import requests
from telethon import events

# Dictionary for coin IDs (as per CoinGecko API)
COINS = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "bnb": "binancecoin",
    "sol": "solana",
    "xrp": "ripple",
    "ada": "cardano",
    "doge": "dogecoin",
    "shib": "shiba-inu",
    "matic": "matic-network",
    "ltc": "litecoin",
    "ton": "the-open-network"  # Added TON (The Open Network)
}

@client.on(events.NewMessage(pattern=r'\.(btc|eth|bnb|sol|xrp|ada|doge|shib|matic|ltc|ton)'))
async def crypto_price_handler(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return
    
    """Fetch the current price of the requested cryptocurrency."""
    try:
        coin_symbol = event.pattern_match.group(1)  # Get coin symbol from command
        coin_id = COINS.get(coin_symbol)  # Get CoinGecko ID
        
        if not coin_id:
            await event.edit("❌ Invalid coin symbol.")
            return

        # Fetch price from CoinGecko API
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()

        if coin_id in data:
            price = data[coin_id]['usd']
            formatted_price = f"${price:.2f}"
            await event.edit(f"💰 {coin_symbol.upper()}'s current price: **{formatted_price}**")
        else:
            await event.edit("❌ Could not fetch price.")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")                  
        
@client.on(events.NewMessage(pattern=r'\.stock'))
async def stock_handler(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return
    """Fetch the stock with the highest increase today for both World and India."""
    try:
        # Define a list of companies to check
        world_companies = ['GOOGL', 'AAPL', 'AMZN', 'TSLA', 'MSFT']  # Example: Google, Apple, Amazon, Tesla, Microsoft
        india_companies = ['TCS.BO', 'INFY.BO', 'RELIANCE.BO', 'HDFC.BO', 'ICICIBANK.BO']  # Example: TCS, Infosys, Reliance, etc.

        # Select a random company for World Market
        world_company = random.choice(world_companies)

        # Display initial loading message
        await event.edit("Fetching Stock Data... Wait a While...")

        # Simulating loading progress
        # Fetch stock data for World (random stock)
        url_world = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={world_company}&interval=5min&apikey={alpha_vantage_api_key}'
        response_world = requests.get(url_world)
        data_world = response_world.json()

        world_stock_details = ""
        if 'Time Series (5min)' in data_world:
            time_series = data_world['Time Series (5min)']
            highest_increase = 0
            highest_increase_stock = None

            for timestamp, stats in time_series.items():
                open_price = float(stats['1. open'])
                close_price = float(stats['4. close'])
                price_change = close_price - open_price

                if price_change > highest_increase:
                    highest_increase = price_change
                    highest_increase_stock = {
                        'symbol': world_company,
                        'open': open_price,
                        'close': close_price,
                        'change': price_change,
                        'time': timestamp
                    }

            if highest_increase_stock:
                world_stock_details = (
                    f"📈** Company** - {world_company}:\n"
                    f"**Symbol**: {highest_increase_stock['symbol']}\n"
                    f"**Open Price**: ${highest_increase_stock['open']:.2f}\n"
                    f"**Close Price**: ${highest_increase_stock['close']:.2f}\n"
                    f"**Price Change**: ${highest_increase_stock['change']:.2f}\n"
                    f"**Time of Change**: {highest_increase_stock['time']}\n"
                )
            else:
                world_stock_details = "❌ Could Not Fetch World Stock Data."
                
             # Final output after loading completes
        final_msg = f"🌎**World Stock Details !!**\n\n{world_stock_details}"
        await event.edit(final_msg)
        
    except Exception as e:
        await event.edit(f"Error: {str(e)}")

# Currency conversion function using a public API
def convert_usd(usd_amount):
    try:
        # Use a currency conversion API (you can use your own API key or another service)
        url = f"https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()

        if 'rates' in data:
            inr_rate = data.get('rates',{}).get('INR','Broked')  # Get INR conversion rate
            pkr_rate = data.get('rates',{}).get('PKR','Broked')  # Get PKR conversion rate
            eur_rate = data.get('rates',{}).get('EUR','Broked')  # Get EUR conversion rate
            if inr_rate == 'Broked' or pkr_rate == 'Broked' or eur_rate == 'Broked':
                return None
            inr_amount = usd_amount * inr_rate  # Convert USD to INR
            pkr_amount = usd_amount * pkr_rate  # Convert USD to PKR
            eur_amount = usd_amount * eur_rate  # Convert USD to EUR
            return inr_amount, pkr_amount, eur_amount
        else:
            return None
    except Exception as e:
        print(f"Error fetching conversion rate: {str(e)}")
        return None

# ========== Usd Converter ==========
@client.on(events.NewMessage(pattern=r'\.pusd (.+)'))
async def price_of_usd(event):
    """To get price of USD in INR, PKR, EUR (Owner only)."""
    if not await is_owner(event):
        return  # Only the owner can use the calculator
    try:
        if not event.pattern_match.group(1):
            await event.edit("❌ Give A Specefic Amount To Convert")
            return
        
        try:
            amount = int(event.pattern_match.group(1))  # Amount of USD To Convert
        except:
            await event.edit("❌ Give A Specefic Amount To Convert")
            return
        await event.edit("Loading 🚀 Wait a While Till I Convert Usd Rates.")
        await asyncio.sleep(1)
        rates = convert_usd(usd_amount=amount)
        if rates:
            price_inr, price_pkr, price_eur = rates
            result = "**Rates Of USD**\n"
            result += f"💸 {amount} USD : {price_inr} INR\n"
            result += f"💸 {amount} USD : {price_pkr} PKR\n"
            result += f"💸 {amount} USD : {price_eur} EUR)"

            await event.edit(result)
    except Exception as e:
        await event.edit(f"❌ Error : {e}")

# ========== Calculator ==========
@client.on(events.NewMessage(pattern=r'^([\d+\-*/().]+)=$'))
async def calculator_handler(event):
    """Evaluate arithmetic expressions and return the result (Owner only)."""
    if not await is_owner(event):
        return  # Only the owner can use the calculator

    expression = event.raw_text.strip()
    try:
        # Evaluate the expression safely
        result = eval(expression[:-1])  # Remove the trailing '=' symbol
        await event.edit(f"{expression[:-1]} = {result}")
    except Exception as e:
        await event.edit(f"Error: Invalid expression `{expression}`")
        
# List of dirty or playful pickup lines
pickup_lines = []
try:
    lines=requests.get('https://raw.githubusercontent.com/RAJXFR/SelfBot/refs/heads/main/pickup').text.splitlines()
    for line in lines:
        pickup_lines.append(line)
except:
    pickup_lines=requests.get('https://raw.githubusercontent.com/RAJXFR/SelfBot/refs/heads/main/pickup').text.splitlines()

# List of 10 different cute emojis to rotate through during loading
loading_emojis = ["💕", "💖", "💘", "💝", "💞", "💗", "💓", "💌", "💟", "❤️"]

@client.on(events.NewMessage(pattern=r'\.pline'))
async def pickup_line_handler(event):
    """Transform a reply into a random pickup line (Owner only)."""
    if not await is_owner(event):
        return  # Only the owner can use this command
    
    if event.is_reply:
        # Show the loading message with the first emoji
        loading_message = await event.edit(f"Hey Cutie🥰 Wait a While for My Pickup-Line...")

        # Simulate loading from 10% to 100% with changing emojis        
        # Choose a random pickup line from the list
        pickup_line = random.choice(pickup_lines)
        
        # Edit the replied message with the pickup line
        await loading_message.edit(pickup_line)
    else:
        await event.edit("❌ Bruhh!! Reply to a Message to Transform it Into a Pickup Line.")
        
# List of dirty lines
pickup_lines = [
    "Are You a Campfire? Because You are Hot and I Want More.",
    "Are You French? Because My Eiffel is for You.",
    "You Look Cold, Want To Use Me As a Blanlet?",
    "Dinner First? or Should We Go Straight to Dessert",
    "You Must Get a lot of Pain, Because I'm Fuckin Worst in Bed.",
    "Can I Borrow a Kiss? I Promiss I'll Give it Back!!",
    "Does Your Name Start With C? Because I Can 'C' us Getting Together Tonight !!",
    "Wanna Help Me Get on Santa's Naughty Lost This Year.??",
    "It's Cold Today Must wear Some Extra Clothes otherwise My Eyes Will Undress You Soon",
    "Do You Want To Relief from Your Period Pain for 9 Month",
]

# List of 10 different cute emojis to rotate through during loading
loading_emojis = ["💕", "💖", "💘", "💝", "💞", "💗", "💓", "💌", "💟", "🙈"]

@client.on(events.NewMessage(pattern=r'\.dline'))
async def pickup_line_handler(event):
    """Transform a reply into a random pickup line (Owner only)."""
    if not await is_owner(event):
        return  # Only the owner can use this command
    
    if event.is_reply:
        # Show the loading message with the first emoji
        loading_message = await event.edit(f"Hey My Bitch🤤 Wait and See How My Lines Fuck you💀...")

        # Simulate loading from 10% to 100% with changing emojis       
        # Choose a random pickup line from the list
        pickup_line = random.choice(pickup_lines)
        
        # Edit the replied message with the pickup line
        await loading_message.edit(pickup_line)
    else:
        await event.edit("❌ Reply To A Message To Use This Command")
    
# ========== Group Lock/Unlock Commands ==========
@client.on(events.NewMessage(pattern=r'\.quiet'))
async def lock_handler(event):
    if not await is_owner(event):
        return  # Only the owner can use this command
    if event.is_group:
        locked_groups.add(event.chat_id)
        await event.edit("🔒 **Shhhhh The Group Chat has been Quieted.")
    else:
        await event.edit("❌ This command works only in groups.")

@client.on(events.NewMessage(pattern=r'\.relief'))
async def unlock_handler(event):
    if not await is_owner(event):
        return
    if event.is_group:
        if event.chat_id in locked_groups:
            locked_groups.remove(event.chat_id)
            await event.edit("🔓 **Ufffffff Let The Group Chat Be Relieved.")
        else:
            await event.edit("❌ The group is not locked.")
    else:
        await event.edit("❌ This command works only in groups.")

@client.on(events.NewMessage(pattern=r'^\.okie(?: (.+))?'))
async def allow_speak(event):
    try:
        if event.pattern_match.group(1):
            # Get username from the command
            username = event.pattern_match.group(1).strip()
            user_full = await client(GetFullUserRequest(username))
            user_info = user_full.users[0] if hasattr(user_full, 'users') else user_full
            if user_info.id not in can_speak:
                can_speak.add(user_info.id)
                await event.edit(f"✅ User @{username} is now allowed to speak when the group is quieted.")
            else:
                await event.edit(f"ℹ️ User @{username} is already in the can-speak list.")
        elif event.is_reply:
            # Get user info from the replied message
            reply = await event.get_reply_message()
            if reply.sender_id not in can_speak:
                can_speak.add(reply.sender_id)
                await event.edit(f"✅ User {reply.sender_id} is now allowed to speak when the group is quieted.")
            else:
                await event.edit(f"ℹ️ User {reply.sender_id} is already in the can-speak list.")
        else:
            await event.edit("❌ Please reply to a user or provide a username.")
    except Exception as e:
        await event.edit(f"❌ Error: {e}")

@client.on(events.NewMessage(pattern=r'^\.naah(?: (.+))?'))
async def disallow_speak(event):
    try:
        if event.pattern_match.group(1):
            # Get username from the command
            username = event.pattern_match.group(1).strip()
            user_full = await client(GetFullUserRequest(username))
            user_info = user_full.users[0] if hasattr(user_full, 'users') else user_full
            if user_info.id in can_speak:
                can_speak.remove(user_info.id)
                await event.edit(f"✅ User @{username} can no longer speak when the group is quieted.")
            else:
                await event.edit(f"ℹ️ User @{username} was not in the can-speak list.")
        elif event.is_reply:
            # Get user info from the replied message
            reply = await event.get_reply_message()
            if reply.sender_id in can_speak:
                can_speak.remove(reply.sender_id)
                await event.edit(f"✅ User {reply.sender_id} can no longer speak when the group is quieted.")
            else:
                await event.edit(f"ℹ️ User {reply.sender_id} was not in the can-speak list.")
        else:
            await event.edit("❌ Please reply to a user or provide a username.")
    except Exception as e:
        await event.edit(f"❌ Error: {e}")

@client.on(events.NewMessage(pattern=r'^\.ufff'))
async def show_can_speak(event):
    try:
        if can_speak:
            user_list = "\n".join([f"- `{user_id}`" for user_id in can_speak])
            await event.edit(f"**Users Allowed to Speak While Group is Quieted:**\n{user_list}")
        else:
            await event.edit("ℹ️ No users are currently allowed to speak while the group is quieted.")
    except Exception as l:
        await event.edit(f"❌ Error: {l}")


@client.on(events.NewMessage())
async def group_message_handler(event):
    if event.chat_id in locked_groups:
        if not (await is_owner(event) or event.sender_id in can_speak):
            await event.delete()

@client.on(events.NewMessage(pattern=r'\.Ogbost'))
async def intro_handler(event):
    """Send the owner's introduction with typing effect when .me command is called."""
    if not await is_owner(event):
        return  # Only the owner can use this command

   # Define the intro message as a list of words
    intro_message = """🗿 [𝗠𝘆 𝗜𝗻𝘁𝗿𝗼](tg://openmessage?user_id=6423034922)
This is  𝐁 𝐨 𝐬 𝐓~ Using Self-Bot of [OG ⚚](https://t.me/Sirr_RJ)...
• From RajsthaN, Age 17, 6.1 Feet Tall
• Just Doing Nothing cuz I'm Talentless
• Full Time Bakchod
Tap Here and Catch Me: [𝐓ᴇʟᴇ𝐆ʀᴀᴍ](https://t.me/ogbost)
""".strip().split()

    try:
        # Start with a placeholder message
        message = await event.edit("Typing...")

        # Add words one by one with a delay
        current_text = ""
        for word in intro_message:
            current_text += f"{word} "
            await message.edit(current_text.strip())  # Strip to avoid trailing spaces
            await sleep(0.2)  # Delay between each word (adjustable)

    except Exception as e:
        print(f"Error: {e}")
        
@client.on(events.NewMessage(pattern=r'\.gana (.+)'))
async def fetch_song_handler(event):
    """Fetch song lyrics using Genius API and provide link to the lyrics page."""
    if not await is_owner(event):
        return  # Only owner can use this command

    song_name = event.pattern_match.group(1)  # Extract the song name
    message = await event.edit(f"🔍 Searching lyrics for **{song_name}**...")

    try:
        # Genius API search endpoint
        search_url = "https://api.genius.com/search"
        headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}  # Add your Genius API key
        params = {"q": song_name}
        search_response = requests.get(search_url, headers=headers, params=params).json()

        # Check if response is valid
        hits = search_response.get('response', {}).get('hits', [])
        if not hits:
            await message.edit(f"❌ No results found for **{song_name}**.")
            return

        # Fetch song URL and ID from Genius
        song_url = hits[0]['result']['url']
        song_title = hits[0]['result']['full_title']

        await message.edit(f"🎶 Found Song: **{song_title}**\n\n👉 Lyrics: [Click Here]({song_url})")

    except Exception as e:
        # Handle unexpected errors
        await message.edit(f"❌ Could not fetch lyrics for **{song_name}**.\nError: {str(e)}")

@client.on(events.NewMessage(pattern=r"\.mm"))
async def create_group_handler(event):
    """Create a private group with a profile photo and send the joinable link to the owner."""
    if not await is_owner(event):
        return  # No response if user is not the owner

    try:
        # Create a new private group (supergroup)
        result = await client(functions.channels.CreateChannelRequest(
            title="Middleman X",
            about="This is a private group created by the Self-Bot of @Ogbost.",
            megagroup=True
        ))

        group = result.chats[0]

        # Fetch the photo from the given public channel link
        channel_username = "bostpluger"
        message_id = 6

        msg = await client.get_messages(channel_username, ids=message_id)

        if not msg or not msg.media or not msg.media.photo:
            await event.edit("❌ Could not find a valid photo in the provided channel or message ID.")
            return

        # Download and set photo as group's profile picture
        photo_file = await msg.download_media()
        await client(functions.channels.EditPhotoRequest(
            channel=group.id,
            photo=await client.upload_file(photo_file)
        ))

        # Add the bot to the group
        bot_username = "MiddlemanX_Bot"
        bot = await client.get_entity(bot_username)
        await client(functions.channels.InviteToChannelRequest(
            channel=group.id,
            users=[bot]
        ))

        # Generate permanent invite link
        invite = await client(functions.messages.ExportChatInviteRequest(
            peer=group.id
        ))

        await event.edit(f"✅ Private Group Created!\nHere is your Joinable Link: {invite.link}\n"
                         f"**This Private Group Created by Ogbost**")

    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        await event.edit(f"❌ An error occurred: {str(e)}")


@client.on(events.NewMessage(pattern=r"\.close (\d+[smh])"))
async def auto_close_group_handler(event):
    """Schedule the group to delete itself after the specified time."""
    if not await is_owner(event):
        return

    try:
        # Parse time from the command
        duration_str = event.pattern_match.group(1)
        time_in_seconds = parse_duration(duration_str)

        # Edit the original `.close` message with notification
        await event.edit(f"✅ This group will be deleted in {duration_str}. Thank You\nDownload anything you need •_•")

        # Wait for the specified duration
        await asyncio.sleep(time_in_seconds)

        # Delete the group
        group_id = event.chat_id
        await client(functions.channels.DeleteChannelRequest(
            channel=group_id
        ))

    except Exception as e:
        logging.error("An error occurred during auto-delete", exc_info=True)
        await event.edit(f"❌ An error occurred: {str(e)}")


async def is_owner(event):
    """Check if the event sender is the owner."""
    sender = await event.get_sender()
    return sender.id == owner_id


def parse_duration(duration_str):
    """
    Convert duration string like '1h', '30m', '45s' into seconds.
    """
    match = re.match(r"(\d+)([smh])", duration_str)
    if not match:
        raise ValueError("Invalid duration format. Use 's', 'm', or 'h'.")
    
    value, unit = int(match.group(1)), match.group(2)
    if unit == "s":  # Seconds
        return value
    elif unit == "m":  # Minutes
        return value * 60
    elif unit == "h":  # Hours
        return value * 3600
    else:
        raise ValueError("Invalid time unit. Use 's', 'm', or 'h'.")
                    
@client.on(events.NewMessage(pattern=r'\.asleep'))
async def sleep_handler(event):
    """Add ~ asleep to your Telegram name."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    try:
        # Fetch the current user details
        user = await client.get_me()
        current_first_name = user.first_name

        # Check if ~ asleep is already in the name
        if "~ asleep" in current_first_name:
            await event.edit("❌ Your Name Already Indicates You are Asleep!")
            return

        # Update the profile with "~ Asleep" appended
        new_name = f"{current_first_name} ~ asleep"
        await client(functions.account.UpdateProfileRequest(first_name=new_name))
        await event.edit("😴 Status Updated: You are Now Asleep.")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")


@client.on(events.NewMessage(pattern=r'\.awake'))
async def wake_handler(event):
    """Remove ~ asleep from your Telegram name."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    try:
        # Fetch the current user details
        user = await client.get_me()
        current_first_name = user.first_name

        # Remove ~ asleep if it exists
        if "~ asleep" in current_first_name:
            new_name = current_first_name.replace(" ~ asleep", "")
            await client(functions.account.UpdateProfileRequest(first_name=new_name))
            await event.edit("🌞 Status Updated: You are Now Awake.")
        else:
            await event.edit("❌ Your Name Does Not Indicate You are Asleep!")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.busy'))
async def sleep_handler(event):
    """Add ~ Busy to your Telegram name."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    try:
        # Fetch the current user details
        user = await client.get_me()
        current_first_name = user.first_name

        # Check if ~ Busy is already in the name
        if "~ Busy" in current_first_name:
            await event.edit("❌ Your Name Already Indicates You Are Busy!")
            return

        # Update the profile with "~ Asleep" appended
        new_name = f"{current_first_name} ~ Busy"
        await client(functions.account.UpdateProfileRequest(first_name=new_name))
        await event.edit("👨🏻‍💻 Status Updated: You are Now Busy.")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")


@client.on(events.NewMessage(pattern=r'\.free'))
async def wake_handler(event):
    """Remove ~ Busy from your Telegram name."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    try:
        # Fetch the current user details
        user = await client.get_me()
        current_first_name = user.first_name

        # Remove ~ Busy if it exists
        if "~ Busy" in current_first_name:
            new_name = current_first_name.replace(" ~ Busy", "")
            await client(functions.account.UpdateProfileRequest(first_name=new_name))
            await event.edit("🥰 Status Updated: You are Now Free.")
        else:
            await event.edit("❌ Your name does not indicate you are busy!")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.count (\d+)'))
async def countdown_handler(event):
    """Countdown from a given number."""
    if not await is_owner(event):
        return  # केवल मालिक (Owner) ही इस कमांड का उपयोग कर सकता है

    # Number extract करना (जितने से काउंटडाउन शुरू करना है)
    try:
        countdown_start = int(event.pattern_match.group(1))
        if countdown_start <= 0:
            await event.edit("❌ कृपया एक पॉजिटिव नंबर दें!")
            return
    except ValueError:
        await event.edit("❌ Must Give a Correct Number Bruhh")
        return

    # Countdown शुरू
    try:
        for i in range(countdown_start, 0, -1):
            await event.edit(f"⏳ Time is Going: {i} Seconds Remaining...")
            await asyncio.sleep(1)  # हर सेकंड पर रुके

        # Countdown खत्म होने पर
        await event.edit("⏰ Time's Up! Countdown Finished.")
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")
        
@client.on(events.NewMessage(pattern=r'\.chud (\d+)?'))
async def dot_spam_handler(event):
    """Spam the mentioned number of unique messages mentioning the replied user's username."""
    if not await is_owner(event):
        return  # If the user is not the owner, do nothing (no response)

    # Check if the command is a reply
    if not event.is_reply:
        await event.reply("❌ Reply To a User To Use This Command!")
        return

    # Extract the number of messages from the command
    match = event.pattern_match.group(1)
    if match:
        num_messages = int(match)  # Convert the number to integer
    else:
        num_messages = 10  # Default to 10 messages if no number is given

    # Get the replied-to message and user info
    replied_message = await event.get_reply_message()
    user = await replied_message.get_sender()  # Fetch the sender's details

    if not user:
        await event.reply("❌ Unable to Fetch The User Details.")
        return

    # Check for username, if not available, fallback to user_id mention
    if user.username:
        mention = f"@{user.username}"  # Mention using username
    else:
        mention = f"[{user.id}](tg://user?id={user.id})"  # Fallback to user ID

    # List of 50 random unique messages
    random_messages = []
    try:
        Galis=requests.get('https://raw.githubusercontent.com/RAJXFR/SelfBot/refs/heads/main/gali').text.splitlines()
        for Gali in Galis:
            random_messages.append(Gali)
    except Exception as e:
        print(e)
    # Check if the number of messages requested is within the list range
    if num_messages > len(random_messages):
        await event.reply(f"❌ Only {len(random_messages)} unique messages are available!")
        return

    # Shuffle and pick the specified number of unique messages
    random.shuffle(random_messages)
    selected_messages = random_messages[:num_messages]

    # Send the messages
    for message in selected_messages:
        await event.respond(f"Sun {mention}, {message}")

# ========== Command to Delete Chat ==========
@client.on(events.NewMessage(pattern=r'\.d'))
async def delete_chat_handler(event):
    """Delete the chat permanently from both sides in private chats (Owner only)."""
    if not await is_owner(event):
        return  # Only the owner can use this command
    
    if event.is_private:
        try:
            await client(functions.messages.DeleteHistoryRequest(
                peer=event.chat_id,
                max_id=0,  # Deletes all messages in the chat
                revoke=True  # Ensures messages are deleted for both sides
            ))
            confirmation = await event.respond("✅ Chat history has been deleted permanently for both sides.")
            # Automatically delete the confirmation message after 5 seconds
            await asyncio.sleep(5)
            await confirmation.delete()
        except Exception as e:
            await event.respond(f"❌ Error occurred: {str(e)}")
    else:
        await event.respond("❌ This command only works in private chats.")

@client.on(events.NewMessage(pattern=r'\.purge (\d+)$'))
async def purge_handler(event):
    """Delete a specific number of messages in the chat."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    # Extract the number of messages to delete
    try:
        num_messages = int(event.pattern_match.group(1))
    except ValueError:
        await event.reply("❌ Provide a valid number of messages to purge.")
        return

    if num_messages < 1:
        await event.reply("❌ The number of messages to purge must be greater than 0.")
        return

    # Delete messages
    chat = await event.get_chat()
    deleted_count = 0
    try:
        async for message in client.iter_messages(chat.id, limit=num_messages + 1):  # +1 to include the command message
            try:
                await message.delete()
                deleted_count += 1
            except MessageDeleteForbiddenError:
                await event.reply("❌ Unable to delete some messages. Ensure you have sufficient permissions.")
                break

        await event.respond(f"✅ Successfully purged {deleted_count - 1} messages.")
    except ChatAdminRequiredError:
        await event.reply("❌ I need admin privileges to purge messages in this chat.")
    except Exception as e:
        await event.reply(f"❌ An error occurred: {str(e)}")

@client.on(events.NewMessage(pattern=r'^\.tinfo(?: (.+))?'))
async def user_info(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return
    try:
        # Check if the command includes a username or if it's a reply
        if event.pattern_match.group(1):
            # Get username from the command
            username = event.pattern_match.group(1).strip()
            user_full = await client(GetFullUserRequest(username))
        elif event.is_reply:
            # Get user info from the replied message
            reply = await event.get_reply_message()
            user_full = await client(GetFullUserRequest(reply.sender_id))
        else:
            await event.edit("❌ Reply to a user or provide a username.")
            return

        # Extract user details
        user_info = user_full.users[0] if hasattr(user_full, 'users') else user_full.user
        result = f"**User Info:**\n"
        result += f"👤 **Name:** `{user_info.first_name or 'N/A'} {user_info.last_name or ''}`\n"
        result += f"🌷 **Username:** @{user_info.username or 'N/A'}\n"
        result += f"🆔 **User ID:** `{user_info.id}`\n"
        result += f"🔗 **ID Link:** [Permanent Link](tg://openmessage?user_id={user_info.id})\n"
        result += f"📞 **Phone:** `{user_info.phone or 'N/A'}`\n"
        result += f"👥 **Is Bot:** {'Yes' if user_info.bot else 'No'}\n"
        result += f"🗓️ **Last Seen:** {user_info.status.__class__.__name__ if user_info.status else 'Hidden'}\n**[𝐅𝐭~ || मृत्यु ||]**(tg://openmessage?user_id=7436995277)"

        await event.edit(result)

    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")

def info(username):
    try:
        oo = f"-1::{username}"
        ee = __import__('base64').b64encode(oo.encode('utf-8')).decode('utf-8')
        headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }
        rr = requests.get(f'https://instanavigation.net/api/v1/stories/{ee}', headers=headers).json()

        return {
        'usr': rr['user_info']['username'],
        'nm': rr['user_info']['full_name'],
        'id': rr['user_info']['id'],
        'fw': rr['user_info']['followers'],
        'fg': rr['user_info']['following'],
        'ps': rr['user_info']['posts'],
        'prv': rr['user_info']['is_private'],
        'st': 'ok'
        }
    except Exception as e:
        print(e)
        return None

import requests
from telethon import events

# Define the reset handler function
def reset_handler_function(username):
    # Add logic for the reset action here
    return f"Reset action triggered for {username}"

# Define the function to get Instagram user info
def info(username):
    try:
        oo = f"-1::{username}"
        ee = __import__('base64').b64encode(oo.encode('utf-8')).decode('utf-8')
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }
        rr = requests.get(f'https://instanavigation.net/api/v1/stories/{ee}', headers=headers).json()
        
        return {
            'usr': rr['user_info']['username'],
            'nm': rr['user_info']['full_name'],
            'id': rr['user_info']['id'],
            'fw': rr['user_info']['followers'],
            'fg': rr['user_info']['following'],
            'ps': rr['user_info']['posts'],
            'prv': rr['user_info']['is_private'],
            'st': 'ok'
        }
    except Exception as e:
        print(f"Error in info function: {e}")
        return {'st': 'error'}

# Function to calculate the year based on the ID range
def date(hy):
    try:
        ranges = [
            (1278889, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2369359761, 2015),
            (4239516754, 2016),
            (6345108209, 2017),
            (10016232395, 2018),
            (27238602159, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023)
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2024
    except:
        pass

# Command handler for Instagram user info
@client.on(events.NewMessage(pattern=r'^\.insta(?: (.+))?'))
async def user_info(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return
    try:
        # Check if the command includes a username or if it's a reply
        if event.pattern_match.group(1):
            username = event.pattern_match.group(1).strip()
            user_full = info(username)
        else:
            await event.edit("❌ Provide a username.")
            return
        
        user_full = user_full if user_full else {}

        link = user_full.get('usr', None)
        link = link if link else user_full.get('usr', 'N/A')
        reset = reset_handler_function(user_full.get('usr', None)) if user_full.get('usr', None) else 'N/A'

        result = f"**Instagram User Info:**\n"
        result += f"👤 Name : {user_full.get('nm', 'N/A')}\n"
        result += f"🔗 Username : [@{user_full.get('usr', 'N/A')}]({link})\n"
        result += f"🆔 User ID : `{user_full.get('id', 'N/A')}`\n"
        result += f"📅 Age : {date(int(user_full.get('id', None))) if user_full.get('id') else 'N/A'}\n"
        result += f"👥 Followers : {user_full.get('fw', 'N/A')}\n"
        result += f"👥 Following : {user_full.get('fg', 'N/A')}\n"
        result += f"📮 Posts : {user_full.get('ps', 'N/A')}\n"
        result += f"🔒 Private : {user_full.get('prv', 'N/A')}\n**[𝐅𝐭~ || मृत्यु ||]**(tg://openmessage?user_id=7436995277)"

        await event.edit(result)
    
    except Exception as e:
        await event.edit(f"❌ Error: {str(e)}")
        
from deep_translator import GoogleTranslator

def translate_to_english(text,lang):
    """Translates the given text to English."""
    try:
        translated_text = GoogleTranslator(source='auto', target=lang).translate(text)
        return translated_text
    except Exception as e:
        return f"An error occurred during translation: {e}"

@client.on(events.NewMessage(pattern=r'\.trl'))
async def translate_message(event):
    """Translate replied messages into English. Owner-only command."""
    if not await is_owner(event):  # Ensure only the owner can use this command
        return

    # Ensure the command is used as a reply
    if event.is_reply:
        try:
            # Get the replied message
            reply = await event.get_reply_message()
            text_to_translate = reply.message

            if not text_to_translate:
                await event.reply("❌ The replied message does not contain any text.")
                return

            # Translate the text to English
            translated_text = translate_to_english(text_to_translate,lang='en')

            # Send the translated message
            await event.edit(f"**Translated to English:**\n`{translated_text}`")
        except Exception as e:
            await event.edit(f"❌ Error: {str(e)}")
    else:
        await event.edit("❌ Please reply to a message to translate it.")

@client.on(events.NewMessage(pattern=r'\.spam (.+) (\d+)$'))
async def spam_handler(event):
    if not await is_owner(event):  # Ensure only the owner can use the command
        return

    try:
        
        message = event.pattern_match.group(1).strip()
        count = int(event.pattern_match.group(2))

        
        if count < 1 or count > 100:  
            await event.reply("❌ Specify a valid number of repetitions (1-100).")
            return

        
        await event.reply(f"🔄 Spamming `{message}` {count} times...")

        
        for i in range(count):
            await event.respond(message)
            await asyncio.sleep(0.1) 

        
        await event.reply(f"✅ Finished spamming `{message}` {count} times!")

    except Exception as e:
        await event.reply(f"❌ An error occurred: {str(e)}")

from telethon import events
import logging

from telethon import events
import logging

@client.on(events.NewMessage(pattern=r"\.dm (.+)"))
async def dm_user_handler(event):
    """Send a DM to the mentioned user or replied user when '.dm <text>' is used."""
    if not await is_owner(event):
        return

    # Check if the owner has replied to a message or mentioned a user
    replied_user = event.reply_to_msg_id
    if replied_user:
        # If owner replied to someone, use that user's ID
        message = await event.get_reply_message()
        user = message.sender
    else:
        # If owner mentions a user, extract the username or ID
        mentioned_user = event.pattern_match.group(1)  # Get the text after .dm
        if mentioned_user:
            try:
                # Check if mentioned_user is a username or ID and resolve accordingly
                if mentioned_user.startswith('@'):
                    user = await client.get_entity(mentioned_user)  # Resolve by username
                else:
                    user = await client.get_entity(int(mentioned_user))  # Resolve by ID
            except Exception as e:
                logging.error(f"Error resolving user: {str(e)}")
                await event.edit(f"❌ Error: Could not resolve {mentioned_user}. Please check the user ID or username.")
                return
        else:
            await event.edit("❌ Mention a user or reply to a user's message.")
            return

    # Get the DM message text from the command
    dm_text = event.pattern_match.group(1)

    try:
        # Send the message to the user's DM
        await client.send_message(user, dm_text)
        await event.edit(f"✅ The message has been sent to @{user.username or f'User {user.id}'} in DM.\n **[𝐅𝐭~ || Og ||]**(tg://openmessage?user_id=6066188248)")
    except Exception as e:
        logging.error(f"Error sending DM: {str(e)}")
        await event.edit("❌ Error: Could not send the message to the user's DM.")                                       

@client.on(events.NewMessage(pattern=r'\.cspam (\d+)'))
async def cspam_handler(event):
    """
    Copy spam the replied message.
    Usage: Reply to any message and use `.cspam <number>` where <number> is the count.
    """
    if not await is_owner(event):
        return

    try:
        # Extract the number from the command
        count = int(event.pattern_match.group(1))

        # Check if the message is a reply
        if not event.is_reply:
            await event.reply("⚠️ Must reply to a message to use this command.")
            return

        # Fetch the replied message
        reply_message = await event.get_reply_message()

        # Prepare the message/media to spam
        if reply_message.text:
            content = reply_message.text  # Text message
        elif reply_message.photo or reply_message.video or reply_message.voice or reply_message.document:
            content = reply_message  # Media message
        else:
            await event.reply("⚠️ Unsupported message type for spamming.")
            return

        await event.edit(f"🔄 Spamming `{count}` times. Wait a While...")
        
        # Spam the message
        for _ in range(count):
            if isinstance(content, str):  # If it's a text message
                await client.send_message(event.chat_id, content)
            else:  # If it's media (photo, video, voice note, etc.)
                await client.send_file(event.chat_id, content)
            await asyncio.sleep(0.5)  # Add a slight delay to avoid being rate-limited

        await event.reply(f"✅ Spammed `{count}` times successfully!")

    except ValueError:
        await event.reply("⚠️ Invalid number. Provide a valid digit.")
    except Exception as e:
        await event.reply(f"❌ An error occurred: {str(e)}")

@client.on(events.NewMessage(pattern=r'\.kick'))
async def kick_handler(event):
    """
    Remove a user from the group.
    Usage: Reply to a user's message with `.kick` to remove them from the group.
    Works only if you are an admin in the group.
    """
    if not await is_owner(event):
        return

    try:
        # Ensure the command is used in a group chat
        if not event.is_group:
            await event.reply("⚠️ This command can only be used in groups.")
            return

        # Ensure the command is used as a reply
        if not event.is_reply:
            await event.reply("⚠️ Must reply to a user's message to kick them.")
            return

        # Fetch the replied user's details
        replied_message = await event.get_reply_message()
        user_id = replied_message.sender_id

        # Store the message that triggered the command
        trigger_message = event.message

        # Check if the bot is an admin in the group
        me = await client.get_me()
        admin_rights = await client(functions.channels.GetParticipantRequest(
            channel=event.chat_id,
            participant=me.id
        ))

        if not admin_rights.participant.admin_rights:
            await event.reply("❌ I am not an admin in this group, so I cannot remove users.")
            return

        # Remove the user from the group
        await client.kick_participant(event.chat_id, user_id)

        # Edit the original .kick message to notify about the kick
        await trigger_message.edit(f"✅ User [ID: {user_id}] has been removed from the group.")

    except Exception as e:
        await event.reply(f"❌ An error occurred: {str(e)}")

# Define the list of responses for the auto-reply
auto_reply_responses = [
    "Janta dukhi hai modi se, teri mummy ko uthne nahi dunga aaj apni godi se",
    "Lund loge lund¿?",
    "विराट कोहली के बल्ले का शॉट और तेरी मम्मी का पेटीकोट, दोनों एक Time पर ऊपर उठते ही हैं",
    "गोभी प्याज भिंडी आलू, क्या तेरी बहन को मैं पटालूं¿?",
    "तेरी मम्मी ने last time अपनी झाटे कब काटी थी...?🤗",
    "प्रशांत महासागर की गहराइयों में लेजाकर तेरी दीदी को चो*द दूंगा",
    "There's a word called WHORE, Your Mom Owns it",
    "1+1=3 (क्योंकि तेरी मम्मी को बिन condom के चो*द दिया था मैं)",
    "Teri mummy ko tajmahal ki नोक par bitha dunga",
    "Agar 1 se pehle 0 aata hai, to A se pehle cya aayega¿?",
    "Teri budhiya dadi mere bathroom me fisal gyi",
    "Teri mummy ko 73वीं hoor bana dunga rndike",
    "jannat me jaakr teri pardadi ko chod dunga",
    "Teri mummy ke muh pr apne lund se knock knock kr dunga",
    "Ek hota hai chutiya ek hota hai maha chutiya or teesra main hu jisne bina condom ke teri mummy chodne ki galti kr di",
    "Aadat se लचार hu, teri mummy ka purana भतार hu",
    "Kati patang tera kon sa rang... Jis rang ki teri behan ne panty pehni hogi wo wala rang",
    "Teri behan ki chut me चाकू 🔪 se fingering kar dunga abb",
    "चुप गरीबी रेखा में रेंगने वाले कीड़े🤫🥱",
    "muh band rakh napunsak ki awlaad",
    "Fruti ya pepsi, teri behan badi sexy",
    "Teri behan ka insta id milega cya😈😉¿?",
    "तू अपनी बहन को बोल न मुझे अपने जांघों के बीच दबा कर मार दे🙈",
    "Koi hota hai pagal, to koi banata hai khayali pulau, cya main teri didi ke boobs dabau?",
    "Sarkari school ke peeche lejakr teri didi ki salwar ka nada khol dunga",
    "Gali gali me rehta hai saand, teri mummy ko itna choda ki wo ban gyi Raand😁",
    "Teri maa 150 wali randi",
    "Jungle me naachta hai Morr, teri mummy ki chudayi dekhkar sb bolte hn once more once more",
    "Teri behan ki chut me kutte ka sperm",
    "Teri behan ki yaado me jee rha hu ab bss",
    "Teri mummy ki flipcart se order kar lunga",
    "Duniya paise laha rahi ghode pe, or teri mummy ghum fir kar aa jaati hai mere 🤭😈",
    "Teri mummy ko itna chodunga ki usko लकवा maar jayega",
    "Bura mat maniyo teri mummy ni chod sakta, apni wali ke liye loyal hu",
    "teri behan ki gand me top chala dunga",
    "Teri mummy ko momos khilakr chod dunga",
    "Move Theatre me teri behan ki panty me hath daal dunga",
    "kaise chudi teri maa¿?",
    "चुदले फेर🤗🤫",
    "Chudayi kar du aapni mummy ki??",
    "Teri behan ko geela kar diya maine",
    "Mere sexting se to tere ghar ki saari aurte khush hai",
    "Ronaldo ka football teri mummy ki gand ke chhed me ghusa dunga",
    "अंधेरे में rehne wala भूत और तेरी मम्मी की काली चूत, दोनों useless hai",
    "ये गरजने वाले बादल है ना ! शेर दहाड़ने wala घायल है ना !! और कहती है मेरे लंड पे मूतेगी, तेरी मम्मी भी कितनी पागल है ना ",
    "बच्चे रोते हैं मिठाई के लिए, और तेरी मम्मी के मुंह में पानी आता है मेरे लंड wale मलाई के लिए",
    "Teri behan ki chut me thanos ka glub",
    "Spiderman ki tarah diwar par latak kar teri mummy ki gand maar lunga",
    "Teri mummy ko superman wali laal chaddi pehna dunga",
    "Maine to sapne bhi teri behan ko chodne wale dekhe hn",
    "Shatap mere bete",
    "Aand bhaat khayega¿?",
    "teri mummy ko apna lwda-paaw khilata hu ruk",
    "Teri mummy ke 2 kaam~ pehla mere lund par baithkar mootna or dusra fir usi lund ko chusna",
    "Teri mummy ko bulu bulu kar du kya🥺🫣¿?",
    "tu apni behan ko meri godi me bitha de",
    "Teri maa chod di, teri behan pel daali, ab aayi teri nani ki baari",
    "teri mummy ki chut me Sidha lund se shot marunga to tera bhai hoga, Aada-Tedha shot maarunga to teri behan hogi, bata tujhe kyw chahiye",
    "Ter behan ko hentai dikha dunga",
    "Teri didi ke boobs chaba jaunga🫦",
    "Teri behan ki gori chut hai ya kaali¿?",
    "Teri mummy meri gulam",
    "Teri behan ki chut pe vimal thuk diya kisi ne¿?",
    "Abe tere or teri mummy ke jaiso ko lund par jhula du",
    "chup madarchod",
    "Jana lwde teri mummy ko chudne se bacha",
    "Teri behan ki pet me mera bachha",
    "Teri randi maa ko kitno ne choda¿?",
    "Teri mummy ke muh se apna zip khulwa lunga",
    "Teri behan bhi teri mummy ki tarah randi nikal gyi",
    "Teri mummy ko apne lund se jhula jhulwa dunga",
    "Tujhe, teri mummy ko, tere bane banaye ghar ke sath khareed lunga gareeb",
    "Teri didi ke sath sexting kr dunga",
    "Chut ka diwana main teri mummy ki chut ka diwana",
    "Your mom, My bitch, Otey¿?",
    "Teri mummy ki brownish chut pe apna paani giraunga",
    "Hawe hawe me teri mummy ko उछालते hue chod dunga",
    "Teri mummy ke sath lawandiyabaazi karu randi ke",
    "Teri mummy ki fati choot apne jhaato se seel dunga",
    "chup chudi hui raand ke bette",
    "Or bete kya haal",
    "Teri mummy ki chut me pura laat ghusa dunga",
    "Teri behan meri khelne wali gudiya ok?",
    "Teri behan ki teady bear dilakr chod dunga",
    "Teri didi ka WhatsApp number milega cya¿?",
    "Teri behan ke noods de to dekhkr delete kar dunga☠️🙈",
    "Just Imagine ki teri mummy ki gand me agar hathi ka lund chala jaaye to☠️😭",
    "Teri mummy mere ghar me kam karne wali baai",
    "Teri mummy ko sexually harass kar dunga😈👍🏻",
    "Teri mummy ko promise kiya hu ki use aaj bikni gift karunga",
    "Teri behan ki chut me captain america ka shield",
    "Teri behan kidnap ho gayi",
    "kutte ke muh me ghee or tu mera lund pee randike",
    "Andhere me teri didi chodkr bhaag jaunga"
    "Apni maa chuda lwde"
]

# This will store the target users for each owner_id
target_users = defaultdict(int)
# This will store the message ID of the .okay command for each target user
okay_message_ids = {}

@client.on(events.NewMessage(pattern=r'\.chudle'))
async def okay_handler(event):
    """
    The owner replies to a user's message with `.okay`, setting them as the target for auto-replies.
    """
    if event.sender_id != owner_id:  # Ensure only the owner can use this command
        return

    if not event.is_reply:
        await event.reply("⚠️ Must reply to a user's message to target them.")
        return

    replied_message = await event.get_reply_message()
    target_user_id = replied_message.sender_id

    # Set the target user for auto-reply
    target_users[target_user_id] = event.chat_id

    # Save the message ID of the .okay command to later edit it
    okay_message_ids[target_user_id] = event.message.id

    # Edit the command message to show that the target has been set
    await event.edit("✅ A Chudakkad Detected for auto-Reply.\n **[𝐅𝐭~ || Og ||]**(tg://openmessage?user_id=6066188248)")

@client.on(events.NewMessage())
async def auto_reply_handler(event):
    """
    Sends an auto-reply to the target user whenever they send a message.
    """
    # Only respond if the sender is the target
    if event.sender_id in target_users:
        # Pick a random response from the list
        response = random.choice(auto_reply_responses)
        await event.reply(response)

@client.on(events.NewMessage(pattern=r'\.soja'))
async def nokoay_handler(event):
    """
    The owner stops the auto-reply for a specific user when `.nokay` is used.
    """
    if event.sender_id != owner_id:  # Ensure only the owner can use this command
        return

    if not event.is_reply:
        await event.reply("⚠️ Must reply to a user's message to stop auto-replying.")
        return

    replied_message = await event.get_reply_message()
    target_user_id = replied_message.sender_id

    # Remove the target user from the auto-reply list
    if target_user_id in target_users:
        # Remove the target user
        target_users.pop(target_user_id)

        # Edit the .nokay message to stop auto-reply
        # Edit the message that initiated the .nokay command to show auto-reply stopped
        await event.edit("✅ Auto-Reply Has Been Stopped for This Chudakkad.\n**[𝐅𝐭~ || Og ||]**(tg://openmessage?user_id=6066188248)")
    else:
        await event.reply("⚠️ No auto-reply is set for this user.")

import requests

# Replace with your OpenWeatherMap API key
weather_api_key = 'a368ca66c8dd935f59461f02c74effea'  # Your API Key from OpenWeatherMap

@client.on(events.NewMessage(pattern=r'\.wthr (.+)'))
async def weather_handler(event):
    """Fetch and display the weather information for a given location."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    location = event.pattern_match.group(1)  # Get the location from the command
    try:
        # Send a request to OpenWeatherMap API
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}&units=metric'
        response = requests.get(weather_url).json()

        if response.get('cod') != 200:
            await event.edit(f"❌ Could not fetch weather data for `{location}`. Please check the location and try again.")
            return

        # Extract weather data
        weather_description = response['weather'][0]['description']
        temperature = response['main']['temp']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        country = response['sys']['country']
        city = response['name']

        # Prepare the weather report message
        weather_report = f"""
        🌍 **Weather in {city}, {country}:**

        ☀️ **Description**: {weather_description.capitalize()}
        🌡️ **Temperature**: {temperature}°C
        💧 **Humidity**: {humidity}%
        💨 **Wind Speed**: {wind_speed} m/s
        """

        await event.edit(weather_report)

    except Exception as e:
        await event.edit(f"❌ An error occurred while fetching weather data: {str(e)}")
 
from deep_translator import GoogleTranslator

@client.on(events.NewMessage(pattern=r'\.trlh',
func=lambda e: e.is_reply))
async def translate_handler(event):
    """Translate a replied message to Hindi."""
    if not await is_owner(event):
        return  # Only the owner can use this command

    replied_message = await event.get_reply_message()
    original_text = replied_message.text

    try:
        # Translate the message to Hindi
        translated_text = GoogleTranslator(source='auto', target='hi').translate(original_text)

        # Send the translated message
        await event.edit(f"**Translated to Hindi :** ```{translated_text}```")

    except Exception as e:
        await event.reply(f"❌ Error in translation: {str(e)}")                                                    
        
# List of how many crypto coins in script               
@client.on(events.NewMessage(pattern=r'\.crypto'))
async def cmds_handler(event):
    """List all available commands with dots."""
    if not await is_owner(event):
        return  # Only the owner can use this command
    
    commands = [
        "1• **Bitcoin :** `.btc`",
    "2• **Ethereum :** `.eth`",
    "3• **Binance Coin :** `.bnb`",
    "4• **Solana :** `.sol`",
    "5• **Ripple :** `.xrp`",
    "6• **Cardano :** `.ada`",
    "7• **Dogecoin :** `.doge`",
    "8• **Shiba Inu :** `.shib`",
    "9• **Polygon :** `.matic`",  # Formerly Matic Network
    "10• **Litecoin :** `.ltc`",
    "11• **The Open Network :** `.ton`",
    ]
    await event.edit("🏗️ **All Crypto Coins**:\n\n" + "\n".join(commands))
    
# List of how many commands in script               
@client.on(events.NewMessage(pattern=r'\.cmds'))
async def cmds_handler(event):
    """List all available commands with dots."""
    if not await is_owner(event):
        return  # Only the owner can use this command
    
    commands = [
        "`.ogbost` : **Owner Introdduction**",
        "`.mute` : **Mute Anyone in DM**",
        "`.unmute` : **Unmute Them Again**",
        "`.mid` : **Mrityu's Info**",
        "`.ban` : **Ban Anyone in DM**",
        "`.unban` : **Unban Them Again**",
        "`.quiet` : **Make The Whole Group Quiet**",
        "`.relief` : **Let The Group Chat be Free**",
        "`.okie` : **Let Someone be Free When Whole Group is Quieted**",
        "`.naah` : **Make That Someone Quiet Again**",
        "`.ufff` : **See Who Can Speak While Quieted**",
        "`.kick` : **Remove Any Member from Group**",
        "`.asleep` : **Make Your Status Asleep**",
        "`.awake` : **Be Awake**",
        "`.busy` : **Make Your Status Busy**",
        "`.free` : **Be Free**",
        "`.reset <@>` : **Reset Insta Password**",
        "`.d` : **Delete Someone's Chat**",
        "`.purge <no>` : **Delete The Msgs**",
        "`.tinfo` : **Get The Info of Someone Telegram**",
        "`.insta <@>` : **Get The Info of Any Insta ID**",
        "`.pusd <digit>` : **Price of Dollar**",
        "`.trl` : **Translate Any Msg**",
        "`.gana <name>` : **Search The Lyrics of Any Song**",
        "`.spam <no>` : **Spam Your Specific Msg**",
        "`.mm` : **Create a Private Group**",
        "`.close <time>` : **Close The Group**",
        "`.chud <no>` : **Fvckk Anyone**",
        "`.pline` : **Pickup Line**",
        "`.dline` : **Dirty Pickup Line**",
        "`.count <time>` : **Start Countdown**",
        "`.calc` : **Calculator**",
        "`.stock` : **Today Highest Increased Stock**",
        "`.dm <text>` : **Send Direct Msg from Group**",
        "`.cspam <no>` : **Copy & Paste Someone's Msg**",
        "`.chudle` : **Start Auto-Reply**",
        "`.soja` : **Stop Auto-Reply**",
        "`.wthr <place>` : **See Weather**",
        "`.crypto` : **All Crypto Coins**"
        "`.shop` : **Show Your Shop/Stock**",
        "`.upi` : **Your Upi ID**",
        "`.selfbot` : **Whose Self-Bot**"
    ]
    await event.edit("📜 **Available Commands**:\n\n" + "\n".join(commands))

# ========== Start the Client ==========
client.start()
client.run_until_disconnected()
