# WebSocket server for numeric conversion with validation and exception handling
import asyncio
import websockets

# Function to convert decimal to binary
def decimal_to_binary(num):
    return bin(num).replace("0b", "")

# Function to convert decimal to octal
def decimal_to_octal(num):
    return oct(num).replace("0o", "")

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(num):
    return hex(num).replace("0x", "")

# Function to convert binary to decimal (validates binary input)
def binary_to_decimal(binary_str):
    if not all(c in '01' for c in binary_str):
        raise ValueError("Invalid binary number! Only 0 and 1 are allowed.")
    return int(binary_str, 2)

# Function to convert octal to decimal (validates octal input)
def octal_to_decimal(octal_str):
    if not all(c in '01234567' for c in octal_str):
        raise ValueError("Invalid octal number! Digits should be between 0 and 7.")
    return int(octal_str, 8)

# Function to convert hexadecimal to decimal (validates hexadecimal input)
def hexadecimal_to_decimal(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal number! Only digits 0-9 and letters A-F are allowed.")

# Handling incoming client requests with exception handling
async def conversion_handler(websocket, path):
    async for message in websocket:
        try:
            # Message should be of the format: conversion_type,value
            conversion_type, value = message.split(',')

            if conversion_type == "decimal_to_binary":
                result = decimal_to_binary(int(value))
            elif conversion_type == "decimal_to_octal":
                result = decimal_to_octal(int(value))
            elif conversion_type == "decimal_to_hexadecimal":
                result = decimal_to_hexadecimal(int(value))
            elif conversion_type == "binary_to_decimal":
                result = str(binary_to_decimal(value))
            elif conversion_type == "octal_to_decimal":
                result = str(octal_to_decimal(value))
            elif conversion_type == "hexadecimal_to_decimal":
                result = str(hexadecimal_to_decimal(value))
            else:
                result = "Invalid conversion type!"
        
        # Catch invalid number formats and send error message to client
        except ValueError as e:
            result = str(e)
        except Exception as e:
            result = f"An error occurred: {str(e)}"
        
        # Send the result or error message back to the client
        await websocket.send(result)

# Main server function
async def main():
    async with websockets.serve(conversion_handler, "0.0.0.0", 8765):

        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
