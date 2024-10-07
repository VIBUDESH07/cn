# WebSocket client with menu options for numeric conversion
import asyncio
import websockets

async def send_conversion(conversion_type, value):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send the conversion request
        await websocket.send(f"{conversion_type},{value}")
        
        # Receive the result from the server
        result = await websocket.recv()
        print(f"\nReceived result: {result}\n")

# Menu for conversion options
def show_menu():
    print("Choose a conversion option:")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Exit")

def get_conversion_type(option):
    conversion_types = {
        "1": "decimal_to_binary",
        "2": "decimal_to_octal",
        "3": "decimal_to_hexadecimal",
        "4": "binary_to_decimal",
        "5": "octal_to_decimal",
        "6": "hexadecimal_to_decimal",
    }
    return conversion_types.get(option, None)

async def main():
    while True:
        show_menu()
        option = input("Enter your choice (1-7): ")
        
        if option == '7':
            print("Exiting client.")
            break

        conversion_type = get_conversion_type(option)
        if conversion_type:
            value = input("Enter the value to convert: ")
            await send_conversion(conversion_type, value)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    asyncio.run(main())
