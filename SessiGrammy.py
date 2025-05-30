import asyncio
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import ApiIdInvalidError as TelethonApiIdInvalidError, \
                                         PhoneNumberInvalidError as TelethonPhoneNumberInvalidError, \
                                         PhoneCodeInvalidError as TelethonPhoneCodeInvalidError, \
                                         SessionPasswordNeededError as TelethonSessionPasswordNeededError

from pyrogram import Client
from pyrogram.errors import ApiIdInvalid as PyrogramApiIdInvalid, \
                            PhoneNumberInvalid as PyrogramPhoneNumberInvalid, \
                            PhoneCodeInvalid as PyrogramPhoneCodeInvalid, \
                            SessionPasswordNeeded as PyrogramSessionPasswordNeeded


banner = """
╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣
╠╣░█▀▀░█▀▀░█▀▀░█▀▀░▀█▀░█▀▀░█▀▄░█▀█░█▄█░█▄█░█░█╠╣
╠╣░▀▀█░█▀▀░▀▀█░▀▀█░░█░░█░█░█▀▄░█▀█░█░█░█░█░░█░╠╣
╠╣░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░░▀░╠╣
╠╣     Effortless session generation for      ╠╣
╠╣           Pyrogram & Telethon.             ╠╣
╠╣       https://github.com/ChocoJaYY         ╠╣                                      
╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣
╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
"""

print(banner)

def get_session_choice():
    """Gets the user's choice for session type."""
    while True:
        print("Choose session type to generate:")
        print("1. Telethon")
        print("2. Pyrogram")
        choice = input("Enter your choice (1 or 2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter 1 for Telethon or 2 for Pyrogram.")

async def main():
    session_choice = get_session_choice()
    
    if session_choice == '1':
        print("You chose: Telethon")
        telethon_client = None 
        session_file = "temp_session.session"
        
        if os.path.exists(session_file):
            try:
                os.remove(session_file)
            except Exception as e:
                print(f"Failed to delete session file: {e}")

        try:
            api_id_str = input("Enter your API ID: ")
            if not api_id_str.isdigit():
                print("API ID must be an integer.")
                return
            api_id = int(api_id_str)
            api_hash = input("Enter your API Hash: ")
            phone_number = input("Enter your phone number (with country code): ")

            # Initialize TelegramClient with StringSession
            session = StringSession()
            telethon_client = TelegramClient(session, api_id, api_hash)
            await telethon_client.connect()

            # Initial authorization check
            if not await telethon_client.is_user_authorized():
                await telethon_client.send_code_request(phone_number)
                try:
                    code = input('Enter the code: ')
                    await telethon_client.sign_in(phone_number, code)
                except TelethonPhoneCodeInvalidError:
                    print("Invalid code.")
                    return
                except TelethonSessionPasswordNeededError:
                    password = input('Two-factor authentication is enabled. Please provide the password: ')
                    try:
                        await telethon_client.sign_in(password=password)
                    except Exception as e:
                        print(f"Failed to complete 2FA login: {e}")
                        return

            # Final check for authorization
            if await telethon_client.is_user_authorized():
                session_string = session.save()
                if session_string:
                    print("\nTelethon session string:")
                    print(session_string)
                    # Save session to file as too
                    try:
                        with open("telethon_session.txt", "w") as f:
                            f.write(session_string)
                        print("Session string also saved to 'telethon_session.txt'")
                    except Exception as e:
                        print(f"Failed to save session to file: {e}")
                else:
                    print("Failed to generate session string.")
            else:
                print("Login failed or was incomplete. Could not retrieve session string.")

        except TelethonApiIdInvalidError:
            print("Invalid API ID or API Hash.")
        except TelethonPhoneNumberInvalidError:
            print("Invalid phone number.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if telethon_client and telethon_client.is_connected():
                await telethon_client.disconnect()
    
    elif session_choice == '2':
        print("You chose: Pyrogram")
        try:
            api_id_str = input("Enter your API ID: ")
            if not api_id_str.isdigit():
                print("API ID must be an integer.")
                return
            api_id = int(api_id_str)
            api_hash = input("Enter your API Hash: ")
            phone_number = input("Enter your phone number (with country code): ")

            async with Client(
                name=":memory:",
                api_id=api_id,
                api_hash=api_hash,
                phone_number=phone_number,
                in_memory=True
            ) as pyrogram_client:
                # Authorization is handled by Client startup
                try:
                    print("Sending code...")
                    sent_code_info = await pyrogram_client.send_code(phone_number)
                except PyrogramPhoneNumberInvalid:
                    print("Invalid phone number.")
                    return

                code = input("Enter the code you received: ")
                try:
                    await pyrogram_client.sign_in(phone_number, sent_code_info.phone_code_hash, code)
                except PyrogramPhoneCodeInvalid:
                    print("Invalid code.")
                    return
                except PyrogramSessionPasswordNeeded:
                    password = input("Two-factor authentication is enabled. Enter your password: ")
                    try:
                        await pyrogram_client.check_password(password)
                    except Exception as e:
                        print(f"An error occurred during password check: {e}")
                        return
                
                # Export session string after successful authorization
                session_string = await pyrogram_client.export_session_string()
                if session_string:
                    print("\nPyrogram session string:")
                    print(session_string)
                    # Save Pyrogram session to file as a fallback
                    try:
                        with open("pyrogram_session.txt", "w") as f:
                            f.write(session_string)
                        print("Session string also saved to 'pyrogram_session.txt'")
                    except Exception as e:
                        print(f"Failed to save session to file: {e}")
                else:
                    print("Failed to generate session string.")

        except PyrogramApiIdInvalid:
            print("Invalid API ID or API Hash.")
        except PyrogramPhoneNumberInvalid:
            print("Invalid phone number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())